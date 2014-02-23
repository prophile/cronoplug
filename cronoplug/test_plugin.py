from cronoplug.plugin import Plugin

import io
import zipfile

def test_base():
    bio = io.BytesIO()
    with Plugin(bio, "Test Plugin") as plg:
        plg.add_file(name = 'main.lua',
                     content = b'I am covered in bees.')
    zp = zipfile.ZipFile(bio, 'r')
    with zp.open('main.lua') as f:
        content = f.read()
        assert content == b'I am covered in bees.'

def test_info():
    bio = io.BytesIO()
    with Plugin(bio, "Test Plugin") as plg:
        pass
    zp = zipfile.ZipFile(bio, 'r')
    info = zp.getinfo('main.lua')
    assert info.comment == b"Test Plugin"

