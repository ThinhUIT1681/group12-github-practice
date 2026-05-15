# pyrefly: ignore [missing-import]
from data_handler import load_data

def search_student_data(keyword):
    """Tìm kiếm sinh viên và trả về danh sách kết quả cho GUI"""
    keyword = keyword.strip().lower()
    if not keyword:
        return []  # Trả về rỗng nếu từ khóa trống
    data = load_data()
    results = []
    
    for student in data:
        for key, value in student.items():
            if isinstance(value, str) and keyword in value.lower():
                results.append(student)
                break  # Tránh trùng lặp
            
    return results
