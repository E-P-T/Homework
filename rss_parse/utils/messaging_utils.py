import sys
from abc import ABC, abstractmethod


class MessageConsumer(ABC):
    """
    Abstraction for adding messages
    """

    @abstractmethod
    def add_message(self, message):
        pass


class MessageConsumerNoop(MessageConsumer):
    """
    Implementation of MessageConsumer that skips messages and does nothing.
    """

    def add_message(self, message):
        pass


class VerboseMessageConsumer(MessageConsumer):
    """
    Implementation of MessageConsumer that prints messages surrounding them with [[[ msg ]]]
    """

    def add_message(self, message):
        print(f'[[[ {message} ]]]')


def get_message_consumer(is_verbose):
    if is_verbose:
        return VerboseMessageConsumer()
    return MESSAGE_CONSUMER_NOOP


MESSAGE_CONSUMER_NOOP = MessageConsumerNoop()


def print_error(*args, **kwargs):
    """
    Shortcut to print error messages to a console
    """
    print(*args, file=sys.stderr, **kwargs)
