'''
Write and read csv file
'''
import csv

def write_to_csv(v):
    offset = 0
    size = len(v)
    lines = 50
    with open('data.csv', 'w') as f:
        csvout = csv.writer(f)
        csvout.writerows(v)

                


if __name__ == '__main__':
    villains = [
        ['Doctor', 'No'],
        ['Rosa', 'Klebb'],
        ['Mister', 'Big'],
        ['Auric', 'Goldfinger'],
        ['Ernst', 'Blofeld']
    ]
    write_to_csv(villains)