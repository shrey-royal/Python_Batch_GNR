class Car:
    def __init__(self, make, model, year, color):
        """
        Initialize a Car Object.

        :param make: The manufacturer of the car (e.g., 'Toyota').
        :param model: The model of the car (e.g., 'Corolla').
        :param year: The year the car was manufactured (e.g., 2022).
        :param color: The color of the car (e.g., 'Blue').
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start(self):
        """Start the car"""
        if not self.is_running:
            self.is_running = True
            print(f"The {self.color} {self.make} {self.model} is now running.")
        else:
            print(f"The {self.color} {self.make} {self.model} is already running!")

    def stop(self):
        """Stop the car"""
        if self.is_running:
            self.is_running = False
            print(f"The {self.color} {self.make} {self.model} is now off.")
        else:
            print(f"The {self.color} {self.make} {self.model} is already off!")

    def drive(self):
        """Drive the car"""
        if self.is_running:
            print(f"The {self.color} {self.make} {self.model} is now driving.")
        else:
            print(f"You need to start the {self.color} {self.make} {self.model} first!")

    def repaint(self, new_color: str):
        """Repaint the car a new color"""
        print(f"The {self.make} {self.model} is now being repainted from {self.color} to {new_color}.")
        self.color = new_color

if __name__ == "__main__":
    c = Car("Hyundai", "i20 sportz", 2024, "white")

    c.start()
    c.drive()
    c.stop()
    c.drive()
    c.repaint("black")
    c.start()
    c.drive()
    c.stop