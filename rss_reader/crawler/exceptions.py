

class BadURLError(Exception):
    def __init__(self, url, *args, **kwargs) -> None:
        self.url = url
        super().__init__(*args, **kwargs)
