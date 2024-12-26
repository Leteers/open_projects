import database

lst = [1,6]
conn = database.Connection()
lst2 = conn.add_element(lst)

print(lst)
print(lst2)