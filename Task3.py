# Task 6.3

from itertools import chain


class Cipher():

    def __init__(self, keyword, cipher=None):
        self._keyword = keyword

    def _create_basic_cipher(self):
        """create a master cipher."""

        from string import ascii_lowercase, whitespace, ascii_uppercase

        original_seq = ascii_lowercase
        upper_original_seq = ascii_uppercase

        cleared_keyword = set(self._keyword)
        missing_chars = [i for i in original_seq if i not in cleared_keyword]

        keyword_seq = list(chain(cleared_keyword, missing_chars))
        upper_keyword_seq = self._get_upper_seq(keyword_seq)

        direct_seq = self._get_dict_seq(original_seq, keyword_seq)
        reverse_seq = self._get_dict_seq(keyword_seq, original_seq)

        upper_direct_seq = self._get_dict_seq(
            upper_original_seq, upper_keyword_seq)

        upper_reverse_seq = self._get_dict_seq(
            upper_keyword_seq, upper_original_seq)

        return {
            'encode': self._merge_dict(
                direct_seq,
                upper_direct_seq,
                self._get_dict_seq(whitespace, whitespace)),
            'decode': self._merge_dict(
                reverse_seq,
                upper_reverse_seq,
                self._get_dict_seq(whitespace, whitespace))
        }
