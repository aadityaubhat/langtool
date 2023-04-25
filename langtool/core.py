from langtool.utils import get_documentation
from langtool.prompts import render_tool_prompt
from langtool.llms.base import LLM
from inspect import isfunction, isclass
import logging
import re

logger = logging.getLogger(__name__)


class Toolify:
    def __init__(self, obj: object, llm: LLM):
        if not isfunction(obj) and not isclass(obj):
            raise TypeError(
                "Expected a function or class object, received: {}".format(type(obj))
            )

        self.obj = obj
        self.llm = llm

    @staticmethod
    def parse_arg_value(arg_value):
        if arg_value.startswith("'") and arg_value.endswith("'"):
            return arg_value[1:-1]
        if arg_value.startswith('"') and arg_value.endswith('"'):
            return arg_value[1:-1]
        try:
            return int(arg_value)
        except ValueError:
            pass
        try:
            return float(arg_value)
        except ValueError:
            pass
        return arg_value

    @staticmethod
    def extract_function_and_args(function_string):
        func_name = re.search(r"\w+", function_string).group()
        arg_string = re.search(r"\((.*)\)", function_string).group(1)

        arg_list = [arg.strip() for arg in re.split(r",\s*(?![^()]*\))", arg_string)]
        positional_args = []
        keyword_args = {}

        for arg in arg_list:
            if "=" in arg:
                key, value = [x.strip() for x in arg.split("=")]
                keyword_args[key] = Toolify.parse_arg_value(value)
            else:
                positional_args.append(Toolify.parse_arg_value(arg))

        return func_name, positional_args, keyword_args

    def _get_code(self, instruction: str) -> str:
        """Get the code for a tool on an instruction.

        Args:
            instruction (str): The instruction to run the tool on.

        Returns:
            str: Code of the tool.
        """
        description = get_documentation(self.obj)
        name = self.obj.__name__
        obj_type = "function" if isfunction(self.obj) else "class"
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
            return code
        else:
            if isfunction(self.obj):
                function_string = code
                (
                    func_name,
                    positional_args,
                    keyword_args,
                ) = Toolify.extract_function_and_args(function_string)

                # Define a dictionary of available functions
                available_functions = {self.obj.__name__: self.obj}

                # Call the function using the extracted name and arguments
                if func_name in available_functions:
                    available_functions[func_name](*positional_args, **keyword_args)
                else:
                    Exception(f"Incorrect LLM output -  \n {code}")
            else:
                exec(code)
