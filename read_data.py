class Game_Data:
    def __init__(self):
        self.file_name = open("save_data/name_data.txt",'r+')
        self.data_name = self.file_name.readlines()
        self.list_name = []
        for data in self.data_name:
            self.list_name.append("save_data/"+data+".txt")
        print("list name is")
        print (self.list_name)

    def add_name_data(self, name)

    def read_data(self,key):
        
