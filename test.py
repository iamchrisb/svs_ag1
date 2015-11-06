#!../svs-vm/bin/python

def intersect(a, b):
    return list(set(a) & set(b))

c = {'A':[],'B':[],'C':[],'D':[]}
# old mapping
a = {'A':['X','K','B'],'B':['Z','C'], 'C':[], 'D' : ['P']}
# current mapping
b = {'A':['X'],'B':['Z'], 'C':['U'], 'D': []}

print(a)
print(b)

for key, value in a.iteritems():
    cur_val = b[key]
    if len(value) == 0:
        print("current value: " + str(cur_val))
        c[key] = cur_val
    else:
        c[key] = intersect(value, cur_val)

print(c)


