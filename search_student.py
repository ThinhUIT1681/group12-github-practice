# pyrefly: ignore [missing-import]
from data_handler import load_data

def search_student_data(keyword):
    """Tìm kiếm sinh viên và trả về danh sách kết quả cho GUI"""
    keyword = keyword.strip().lower()
    data = load_data()
    results = []
    
    for student in data:
        if keyword in str(student['id']).lower() or keyword in str(student['name']).lower():
            results.append(student)
            
    return results
