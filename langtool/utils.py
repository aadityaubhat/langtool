import inspect
from openai import ChatCompletion
import re


def get_docstring(obj) -> str:
    """Return the docstring for an object, or None if no docstring is found."""
    docstring = obj.__doc__
    if docstring is None:
        docstring = inspect.getcomments(obj)
    return docstring


def get_members(obj, predicate=None) -> list:
    """Return a list of members of an object, optionally filtered by a predicate."""
    members = inspect.getmembers(obj, predicate)
    return [member for member in members if not member[0].startswith("_")]


def parse_arg_descriptions(docstring) -> dict:
    """Extract argument descriptions from the docstring."""
    arg_descriptions = {}
    if docstring:
        pattern = re.compile(r":param (\w+): (.+)")
        matches = pattern.findall(docstring)
        for match in matches:
            arg_descriptions[match[0]] = match[1]
    return arg_descriptions


def get_function_documentation(func) -> str:
    """Return the formatted documentation for a function, including argument descriptions."""
    if not inspect.isfunction(func):
        raise TypeError("Expected a function object, received: {}".format(type(func)))

    func_docstring = get_docstring(func)
    signature = inspect.signature(func)
    parameters = signature.parameters
    return_annotation = signature.return_annotation

    arg_descriptions = parse_arg_descriptions(func_docstring)

    documentation = "Function: {}\n".format(func.__name__)
    if func_docstring:
        documentation += "Description:\n{}\n".format(func_docstring.strip())

    if parameters:
        documentation += "\nArguments:\n"
        for name, param in parameters.items():
            annotation = (
                param.annotation if param.annotation != inspect.Parameter.empty else ""
            )
            description = arg_descriptions.get(name, "")
            documentation += "- {}: {} - {}\n".format(name, annotation, description)

    if return_annotation != inspect.Signature.empty:
        documentation += "\nReturn Type:\n- {}\n".format(return_annotation)

    return documentation


def get_class_documentation(cls):
    """Return the formatted documentation for a class, including its methods."""
    if not inspect.isclass(cls):
        raise TypeError("Expected a class object, received: {}".format(type(cls)))

    class_docstring = get_docstring(cls)
    class_members = get_members(cls, predicate=inspect.isfunction)

    documentation = "Class: {}\n".format(cls.__name__)
    if class_docstring:
        documentation += "Description:\n{}\n".format(class_docstring.strip())

    documentation += "\nMethods:\n"
    for name, member in class_members:
        documentation += "{}\n".format(name)

    return documentation


def get_documentation(obj):
    """Return the formatted documentation for an object, depending on its type."""
    if inspect.isfunction(obj):
        return get_function_documentation(obj)
    elif inspect.isclass(obj):
        return get_class_documentation(obj)
    else:
        raise TypeError(
            "Unsupported object type: {}. Expected a class or function object.".format(
                type(obj)
            )
        )
