# This module implements the Building Class for use in Roman Empire RTS City Builder Game
FILE_LOCATION = '\Images\Buildings\\'


class Building:
    def __init__(self):
        self.level = 1  # Default level of a building is 1, not 0
        self.type = ''
        self.file = ''
        self.range = 0
        self.locationx = 0  # X-coordinate for building
        self.locationy = 0  # y-coordinate for building
        self.has_entertainment = False
        self.entertainment_level = 0
        self.has_food = False
        self.food_level = 0
        self.has_education = False
        self.education_level = 0
        self.has_religion = False
        self.religion_level = 0
        self.has_bath_access = False
        self.has_road_access = False
        self.has_doctor = False
        self.medical_level = 0
        self.has_water = False
        self.water_level = 0
        self.desirability_level = 1

    def new_building(self, building_type, x, y, range):
        self.type = building_type
        self.locationx = x
        self.locationy = y
        self.file = FILE_LOCATION + building_type + str(self.level) + '.png'
        self.range = range

    def determine_entertainment(self, building_list):
        # This method needs to determine if a entertainment building falls within its range and then set the
        # building's 'has_entertainment' attribute to True.

        # First determine which buildings are within range
        buildings_in_range = []
        for building in building_list:
            if (building.locationx - self.locationx) ^ 2 + (building.locationy - self.locationy) ^ 2 <= self.range ^ 2:
                buildings_in_range.append(building)

        # Now we determine if the building is an entertainment building. If so we declare it as having access to
        # entertainment and increase it's entertainment level by 1
        for building in buildings_in_range:
            if building.type == 'Theater' or building.type == 'Amphitheater' or building.type == 'Coliseum':
                self.has_entertainment = True
                self.entertainment_level += 1

    def determine_food(self, building_list):
        # This method determines if the building has access to food through markets. It will first
        # need to determine if there is a market within its range, then determine if the market has food.
        # If both requirements are met, it will obtain food from the market (house food level goes up,
        # market goes down) and set the 'has_food' attribute to True

        # First determine which buildings are within range
        buildings_in_range = []
        for building in building_list:
            if (building.locationx - self.locationx) ^ 2 + (building.locationy - self.locationy) ^ 2 <= self.range ^ 2:
                buildings_in_range.append(building)

        # Next we determine if the building is a market, determine if the house needs food and then get food from market
        for building in buildings_in_range:
            if building.type == 'Market':
                self.has_food = True
                if self.food_level < 500:
                    building.food_level -= 100
                    self.food_level += 100

    def determine_education(self, building_list):
        # This method determines if the building has access to education facilities (schools, libraries, academies)

        # First determine which buildings are within range
        buildings_in_range = []
        for building in building_list:
            if (building.locationx - self.locationx) ^ 2 + (building.locationy - self.locationy) ^ 2 <= self.range ^ 2:
                buildings_in_range.append(building)

        # Now we determine if the building is an education building. If so we declare it as having access to
        # education and increase it's education level by 1
        for building in buildings_in_range:
            if building.type == 'School' or building.type == 'Library' or building.type == 'Academy':
                self.has_education = True
                self.education_level += 1

    def determine_religion(self, building_list):
        # This method determines if the building has access to a temple or shrine

        # First determine which buildings are within range
        buildings_in_range = []
        for building in building_list:
            if (building.locationx - self.locationx) ^ 2 + (building.locationy - self.locationy) ^ 2 <= self.range ^ 2:
                buildings_in_range.append(building)

        # Now we determine if the building is an religious building. If so we declare it as having access to
        # religion and increase it's religion level by 1
        for building in buildings_in_range:
            if building.type == 'Temple' or building.type == 'Shrine':
                self.has_religion = True
                self.religion_level += 1

    def determine_water(self):
        # This method determines if the building has access to either a well or a fountain
        pass

    def determine_medical_access(self):
        # This method determines if the building has access to a clinic or hospital
        pass
