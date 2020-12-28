import json
import sys

class Database:
    ''' 
    accepts the location of the file(if not existing it will create a new one) and provide CRUD on the database.
    '''
    database = {}    # for handling data from the file
    location = ""    # stores the location of the file
    fileobj = object # file object for database
    working = True   # flag to check that every validation is passed for successfull processing
    def __init__(self, location):
        '''
        accepts the location and checks if location is valid or not. 
        If a file of same name exits it will open the exiting file otherwise
        it will create a new one.
        '''
        if not location.isspace():  #checks if location is white space or not i.e invalid address
            self.location  = location
            try:
                self.fileobj = open(location,'r+')
                data = json.load(self.fileobj)
            except:
                data = {"Database":{}}
                self.fileobj = open(self.location,'w+')
            self.database = data["Database"]
        else:
            self.working = False
            print("Error: Not a valid location or file name")

        
    def create(self,key,value):
        '''
        Accepts key and value and creates an new entry into the database.
        If key already exists it raises error.
        '''
        if self.working and self.sizevalidate(key, value) and self.typevalidate(key, value):
            self.database[key] = value
            self.save()
        
    def read(self,key):
        '''
        Return the value corresponding to the key (if exists).
        '''
        if self.working:
            if key not in self.database:
                print("Error: Can't read. No such key exists.")
            else:
                return self.database[key]
    
    def delete(self,key):
        '''
        Deletes the key-value pair corresponding to the key provided.
        '''
        if self.working:
            if key not in self.database:
                print("Error: Can't delete. No such key exists.")
            else:
                self.database.pop(key)
                self.save()
    
    def update(self,key,value):
        '''
        Updates the value corressponding the given key.
        '''
        if self.working:
            if key not in self.database:
                print("Error: Can't update. No such key present.")
            else:
                self.database[key] = value
                self.save()
    
    def show(self):
        '''
        Prints the data currently existing in the database.
        '''
        if self.working:
            for i in self.database:
                print("{}  : {}".format(i,self.database[i]))
            
    def save(self):
        '''
        Commits the data of the trasaction into data file.
        '''
        if self.working:
            data = {'Database':self.database }
            if sys.getsizeof(Database) > 1024 * 1024* 1024:
                print("Warning: size of data is exceeding 1 GB. It can't be stored")
            else:
                self.fileobj.truncate()
                self.fileobj = open(self.location,'w+')
                json.dump(data,self.fileobj)

    def clear(self):
        '''
        deletes all the record in the existing database.
        '''
        if self.working:
            self.database = {}
            self.save()

    def sizevalidate(self,key, value):
        '''
        Validates the size of key and value as per requirement.
        '''
        if len(key) > 32 or sys.getsizeof(value) > (16 * 1024):
            print("Warning: key/Value size is greater than its limit. Try again")
            return False
        if key in self.database:
            print("Error: Can't create. Key already exists.")
            return False
        return True
    
    def typevalidate(self,key,value):
        if not type(key) == str :
            print("Error: Key can only be string.")
            return False
        if not type(value) == dict:
            print("Error: Value can only be json object")
            return False
        return True



if __name__ == "__main__":
    pass