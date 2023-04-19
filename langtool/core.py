from langtool.utils import get_documentation
from langtool.prompts import render_tool_prompt
from langtool.llms.base import LLM
from inspect import isfunction, isclass
import logging

logger = logging.getLogger(__name__)

class Toolify:
    def __init__(self, obj:object, llm: LLM):
        if not isfunction(obj) and not isclass(obj):
            raise TypeError("Expected a function or class object, received: {}".format(type(obj)))
        
        self.obj = obj
        self.llm = llm

    def _get_code(self, instruction: str) -> str:
        """Get the code for a tool on an instruction.

        Args:
            instruction (str): The instruction to run the tool on.

        Returns:
            str: Code of the tool.
        """
        description = get_documentation(self.obj)
        name = self.obj.__name__
        obj_type = 'function' if isfunction(self.obj) else 'class'
        prompt = render_tool_prompt(name, obj_type, description, instruction)
        logger.info("Prompt: \n {}".format(prompt))
        
        code = self.llm.get_reply(prompt)
        return code

    def run(self, instruction: str, safe_mode: bool = True):
        """Run a tool on an instruction.

        Args:
            instruction (str): The instruction to run the tool on.
            safe_mode (bool, optional): Whether to run the tool in safe mode. Defaults to True.

        Returns:
            str: Code of the tool.
        """
        code = self._get_code(instruction)

        if safe_mode:
            return(code)
        else:
            raise NotImplementedError("Unsafe mode not implemented yet.")
