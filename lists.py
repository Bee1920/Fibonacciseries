#assigning elements to different lists
l = [4, 5]
l.append(6)
print(l)
l.insert(2,19)
print(l)
l.extend(range(12,18))
print(l)

#accessing elements from a tuple
tu = ("Happy", "Birth", "Day", "to", "you")
print(tu[1:3])
      
#deleting differnt dictonary elements
dictonary = { 1: 'Happy', 2: 'Birth', 3:'Day', 4: 'to', 5: 'you'}
print(dictionary.pop(3))
print(dictionary.pop(4))
