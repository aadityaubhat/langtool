import jinja2

environment = jinja2.Environment()

system_start_prompt = (
    "You are a helpful assistant that converts instructions into python code"
)

tool_prompt = environment.from_string(
    """You have the following python {{ type }} available:

name: {{ name }}
description: {{ description }}
documentation: {{ documentation }}

Do the following only using the {{ name }} {{ type }}.:
{{ instruction }}"""
)


def render_tool_prompt(name, type, description, instruction):
    return tool_prompt.render(
        name=name, type=type, description=description, instruction=instruction
    )
