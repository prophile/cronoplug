import zipfile
import io

class Plugin:
    def __init__(self, stream, name, source = lambda x: None):
        self.file = zipfile.ZipFile(stream, 'w')
        self._wrote_main = False
        self.name = name
        self._src = source

    def __enter__(self):
        return self

    def add_file(self, name, content):
        info = zipfile.ZipInfo(filename=name)
        if name == 'main.lua':
            self._wrote_main = True
            info.comment = self.name.encode('utf-8')
        if isinstance(content, io.IOBase):
            content = content.read()
        self.file.writestr(info, content)

    def import_file(self, name):
        content = self._src(name)
        if content is None:
            raise KeyError("No file {}".format(name))
        self.add_file(name, self._src(name))

    def __exit__(self, type, value, traceback):
        if not self._wrote_main:
            self.add_file(name = 'main.lua', content = b'')
        self.file.close()

