from loguru import logger


class Printer:
    """Print result in stdout"""

    def __init__(self, data: dict) -> None:
        logger.debug("Data is available (debug)!")
        self.data = data

    def __str__(self) -> str:
        return self.data["name"] + '\n' + ''.join([(f'{self.data["title"][i]}\n'
                                                    f'{self.data["pubDate"][i]}\n\n'
                                                    f'{self.data["description"][i]}\n\n'
                                                    f'{self.data["link"][i]}\n\n---------------\n\n') for i in
                                                   range(self.data["size"])])
