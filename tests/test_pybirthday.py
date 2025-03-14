import pytest
from src.pybirthday.pybirthday import cake


class Tests:

    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at th=e yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    #
    # Test functions
    #

    def test_cake(self):
        name = "Alex"
        words = "Happy Birthday!"
        actual = cake(name, words)
        expected = ""
        assert actual == expected, "Expected True to be equal to True!"