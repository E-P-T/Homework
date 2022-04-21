'''Task 4.1
Implement a function which receives a string and replaces all " symbols with ' and vise versa.'''

# вопрос! можно использовать функцию translate

def replace_symbols(s):
    # s = s.replace("'", '"').replace('"',"'")
    s = s.translate({ord("'"): '"', ord('"'): "'"})
    return s


def replace_quotes(s):
    res = ""
    table = {"'": "\"", "\"": "'"}
    for i in s:
        if i in table.keys():
            res += table[i]
        else:
            res += i
    return res


print(replace_symbols("'''\"\"\""))
print(replace_quotes("'''\"\"\""))


# def is_palindrome(s):
#     length = len(s)
#     for i in range(length // 2):
#         if s[i] != s[length - 1 - i]:
#             return False
#     return True
#
#
# print(is_palindrome(""))
# print(is_palindrome("abc"))
# print(is_palindrome("aba"))
# print(is_palindrome("abba"))
# print(is_palindrome("abda"))
# print(is_palindrome("asdfghjkkjhgfdsa"))