

class PathFile(ICreateFile):
    def create_file(self, file: str) -> None:
        file = Path(file)
        file.touch(exist_ok=True)
