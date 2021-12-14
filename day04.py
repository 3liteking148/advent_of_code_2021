from functools import reduce
import re


def test(card, slicer, slice_):
    if slice_ == 0:
        return False

    test_now = reduce(lambda a, b: a and b == -1, [True] + card[slice(*slice_)])
    test_next = test(card, slicer, slicer(slice_))
    return test_now or test_next


def col_slicer(slice_):
    return (slice_[0]+1, slice_[1], slice_[2]) if slice_[0] < 5 else 0


def col_test(card):
    return test(card, col_slicer, (0, 25, 5))


def row_slicer(slice_):
    return (slice_[0]+5, slice_[1]+5, slice_[2]) if slice_[1] < 25 else 0


def row_test(card):
    return test(card, row_slicer, (0,  5, 1))


def bingo(card, seq, prev):
    if col_test(card) or row_test(card):
        card_sum = sum([0 if x == -1 else x for x in card])
        return (len(seq), card_sum * prev)

    card_new = [-1 if x == seq[0] else x for x in card]
    return bingo(card_new, seq[1:], seq[0])


if __name__ == '__main__':
    with open('day4.txt', 'r') as file:
        text = file.read()
        input_ = [int(x) for x in re.findall(r'\b\d+\b', text)]
        seq_size = len(re.findall(r',', text)) + 1

        scores = []
        for i in range(seq_size, len(input_), 25):
            scores.append(bingo(input_[i:i+25], input_[0:seq_size], None))

        print(reduce(lambda a, b: a if a[0] > b[0] else b, scores)[1])
        print(reduce(lambda a, b: a if a[0] < b[0] else b, scores)[1])
