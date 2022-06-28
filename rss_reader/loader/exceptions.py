

class EmptyURLError(Exception):
    """Occurs when the url is empty."""


class DataEmptyError(Exception):
    """Occurs when there is no data."""


class DataFileEmptyError(EmptyDataError):
    """Occurs when there is no data in the uploaded file."""

    def __init__(self, file, *args, **kwargs) -> None:
        self.file = file
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        a = f'No columns to parse from file ({self.file}). '\
            f'Delete the file and run the program in the mode of reading '\
            f'news from the Internet.'
        return a


class DataFileNotFoundError(EmptyDataError):
    """Occurs when the file is not found."""

    def __init__(self, file, *args, **kwargs) -> None:
        self.file = file
        super().__init__(*args, **kwargs)

    def __str__(self) -> str:
        a = f'File ({self.file}) does not exist. '\
            f'Run the program in the mode of reading '\
            f'news from the Internet.'
        return a
