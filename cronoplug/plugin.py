import zipfile

class Plugin:
    def __init__(self, stream):
        self.file = zipfile.ZipFile(stream, 'w')

    def __enter__(self):
        return self

    def add_file(self, name, content):
        self.file.writestr(name, content)

    def __exit__(self, type, value, traceback):
        self.file.close()

