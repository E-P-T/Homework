import argparse


def get_args():
    """
    This function parser received arguments into a Namespace object
    :return: Namespace containing parsed arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('source', default=None, nargs='?', help='RSS feed URL')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show all program logs to the user.')
    parser.add_argument('-j', '--json', action='store_true', help='Print the result of the program in JSON format.')
    parser.add_argument('-V', '--version', action='store_true',
                        help='Will output current version of the program and exit.')
    parser.add_argument('-l', '--limit', help='Specify the amount of articles shown.')

    return parser.parse_args()
