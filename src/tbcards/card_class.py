class Card:
    """A class to represent a card. Has a rank and a suit, which must be in the
    keys of the class variables suits and ranks."""

    suits = {"h": "♥", "d": "♦", "c": "♣", "s": "♠"}
    ranks = {
        1: "A",
        2: "2",
        3: "3",
        4: "4",
        5: "5",
        6: "6",
        7: "7",
        8: "8",
        9: "9",
        10: "10",
        11: "J",
        12: "Q",
        13: "K",
    }

    def __init__(self, rank, suit):
        self._rank = rank
        self._suit = suit
        self._cleanup()

    def __repr__(self):
        return f"Card({self._rank}, {self._suit})"

    def __str__(self):
        return self.ranks[self._rank] + self.suits[self._suit]

    def __eq__(self, other):
        return (self._rank == other.get_rank()) and (
            self._suit == other.get_suit()
        )  # noqa

    def __lt__(self, other):
        return self._rank < other.get_rank()

    def _cleanup(self):
        if self._rank not in self.ranks:
            raise ValueError(
                f"The rank {self._rank} is invalid. Ranks must be in "
                f"{list(self.ranks.keys())}"
            )
        if self._suit not in self.suits:
            raise ValueError(
                f"The suit {self._suit} is invalid. Suits must be in "
                f"{list(self.suits.keys())}"
            )

    def get_rank(self):
        return self._rank

    def set_rank(self, new_rank):
        self._rank = new_rank
        self._cleanup()

    def get_suit(self):
        return self._suit

    def set_suit(self, new_suit):
        self._suit = new_suit
        self._cleanup()
