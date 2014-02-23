import cronoplug.driver as drv

def test_argparse():
    generator_called = 0
    def fake_generator(srcdir, dstfile, plugin_name):
        nonlocal generator_called
        assert srcdir == "ponygravity"
        assert dstfile == "death star"
        assert plugin_name == "Pony Mann"
        generator_called += 1
    drv.cronoplug(["ponygravity", "death star", "-n", "Pony Mann"],
                  generate = fake_generator)
    assert generator_called == 1

def test_argparse_longhand():
    generator_called = 0
    def fake_generator(srcdir, dstfile, plugin_name):
        nonlocal generator_called
        assert srcdir == "ponygravity"
        assert dstfile == "death star"
        assert plugin_name == "Pony Mann"
        generator_called += 1
    drv.cronoplug(["ponygravity", "death star", "--name", "Pony Mann"],
                  generate = fake_generator)
    assert generator_called == 1

def test_argparse_implicit_name():
    generator_called = 0
    def fake_generator(srcdir, dstfile, plugin_name):
        nonlocal generator_called
        assert srcdir == "ponygravity"
        assert dstfile == "death star"
        assert plugin_name == "ponygravity"
        generator_called += 1
    drv.cronoplug(["ponygravity", "death star"],
                  generate = fake_generator)
    assert generator_called == 1

