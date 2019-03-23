import unittest

from src import app


class TestApp(unittest.TestCase):
    def test_find_closest_defibrillator_should_be_defibrillator1(self):
        defibrillator1_coordinates = app.Coordinates(longitude=0.06771044336198246694, latitude=0.7610879702554135262)
        defibrillator1 = app.Defibrillator(name='defibrillator1', coordinates=defibrillator1_coordinates)

        defibrillator2_coordinates = app.Coordinates(longitude=0.06800714511754575586, latitude=0.7609413872311810989)
        defibrillator2 = app.Defibrillator(name='defibrillator1', coordinates=defibrillator2_coordinates)

        defibrillator3_coordinates = app.Coordinates(longitude=0.06761196626214324712, latitude=0.7616544822086404043)
        defibrillator3 = app.Defibrillator(name='defibrillator1', coordinates=defibrillator3_coordinates)

        person_coordinates = app.Coordinates(latitude=0.761106269441, longitude=0.067709751625)

        defibrillators = [defibrillator1, defibrillator2, defibrillator3]
        self.assertEquals('defibrillator1', app.find_closest_defibrillator(person_coordinates=person_coordinates,
                                                                           defibrillators=defibrillators))


if __name__ == '__main__':
    unittest.main()
