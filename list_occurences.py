def list_occurences(l):
        return True if l.count(19)==2 and l.count(5) >=3 else False

print(list_occurences([19,19,5,5,5,5,5])) 
print(list_occurences([19,19,15,5,3,5,5,2]))
print(list_occurences([19,15,15,5,3,3,5,2]))