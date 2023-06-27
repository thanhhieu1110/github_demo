def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Trả về vị trí khi tìm thấy phần tử
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Trả về -1 nếu không tìm thấy phần tử

# Sử dụng thuật toán tìm kiếm nhị phân
arr = [1, 2, 4, 5, 7, 9]
target = 7
result = binary_search(arr, target)
if result != -1:
    print("Phần tử", target, "được tìm thấy tại vị trí", result)
else:
    print("Phần tử", target, "không có trong danh sách")
