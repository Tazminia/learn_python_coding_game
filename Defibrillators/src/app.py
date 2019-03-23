from math import cos, sqrt, pow, radians


class Coordinates:
    def __init__(self, latitude, longitude):
        self.latitude, self.longitude = latitude, longitude


class Defibrillator:
    def __init__(self, name, coordinates):
        self.name = name
        self.coordinates = coordinates


def parse_radians(number):
    return radians(float(number.replace(',', '.')))


def parse_defibrillator(defibrillator_input_line):
    number, name, address, phone, lon, lat = defibrillator_input_line.split(';')
    longitude = parse_radians(lon)
    latitude = parse_radians(lat)
    coordinates = Coordinates(longitude=longitude, latitude=latitude)
    return Defibrillator(name=name, coordinates=coordinates)


def calculate_distance(source, destination):
    if source == destination:
        return 0
    # Distance formula from puzzle
    x = (destination.longitude - source.longitude) * cos((destination.latitude + source.latitude) / 2)
    y = destination.latitude - source.latitude
    distance = sqrt(pow(x, 2) + pow(y, 2)) * 6371
    return distance


def find_closest_defibrillator(person_coordinates, defibrillators):
    defibrillator_distances = dict()
    closest_defibrillator_distance = 10**10
    closest_defibrillator = defibrillators[0].name

    for defibrillator in defibrillators:
        current_defibrillator_distance = calculate_distance(person_coordinates, defibrillator.coordinates)
        defibrillator_distances[defibrillator.name] = current_defibrillator_distance

        if closest_defibrillator_distance > current_defibrillator_distance:
            closest_defibrillator = defibrillator.name
            closest_defibrillator_distance = current_defibrillator_distance

    return closest_defibrillator
