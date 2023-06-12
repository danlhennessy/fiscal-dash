import unittest
from src.flask_app import create_pie_chart


class TestCreatePieChart(unittest.TestCase):
    def test_create_pie_chart(self):
        data = [
            (1, "user1", "category1", 10),
            (2, "user2", "category2", 10),
            (3, "user3", "category3", 10),
            (4, "user2", "category3", 40)
        ]
        result_html = create_pie_chart(data)

        self.assertIsInstance(result_html, str)
        self.assertTrue(3000000 <= len(result_html) <= 5000000)


if __name__ == '__main__':
    unittest.main()
