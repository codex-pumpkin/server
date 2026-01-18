from typing_extensions import Final
import textwrap
from openai import AsyncOpenAI
from src.persistence.impl.chroma_database import SemanticRepository
from src.persistence.interfaces import IAIClient

_PREPROMPT: Final[str] = textwrap.dedent("""\
    You are an expert analog circuit designer.
    Use the retrieved context only as reference material.
    If the context is incomplete or suboptimal, improve it.
    Do NOT copy node naming errors.
    Generate a clean, correct SPICE netlist.
    Return SPICE code only, without any explanations.
""")

class AIClient(IAIClient):

    def __init__(self) -> None:
        self.SemanticRepository = SemanticRepository()

    async def get_response(self, user_question: str, api_key: str, model: str="gpt-4o-mini") -> str:
        '''Client for interacting with OpenAI API to get chat completions
        prompt: the input text prompt for the AI model
        api_key: API key for authentication
        model: the AI model to use (default: "gpt-4o-mini")
        Returns the AI-generated response as a string
     '''
        context = self._retrieve_context(user_question.strip())
        client = AsyncOpenAI(api_key=api_key)
        resp = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system",  "content": _PREPROMPT},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{user_question}"}
                ],
            temperature=0.7,
            max_tokens=None,
        )
        return resp.choices[0].message.content
    
    @staticmethod
    async def _retrieve_context(self, user_input: str, top_k: int = 3) -> str:
        """Return top-k matching documents as a single newline-separated string."""
        chunks = self.SemanticRepository.get_similar_chunks(user_input, top_k)
        return "\n".join(chunks)
    
    


