def linear_search(arr, target):#linear_search nhận vào một danh sách (arr) linear_search nhận vào một danh sách (arr)
    for i in range(len(arr)):# Hàm này sử dụng vòng lặp for để duyệt qua từng phần tử trong danh sách. Nếu tìm thấy phần tử trùng khớp với giá trị cần tìm (arr[i] == target), 
        if arr[i] == target:
            return i  # Trả về vị trí khi tìm thấy phần tử
    return -1  # Trả về -1 nếu không tìm thấy phần tử

# Sử dụng thuật toán tìm kiếm tuyến tính
arr = [4, 2, 9, 7, 1, 5]
target = 2
result = linear_search(arr, target)
if result != -1:
    print("Phần tử", target, "được tìm thấy tại vị trí", result)
else:
    print("Phần tử", target, "không có trong danh sách")
