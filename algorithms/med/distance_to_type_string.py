class Solution(object):
    def totalDistance(self, s):
        """
        :type s: str
        :rtype: int
        """
        keyboard = {
            'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9),
            'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8),
            'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)
        }

        prev = keyboard.get('a')
        distance = 0
        for char in s:
            x1, y1 = prev
            x2, y2 = keyboard.get(char)
            distance += (abs(x1 - x2) + abs(y1 - y2))

            prev = keyboard.get(char)
    
        return distance