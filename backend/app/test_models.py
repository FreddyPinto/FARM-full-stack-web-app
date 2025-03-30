import unittest
from models import CarModel
from pydantic import ValidationError


class TestCarModel(unittest.TestCase):
    def test_valid_car(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 1500,
            "km": 120000,
            "price": 10000,
        }
        car = CarModel(**car_data)
        self.assertEqual(car.brand, "Ford")
        self.assertEqual(car.make, "Fiesta")
        self.assertEqual(car.year, 2019)
        self.assertEqual(car.cm3, 1500)
        self.assertEqual(car.km, 120000)
        self.assertEqual(car.price, 10000)

    def test_invalid_year_too_low(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 1969,
            "cm3": 1500,
            "km": 120000,
            "price": 10000,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)

    def test_invalid_year_too_high(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2026,
            "cm3": 1500,
            "km": 120000,
            "price": 10000,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)
    
    def test_invalid_cm3_too_low(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 0,
            "km": 120000,
            "price": 10000,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)

    def test_invalid_cm3_too_high(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 5001,
            "km": 120000,
            "price": 10000,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)

    def test_invalid_km_too_low(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 1500,
            "km": 0,
            "price": 10000,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)

    def test_invalid_km_too_high(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 1500,
            "km": 5000001,
            "price": 10000,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)

    def test_invalid_price_too_low(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 1500,
            "km": 120000,
            "price": 0,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)
    
    def test_invalid_price_too_high(self):
        car_data = {
            "brand": "Ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 1500,
            "km": 120000,
            "price": 1000001,
        }
        with self.assertRaises(ValidationError):
            CarModel(**car_data)
    
    def test_brand_title_case(self):
        car_data = {
            "brand": "ford",
            "make": "Fiesta",
            "year": 2019,
            "cm3": 1500,
            "km": 120000,
            "price": 10000,
        }
        car = CarModel(**car_data)
        self.assertEqual(car.brand, "Ford")

    def test_make_title_case(self):
        car_data = {
            "brand": "Ford",
            "make": "fiesta",
            "year": 2019,
            "cm3": 1500,
            "km": 120000,
            "price": 10000,
        }
        car = CarModel(**car_data)
        self.assertEqual(car.make, "Fiesta")
    
    def test_optional_id(self):
      car_data = {
        "brand": "Ford",
        "make": "fiesta",
        "year": 2019,
        "cm3": 1500,
        "km": 120000,
        "price": 10000,
      }
      car = CarModel(**car_data)
      self.assertIsNone(car.id)

if __name__ == "__main__":
    unittest.main()
