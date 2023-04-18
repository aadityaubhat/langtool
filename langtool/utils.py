import inspect

def get_docstring(obj):
    """Return the docstring for an object, or None if no docstring is found."""
    docstring = obj.__doc__
    if docstring is None:
        docstring = inspect.getcomments(obj)
    return docstring

def get_members(obj, predicate=None):
    """Return a list of members of an object, optionally filtered by a predicate."""
    members = inspect.getmembers(obj, predicate)
    return [member for member in members if not member[0].startswith('_')]