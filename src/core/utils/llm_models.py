"""Module for managing LLM models and their configurations."""

from enum import Enum

from llama_index.llms.openai import OpenAI
from llama_index.llms.openrouter import OpenRouter

from src.core.config import Config

class LLMType(Enum):
    """Enumeration of supported LLM types."""
    NVIDIA_LEMOTRON = "nvidia/lemotron",


class LLMModels:
    """Class to manage LLM model configurations."""
    def __init__(self,
                 config: Config):
        self._config = config

        self._nvidia_llm = OpenRouter(
            api_key=self._config.api_key,
            max_tokens=256,
            context_window=4096,
            model="nvidia/nemotron-nano-9b-v2:free",
        )

    def get_llm(self, llm_type: LLMType):
        """Retrieve the LLM instance based on the specified type."""
        if llm_type == LLMType.NVIDIA_LEMOTRON:
            return self._nvidia_llm
        else:
            raise ValueError(f"Unsupported LLM type: {llm_type}")