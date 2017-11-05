import arcade, arcade.key, time, random

from input_data import Input_Character
from detail_of_map import Map

SCREEN_WIDTH = 1200
SCREEN_HIGHT = 600

class Game_Character(arcade.Sprite):
    def __init__(self, *array_data, **dictionary_data):
        self.human = dictionary_data.pop("human",None)
        self.coin = dictionary_data.pop("coin",None)
        self.wood = dictionary_data.pop("wood",None)
        super().__init__(*array_data, **dictionary_data)

    def sync_with_model(self):
        if self.human:
            self.set_position(self.human.pos_x, self.human.pos_y)
        elif self.coin:
            self.coin.update()
            self.set_position(self.coin.pos_x, self.coin.pos_y)
        elif self.wood:
            self.wood.update()
            self.set_position(self.wood.pos_x, self.wood.pos_y)
            self.angle = self.wood.angler
        
    def draw(self):
        self.sync_with_model()
        super().draw()

class Game_Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.GRAY)
        self.width = width
        self.hight = height
        self.current_state = "set up game"
        self.point = 1
        self.input = Input_Character()
        self.name = "" 
        self.picture_of_interface = arcade.Sprite("images/first_page.png")
        self.picture_of_interface.set_position(293,300)
        self.price_potion = 20
        self.price_scissors = 40
        self.price_first_aid_kit = 60
        self.price_stethoscopes = 300
        
    def update(self, delta):
        if self.current_state == "game running":
            self.distance = (time.time() - self.distance_time) 
            if self.distance - self.distance_get_money > 50:
                self.money += 20*self.map.level
                self.distance_get_money = self.distance
            self.map.random_building()
            self.current_time = time.time()
            self.different_human_time = self.current_time - self.human_time
            if self.different_human_time < 0.2:
                if self.human_sprite.human.pos_y == 210:
                    self.human_sprite = Game_Character("images/human_01_80.png", human = self.human_sprite.human)
                elif self.human_sprite.human.pos_y == 150:
                    self.human_sprite = Game_Character("images/human_01_100.png", human = self.human_sprite.human)
                elif self.human_sprite.human.pos_y == 70:
                    self.human_sprite = Game_Character("images/human_01_120.png", human = self.human_sprite.human)
            elif self.different_human_time < 0.5:
                if self.human_sprite.human.pos_y == 210:
                    self.human_sprite = Game_Character("images/human_02_80.png", human = self.human_sprite.human)
                elif self.human_sprite.human.pos_y == 150:
                    self.human_sprite = Game_Character("images/human_02_100.png", human = self.human_sprite.human)
                elif self.human_sprite.human.pos_y == 70:
                    self.human_sprite = Game_Character("images/human_02_120.png", human = self.human_sprite.human)
            else:
                self.human_time = time.time()
            self.different_coin_time = self.current_time - self.coin_time
            if self.different_coin_time > 1.5:
                self.coin_count += 1
                self.coin_time = time.time()
                coin_lane = random.randint(0,99)%3+1
                self.map.set_coin(self.coin_count, coin_lane)
                if coin_lane == 1:
                    self.coin_list[self.coin_count] = Game_Character("images/coin_60.png", coin=self.map.coin_01)
                elif coin_lane == 2:
                    self.coin_list[self.coin_count] = Game_Character("images/coin_50.png", coin=self.map.coin_02)
                elif coin_lane == 3:
                    self.coin_list[self.coin_count] = Game_Character("images/coin_40.png", coin=self.map.coin_03)
                if self.coin_count > 5:
                    self.coin_count = 0
                print("keys of coin is : ",end = "")
                print(self.coin_list.keys())
            self.different_wood_time = self.current_time - self.wood_time
            if self.different_wood_time > 0.8:
                self.wood_count += 1
                wood_lane = random.randint(1,4)
                self.map.set_wood(self.wood_count, wood_lane)
                if wood_lane == 1:
                    self.wood_list[self.wood_count] = Game_Character("images/wood_60.png", wood=self.map.wood_01)
                elif wood_lane == 2:
                    self.wood_list[self.wood_count] = Game_Character("images/wood_50.png", wood=self.map.wood_02)
                elif wood_lane == 3:
                    self.wood_list[self.wood_count] = Game_Character("images/wood_40.png", wood=self.map.wood_03)
                if self.wood_count > 8:
                    self.wood_count = 0
                self.wood_time = time.time()
                print("keys of coin is : ",end = "")
                print(self.wood_list.keys())
                
    def on_draw(self):
        arcade.start_render()
        if self.current_state == "set up game":
            self.set_up_game()
        elif self.current_state == "set name":
            self.set_name()
        elif self.current_state == "game running":
            self.game_running()
        elif self.current_state == "normal interface":
            self.normal_interface()
        elif self.current_state == "shopping":
            self.shopping()
