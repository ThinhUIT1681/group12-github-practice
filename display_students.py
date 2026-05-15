# pyrefly: ignore [missing-import]
from data_handler import load_data

def get_all_students():
    """Trả về toàn bộ danh sách sinh viên để hiển thị lên bảng GUI"""
    return load_data()
