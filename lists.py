Lists []:-
 Lists are ordered sequences of objects. The objects do not have to be the
 same type. They are indicated by square brackets and the elements of the
 list are separated by commas. You can append an item to the end of a list
 L by using the command L.append(newitem). It is possible to index into a
 list exactly as we did with strings


l=[1,2,3,4,5,6]

print(type(l))
print(l)

l.append(100)
print(l)

print("the first item is",l[0])
print("The second index is",l[1])
print("The third index is",l[2])
print("the fourth index is:",l[3])
print("the last item is",l[-1])
print("the second to last item is",l[-2])

l[2] ='skip'
l[3]="a"
l[4]="few"
print()
print(l)
print()


