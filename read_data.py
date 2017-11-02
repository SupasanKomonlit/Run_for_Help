class Game_Data:
    def __init__(self):
        file_name = open("save_data/name_data.txt")
        data_name = file_name.readlines()
        self.list_name = {}
        for data in data_name:
            self.list_name = 
