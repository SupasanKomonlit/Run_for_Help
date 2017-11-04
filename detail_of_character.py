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
