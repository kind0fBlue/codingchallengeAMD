import sys
import unittest


class TestFindPetersLastNumber(unittest.TestCase):
    def test_find_peters_last_number(self):
        for arg, res in [
            (110, 99),
            (112, 112),
            (23245, 22999),
            (11235888, 11235888),
            (111110, 99999),
            (33245, 29999),
            (1010, 999),
            (11010, 9999),
            (21010, 19999),
            (12010, 11999),
            (12110, 11999),
        ]:
            self.assertEqual(find_peters_last_number(arg), res)


def find_peters_last_number(number):
    place = 1
    pre = None
    for i in range(1, 10):
        place = 10**i
        if place > number:
            return number

        cur = (number // place) % 10
        pre = (number // (place // 10)) % 10

        if cur > pre:
            number -= (number % place) + 1

    return number


def main():
    try:
        number = int(sys.argv[1])
    except IndexError:
        print("Pass a number as arg to compute Peter's last number")
    else:
        print(find_peters_last_number(number))


if __name__ == "__main__":
    main()
