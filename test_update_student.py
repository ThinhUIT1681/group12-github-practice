import unittest
from unittest.mock import patch

from update_student import update_student_data


class TestUpdateStudent(unittest.TestCase):
    def setUp(self):
        self.students = [
            {
                "id": "1",
                "name": "Nguyen Van A",
                "age": "20",
                "major": "CNTT",
                "email": "a@example.com",
                "phone": "0912345678"
            },
            {
                "id": "2",
                "name": "Tran Thi B",
                "age": "21",
                "major": "Ke toan",
                "email": "b@example.com",
                "phone": "0987654321"
            }
        ]
        self.saved_data = None

    def fake_load_data(self):
        return [student.copy() for student in self.students]

    def fake_save_data(self, data):
        self.saved_data = data

    def test_update_student_success(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("1", {
                "name": "Nguyen Van A Updated",
                "age": "22",
                "major": "Khoa hoc may tinh"
            })

        self.assertTrue(success)
        self.assertEqual(msg, "Cap nhat sinh vien thanh cong!")
        self.assertEqual(self.saved_data[0]["name"], "Nguyen Van A Updated")
        self.assertEqual(self.saved_data[0]["age"], "22")
        self.assertEqual(self.saved_data[0]["major"], "Khoa hoc may tinh")

    def test_update_keeps_old_fields_when_value_empty(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("1", {
                "age": "",
                "major": "An toan thong tin"
            })

        self.assertTrue(success)
        self.assertEqual(self.saved_data[0]["age"], "20")
        self.assertEqual(self.saved_data[0]["major"], "An toan thong tin")

    def test_update_student_not_found(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("99", {"name": "Khong Ton Tai"})

        self.assertFalse(success)
        self.assertEqual(msg, "Loi: Khong tim thay ma sinh vien nay.")
        self.assertIsNone(self.saved_data)

    def test_update_duplicate_id(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("1", {"id": "2"})

        self.assertFalse(success)
        self.assertEqual(msg, "Loi: Ma sinh vien da ton tai!")
        self.assertIsNone(self.saved_data)

    def test_update_empty_student_id(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("", {"name": "Ten Moi"})

        self.assertFalse(success)
        self.assertEqual(msg, "Ma sinh vien khong duoc de trong!")

    def test_update_empty_name_is_invalid(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("1", {"name": ""})

        self.assertFalse(success)
        self.assertEqual(msg, "Ho ten khong duoc de trong!")

    def test_update_invalid_age(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("1", {"age": "abc"})

        self.assertFalse(success)
        self.assertEqual(msg, "Tuoi phai la so nguyen hop le!")

    def test_update_invalid_email(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("1", {"email": "abc"})

        self.assertFalse(success)
        self.assertEqual(msg, "Email khong hop le!")

    def test_update_invalid_phone(self):
        with patch("update_student.load_data", self.fake_load_data), \
             patch("update_student.save_data", self.fake_save_data):
            success, msg = update_student_data("1", {"phone": "09abc"})

        self.assertFalse(success)
        self.assertEqual(msg, "So dien thoai chi gom chu so va co do dai tu 9 den 11!")


if __name__ == "__main__":
    unittest.main()
