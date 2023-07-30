import unittest
from tur_oppdatert import Tur, Posisjon


class TestTur(unittest.TestCase):
    def test_slutttidspunkt(self):
        tur_1 = Tur('Tur 1', 20, 40)
        tur_2 = Tur('Tur 2', 20, 25)

        self.assertGreaterEqual(tur_1.sluttidspunkt, tur_1.starttidspunkt)
        self.assertGreaterEqual(tur_2.sluttidspunkt, tur_2.starttidspunkt)

    def test_add_posisjon(self):
        tur_1 = Tur('Tur 1', 20, 40)
        tur_2 = Tur('Tur 2', 20, 25)
        pos_1 = Posisjon(2, 4, 20)
        pos_2 = Posisjon(6, 1, 25)
        tur_1.add_posisjon(pos_1)
        tur_2.add_posisjon(pos_2)

        self.assertEqual(pos_1, tur_1.posisjoner[-1])
        self.assertEqual(pos_2, tur_2.posisjoner[-1])

    def test_add_posisjon_koordinater(self):
        tur_1 = Tur('Tur 1', 20, 40)
        tur_2 = Tur('Tur 2', 20, 25)
        x_1, y_1, h_1 = 7, 4, 10
        x_2, y_2, h_2 = 8, 2, 50
        pos_1 = Posisjon(x_1, y_1, h_1)
        pos_2 = Posisjon(x_2, y_2, h_2)
        tur_1.add_posisjon_koordinater(x_1, y_1, h_1)
        tur_2.add_posisjon_koordinater(x_2, y_2, h_2)

        self.assertEqual(pos_1, tur_1.posisjoner[-1])
        self.assertEqual(pos_2, tur_2.posisjoner[-1])

    def test_er_rundtur(self):
        tur_1 = Tur('Tur 1', 20, 40)
        tur_1.add_posisjon_koordinater(2, 4, 20)
        tur_1.add_posisjon_koordinater(2, 4, 20)
        tur_2 = Tur('Tur 2', 26, 120)
        tur_2.add_posisjon_koordinater(2, 4, 20)
        tur_2.add_posisjon_koordinater(3, 4, 20)

        self.assertTrue(tur_1.er_rundtur())
        self.assertFalse(tur_2.er_rundtur())

    def test_hoydemeter(self):
        tur_1 = Tur('Tur 1', 20, 40)
        tur_1.add_posisjon_koordinater(2, 4, 30)
        tur_1.add_posisjon_koordinater(2, 8, 20)
        tur_1.add_posisjon_koordinater(6, 3, 50)
        tur_1.add_posisjon_koordinater(2, 4, 30)

        tur_2 = Tur('Tur 2', 10, 30)
        tur_2.add_posisjon_koordinater(2, 4, 30)
        tur_2.add_posisjon_koordinater(2, 8, 25)
        tur_2.add_posisjon_koordinater(6, 3, 45)
        tur_2.add_posisjon_koordinater(2, 4, 38)

        self.assertEqual(tur_1.hoydemeter(), 60)
        self.assertNotEqual(tur_2.hoydemeter(), 67)


if __name__ == '__main__':
    unittest.main()
