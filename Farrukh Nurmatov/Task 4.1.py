"""Implement a function which receives a string and replaces all `"` symbols
with `'` and vise versa."""


def replacer(txt: str):
    """This function receives string and if ' symbol is in string changes in to " symbol and vise versa"""
    ret_txt = ""
    for char in txt:
        if char == "\'":
            ret_txt += "\""
        elif char == '\"':
            ret_txt += '\''
        else:
            ret_txt += char
    return ret_txt


if __name__ == '__main__':
    text = "I'm a bat\"man"
    print(replacer(text))