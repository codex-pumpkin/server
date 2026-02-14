from typing_extensions import Final
import textwrap
from openai import AsyncOpenAI
from src.persistence.impl.chroma_database import SemanticRepository
from src.persistence.interfaces import IAIClient

_PREPROMPT: Final[str] = textwrap.dedent("""
    You are an expert analog circuit designer.
    Generate SPICE code based on the user question and retrieved context, only 1 circuit, do not generate multiple circuits.
    Use the retrieved context only as reference material.
    If the context is incomplete or suboptimal, improve it.
    Do NOT copy node naming errors.

    CRITICAL SYNTAX RULES:
    - Subcircuit instantiation: X<name> <node1> <node2> ... <subckt_name> (nodes first, name last)
    - Subcircuit definition: .SUBCKT <name> <node1> <node2> ... (match node count to instantiation)
    - ALWAYS include .PRINT or .PLOT statement before .END (required for batch mode)
    - TSTEP must be greater than 0
    - Title line must start with * (SPICE requirement, not optional)

    Generate a clean, correct SPICE netlist.
    Return SPICE code only that can be directly pasted into ngspice, 
    without any explanations.
""")

_REGENRATION_PREPROMPT: Final[str] = textwrap.dedent("""\
    You are an expert analog circuit designer.
    Generate SPICE code based on the user question and retrieved context, only 1 circuit, do not generate multiple circuits.
    The previous code you generated had some issues.
    We send you code you generated earlier for reference,
    along with exitCode, rawOutput from ngspice 
    and the user question itself.
                                                     
    CRITICAL SYNTAX RULES:
    - Subcircuit instantiation: X<name> <node1> <node2> ... <subckt_name> (nodes first, name last)
    - Subcircuit definition: .SUBCKT <name> <node1> <node2> ... (match node count to instantiation)
    - ALWAYS include .PRINT or .PLOT statement before .END (required for batch mode)
    - TSTEP must be greater than 0
    - Title line must start with * (SPICE requirement, not optional)
                                                     
    Generate a clean, correct SPICE netlist.
    Return SPICE code only that can be directly pasted into ngspice, 
    without any explanations and any comments.
""")

class AIClient(IAIClient):

    async def get_response(self, user_question: str, retrieved_context: str, conversation_history: str, api_key: str, model: str="gpt-4o-mini") -> str:
        """
        Client for interacting with OpenAI API to get chat completions
        prompt: the input text prompt for the AI model
        api_key: API key for authentication
        model: the AI model to use (default: "gpt-4o-mini")
        Returns the AI-generated response as a string
        """

        client = AsyncOpenAI(api_key=api_key)
        resp = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system",  "content": _PREPROMPT},
                {"role": "user", "content": f"Context:\n{retrieved_context}\n\n{conversation_history}\n\nQuestion:\n{user_question}"}
                ],
            temperature=0.7,
            max_tokens=512,
        )
        return resp.choices[0].message.content
    

    async def regenerate(self, user_question: str, regeneration_context: str, code: str, api_key: str, model: str="gpt-4o-mini") -> str:
        """
        Client for interacting with OpenAI API to get chat completions
        prompt: the input text prompt for the AI model
        api_key: API key for authentication
        model: the AI model to use (default: "gpt-4o-mini")
        Returns the AI-generated response as a string
        """

        client = AsyncOpenAI(api_key=api_key)
        resp = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system",  "content": _REGENRATION_PREPROMPT},
                {"role": "user", "content": f"Question:\n{user_question}\n \
                 \n Code:\n{code} Context:\n{regeneration_context}\n"}
                ],
            temperature=0.7,
            max_tokens=512,
        )
        return resp.choices[0].message.content
    
    


