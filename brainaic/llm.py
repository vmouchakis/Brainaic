from langchain_community.llms.ollama import Ollama
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.callbacks.manager import CallbackManager
from brainaic.config import MODELS
import logging


class Llm:
    def __init__(self, model_name: str, temperature: float = 0.0, verbose: bool = False) -> None:
        self._model_type = model_name
        self._temperature = temperature
        self._verbose = verbose
        self.llm = self._load_model()

    def _load_model(self) -> Ollama:
        try:
            model = MODELS.get(self._model_type)
            callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
            return Ollama(model=model, temperature=self._temperature, verbose=self._verbose, callbacks=callback_manager)
        except Exception:
            logging.error(f'Could not load model of type {self._model_type}')
            raise RuntimeError(f"Model '{self._model_type}' is not supported. Supported model types: {MODELS.keys()}.")

    def generate(self, prompt: str) -> str:
        response = self.llm.generate([prompt])
        return response.generations[0][0].text

    def stream(self, prompt: str):
        response = self.llm.invoke(prompt)
        return response
