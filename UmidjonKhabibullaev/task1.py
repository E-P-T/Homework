def replace_quotes(string: str) -> str:
    """ Function which receives a string as argument and replaces all instances of
        a single quote character with double quote character and vice versa.
    """
    string = string.replace("'", "\`")
    string = string.replace("\"", "'")
    string = string.replace("`", "\"")
    string = string.replace("\\", "")

    return string


if __name__ == "__main__":
    s = "Some string with single ' quote '. They should be replaced by the double \" quote. \nThe result might be a bit strange. But read it in reverse order if you wish. \nThis is single quote: '. \nAnd this is double qoute: \""
    print(replace_quotes(s))