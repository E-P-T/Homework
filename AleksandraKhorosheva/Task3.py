### Task 4.3
'''Implement a function which works the same as `str.split` method
(without using `str.split` itself, ofcourse).'''
# в какую сторону лучше смотреть regex или for
import re

# s = "Hello world"
# print(s.split())


# def test_split(s, spl=None, max_occ=None):
#     orig = s.split(spl, max_occ if max_occ else -1)
#     mine = split_str(s, spl, max_occ if max_occ else 0)
#     if orig != mine:
#         print(f"ERROR: {s}, {spl}, {max_occ}: {orig} vs {mine}")
#     else:
#         print(f"INFO: {orig}")


def split_str(s, spl=None, max_occ=0):
    if not spl:
        patt = "\\W+"
        s = s.strip()
    else:
        patt = f'({spl})'
    return list(filter(lambda x: x != spl, re.split(patt, s, max_occ)))


print(split_str("Hello world"))

# print("Hello World".split(" W"))
# print(re.compile("( W)").split("Hello World"))
# print(re.split("( W)", "Hello World"))
#
# test_split("Hello World", " W")
# test_split("Hello World", "o")
# test_split("Hello World", "o", 1)
# test_split("Hello World", "Hello")
# test_split(" Hello   World\t asd ")
# test_split("Hello   World    ", " ")
