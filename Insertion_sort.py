def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

# Sử dụng hàm insertion_sort
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Mảng đã được sắp xếp:")
print(arr)
# Trong đoạn code trên, hàm insertion_sort nhận một mảng arr làm đối số và sắp xếp mảng đó theo thứ tự tăng dần. Đầu tiên, ta lấy độ dài của mảng n.

# Vòng lặp bên ngoài (for i in range(1, n)) chạy qua các phần tử từ vị trí thứ hai đến cuối mảng. Ta gán giá trị của phần tử hiện tại vào biến key. Biến j được sử dụng để duyệt qua các phần tử trong phần đã sắp xếp, bắt đầu từ vị trí trước đó của i.

# Vòng lặp bên trong (while j >= 0 and arr[j] > key) được sử dụng để di chuyển các phần tử lớn hơn key về sau. Các phần tử này được dịch chuyển một vị trí sang phải và j giảm giá trị để trỏ tới phần tử trước đó.

# Sau khi hoàn thành vòng lặp bên trong, ta gán key vào vị trí đúng trong phần đã sắp xếp.

# Sau khi hoàn thành quá trình sắp xếp, ta in ra mảng đã được sắp xếp. Trong đoạn code ví dụ, mảng [12, 11, 13, 5, 6] đã được sắp xếp thành