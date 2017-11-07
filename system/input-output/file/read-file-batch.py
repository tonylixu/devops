'''
Read from file in batches
'''
def read_whole_file():
    offset = 0
    chunk = 50
    with open('poem.txt', 'r') as f:
        while True:
            print "read 50..."
            fragment = f.read(chunk)
            if fragment:
                print fragment
            else:
                break
                
def read_line():
    with open('poem.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            print line

def read_lines():
    with open('poem.txt', 'r') as f:
        lines = f.readlines()
    print lines
    
if __name__ == '__main__':
    #read_whole_file()
    #read_line()
    read_lines()