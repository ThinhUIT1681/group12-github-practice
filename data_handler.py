import json
import os

FILE_PATH = "students.json"

def load_data():
    """Tải dữ liệu sinh viên từ file JSON."""
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(data):
    """Lưu trữ danh sách sinh viên vào file JSON."""
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
