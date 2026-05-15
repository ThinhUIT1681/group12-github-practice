import re


def is_valid_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", str(email)) is not None


def is_valid_phone(phone):
    phone = str(phone).strip()
    return phone.isdigit() and 9 <= len(phone) <= 11


def validate_student_data(student_data, require_all=False):
    student_id = str(student_data.get("id", "")).strip()
    name = str(student_data.get("name", "")).strip()

    if require_all or "id" in student_data:
        if not student_id:
            return False, "Ma sinh vien khong duoc de trong!"

    if require_all or "name" in student_data:
        if not name:
            return False, "Ho ten khong duoc de trong!"

    if require_all or "age" in student_data:
        age_value = str(student_data.get("age", "")).strip()
        if not age_value:
            return False, "Tuoi phai la so nguyen hop le!"
        try:
            age = int(age_value)
            if age < 0:
                return False, "Tuoi phai la so nguyen hop le!"
        except ValueError:
            return False, "Tuoi phai la so nguyen hop le!"

    if "email" in student_data and str(student_data.get("email", "")).strip():
        if not is_valid_email(student_data["email"]):
            return False, "Email khong hop le!"

    if "phone" in student_data and str(student_data.get("phone", "")).strip():
        if not is_valid_phone(student_data["phone"]):
            return False, "So dien thoai chi gom chu so va co do dai tu 9 den 11!"

    return True, ""
