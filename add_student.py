from data_handler import load_data, save_data

def add_student_data(student_id, name, age, major):
    student_id = student_id.strip()
    if not student_id:
        return False, "Mã sinh viên không được để trống!"
        
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
