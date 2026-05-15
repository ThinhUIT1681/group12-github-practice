# pyrefly: ignore [missing-import]
import re

from data_handler import load_data, save_data


def _is_valid_email(email):
    return re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email) is not None


def _is_valid_phone(phone):
    return phone.isdigit() and 9 <= len(phone) <= 11


def update_student_data(student_id, updated_data):
    """Cap nhat thong tin sinh vien va tra ve ket qua cho GUI."""
    student_id = str(student_id).strip()
    if not student_id:
        return False, "Ma sinh vien khong duoc de trong!"

    if not isinstance(updated_data, dict):
        return False, "Du lieu cap nhat khong hop le!"

    data = load_data()
    student_index = None

    for i, student in enumerate(data):
        if str(student.get("id")) == student_id:
            student_index = i
            break

    if student_index is None:
        return False, "Loi: Khong tim thay ma sinh vien nay."

    cleaned_data = {}
    for key, value in updated_data.items():
        if value is None:
            continue

        if isinstance(value, str):
            value = value.strip()
            if not value:
                if key == "id":
                    return False, "Ma sinh vien khong duoc de trong!"
                continue

        cleaned_data[key] = value

    new_id = str(cleaned_data.get("id", student_id)).strip()
    if not new_id:
        return False, "Ma sinh vien khong duoc de trong!"

    if new_id != student_id:
        for student in data:
            if str(student.get("id")) == new_id:
                return False, "Loi: Ma sinh vien da ton tai!"
        cleaned_data["id"] = new_id

    if "name" in cleaned_data and not str(cleaned_data["name"]).strip():
        return False, "Ho ten khong duoc de trong!"

    if "age" in cleaned_data:
        try:
            age = int(cleaned_data["age"])
            if age < 0:
                return False, "Tuoi phai la so nguyen hop le!"
            cleaned_data["age"] = str(age)
        except (TypeError, ValueError):
            return False, "Tuoi phai la so nguyen hop le!"

    if "email" in cleaned_data and not _is_valid_email(str(cleaned_data["email"])):
        return False, "Email khong hop le!"

    if "phone" in cleaned_data and not _is_valid_phone(str(cleaned_data["phone"])):
        return False, "So dien thoai chi gom chu so va co do dai tu 9 den 11!"

    data[student_index].update(cleaned_data)
    save_data(data)
    return True, "Cap nhat sinh vien thanh cong!"
