import litellm
from typing_extensions import Final
import textwrap
from src.core.exceptions import (
    LLMAuthenticationError,
    LLMNotFoundError,
    LLMPermissionDeniedError,  
    LLMBadRequestError,
    LLMAPIConnectionError,
    LLMAPIError,
    LLMRateLimitError
)
from src.persistence.interfaces import IAIClient

_PREPROMPT: Final[str] = textwrap.dedent("""
    You are an expert analog circuit designer.
    Generate SPICE code based on the user question and retrieved context.
    **Ignore the context entirely if it's not directly relevant to the requested circuit (e.g., do not add hierarchical elements or macro-models unless explicitly asked).**
    Do not copy naming errors.
    Only 1 circuit, do not divide code in multiple circuits!!!
    In all circuits include ".plot", ".print", or ".fourier" lines for execution in batch mode!!!

    CRITICAL STRUCTURAL RULES (ORDER MATTERS):
    1. Title line starting with *
    2. .SUBCKT definitions (if any) — BEFORE they are used with X...
    3. Circuit elements: sources (V, I), components (R, L, C), subcircuit instances (X...)
    4. Analysis commands: .TRAN, .DC, .AC (choose ONE)
    5. Output: .PRINT or .PLOT with specific variables (e.g., V(1) I(V1))
    6. .END — ABSOLUTE LAST LINE, nothing after it

    CRITICAL SYNTAX RULES:
    - B-sources (Bx, Ex, Gx, Hx): use EXPLICIT math expressions ONLY
    VALID: v(pos,neg)^2, abs(v(pos,neg)), 1u*v(pos,neg), exp(v(pos,neg))
    INVALID: f(v(pos,neg)), g(x), h(t) — any single-letter function name
    - Subcircuit: X<name> <node1> <node2> ... <subckt_name>
    - Subckt node count must match between definition and instantiation
    - .TRAN syntax: .TRAN <tstep> <tstop> [UIC], tstep>0, tstop>0 **(choose tstep as 1/(100*freq) for sinusoidal sources to ensure good resolution)**
    - Every circuit needs at least one source (V or I)
    - Use * for comments at line start, NEVER use ; for inline comments
    - .END must be the final line
    - .PRINT MUST include analysis type: .PRINT TRAN V(1), never .PRINT V(1)
    - Only print nodes that exist in the main circuit (not subcircuit internal nodes)
    - NO unit suffixes on values: use 0, not 0Volts; 1u, not 1uF
    - Component names must be UNIQUE across entire netlist (including inside .SUBCKT)
    - Never reuse V1, R1, etc. in subcircuit if used in main circuit
    - Subcircuit internal nodes must NOT collide with main circuit node numbers
    - Use high-numbered nodes in subckt (10, 20, 100, 101) never 0-9
    - pos/neg in v(pos,neg) refer to EXTERNAL nodes passed to subckt
    ** - For sources: Use DC for .DC analysis; AC for .AC; SIN(offset amp freq delay td phase) for .TRAN sinusoidal (e.g., SIN(0 5 1k 0 0 0) for 5V peak at 1kHz). Default to peak amplitude unless RMS specified.**

    CRITICAL CIRCUIT RULES:
    - Every node must have a DC path to ground (resistor, source, or .IC)
    - NEVER connect capacitor directly between two nodes without resistance to ground
    - RC circuits need: source → resistor → capacitor → ground
    - Add high-value resistor (1meg) to ground for floating nodes if needed

    **Before generating, think step-by-step internally: 1. Parse user request for components and analysis. 2. Assign unique nodes starting from 0 (ground) and 1 upward. 3. Ensure DC paths. 4. Choose appropriate source type. 5. Select reasonable tstep/tstop for .TRAN. Do not output this thinking—generate clean SPICE netlist only, no explanations.**
""")

