import arcade, arcade.key
from detail_of_character import Main_Character, Coin, Wood_Box

class Map:
    def __init__(self, main_program, width, hight):
        self.width = width
        self.hight = hight
        self.main = main_program
        self.level = 1
#        self.human = Main_Character(self,40, 60)
        self.human = Main_Character(self,40, 150)
#        self.human = Main_Character(self,40, 190)

    def draw_road(self):
        arcade.draw_line(0,10,self.width,10,arcade.color.YELLOW,3)
        arcade.draw_line(0,100,self.width,100,arcade.color.YELLOW,3)
        arcade.draw_line(0,170,self.width,170,arcade.color.YELLOW,3)
        arcade.draw_line(0,220,self.width,220,arcade.color.RED,3)
