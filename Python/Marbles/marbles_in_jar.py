# This program will determine the approximate number of marbles that will fit in a container. Allows
# for input of Marble Diameter, color and for the type of the container. Uses a defined Marble and
# Container class with box, cylinder and cone options.

import math

KEPLARS_CONJECTURE_CONST = math.pi/(3*math.sqrt(2))


class Marble:
    def __init__(self):
        self.diameter = 0
        self.color = ''
        self.volume = 0.0
        self.radius = 0.0

    def assign_volume(self):
        self.volume = (4 / 3) * math.pi * self.radius**3

    def set_diameter(self, diameter):
        self.diameter = diameter

    def set_color(self, color):
        self.color = color

    def change_marbles(self):
        self.diameter = float(input('Enter the diameter of the marbles in the container: '))
        self.radius = self.diameter / 2
        self.assign_volume()
        self.color = str(input('Enter the color of the marbles: '))
# End Marble Class


class Container:
    def __init__(self):
        self.volume = 0.0
        self.length = 0.0
        self.width = 0.0
        self.height = 0.0
        self.circumference = 0.0
        self.diameter = 0.0
        self.radius = 0.0

    def create_box(self):
        # This method receives input (length, width, and height) from the user and creates a box container
        self.length = float(input('What is the length of the box? '))
        self.width = float(input('What is the width of the box? '))
        self.height = float(input('What is the height of the box?'))
        self.volume = self.length * self.width * self.height
        return self

    def create_cylinder(self):
        # This method receives input (height and diameter) from the user and creates a cylinder container
        self.height = float(input('What is the height of the cylinder? '))
        self.diameter = float(input('What is the diameter of the cylinder? '))
        self.radius = self.diameter / 2
        self.volume = math.pi * self.radius**2 * self.height
        return self

    def create_cone(self):
        # This method receives input (height and diameter) from the user and creates a cone container
        self.height = float(input('What is the height of the cone? '))
        self.diameter = float(input('What is the diameter of the cone? '))
        self.radius = self.diameter / 2
        self.volume = (math.pi * self.radius**2 * self.height) / 3
        return self

    def choose_container_type(self):
        # This method allows the user to define the container type
        print('Choose one of the following types of containers:')
        print('1 - Box')
        print('2 - Cylinder')
        print('3 - Cone')
        selection = int(input('Which one do you want to choose:  '))
        if selection == 1:
            self.create_box()
        elif selection == 2:
            self.create_cylinder()
        elif selection == 3:
            self.create_cone()
        else:
            print('Invalid Selection. Returning to main menu...')


def simulate(marble, container):
    # This method simulates counting the number of marbles that would fit in the container based
    # on comparing the volume of the marbles to the volume of the container and applying
    # The Kepler Conjecture. See https://en.wikipedia.org/wiki/Kepler_conjecture for details.
    print('The marble has a volume of', marble.volume)
    print('The container has a volume of', container.volume)
    marble_count = (container.volume * KEPLARS_CONJECTURE_CONST) // marble.volume
    ratio = (marble_count * marble.volume) / container.volume
    print('Dead-space ratio is ', ratio)
    return marble_count


def print_main_menu():
    # This function displays the program menu and sends back the user response.
    print('Choose from the following list of options:')
    print('1 - Change the marble options')
    print('2 - Choose the type of container')
    print('3 - Run Simulation')
    print('9 - Quit Program')
    user_selection = int(input('Enter your selection: '))
    return user_selection


# Main Program Loop
my_marbles = Marble()
my_container = Container()
running = True
print('Welcome to the Marble in a Jar Guesser program')
while running:
    try:
        user_input = print_main_menu()
    except ValueError:
        print('Invalid Input. Please use only numbers...')
        user_input = print_main_menu()
    if user_input == 1:
        my_marbles.change_marbles()
    elif user_input == 2:
        my_container.choose_container_type()
    elif user_input == 3:
        try:
            result = simulate(my_marbles, my_container)
            print('Your container will hold approximately', result, my_marbles.color, 'marbles.')
        except ZeroDivisionError:
            print('You failed to configure your container....')
            print('Please ensure to configure your container and marbles before simulating.')
            print('Please try again...')
    elif user_input == 9:
        print('Thanks for using the Marble in a Jar Guesser program!')
        running = False
    else:
        print('Invalid Selection! Please try again...')
        user_input = print_main_menu()
