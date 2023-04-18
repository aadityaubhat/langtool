from langtool.utils import get_docstring, get_members

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

    assert get_members(TestClass) == [('test_method', TestClass.test_method)]