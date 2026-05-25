student_name = input("Nhap ten sinh vien: ")
student_age = int(input("Nhap tuoi: "))
average_score = float(input("Nhap diem trung binh: "))

bonus_score = average_score + 0.5

print("\nThong tin sinh vien:")
print(f"Ten sinh vien: {student_name}")
print(f"Tuoi: {student_age}")
print(f"Diem trung binh: {average_score}")
print(f"Diem sau thuong: {bonus_score}")

print("\nKieu du lieu cua cac bien:")
print(type(student_name))
print(type(student_age))
print(type(average_score))
print(type(bonus_score))