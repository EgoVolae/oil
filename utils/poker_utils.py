import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from enum import Enum
from dataclasses import dataclass
from typing import Dict, Set, Tuple

RANK_MAP = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

class HandRank(Enum):
    HIGH_CARD = 0
    ONE_PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    STRAIGHT = 4
    FLUSH = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    STRAIGHT_FLUSH = 8

@dataclass
class Card:
    rank: int  # Integer from 2-14
    suit: str  # One of "S", "C", "D", "H"

    # We rank T=10, J=11, Q=12, K=13, A=14

    def from_str(x: str) -> "Card":
        
        if x[0] in RANK_MAP.keys():
            rank = RANK_MAP[x[0]]
        else:
            rank = int(x[0])

        suit = x[1]

        return Card(rank, suit)

    def __str__(self) -> str:
        return f"({self.rank},{self.suit})"

class Hand:

    cards: Tuple[Card]
    card_ranks: Tuple[int]
    unique_ranks: Set[int]
    num_unique_ranks: int
    low_rank: int
    high_rank: int
    rank_dist_map: Dict[int, int]
    card_suits: Tuple[str]

    def __init__(self, cards: Tuple[Card]):
        self.cards = sorted(cards, key= lambda card: card.rank)

        self.card_ranks = tuple(sorted([card.rank for card in self.cards]))
        self.unique_ranks = set(self.card_ranks)
        self.num_unique_ranks = len(self.unique_ranks)
        self.low_rank = self.card_ranks[0]
        self.high_rank = self.card_ranks[-1]
        self.rank_dist_map = {x: len([y for y in self.card_ranks if y == x]) for x in self.unique_ranks}
        self.card_suits = tuple([card.suit for card in self.cards])
        pass

    def from_card_strings(card_strings: Tuple[str]) -> "Hand":
        return Hand(tuple(Card.from_str(card_string) for card_string in card_strings))

    @property
    def hand_rank(self) -> HandRank:

        has_straight = False
        has_flush = False

        if self.card_ranks == tuple([x for x in range(self.low_rank, self.low_rank + 5)]):
            has_straight = True
        if self.high_rank == 14 and self.card_ranks[:4] == [x for x in range(2, 6)]:
            has_straight = True
        
        if len(set(self.card_suits)) == 1:
            has_flush = True
        
        if has_flush and has_straight:
            return HandRank.STRAIGHT_FLUSH

        if self.num_unique_ranks == 2:
            if 4 in self.rank_dist_map.values():
                return HandRank.FOUR_OF_A_KIND
            return HandRank.FULL_HOUSE
        
        if has_flush:
            return HandRank.FLUSH
        
        if has_straight:
            return HandRank.STRAIGHT
        
        if self.num_unique_ranks == 3:
            if 3 in self.rank_dist_map.values():
                return HandRank.THREE_OF_A_KIND
            return HandRank.TWO_PAIR
        
        if self.num_unique_ranks == 4:
            return HandRank.ONE_PAIR
        
        return HandRank.HIGH_CARD
    
    def beats(self, other: "Hand") -> bool:
        """
        Note: this method is incomplete - it does not handle the case where
        both have hands the same hand rank that is better than one pair
        """
        own_hand_rank = self.hand_rank.value
        other_hand_rank = other.hand_rank.value

        if own_hand_rank > other_hand_rank:
            return True
        
        if other_hand_rank > own_hand_rank:
            return False

        # Both have HIGH_CARD
        if own_hand_rank == 0:
            
            for r1, r2 in zip(reversed(self.card_ranks), reversed(other.card_ranks)):
                if r1 == r2:
                    continue
                return r1 > r2
            
            raise Exception("Should not be here")
        
        # Both have ONE_PAIR
        if own_hand_rank == 1:
            self_pair_rank = [x for x in self.unique_ranks if self.rank_dist_map[x] == 2][0]
            other_pair_rank = [x for x in other.unique_ranks if other.rank_dist_map[x] == 2][0]

            if self_pair_rank > other_pair_rank:
                return True
            
            if other_pair_rank > self_pair_rank:
                return False
            
            for r1, r2 in zip(
                reversed([x for x in self.card_ranks if x != self_pair_rank]), 
                reversed([x for x in other.card_ranks if x != other_pair_rank])
            ):
                if r1 == r2:
                    continue
                return r1 > r2
            
    def __str__(self) -> str:
        return ",".join([str(card) for card in self.cards])
