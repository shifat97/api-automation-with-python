import pytest

# session, module, function, autouse and many more
# read the docs

@pytest.fixture(params=[1, 2, 3, 4], ids=["one", "two", "three", "four"])
def number_fixture(request):
    return request.param

def test_number_fixture(number_fixture):
    assert isinstance(number_fixture, int)
