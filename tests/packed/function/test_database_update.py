import unittest
from tests.packed.test_database import TestDatabase
from src.database import retrieve_database, update_database


class TestUpdateDatabase(TestDatabase):
    def test_retrieve_database(self):
        update_database(
            "test_table",
            ["id", "name", "age"],
            [1, "Dan", 30],
            self.connection
            )

        result = retrieve_database(
            "test_table",
            ["id", "name", "age"],
            self.connection
            )

        expected_result = [(1, 'Dan', 30)]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
