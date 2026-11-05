import unittest

from bmi_service import bmi_guidance, calculate_bmi, parse_positive_number


class BmiGuidanceTests(unittest.TestCase):
    def test_taiwan_adult_thresholds(self):
        for bmi, category in [
            (18.4, "體重過輕"),
            (18.5, "健康體位"),
            (23.9, "健康體位"),
            (24.0, "體重過重"),
            (26.9, "體重過重"),
            (27.0, "肥胖"),
        ]:
            with self.subTest(bmi=bmi):
                self.assertEqual(bmi_guidance(bmi)["label"], category)

    def test_calculate_bmi(self):
        self.assertAlmostEqual(calculate_bmi(170, 65), 22.4913, places=3)

    def test_parse_positive_number_rejects_invalid_values(self):
        for value in ("", "0", "-1", "nan", "inf", "invalid"):
            with self.subTest(value=value):
                self.assertIsNone(parse_positive_number(value))


if __name__ == "__main__":
    unittest.main()
