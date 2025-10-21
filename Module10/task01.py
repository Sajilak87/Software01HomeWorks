class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

        def go_to_floor(self, count):
            while self.current_floor < top_floor:
                floor_up()
            while self.current_floor > top_floor:
                floor_down()

        def floor_up(self):
            if self.current_floor + 1 >= self.top_floor:
                self.current_floor = self.top_floor
            else:
                self.current_floor = self.current_floor + 1

        def floor_down(self):
            if self.current_floor - 1 <= self.bottom_floor:
                self.current_floor = self.bottom_floor
            else:
                self.current_floor = self.current_floor - 1

