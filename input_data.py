import arcade, arcade.key

class Input_Character:
    def __init__(self):
        super().__init__()
        all_count = 97
        self.upper_dictionary = {}
        self.lower_dictionary = {}
        lower_count = 97
        upper_count = 65
        while all_count < 123:
            self.upper_dictionary[all_count] = chr(upper_count)
            self.lower_dictionary[all_count] = chr(lower_count)
            lower_count += 1
            upper_count += 1
            all_count += 1
    def return_chr(self,code,capital):
        if capital in [1,8,9,17,24,25]:
            return self.upper_dictionary[code]
        else:
            return self.lower_dictionary[code]

if __name__=="__main__":
    start = Input_Character()
    print(start.upper_dictionary)
    print(start.lower_dictionary)
