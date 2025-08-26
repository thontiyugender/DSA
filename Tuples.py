Tuples(tuple):

 Tuples are also ordered sequences of objects, but unlike lists, they are
 immutable. You can access the items but you cant change what items are
 in the tuple after you create it. For example, trying to append raises an
 exception.




t=("1","yugender","mana","snehithudusa","131","917")

print()
print(t)
print()
print("the type of t is:",type(t))
print()
print(id(t))
print(t[3]) 
 
# t.append(55)  ----APPEND IS NOT GONNA PERFORM IN TUPLES----   

 # t[4]=99.5       ====not gonna perform =====

s="000000"
s[4]="x"


