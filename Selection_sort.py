def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Sử dụng hàm selection_sort
arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Mảng đã được sắp xếp:")
print(arr)
# Trong đoạn code trên, hàm selection_sort nhận một mảng arr làm đối số và sắp xếp mảng đó theo thứ tự tăng dần. Đầu tiên, ta lấy độ dài của mảng n. Sau đó, ta sử dụng hai vòng lặp for để duyệt qua mảng.

# Vòng lặp bên ngoài (for i in range(n)) chạy qua các phần tử từ đầu đến cuối mảng. Ta khởi tạo biến min_idx là chỉ số của phần tử nhỏ nhất tìm thấy trong phạm vi chưa được sắp xếp.

# Vòng lặp bên trong (for j in range(i + 1, n)) duyệt qua các phần tử từ i+1 đến cuối mảng. Nếu phần tử arr[j] nhỏ hơn phần tử tại chỉ số min_idx, ta cập nhật min_idx thành j.

# Sau khi hoàn thành vòng lặp bên trong, ta hoán đổi vị trí giữa phần tử tại chỉ số i và phần tử nhỏ nhất tìm thấy (arr[min_idx]). Quá trình này đảm bảo phần tử nhỏ nhất trong phạm vi chưa được sắp xếp được đặt vào vị trí đúng.

# Sau khi hoàn thành quá trình sắp xếp, ta in ra mảng đã được sắp xếp. Trong đoạn code ví dụ, mảng [64, 25, 12, 22, 11] đã được sắp xếp thành [11, 12, 22, 25, 64].