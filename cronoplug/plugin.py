import zipfile

class Plugin:
    def __init__(self, stream, name):
        self.file = zipfile.ZipFile(stream, 'w')
        self._wrote_main = False
        self.name = name

    def __enter__(self):
        return self

    def add_file(self, name, content):
        info = zipfile.ZipInfo(filename=name)
        if name == 'main.lua':
            self._wrote_main = True
            info.comment = self.name.encode('utf-8')
        self.file.writestr(info, content)

    def __exit__(self, type, value, traceback):
        if not self._wrote_main:
            self.add_file(name = 'main.lua', content = b'')
        self.file.close()

