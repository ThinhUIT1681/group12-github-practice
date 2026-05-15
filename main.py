import tkinter as tk
from tkinter import ttk, messagebox

try:
    from add_student import add_student_data
except ImportError:
    def add_student_data(*args): return False, "Chức năng Thêm SV đang được phát triển"

try:
    from display_students import get_all_students
except ImportError:
    def get_all_students(): return []

try:
    from search_student import search_student_data
except ImportError:
    def search_student_data(*args): return []

try:
    from delete_student import delete_student_data
except ImportError:
    def delete_student_data(*args): return False, "Chức năng Xóa SV đang được phát triển"

class StudentManagerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Chương trình Quản lý Sinh viên")
        self.root.geometry("800x500")
        
        # --- Khung nhập liệu ---
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=15)
        
        tk.Label(input_frame, text="Mã SV:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.ent_id = tk.Entry(input_frame, width=20)
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Họ và Tên:").grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)
        self.ent_name = tk.Entry(input_frame, width=30)
        self.ent_name.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(input_frame, text="Tuổi:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.ent_age = tk.Entry(input_frame, width=20)
        self.ent_age.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Chuyên ngành:").grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)
        self.ent_major = tk.Entry(input_frame, width=30)
        self.ent_major.grid(row=1, column=3, padx=5, pady=5)
        
        # --- Khung nút bấm ---
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=5)
        
        tk.Button(btn_frame, text="Thêm SV", command=self.add_student, width=12).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Xóa SV (chọn bảng)", command=self.delete_student, width=15).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Hiển thị tất cả", command=self.load_table, width=12).grid(row=0, column=2, padx=10)
        
        tk.Label(btn_frame, text="Tìm kiếm:").grid(row=0, column=3, padx=(20, 5))
        self.ent_search = tk.Entry(btn_frame, width=20)
        self.ent_search.grid(row=0, column=4, padx=5)
        tk.Button(btn_frame, text="Tìm", command=self.search_student, width=8).grid(row=0, column=5, padx=5)

        # --- Bảng hiển thị (Treeview) ---
        cols = ("ID", "Name", "Age", "Major")
        self.tree = ttk.Treeview(self.root, columns=cols, show="headings", height=15)
        self.tree.heading("ID", text="Mã SV")
        self.tree.heading("Name", text="Họ và Tên")
        self.tree.heading("Age", text="Tuổi")
        self.tree.heading("Major", text="Chuyên ngành")
        
        self.tree.column("ID", width=100, anchor=tk.CENTER)
        self.tree.column("Name", width=250, anchor=tk.W)
        self.tree.column("Age", width=80, anchor=tk.CENTER)
        self.tree.column("Major", width=200, anchor=tk.W)
        
        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        # Tải dữ liệu khi mở app
        self.load_table()

    def load_table(self):
        """Lấy toàn bộ dữ liệu và nạp vào bảng"""
        # Xóa dữ liệu cũ trên bảng
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        data = get_all_students()
        for s in data:
            self.tree.insert("", tk.END, values=(s['id'], s['name'], s['age'], s['major']))

    def add_student(self):
        """Xử lý sự kiện bấm nút Thêm SV"""
        s_id = self.ent_id.get()
        name = self.ent_name.get()
        age = self.ent_age.get()
        major = self.ent_major.get()
        
        success, msg = add_student_data(s_id, name, age, major)
        if success:
            messagebox.showinfo("Thành công", msg)
            self.load_table() # Cập nhật lại bảng
            
            # Xóa các ô nhập liệu
            self.ent_id.delete(0, tk.END)
            self.ent_name.delete(0, tk.END)
            self.ent_age.delete(0, tk.END)
            self.ent_major.delete(0, tk.END)
        else:
            messagebox.showerror("Lỗi", msg)

    def delete_student(self):
        """Xử lý sự kiện xóa SV đang chọn trên bảng"""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Cảnh báo", "Vui lòng click chọn một sinh viên trên bảng để xóa!")
            return
            
        item = self.tree.item(selected[0])
        student_id = item['values'][0]
        
        confirm = messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa sinh viên mã {student_id}?")
        if confirm:
            success, msg = delete_student_data(student_id)
            if success:
                messagebox.showinfo("Thành công", msg)
                self.load_table()
            else:
                messagebox.showerror("Lỗi", msg)

    def search_student(self):
        """Xử lý sự kiện tìm kiếm"""
        keyword = self.ent_search.get()
        if not keyword.strip():
            self.load_table()
            return
            
        results = search_student_data(keyword)
        
        # Xóa dữ liệu cũ trên bảng
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        # Hiển thị kết quả tìm kiếm
        for s in results:
            self.tree.insert("", tk.END, values=(s['id'], s['name'], s['age'], s['major']))

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagerGUI(root)
    root.mainloop()
