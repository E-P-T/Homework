from abc import ABC, abstractmethod


class MessageConsumer(ABC):

    @abstractmethod
    def add_message(self, message):
        pass


class MessageConsumerNoop(MessageConsumer):

    def add_message(self, message):
        pass


class VerboseMessageConsumer(MessageConsumer):

    def add_message(self, message):
        print(f'[[[ {message} ]]]')


def get_message_consumer(is_verbose):
    if is_verbose:
        return VerboseMessageConsumer()
    return MESSAGE_CONSUMER_NOOP


MESSAGE_CONSUMER_NOOP = MessageConsumerNoop()
