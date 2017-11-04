import arcade, arcade.key, random

from detail_of_character import Main_Character, Coin, Wood_Box

class Map:
    def __init__(self, main_program, width, hight):
        self.width = width
        self.hight = hight
        self.main = main_program
        self.level = 1
#        self.human = Main_Character(self,40, 70)
        self.human = Main_Character(self,40, 150)
#        self.human = Main_Character(self,40, 250)

    def draw_road(self):
        arcade.draw_line(0,10,self.width,10,arcade.color.YELLOW,3)
        arcade.draw_line(0,100,self.width,100,arcade.color.YELLOW,3)
        arcade.draw_line(0,170,self.width,170,arcade.color.YELLOW,3)
        arcade.draw_line(0,220,self.width,220,arcade.color.RED,3)
    
    def draw_sky(self):
        arcade.draw_rectangle_filled(0,220,self.width,self.hight,arcade.color.COLUMBIA_BLUE)
    
    def set_coin(self, coin_id, lane):
        self.coin_01 = Coin(self,1260,50,coin_id, lane)
        self.coin_02 = Coin(self,1260,135,coin_id, lane)
        self.coin_03 = Coin(self,1260,200,coin_id, lane)

#  picture building_01 140*201
#  picture building_02 175*300
#  picture hospital 230*330
#  picture seven 145*157
