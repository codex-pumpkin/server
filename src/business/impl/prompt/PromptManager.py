from src.persistence.factory.PersistenceFactory import PersistenceFactory
from src.core import settings

from src.business.interfaces import IPromptManager
from typing import Tuple, List

class PromptManager(IPromptManager):
    async def retrieve_context(self, user_input: str, top_k: int = settings.chroma_settings.num_of_chunks) -> str:
        """
        Retrieve semantically similar documentation chunks for the user prompt.

        @param
            user_input (str): User prompt used to query vector similarity.
            top_k (int, optional): Number of top matching chunks to fetch.
            Defaults to 2.

        @return
            str: Newline-separated context snippets injected into LLM prompting.
        """
        repo = await PersistenceFactory.get_semantic_repository()
        chunks = await repo.get_similar_chunks(user_input, top_k)
        return "\n".join(chunks)

    def make_regeneration_context(self, exit_code: int, raw_output: str) -> str:
        """
        Build a regeneration hint from validator execution results.

        @param
            exit_code (int): Exit code returned by the code validator process.
            raw_output (str): Raw validator stderr/stdout output text.

        @return
            str: Prompt-ready context string describing why regeneration is needed.
        """
        context = "Ngspice exited with code: {} .Ngspice output is: {}".format(exit_code, raw_output)
        return context
    
    def get_conversation_context(self, conversation_history: List[Tuple[str, str]]) -> str:
        """
        Format prior user/assistant turns into a single context block.

        @param
            conversation_history (List[Tuple[str, str]]): Ordered list of
            `(user_message, ai_message)` pairs from earlier turns.

        @return
            str: Readable transcript block used as conversational context for LLM calls.
        """
        if not conversation_history:
            return ""
        context = "Conversation history:\n"
        for user_msg, ai_msg in conversation_history:
            context += "User: {}\nAI: {}\n".format(user_msg, ai_msg)
        return context
