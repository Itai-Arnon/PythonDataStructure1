# we will create a dictionary and try to reverse b/w its keys and values
myDi = dict()
myDi = {1: 'a', 3: 'b', 5: 'b', 4: 'd'}

for c in myDi:
    print(myDi[c], c)

# reversing keys and vals
reverse = dict()
for k in myDi: #transverse myDi while switching between key and value
    d = myDi[k]
    if d not in reverse:
        reverse[d] = [k] # singleton- defines a new list belonging to key d
    else:
        reverse[d].append(k)
print(reverse)

