from random import Random
from car import Car


def is_position_occupied(new_car, starting_cars):
    for car_in_list in starting_cars:
        if car_in_list.ycor() == new_car.ycor():
            return True
    return False


class CarManager:
    all_cars = []

    def create_cars(self):
        num_cars = Random().randint(0, 5)
        print(num_cars, len(self.all_cars))
        starting_cars = []
        for _ in range(num_cars):
            car = Car()
            if not is_position_occupied(car, starting_cars):
                self.all_cars.append(car)
            else:
                car.hideturtle()
                car.clear()

    def move_cars(self):
        for _ in range(Random().randint(0, 5)):
            for car in self.all_cars:
                car.move()

        self.create_cars()
