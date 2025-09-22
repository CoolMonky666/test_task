import pytest
from heroes import find_tallest_hero



def test_gender_male_or_female_pozitive():
    assert find_tallest_hero("Male", True) != (None,0)
    assert find_tallest_hero("Male", False) != (None,0)
    assert find_tallest_hero("Female", True) != (None,0)
    assert find_tallest_hero("Female", False) != (None,0)

@pytest.mark.parametrize("G",["Male","Female"])
def test_return_type_gender(G):
    result = find_tallest_hero(G, True)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], (int, type(None)))
    assert isinstance(result[1], (float, int))

@pytest.mark.parametrize("G",["Male","Female"])
def test_return_type_gender_work(G):
    result = find_tallest_hero(G, False)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert isinstance(result[0], (int, type(None)))
    assert isinstance(result[1], (float, int))