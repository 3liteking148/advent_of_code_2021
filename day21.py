import re

class Player:
    def __init__(self, initial_position):
        self.position = initial_position
        self.score = 0
        self.backup = None

    def tuple(self):
        return (self.position, self.score)

    def revert(self, tuple):
        self.position = tuple[0]
        self.score = tuple[1]

    def move(self, x):
        self.position = (self.position + x) % 10
        if self.position == 0:
            self.position = 10
        self.score += self.position


class Dice:
    def __init__(self):
        self.value = 0
        self.counter = 0

    def roll(self):
        self.counter += 1
        self.value = (self.value + 1) % 100
        if self.value == 0:
            self.value = 100

        return self.value

    def roll3x(self):
        return self.roll() + self.roll() + self.roll()


ranges = [(i, j, k) for i in range(1, 4) for j in range(1, 4) for k in range(1, 4)]
def dirac_dice(dp, p1, p2, turn):
    if p1.score >= 21:
        return (1, 0)
    if p2.score >= 21:
        return (0, 1)

    key = p1.tuple() + p2.tuple() + (turn,)
    if key in dp:
        return dp[key]

    ret = (0, 0)
    for i, j, k in ranges:
        if turn == 'p1':
            backup = p1.tuple()
            p1.move(i + j + k)
            a, b = dirac_dice(dp, p1, p2, 'p2')
            p1.revert(backup)
        else:
            backup = p2.tuple()
            p2.move(i + j + k)
            a, b = dirac_dice(dp, p1, p2, 'p1')
            p2.revert(backup)

        ret = (ret[0] + a, ret[1] + b)

    dp[key] = ret
    return ret


with open('day21.txt', 'r') as inp:
    p1, p2 = re.findall(r'\d.+(\d+)', inp.read())

    # part 1
    player1 = Player(int(p1))
    player2 = Player(int(p2))
    dice = Dice()
    while player1.score < 1000 and player2.score < 1000:
        player1.move(dice.roll3x())
        if player1.score >= 1000:
            break
        player2.move(dice.roll3x())

    print(dice.counter * min(player1.score, player2.score))
    print(max(dirac_dice({}, Player(int(p1)), Player(int(p2)), 'p1')))
