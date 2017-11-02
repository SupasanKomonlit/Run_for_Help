import arcade, arcade.key, time
from input_data import Input_Character
SCREEN_WIDTH = 800
SCREEN_HIGHT = 600

class Game_Character(arcade.Sprite):
    def __init__(self, *array_data, **dictionary_data):
        None

    def sync_with_model(self):
        None

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

    def update(self, data):
        None

    def on_draw(self):
        arcade.start_render()
        if self.current_state == "set up game":
            self.set_up_game()
        elif self.current_state == "set name":
            self.set_name()

    def set_name(self):
        arcade.draw_text("Your name",self.width/2,self.hight/2+30, arcade.color.ALABAMA_CRIMSON,30,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text(self.name,self.width/2,self.hight/2-30, arcade.color.AZURE, 30, anchor_x = "center", anchor_y = "center", align="center")

    def set_up_game(self):
        arcade.draw_text("New Game",self.width/2,self.hight/2+80,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text("Load Game",self.width/2,self.hight/2+0,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        arcade.draw_text("Delete Game",self.width/2,self.hight/2-80,arcade.color.RED,20,anchor_x="center",anchor_y="center",align="center")
        if self.point == 1:
            arcade.draw_line(self.width/2-75,self.hight/2+70,self.width/2+75,self.hight/2+70,arcade.color.BROWN_NOSE,4)
        elif self.point == 2:
            arcade.draw_line(self.width/2-75,self.hight/2-10,self.width/2+75,self.hight/2-10,arcade.color.BROWN_NOSE,4)
        elif self.point == 3:
            arcade.draw_line(self.width/2-85,self.hight/2-90,self.width/2+85,self.hight/2-90,arcade.color.BROWN_NOSE,4)

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
                self.current_state = "game running"
            
if __name__=="__main__":
    window = Game_Window(SCREEN_WIDTH, SCREEN_HIGHT)
    arcade.run()
