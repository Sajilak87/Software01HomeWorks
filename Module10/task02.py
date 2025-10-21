class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1

    def go_to_floor(self, target_floor):
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators

        self.elevators = []
        for _ in range(number_of_elevators):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevators.append(elevator)

    def run_elevator(self, elevator_number, destination_floor):
        self.elevators[elevator_number].go_to_floor(destination_floor)