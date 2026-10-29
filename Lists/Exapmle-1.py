#List creation
students = ["Ismael", "Arnoud", "Maxim", "Emelyne", "Ismael"]

print (": Original List:")
print (students)

#Copy the List 1. copy()
students_copy = students.copy()
print("\n : This is the copy of the list")
print(students_copy)

#counting the elements in the list 2. count()
Ismael_count = students.count("Ismael")
print ("\n Number of times I appeared are :", Ismael_count )

#Add multiple elements 3. extend()
new_students = ["Jackson", "David"]
students.extend(new_students)
print("\n After extending the lists:", students)

#Appending elements
for Ismael in students:
    print ("\n the Appending element", students)

#concatenaton of string lists
students = students + new_students
print ( " \n This is concatrnated list:", students)

#Find the position of the elements in the list 4.index()
position = students.index("David")
print ("\n Position of Ismael in the list:", position)

#insert an element at given position 5. insert()
students.insert(5, "Peter")
print ( "\n After inserting Peter :", students)

students.clear()
print(students)