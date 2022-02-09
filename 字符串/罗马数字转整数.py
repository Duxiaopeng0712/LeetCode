class Solution:
    def romanToInt(s: str) -> int:
        roman_normal = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_special = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        number = 0
        for i in roman_special:
            if i in s:
                s = s.replace(i, '')
                number += roman_special[i]

        for i in s:
            if i in roman_normal:
                number += roman_normal[i]
        print(number)
        return number


if __name__ == '__main__':
    s = "IX"
    Solution.romanToInt(s)
