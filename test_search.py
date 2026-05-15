import unittest
from search_student import search_student_data

class TestSearchStudent(unittest.TestCase):
    def test_search_by_name(self):
        results = search_student_data("nguyen")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['name'], "Nguyen Van A")

    def test_search_by_class(self):
        results = search_student_data("12a")
        self.assertEqual(len(results), 2)

    def test_search_empty_keyword(self):
        results = search_student_data("")
        self.assertEqual(results, [])

    def test_search_no_match(self):
        results = search_student_data("xyz")
        self.assertEqual(results, [])

if __name__ == '__main__':
    unittest.main()