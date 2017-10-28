data = ['trees', 'bike', 'cars', 'steer', 'arcs']
d = {}
for w in data:
    key = ''.join(sorted(w))
    mylist = []
    if key in d:
        mylist = d[key]
        mylist.append(w)
        d[key] = mylist
    else:
        mylist.append(w)
        d[key] = mylist
for l in d.values():
    print l