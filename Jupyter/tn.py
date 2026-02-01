def main():
    classroom_data = []

    while True:
        
        print("--- QUẢN LÝ DỮ LIỆU LỚP HỌC ---")
        print("1. Thêm học sinh mới (Add a new student)")
        print("2. Tìm kiếm theo ID (Search by student ID)")
        print("3. Hiển thị tất cả điểm (Display all scores)")
        print("4. Thoát (Exit)")
        
        choice = input("Nhập lựa chọn của bạn (1-4): ")

        if choice == '1':
            print("-- Nhập thông tin --")
            s_id = input("Nhập ID học sinh: ")
            name = input("Nhập tên học sinh: ")
            try:
                score = float(input("Nhập điểm số: "))
                
                student_record = {
                    "id": s_id,
                    "name": name,
                    "score": score
                }
                
                classroom_data.append(student_record)
                print(f"Đã thêm học sinh {name} thành công!")
            except ValueError:
                print("Lỗi: Điểm số phải là một con số.")

        elif choice == '2':
            search_id = input("Nhập ID cần tìm: ")
            found = False
            
            for student in classroom_data:
                if student['id'] == search_id:
                    print(f"--> TÌM THẤY: Tên: {student['name']} | Điểm: {student['score']}")
                    found = True
                    break 
            
            if found==False:
                print(f"Không tìm thấy học sinh nào có ID là {search_id}")

        elif choice == '3':
            print("--- BẢNG ĐIỂM LỚP HỌC ---")
            if not classroom_data:
                print("Danh sách trống.")
            else:
                print(f"{'ID':<10} {'Tên':<20} {'Điểm':<10}")
                print("-" * 40)
                for student in classroom_data:
                    print(f"{student['id']:<10} {student['name']:<20} {student['score']:<10}")

        elif choice == '4':
            print("Đã thoát chương trình.")
            break
        
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


main()