from Database import Database as db



############################# INITIALIZE #################################

# Example d = db("location {.txt / .json")   or       d = db("c:/anydirectory/location { .txt / .json")
d  = db("Student.json") 



############################ CREATE ######################################
# syntax : object.create(key, value)

d.create("Class", {"class":"CSE", "section": "CS-2" } ) 
d.create("Sports", {"Football":"Outdoor","Chess":"Indoor"})


# Create existing key throughs error
d.create("Class","Gupta")
#output: "Error: Key already exists."



############################# READ #########################################
# syntax : object.read(key)

x = d.read("Class")
print(x)
# Output: jaiswal

# Read on non-existing key
x = d.read("Hello")
# output: Error: Can't read. No such key exists.



############################## DELETE ######################################
# syntax : object.delete(key)

d.delete("Sports")

# deleting a non-exiting key
d.delete("Hello")
# Output: Error: Can't delete. No such key exists.



############################## UPDATE #######################################
# syntax : object.update(key, value)

d.update("Class", {"class":"IT", "section": "IT-2"})

# updating  a non-existing key
d.update("Hello", " world")
#output:  Error: Can't update. No such key present.

############################# SHOW ##########################################
# syntax : object.show()
d.show()
#output: Prints all the data in the database
