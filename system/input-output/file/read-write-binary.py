'''
Read and write file in binary mode
'''
def read_binary():
    chunk = 50
    with open('bdata','rb') as f:
        while True:
            fragment = f.read(chunk)
            if not fragment:
                break
            else:
                print fragment

def write_binary(bdata):
    offset = 0
    chunk = 50
    size = len(bdata)
    with open('bdata','wb') as f:
        while True:
            if offset > size:
                break
            else:
                f.write(bdata[offset:offset+chunk])
                offset += chunk


if __name__ == '__main__':
    bdata = bytes(range(0, 256))
    write_binary(bdata)
    read_binary()
    