# File: test_hello_world.py
import hello_world

def test_hello_world(capsys): 
    hello_world.hello_world() 
    out, _ = capsys.readouterr()
    assert out == "Hello World!\n"
