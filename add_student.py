# pyrefly: ignore [missing-import]
from data_handler import load_data, save_data
from validate_student import validate_student_data

def add_student_data(student_id, name, age, major):
    student_id = student_id.strip()
    is_valid, msg = validate_student_data({
        "id": student_id,
        "name": name,
        "age": age
    }, require_all=True)
    if not is_valid:
        return False, msg
        
    data = load_data()
    for student in data:
        if str(student['id']) == student_id:
            return False, "Lỗi: Mã sinh viên đã tồn tại!"
            
    new_student = {
        "id": student_id,
        "name": name.strip(),
        "age": age.strip(),
        "major": major.strip()
    }
    
    data.append(new_student)
    save_data(data)
    return True, "Thêm sinh viên thành công!"
