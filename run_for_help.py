import arcade

SCREEN_WIDTH = 800
SCREEN_HIGHT = 500

class Game_Character(arcade.Sprite):
    def __init__(self, *array_data, **dictionary_data):

    def sync_with_model(self):

    def draw(self):
        self.sync_with)model()
        super().draw()

class Game_window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(widht, height)
        arcade.set_background_color(arcade.color.GRAY)
        self.current_state = "set up game"

    def update(self, data):


    def on_draw(self):
        arcade.start_render()
        if self.curent_state == "set up game":
            self.set_up_game()

    def set_up_game(self):
        arcade.draw_text("")

if __name__=="__main__":
    window = Game_Window(SCREEN_WIDTH, SCREEN_HIGHT)
    arcade.run()