#screen 1200*600 potion 180*300 scissors 285*300 stethoscopes 270*300 first_aid_kit 255*300
    def shopping(self):
        arcade.draw_rectangle_filled(95,self.hight/2,180,self.hight-10,arcade.color.PINK)
        arcade.draw_rectangle_filled(332.5,self.hight/2,285,self.hight-10,arcade.color.PINK)
        arcade.draw_rectangle_filled(615,self.hight/2,270,self.hight-10,arcade.color.PINK)
        arcade.draw_rectangle_filled(882.5,self.hight/2,255,self.hight-10,arcade.color.PINK)
        self.map.potion.draw()
        self.map.scissors.draw()
        self.map.stethoscopes.draw()
        self.map.first_aid_kit.draw()
        arcade.draw_text("potion",95, 250, arcade.color.AMERICAN_ROSE,30,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("scissors",332.5, 250, arcade.color.AMERICAN_ROSE,30,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("stethoscopes",615, 250, arcade.color.AMERICAN_ROSE,30,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("first aid kit",882.5, 250, arcade.color.AMERICAN_ROSE,30,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("20 Bath",95, 200, arcade.color.BLACK,20,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("40 Bath",332.5, 200, arcade.color.BLACK,20,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("300 Bath",615, 200, arcade.color.BLACK,20,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("60 Bath",882.5, 200, arcade.color.BLACK,20,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("have {}".format(self.potion),95, 160, arcade.color.BLACK,15,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("have {}".format(self.scissors),332.5, 160, arcade.color.BLACK,15,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("have {}".format(self.stethoscopes),615, 160, arcade.color.BLACK,15,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("have {}".format(self.first_aid_kit),882.5, 160, arcade.color.BLACK,15,anchor_x = "center", anchor_y = "center", align = "center")
        arcade.draw_text("Your Money",1107.5 ,540 ,arcade.color.ANTIQUE_RUBY ,20 ,anchor_x = "center", anchor_y= "center", align="center")
        arcade.draw_text(str(self.all_money),1107.5 , 480 ,arcade.color.ANTIQUE_RUBY ,20 ,anchor_x = "center", anchor_y= "center", align="center")
        arcade.draw_text("EXIT" ,1107.5 ,100 ,arcade.color.AO ,30 ,anchor_x = "center", anchor_y= "center", align="center")
        if self.point == 2:
            self.draw_4_line(185.5,5,477.5,595,arcade.color.BISTRE,5,1)
        elif self.point == 1:
            self.draw_4_line(5,5,185,595,arcade.color.BISTRE,5,1)
        elif self.point == 3:
            self.draw_4_line(480,5,750,595,arcade.color.BISTRE,5,1)
        elif self.point == 4:
            self.draw_4_line(755,5,1010,595,arcade.color.BISTRE,5,1)
        elif self.point == 5:
            self.draw_4_line(1050 ,80 , 1160 ,120, arcade.color.BLACK,5,0)

    def draw_4_line(self,x1,y1,x2,y2,color,size,special):
            arcade.draw_line(x1,y1,x2,y1,color,size)
            arcade.draw_line(x1,y1,x1,y2,color,size)
            arcade.draw_line(x2,y2,x1,y2,color,size)
            arcade.draw_line(x2,y2,x2,y1,color,size)
            if special == 1:
                arcade.draw_rectangle_filled((x1+x2)/2, 80, 90, 40, arcade.color.BUD_GREEN)
                arcade.draw_text("BUY",(x1+x2)/2 ,80 ,arcade.color.YELLOW,20, anchor_x = "center", anchor_y = "center", align = "center")

    def normal_interface(self):
        arcade.draw_rectangle_filled(self.width/2,self.hight/2,self.width,self.hight,(42,209,252))
        self.picture_of_interface.draw()
        arcade.draw_text("Run Again",self.width/2+300,self.hight/2+80,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text("Shoping",self.width/2+300,self.hight/2+0,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text("Load Game",self.width/2+300,self.hight/2-80,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        if self.point == 1:
            arcade.draw_line(self.width/2-65+300,self.hight/2+70,self.width/2+65+300,self.hight/2+70,arcade.color.BROWN_NOSE,4)
        elif self.point == 2:
            arcade.draw_line(self.width/2-50+300,self.hight/2-10,self.width/2+50+300,self.hight/2-10,arcade.color.BROWN_NOSE,4)
        elif self.point == 3:
            arcade.draw_line(self.width/2-75+300,self.hight/2-90,self.width/2+75+300,self.hight/2-90,arcade.color.BROWN_NOSE,4)

    def game_running(self):
        self.map.draw_sky()
        self.map.draw_building()
        self.map.draw_road()
        for draw_coin in self.coin_list.keys():
            self.coin_list[draw_coin].draw()
            if self.coin_list[draw_coin].coin.finish == 1:
                self.coin_list[draw_coin] = Game_Character("images/gap.png", coin=self.coin_list[draw_coin].coin)
                self.coin_list[draw_coin].coin.finish = 2
        for draw_wood in self.wood_list.keys():
            self.wood_list[draw_wood].draw()
            if self.wood_list[draw_wood].wood.finish == 1:
                self.wood_list[draw_wood] = Game_Character("images/gap.png", wood=self.wood_list[draw_wood].wood)
                self.wood_list[draw_wood].wood.finish = 2
        arcade.draw_text("Distance : {:0>6.1f}".format(self.distance), 10, self.hight - 40, arcade.color.BLACK, 20)
        arcade.draw_text("Money : {:0>6.0f}".format(self.money), self.width-200, self.hight - 40, arcade.color.BLACK, 20)
        self.human_sprite.draw()

    def set_game(self):
        self.map = Map(self, self.width, self.hight)
        self.money = 0
        self.distance = 0
        self.human_sprite = Game_Character("images/human_01_100.png",human=self.map.human)
        self.human_time = time.time()
        self.coin_time = time.time()   
        self.coin_list = {}
        self.coin_count = 0
        self.wood_time = time.time()
        self.wood_list = {}
        self.wood_count = 0
        self.distance_time = time.time()
        self.distance_get_money = 0

    def set_name(self):
        arcade.draw_text("Your name",self.width/2,self.hight/2+30, arcade.color.ALABAMA_CRIMSON,30,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text(self.name,self.width/2,self.hight/2-30, arcade.color.AZURE, 30, anchor_x = "center", anchor_y = "center", align="center")
        self.first_aid_kit = 0
        self.potion = 0
        self.scissors = 0
        self.stethoscopes = 0
        self.all_money = 0
#293 300
    def set_up_game(self):
        arcade.draw_rectangle_filled(self.width/2,self.hight/2,self.width,self.hight,(42,209,252))
        self.picture_of_interface.draw()
        arcade.draw_text("New Game",self.width/2+300,self.hight/2+80,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text("Load Game",self.width/2+300,self.hight/2+0,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text("Delete Game",self.width/2+300,self.hight/2-80,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        if self.point == 1:
            arcade.draw_line(self.width/2-75+300,self.hight/2+70,self.width/2+75+300,self.hight/2+70,arcade.color.BROWN_NOSE,4)
        elif self.point == 2:
            arcade.draw_line(self.width/2-75+300,self.hight/2-10,self.width/2+75+300,self.hight/2-10,arcade.color.BROWN_NOSE,4)
        elif self.point == 3:
            arcade.draw_line(self.width/2-85+300,self.hight/2-90,self.width/2+85+300,self.hight/2-90,arcade.color.BROWN_NOSE,4)

    def on_key_press(self ,key, key_modifiers):
        print("key: {}".format(key))
        print("key_modifiers: {}".format(key_modifiers))
        if key == 65307:
            exit(0)
        if self.current_state == "set up game":
            if key == 65362 and self.point in [2,3]:
                self.point -= 1
            elif key == 65364 and self.point in [2,1]:
                self.point += 1
            elif key == 65293:
                if self.point == 1:
                    self.current_state = "set name"
                elif self.point == 2:
                    None
                elif self.point == 3:
                    None
        elif self.current_state == "set name":
            if key in range(97,123):
                self.name += self.input.return_chr(key,key_modifiers)
            elif key in [65288,65535] and len(self.name) != 0:
                self.name = self.name[:len(self.name)-1]
            elif key == 65293:
#                self.current_state = "set game"
                self.set_game()
                self.current_state = "game running"
        elif self.current_state == "game running":
            if key == 65364:
                if self.human_sprite.human.pos_y == 210:
                    self.human_sprite.human.pos_y = 150
                    self.human_sprite.human.lane = 2
                elif self.human_sprite.human.pos_y == 150:
                    self.human_sprite.human.pos_y = 70
                    self.human_sprite.human.lane = 1
            elif key == 65362:
                if self.human_sprite.human.pos_y == 150:
                    self.human_sprite.human.pos_y = 210
                    self.human_sprite.human.lane = 3
                elif self.human_sprite.human.pos_y == 70:
                    self.human_sprite.human.pos_y = 150
                    self.human_sprite.human.lane = 2
        elif self.current_state == "normal interface":
            if key == 65362 and self.point in [2,3]:
                self.point -= 1
            elif key == 65364 and self.point in [2,1]:
                self.point += 1
            elif key == 65293:
                if self.point == 1:
                    self.set_game()
                    self.current_state = "game running"
                elif self.point == 2:
                    self.current_state = "shopping"
                    self.point = 1
                elif self.point == 3:
                    None
        elif self.current_state == "shopping":
            if key == 65361 and self.point in range(2,6):
                self.point -= 1
            elif key == 65363 and self.point in range(1,5):
                self.point += 1
            elif key == 65293:
                if self.point == 5:
                    self.current_state = "normal interface"
                    self.point = 1
                elif self.point == 1 and self.all_money > self.price_potion:
                    self.all_money -= self.price_potion
                    self.potion += 1
                elif self.point == 2 and self.all_money > self.price_scissors:
                    self.all_money -= self.price_scissors
                    self.scissors += 1
                elif self.point == 3 and self.all_money > self.price_stethoscopes:
                    self.all_money -= self.price_stethoscopes
                    self.stethoscopes += 1
                elif self.point == 4 and self.all_money > self.price_first_aid_kit:
                    self.all_money -= self.price_first_aid_kit
                    self.first_aid_kit += 1

if __name__=="__main__":
    window = Game_Window(SCREEN_WIDTH, SCREEN_HIGHT)
    arcade.run()
