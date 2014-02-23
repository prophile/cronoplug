from cronoplug.plugin import Plugin

import io
import zipfile

def test_base():
    bio = io.BytesIO()
    with Plugin(bio) as plg:
        plg.add_file(name = 'main.lua',
                     content = 'I am covered in bees.')
    zp = zipfile.ZipFile(bio, 'r')
    with zp.open('main.lua') as f:
        content = f.read()
        assert content == 'I am covered in bees.'

