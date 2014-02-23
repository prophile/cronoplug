from nose.tools import *

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

def test_source():
    bio = io.BytesIO()
    src = io.BytesIO(b"I'm on a boat")
    with Plugin(bio, "Test Plugin", lambda f: src) as plg:
        plg.import_file('boat.txt')
    zp = zipfile.ZipFile(bio, 'r')
    with zp.open('boat.txt') as f:
        content = f.read()
        assert content == b"I'm on a boat"

@raises(KeyError)
def test_source_error():
    bio = io.BytesIO()
    with Plugin(bio, "Test Plugin", lambda f: None) as plg:
        plg.import_file('pony.txt')

