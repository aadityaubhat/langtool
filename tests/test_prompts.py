from langtool.prompts import render_tool_prompt
import pytest


def sample_data():
    return [
        (
            "Counter",
            "class",
            "A class for counting hashable objects.",
            "Create a Counter object and count the occurrences of elements in a list.",
            "You have the following python class available:\n\n"
            "name: Counter\n"
            "description: A class for counting hashable objects.\n"
            "documentation: \n\n"
            "Do the following only using the Counter class.:\n"
            "Create a Counter object and count the occurrences of elements in a list."
        ),
        (
            "os.path.join",
            "function",
            "A function to join one or more path components intelligently.",
            "Join the given path components to form a single path.",
            "You have the following python function available:\n\n"
            "name: os.path.join\n"
            "description: A function to join one or more path components intelligently.\n"
            "documentation: \n\n"
            "Do the following only using the os.path.join function.:\n"
            "Join the given path components to form a single path."
        ),
    ]


class TestRenderToolPrompt:
    @pytest.mark.parametrize("name, type, description, instruction, expected", sample_data())
    def test_render_tool_prompt(self, name, type, description, instruction, expected):
        result = render_tool_prompt(name, type, description, instruction)
        assert result == expected