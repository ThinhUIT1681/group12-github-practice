# pyrefly: ignore [missing-import]
from data_handler import load_data, save_data

def delete_student_data(student_id):
    """Xóa sinh viên theo mã và trả về kết quả cho GUI"""
    data = load_data()
    
    for i, student in enumerate(data):
        if str(student['id']) == str(student_id):
            del data[i]
            save_data(data)
            return True, "Xóa sinh viên thành công!"
            
    return False, "Lỗi: Không tìm thấy mã sinh viên này."
