import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import utils.poker_utils as pu

dummy_straight_flush = pu.Hand.from_card_strings(["2H", "3H", "4H", "5H", "6H"])
dummy_four_of_a_kind = pu.Hand.from_card_strings(["2H", "2C", "2D", "2H", "7H"])
dummy_full_house = pu.Hand.from_card_strings(["2H", "2C", "2D", "5H", "5C"])
dummy_flush = pu.Hand.from_card_strings(["2H", "3H", "4H", "5H", "7H"])
dummy_straight = pu.Hand.from_card_strings(["2H", "3H", "4C", "5H", "6H"])
dummy_three_of_a_kind = pu.Hand.from_card_strings(["2H", "2C", "2D", "5H", "7H"])
dummy_hand_two_pair = pu.Hand.from_card_strings(["2H", "2C", "4H", "4C", "7H"])
dummy_hand_one_pair = pu.Hand.from_card_strings(["2H", "2C", "4H", "5C", "7H"])
dummy_hand_high_card = pu.Hand.from_card_strings(["2H", "4C", "5H", "7C", "9H"])

def test_ranks():
    
    assert dummy_straight_flush.hand_rank == pu.HandRank.STRAIGHT_FLUSH
    assert dummy_four_of_a_kind.hand_rank == pu.HandRank.FOUR_OF_A_KIND
    assert dummy_full_house.hand_rank == pu.HandRank.FULL_HOUSE
    assert dummy_flush.hand_rank == pu.HandRank.FLUSH
    assert dummy_straight.hand_rank == pu.HandRank.STRAIGHT
    assert dummy_three_of_a_kind.hand_rank == pu.HandRank.THREE_OF_A_KIND
    assert dummy_hand_two_pair.hand_rank == pu.HandRank.TWO_PAIR
