

class BadURLError(Exception):
    def __init__(self, url, *args, **kwargs) -> None:
        self.url = url
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        return f'It is not possible to get data for the given url ({self.url})'


class FailStatusCodeError(Exception):
    pass
