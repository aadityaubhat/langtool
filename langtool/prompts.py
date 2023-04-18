import jinja2

environment = jinja2.Environment()

system_start_prompt = "You are a helpful assistant that converts instructions into python code"

tool_prompt = environment.from_string("""
You have the following python {{ tool.type }} available:

name: {{ tool.name }}
description: {{ tool.description }}
documentation: {{ tool.documentation }}

Do the following only using the {{ tool.name }} {{ tool.type }}.}}:
{{ instruction }}""")


def render_tool_prompt(tool, instruction):
    return tool_prompt.render(tool=tool, instruction=instruction)
