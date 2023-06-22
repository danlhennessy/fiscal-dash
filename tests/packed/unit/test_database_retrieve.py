import unittest
from tests.packed.test_database import TestDatabase
from src.database import retrieve_database


class TestRetrieveDatabase(TestDatabase):
    def test_retrieve_database(self):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO test_table (id, name, age) VALUES (1, 'John', 25)"
            )
        cursor.execute(
            "INSERT INTO test_table (id, name, age) VALUES (2, 'Jane', 30)"
            )
        self.connection.commit()

        result = retrieve_database(self.connection)

        expected_result = [(1, 'John', 25), (2, 'Jane', 30)]
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
