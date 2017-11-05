import arcade, arcade.key, random

from detail_of_character import Main_Character, Coin, Wood, Building

class Map:
    def __init__(self, main_program, width, hight):
        self.width = width
        self.hight = hight
        self.main = main_program
        self.level = 1
#        self.human = Main_Character(self,40, 70)
        self.human = Main_Character(self,40, 150)
#        self.human = Main_Character(self,40, 250)
        self.building_array = []
        self.past_building = 0
        self.count_building = 0
        self.current_building = 0
        self.max_building = False
        self.have_hospital = -1
        self.potion = arcade.Sprite("images/potion.png")
        self.first_aid_kit = arcade.Sprite("images/first_aid_kit.png")
        self.scissors = arcade.Sprite("images/scissors.png")
        self.stethoscopes = arcade.Sprite("images/stethoscopes.png")
        self.potion.set_position(95,425)
        self.first_aid_kit.set_position(882.5,425)
        self.scissors.set_position(332.5,425)
        self.stethoscopes.set_position(615,425)
#95 332.5 615 882.5

    def draw_road(self):
        arcade.draw_line(0,10,self.width,10,arcade.color.YELLOW,3)
        arcade.draw_line(0,100,self.width,100,arcade.color.YELLOW,3)
        arcade.draw_line(0,170,self.width,170,arcade.color.YELLOW,3)
        arcade.draw_line(0,220,self.width,220,arcade.color.RED,3)
    
    def draw_sky(self):
        arcade.draw_rectangle_filled(600,410,self.width,380,arcade.color.COLUMBIA_BLUE)

    def random_building(self):
        self.type_building = random.randint(0,4)%4+1
        if not self.max_building:
            if self.past_building == 0:
                self.building_array.append(Building(self, "images/building_01.png", self.width + self.distance_x(1), self.distance_y(1), self.distance_x(1), self.count_building))
                self.past_building = 1
                self.count_building += 1
            elif self.type_building == 1 and self.building_array[self.count_building -1].pos_x < self.width - self.distance_x(self.past_building):
                self.building_array.append(Building(self, "images/building_01.png", self.width + self.distance_x(self.type_building), self.distance_y(self.type_building), self.distance_x(self.type_building), self.count_building))
                self.past_building = self.type_building
                self.count_building += 1
            elif self.type_building == 2 and self.building_array[self.count_building -1].pos_x < self.width - self.distance_x(self.past_building):
                self.building_array.append(Building(self, "images/building_02.png", self.width + self.distance_x(self.type_building), self.distance_y(self.type_building), self.distance_x(self.type_building), self.count_building))
                self.past_building = self.type_building
                self.count_building += 1
            elif self.type_building == 4 and self.building_array[self.count_building -1].pos_x < self.width - self.distance_x(self.past_building) and self.past_building != 4:
                self.building_array.append(Building(self, "images/seven.png", self.width + self.distance_x(self.type_building), self.distance_y(self.type_building), self.distance_x(self.type_building), self.count_building))
                self.past_building = self.type_building
                self.count_building += 1
            if self.count_building == 13:
                self.max_building = True
        else:
            if self.current_building == 0:
                self.check_building = 12
            else:
                self.check_building = self.current_building - 1
            if self.have_hospital == -1:
                self.type_building = 3
                self.have_hospital = 0
            elif self.have_hospital < 6:
                if self.type_building == 3:
                    self.type_building = 2
            if self.type_building == 1 and self.building_array[self.check_building].pos_x < self.width - self.building_array[self.check_building].distance:
                self.building_array[self.current_building] = Building(self, "images/building_01.png", self.width+self.distance_x(self.type_building), self.distance_y(self.type_building), self.distance_x(self.type_building), self.current_building)
                self.past_building = self.type_building
                self.current_building += 1
                self.have_hospital += 1
            elif self.type_building == 2 and self.building_array[self.check_building].pos_x < self.width - self.building_array[self.check_building].distance:
                self.building_array[self.current_building] = Building(self, "images/building_02.png", self.width+self.distance_x(self.type_building), self.distance_y(self.type_building), self.distance_x(self.type_building), self.current_building)
                self.past_building = self.type_building
                self.current_building += 1
                self.have_hospital += 1
            elif self.type_building == 4 and self.building_array[self.check_building].pos_x < self.width - self.building_array[self.check_building].distance and self.past_building != 4:
                self.building_array[self.current_building] = Building(self, "images/seven.png", self.width+self.distance_x(self.type_building), self.distance_y(self.type_building), self.distance_x(self.type_building), self.current_building)
                self.past_building = self.type_building
                self.current_building += 1
                self.have_hospital += 1
            elif self.type_building == 3 and self.building_array[self.check_building].pos_x < self.width - self.building_array[self.check_building].distance:
                self.building_array[self.current_building] = Building(self, "images/hospital.png", self.width+self.distance_x(self.type_building), self.distance_y(self.type_building), self.distance_x(self.type_building), self.current_building)
                self.past_building = self.type_building
                self.current_building += 1
                self.have_hospital = 0
                if self.level < 2:
                    self.level += 0.5
                elif self.level < 4:
                    self.level += 0.3
                else:
                    self.level += 0.1
            if self.current_building == 13:
                self.current_building = 0
#            print(self.have_hospital)
            
    def distance_x(self, type_building):
        if type_building == 1:
            return 70
        elif type_building == 2:
            return 87.5
        elif type_building == 3:
            return 115
        else:
            return 72.5

    def distance_y(self, type_building):
        if type_building == 1:
            return 100 + 220
        elif type_building == 2:
            return 150 + 220
        elif type_building == 3:
            return 165 + 220
        else:
            return 78.5 + 220

    def draw_building(self):
        for draw in range(len(self.building_array)):
            if not self.building_array[draw].finish:
                self.building_array[draw].draw()

    def draw_score(self):
        None
    
    def set_coin(self, coin_id, lane):
        self.coin_01 = Coin(self,1260,50,coin_id, lane)
        self.coin_02 = Coin(self,1260,135,coin_id, lane)
        self.coin_03 = Coin(self,1260,200,coin_id, lane)
    
    def set_wood(self, wood_id, lane):
        self.wood_01 = Wood(self,1260,50,wood_id, lane)
        self.wood_02 = Wood(self,1260,135,wood_id, lane)
        self.wood_03 = Wood(self,1260,200,wood_id, lane)

#  picture building_01 140*201
#  picture building_02 175*300
#  picture hospital 230*330
#  picture seven 145*157
