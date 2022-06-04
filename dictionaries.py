people = {"A" : 1290, "B" : 1291, "C" : 1292}

for name, number in people.items():
    print("Phone number of %s is %d" % (name, number))

del people["A"]
print(people)
people.pop("B")
print(people)

if "C" in people:
    print("C is in people")
