#KHAI BÁO DANH SÁCH LIST
#khai báo danh sách hoc_sinh gồm các chuỗi tên của học sinh
hoc_sinh=['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy']
print(hoc_sinh)

#Khai báo danh sách diem_chu gồm các chuỗi ký tự
diem = ['A+', 'A', 'B+', 'C+', 'C', 'D+', 'D', 'F']
print(diem)

#Khai báo danh sách các số nguyên
list_so = [9,5,8,13,0,4,7,-9,11]
print(list_so)

#Khai báo danh sách với nhiều kiểu dữ liệu khác nhau
person_info = ['Mary', 1998, 'Toky0, Japan', 1.70, 65]
print(person_info)

#Khai báo danh sách rỗng
list_rong =[]
print(list_rong)

#Sử dụng hàm list tạo danh sách:
items = list('2021')
print(items)

#Truy xuất dữ liệu trong danh sách:
#Hiển thị tên học sinh ở vị trí thứ 3
print('Học sinh vị trí thứ 3: ', hoc_sinh[2])

#Hiển thị tên người - chiều cao trong biến person_info
print('Họ tên: ', person_info[0], '---Chiều cao: ', person_info[3])

#Truy xuất nhiều phần tử trong danh sách
print(list_so[3:8])

#Thay đổi giá trị của một phần tử trong danh sách
hoc_sinh = ['Lê Thùy Dung', 'Trần Đức Hùng', 'Nguyễn Lan Anh', 'Mai Phương Thúy']
print('Ban đầu: ', hoc_sinh)
hoc_sinh[2] = 'Nguyễn Thị Lan Anh'
print('Thay đổi: ', hoc_sinh)

list_so = [9,5,8,13,0,4,7,-9,11]
print('Ban đầu: ', list_so)

#Thay giá trị của phần tử cuối cùng trong list = 0
list_so[-1] = 0
print('Thay đổi:', list_so)

list_a = [8,4,8,2]
list_b = [3,0,7,6,5]
#---Cộng hai danh sách (+)---:
list_ab = list_a + list_b
print('List mới: ', list_ab)

#Lấy độ dài của danh sách list_ab: Len(list_ab)
print(list_ab, 'Có số phần tử là: ', len(list_ab))

#Kiểm tra phần tử có thuộc danh sách không?
print(list_ab)

#Kiểm tra phần tử 0:
bol_0 = 0 in list_ab
print('Phần tử 0 có thuộc list_ab ?', bol_0)

#Kiểm tra phần tử 9:
bol_9 = 9 in list_ab
print('Phần tử 9 có thuộc list_ab ?', bol_9)

print('Danh sách ban đầu: \n', list_ab)

#Thêm phần tử vào cuối danh sách:
list_ab.append(10)
print('Danh sách thêm với append:', list_ab)

#Thêm vào vị trí bất kỳ trong danh sách:
list_ab.insert(1, 100)
print('Thêm phần tử với insert:', list_ab)

list_ab.extend([7,8,0])
print('Thêm phần tử với extend:', list_ab)

#Xóa phần tử khỏi danh sách:
print('Danh sách ban đầu: \n', list_ab)

#Xóa phần tử cuối
list_ab.pop()
print('Danh sách xóa phần tử cuối: \n', list_ab)

#Xóa phần tử tại vị trí số 2
del list_ab[1]
print('Danh sách xóa phần tử ở vị trí số 2: \n', list_ab)

# Xóa phần tử có giá trị 0 xuất hiện đầu tiên
list_ab.remove(0)
print('Xóa phần tử có giá trị 0 đầu tiên: \n', list_ab)

#Đếm số lần xuất hiện của một phần tử trong danh sách
print('Danh sách ban đầu: \n', list_ab)

#Số lần xuất hiện số 8 trong danh sách
print(' Số 8 xuất hiện: ', list_ab.count(8))

#Số lần xuất hiện số 1 trong danh sách
print(' Số 1 xuất hiện: ', list_ab.count(1))

#Sắp xếp danh sách list_ab: Tăng dần
list_ab = [8, 4, 8, 2, 3, 0, 8, 6, 5, 8]
print('Danh sách ban đầu         : ', list_ab)

list_ab.sort()  #Mặc định sắp xếp theo thứ tự tăng dần
print('Danh sách sắp xếp tăng dần:', list_ab)

#Sắp xếp danh sách list_ab: Giảm dần
list_ab = [8, 4, 8, 2, 3, 0, 8, 6, 5, 8]
print('Danh sách ban đầu         :', list_ab)

list_ab.sort(reverse=True)
print('Danh sách sắp xếp giảm dần:', list_ab)

#Đảo ngược danh sách list_ab
list_ab = [8, 4, 8, 2, 3, 0, 8, 6, 5, 8]
print('Danh sách ban đầu          : ', list_ab)

list_ab.reverse()
print('Danh sách sau khi đảo ngược:',list_ab)

#Trường hợp số, chuỗi
a = 10      #Khai báo biến a có giá trị = 10
b = a       #Gán giá trị của biến a cho biến b
b = 5       #Thay đổi giá trị của biến b, bằng giá trị mới
#---------------
print('Giá trị của biến a:', a)
print('Giá trị của biến a:', a)

#Trường hợp danh sách:
ds_a = [4, 5, 8, 9]     #Khai báo danh sách ds_a
ds_b = ds_a             #Gán giá trị của biến ds_a cho ds_b
ds_b[1] = 10            #Thay đổi giá trị vị trí số 2 trong ds_b
#----------------
print('Biến ds_a: ', ds_a)
print('Biến ds_b: ', ds_b)

#Sao chép một danh sách độc lập:
ds_a = [4,5,8,9]
ds_b = ds_a.copy() #Sao chép ds_a cho ds_b
#-------------------------------
print('Biến ds_a: ', ds_a)
print('Biến ds_b: ', ds_b)

#Khai báo biến kiểu dữ liệu Boolean:
x = True
y = False
#Khai báo biến kiểu dữ liệu boolean qua biểu thức
z = 5 > 8
w = 12 == 12
#--------------
print('Kiểu dữ liệu của biến x:', type(x),', Giá trị: ', x)
print('Kiểu dữ liệu của biến y:', type(y),', Giá trị: ', y)
print('Kiểu dữ liệu của biến z:', type(z),', Giá trị: ', z)
print('Kiểu dữ liệu của biến w:', type(w),', Giá trị: ', w)

