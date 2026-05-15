# pyrefly: ignore [missing-import]
from data_handler import load_data, save_data
from validate_student import validate_student_data


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
                if key == "name":
                    return False, "Ho ten khong duoc de trong!"
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

    is_valid, msg = validate_student_data(cleaned_data)
    if not is_valid:
        return False, msg

    if "age" in cleaned_data:
        cleaned_data["age"] = str(int(str(cleaned_data["age"]).strip()))

    data[student_index].update(cleaned_data)
    save_data(data)
    return True, "Cap nhat sinh vien thanh cong!"
