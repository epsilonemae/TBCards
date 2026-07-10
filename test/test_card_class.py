import pytest

from tbcards.card_class import Card


@pytest.fixture
def kspade():
    return Card(13, "s")


def test_eq(kspade):
    assert kspade == Card(13, "s")


def test_lt(kspade):
    assert kspade > Card(12, "d")


def test_repr(kspade):
    assert repr(kspade) == "Card(13, s)"


def test_str(kspade):
    assert str(kspade) == "K♠"


def test_get_rank(kspade):
    assert kspade.get_rank() == 13


def test_set_rank_valid(kspade):
    kspade.set_rank(10)
    assert kspade.get_rank() == 10


def test_set_rank_invalid(kspade):
    with pytest.raises(ValueError) as exc:
        kspade.set_rank(14)
    assert (
        exc.exconly(True) == "ValueError: The rank 14 is invalid. Ranks "
        "must be in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]"
    )


def test_get_suit(kspade):
    assert kspade.get_suit() == "s"


def test_set_suit_valid(kspade):
    kspade.set_suit("d")
    assert kspade.get_suit() == "d"


def test_set_suit_invalid(kspade):
    with pytest.raises(ValueError) as exc:
        kspade.set_suit("t")
    assert (
        exc.exconly(True) == "ValueError: The suit t is invalid. Suits "
        "must be in ['h', 'd', 'c', 's']"
    )
