'''
How to write data into file as batches
'''
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way
And returned on the previous night.
'''

offset = 0
size = len(poem)
print size
chunk = 50
with open('poem.txt', 'xt') as f:
    while True:
        if offset > size:
            break
        else:
            f.write(poem[offset:offset+chunk])
            offset += chunk