class Solution:
    def judgeCircle(moves: str) -> bool:
        x, y = 0, 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                y += 1
            elif moves[i] == 'D':
                y -= 1
            elif moves[i] == 'R':
                x -= 1
            else:
                x += 1

        return x == y == 0