_REGENRATION_PREPROMPT: Final[str] = textwrap.dedent("""\
    You are an expert analog circuit designer.
    Generate SPICE code based on the user question and retrieved context.
    Only 1 circuit, do not divide code in multiple circuits!!!
    The previous code you generated had some issues.
    We send you code you generated earlier for reference,
    along with exitCode, rawOutput from ngspice 
    and the user question itself.
    In all circuits include ".plot", ".print", or ".fourier" lines for execution in batch mode!!!
                                                     
    CRITICAL STRUCTURAL RULES (ORDER MATTERS):
    1. Title line starting with *
    2. .SUBCKT definitions (if any) — BEFORE they are used with X...
    3. Circuit elements: sources (V, I), components (R, L, C), subcircuit instances (X...)
    4. Analysis commands: .TRAN, .DC, .AC (choose ONE)
    5. Output: .PRINT or .PLOT with specific variables (e.g., V(1) I(V1))
    6. .END — ABSOLUTE LAST LINE, nothing after it

    CRITICAL SYNTAX RULES:
    - B-sources (Bx, Ex, Gx, Hx): use EXPLICIT math expressions ONLY
    VALID: v(pos,neg)^2, abs(v(pos,neg)), 1u*v(pos,neg), exp(v(pos,neg))
    INVALID: f(v(pos,neg)), g(x), h(t) — any single-letter function name
    - Subcircuit: X<name> <node1> <node2> ... <subckt_name>
    - Subckt node count must match between definition and instantiation
    - .TRAN syntax: .TRAN <tstep> <tstop> [UIC], tstep>0, tstop>0 **(choose tstep as 1/(100*freq) for sinusoidal sources to ensure good resolution)**
    - Every circuit needs at least one source (V or I)
    - Use * for comments at line start, NEVER use ; for inline comments
    - .END must be the final line
    - .PRINT MUST include analysis type: .PRINT TRAN V(1), never .PRINT V(1)
    - Only print nodes that exist in the main circuit (not subcircuit internal nodes)
    - NO unit suffixes on values: use 0, not 0Volts; 1u, not 1uF
    - Component names must be UNIQUE across entire netlist (including inside .SUBCKT)
    - Never reuse V1, R1, etc. in subcircuit if used in main circuit
    - Subcircuit internal nodes must NOT collide with main circuit node numbers
    - Use high-numbered nodes in subckt (10, 20, 100, 101) never 0-9
    - pos/neg in v(pos,neg) refer to EXTERNAL nodes passed to subckt
    ** - For sources: Use DC for .DC analysis; AC for .AC; SIN(offset amp freq delay td phase) for .TRAN sinusoidal (e.g., SIN(0 5 1k 0 0 0) for 5V peak at 1kHz). Default to peak amplitude unless RMS specified.**

    CRITICAL CIRCUIT RULES:
    - Every node must have a DC path to ground (resistor, source, or .IC)
    - NEVER connect capacitor directly between two nodes without resistance to ground
    - RC circuits need: source → resistor → capacitor → ground
    - Add high-value resistor (1meg) to ground for floating nodes if needed

    **Before generating, think step-by-step internally: 1. Parse user request for components and analysis. 2. Assign unique nodes starting from 0 (ground) and 1 upward. 3. Ensure DC paths. 4. Choose appropriate source type. 5. Select reasonable tstep/tstop for .TRAN. Do not output this thinking—generate clean SPICE netlist only, no explanations.**
                                                     
    Generate a clean, correct SPICE netlist.
    Return SPICE code only that can be directly pasted into ngspice, 
    without any explanations and any comments.
""")

class AIClient(IAIClient):

    async def get_response(
        self,
        user_question: str,
        retrieved_context: str,
        conversation_history: str,
        api_key: str,
        model: str = "gpt-o4-mini",
        api_url: str = "https://api.openai.com/v1"
    ) -> str:
        """
        Client for interacting with OpenAI API to get chat completions
        prompt: the input text prompt for the AI model
        api_key: API key for authentication
        model: the AI model to use (default: "gpt-4o-mini")
        Returns the AI-generated response as a string
        """

        return await self._get_response(user_question, retrieved_context, conversation_history, api_key, model, api_url)

    async def regenerate(
        self,
        user_question: str,
        regeneration_context: str,
        code: str,
        api_key: str,
        model: str="gpt-o4-mini",
        api_url: str="https://api.openai.com/v1"
    ) -> str:
        """
        Client for interacting with OpenAI API to get chat completions
        prompt: the input text prompt for the AI model
        api_key: API key for authentication
        model: the AI model to use (default: "gpt-4o-mini")
        Returns the AI-generated response as a string
        """

        return await self._regenerate(user_question, regeneration_context, code, api_key, model, api_url)
        

    async def _get_response(
            self,
            user_question: str,
            retrieved_context: str,
            conversation_history: str,
            api_key: str,
            model: str = None,
            api_url: str = None,
            ) -> str:
        
        """Get response using LiteLLM."""
        try:
            kwargs = {
                "model": model,
                "messages": [
                    {"role": "system", "content": _PREPROMPT},
                    {"role": "user", "content": f"Context:\n{retrieved_context}\n\n{conversation_history}\n\nQuestion:\n{user_question}"}
                ],
                "max_tokens": 1024,
                "api_key": api_key,
            }

            # Only set api_base for custom/local endpoints, not for default provider URLs
            if api_url:
                kwargs["api_base"] = api_url

            resp = await litellm.acompletion(**kwargs)
            return resp.choices[0].message.content
        
        except litellm.AuthenticationError:
            raise LLMAuthenticationError()

        except litellm.APIConnectionError:
            raise LLMAPIConnectionError()

        except litellm.NotFoundError:
            raise LLMNotFoundError()

        except litellm.BadRequestError:
            raise LLMBadRequestError()

        except litellm.PermissionDeniedError:
            raise LLMPermissionDeniedError()

        except litellm.APIError:
            raise LLMAPIError()

        except litellm.RateLimitError:
            raise LLMRateLimitError()

    async def _regenerate(self,
            user_question: str,
            regeneration_context: str,
            code: str,
            api_key: str,
            model: str = None,
            api_url: str = None,
            ) -> str:
        
        """Regenerate using LiteLLM."""
        try:
            kwargs = {
                "model": model,
                "messages": [
                    {"role": "system", "content": _REGENRATION_PREPROMPT},
                    {"role": "user", "content": f"Question:\n{user_question}\n\nCode:\n{code}\n\nContext:\n{regeneration_context}\n"}
                ],
                "max_tokens": 1024,
                "api_key": api_key,
            }

            if api_url:
                kwargs["api_base"] = api_url

            resp = await litellm.acompletion(**kwargs)
            return resp.choices[0].message.content
        
        except litellm.AuthenticationError:
            raise LLMAuthenticationError()

        except litellm.APIConnectionError:
            raise LLMAPIConnectionError()

        except litellm.NotFoundError:
            raise LLMNotFoundError()

        except litellm.BadRequestError:
            raise LLMBadRequestError()

        except litellm.PermissionDeniedError:
            raise LLMPermissionDeniedError()

        except litellm.APIError:
            raise LLMAPIError()

        except litellm.RateLimitError:
            raise LLMRateLimitError()



