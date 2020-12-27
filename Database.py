import json

class Base:
    database = {}
    location = ""
    def __init__(self, location):
        #validation required to be done
        self.location  = location
        try:
            FileObj = open(location,'r+')
            data = json.load(FileObj)
        except:
            data = {"Database":{}}
            FileObj = open(location,'w+')
        self.database = data["Database"]

        
    def create(self,key,value):
        self.database[key] = value
        
    def read(self,key):
        return self.database[key]
    
    def delete(self,key):
        return self.database.pop(key)
    
    def update(self,key,value):
        self.database[key] = value
    
    def show(self):
        for i in self.database:
            print("{}  : {}".format(i,self.database[i]))
            
    def save(self):
        data = {'Database':self.database}
        with open(self.location, 'w+') as FileObj:
              json.dump(data,FileObj)
                
    def __del__(self):
        data = {'Database':self.database}
        with open(self.location, 'w+') as FileObj:
            json.dump(data,FileObj)


if __name__ == "__main__":
    pass