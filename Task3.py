# Task 6.3

from itertools import chain


class Cipher():

    def __init__(self, keyword, cipher=None):
        self._keyword = keyword
        self._cipher = self._create_basic_cipher() if not cipher else cipher

    def _get_dict_seq(self, seq_1, seq_2):
        """Create a dictionary from two sequences."""
        return dict(zip(seq_1, seq_2))

    def _get_upper_seq(self, seq):
        """Convert characters to upper case in sequence."""
        return list(map(str.upper, seq))

    def _merge_dict(self, *args):
        """Concatenate multiple sequences into a dictionary."""
        d = {}
        for i in args:
            d.update(i)
        return d

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

    def encode(self, str_):
        """Encodes a string.

        Args:
            str_ (str): string to be encoded

        Returns:
            str: encoded string
        """
        return ''.join(self._cipher['encode'][i] for i in str_ if i in
                       self._cipher['encode'])

    def decode(self, str_):
        """Decode string

        Args:
            str_ (str): string to be decoded

        Returns:
            str: decoded string
        """
        return ''.join(self._cipher['decode'][i] for i in str_ if i in
                       self._cipher['decode'])

    def get_cipher(self):
        """Used to check if the character encoding is correct.

        Returns:
            dict: dictionary for character encoding and decoding
        """
        return self._cipher


def main():
    """Main function."""

    print('\n{:*^30}'.format('Task 6.3'), end='\n\n')

    c = Cipher('crypto')
    mes = c.encode('Hello world')
    print(f'Encoded word: {mes}')
    print(f'Decoded word: {c.decode(mes)}', end='\n\n')

    print(f'For check: {c.get_cipher()}', end='\n\n')
