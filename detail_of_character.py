import arcade

class Main_Character:
    def __init__(self, detail_map, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lane = 2

class Coin:
    def __init__(self, detail_map, pos_x, pos_y, coin_id, coin_lane):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.map = detail_map
        self.id = coin_id
        self.lane = coin_lane
        self.finish = 0
        if self.lane == 1:
            self.distance = 15
        elif self.lane == 2:
            self.distance = 10
        else:
            self.distance = 6

    def update(self):
        if self.finish == 2:
            None
        elif self.pos_x < 0:
            self.finish = 1
        elif self.map.main.human_sprite.human.lane == self.lane and self.pos_x in range(self.map.main.human_sprite.human.pos_x-self.distance,self.map.main.human_sprite.human.pos_x+self.distance+1):
            self.map.main.money += self.map.level * 10
            self.finish = 1
        else:
            self.pos_x -= self.map.level*5

class Wood_Box:
    None

class Building(arcade.Sprite):
    def __init__(self, detail_map, location_picture, pos_x, pos_y, distance_x, building_id):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.distance = distance_x
        self.id = building_id
        self.map = detail_map
        self.finish = False
        super().__init__(location_picture)
    
    def update(self):
        if not self.finish:
            self.pos_x -= self.map.level * 3
            if self.pos_x < (-1)*self.distance:
                self.finish = True
            self.set_position(self.pos_x,self.pos_y)

    def draw(self):
        self.update()
        super().draw()
