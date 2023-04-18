from langtool.utils import (
    get_docstring,
    get_members,
    get_function_documentation,
    get_class_documentation,
)


class TestClass:
    """This is a sample TestClass for testing documentation functions."""

    def method_one(self, arg1: int, arg2: str) -> str:
        """This method takes two arguments and returns a formatted string."""
        return f"Argument 1: {arg1}, Argument 2: {arg2}"

    def method_two(self, arg1: float) -> float:
        """This method takes one argument and returns its square."""
        return arg1**2


def test_get_docstring():
    """Test that get_docstring returns the docstring for an object."""

    def test_function():
        """This is a test function."""
        pass

    assert get_docstring(test_function) == "This is a test function."


def test_get_members():
    """Test that get_members returns a list of members of an object."""

    class TestClass(object):
        def test_method(self):
            """This is a test method."""
            pass

        def _private_method(self):
            pass

    assert get_members(TestClass) == [("test_method", TestClass.test_method)]


def test_get_class_documentation():
    class_doc = get_class_documentation(TestClass)
    assert "Class: TestClass" in class_doc
    assert "Description:" in class_doc
    assert (
        "This is a sample TestClass for testing documentation functions." in class_doc
    )
    assert "Methods:" in class_doc
    assert "Function: method_one" in class_doc
    assert "Function: method_two" in class_doc


def test_get_function_documentation():
    method_one_doc = get_function_documentation(TestClass.method_one)
    assert "Function: method_one" in method_one_doc
    assert "Description:" in method_one_doc
    assert (
        "This method takes two arguments and returns a formatted string."
        in method_one_doc
    )
    assert "Arguments:" in method_one_doc
    assert "- arg1: <class 'int'>" in method_one_doc
    assert "- arg2: <class 'str'>" in method_one_doc
    assert "Return Type:" in method_one_doc
    assert "- <class 'str'>" in method_one_doc

    method_two_doc = get_function_documentation(TestClass.method_two)
    assert "Function: method_two" in method_two_doc
    assert "Description:" in method_two_doc
    assert "This method takes one argument and returns its square." in method_two_doc
    assert "Arguments:" in method_two_doc
    assert "- arg1: <class 'float'>" in method_two_doc
    assert "Return Type:" in method_two_doc
    assert "- <class 'float'>" in method_two_doc
