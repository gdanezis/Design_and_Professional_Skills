"""

    >>> f = open(r"src/names.txt", "rt", encoding="utf8")
    >>> data = f.read()  # Read full contents
    >>> data.split()     # Split on new lines
    ['Ania', 'Jamie', 'Vasilis', 'Alberto', 'Mustafa', 'Marios', 'Raphael']
    >>> f.close()        # Close the file

"""

def test_write():
    f = open(r"src/store.txt", "wt")
    f.write("Hello\n")
    f.write("World\n")
    f.close()

    f2 = open(r"src/store.txt", "rt")
    for line in f2:
        print(line)
    f2.close()

def test_write_with():
    with open(r"src/store.txt", "wt") as f:
        f.write("Hello\n")
        f.write("World\n")

    with open(r"src/store.txt", "rt") as f2:
        for line in f2:
            print(line)

def test_binary():
    with open("src/store.bin", "wb") as f:
        f.write(b"\x00\x01\x02\x04")

    with open("src/store.bin", "r+b") as f2:
        f2.seek(2)            # goto byte 2.
        b = f2.read(1)        # read 1 byte
        assert b == b"\x02"
        assert f2.tell() == 3 # new position