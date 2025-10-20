import random


class Car:
    def __init__(self, license_plate, maximum_speed):
        self.license_plate = license_plate
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change_of_speed):
        self.current_speed += change_of_speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        if hours > 0:
            self.travelled_distance += self.current_speed * hours


def race():
    cars = []
    for i in range(1, 11):
        plate = f"ABC-{i}"
        max_speed = random.randint(100, 200)
        cars.append(Car(plate, max_speed))

    race_finished = False
    while not race_finished:
        for car in cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)
            if car.travelled_distance >= 10000:
                race_finished = True
                break

    cars.sort(key=lambda x: x.travelled_distance, reverse=True)
    return cars