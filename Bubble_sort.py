def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Sử dụng hàm bubble_sort
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Mảng đã được sắp xếp:")
print(arr)
# Trong đoạn code trên, hàm bubble_sort nhận một mảng arr làm đối số và sắp xếp mảng đó theo thứ tự tăng dần.
#  Đầu tiên, ta lấy độ dài của mảng n. Sau đó, ta sử dụng hai vòng lặp for lồng nhau để duyệt qua từng cặp phần tử liền kề và so sánh chúng.

# Trong vòng lặp thứ nhất (for i in range(n - 1)), 
# ta duyệt qua các phần tử từ đầu đến cuối mảng, đồng thời giảm số lần lặp đi 1 sau mỗi vòng lặp. Vòng lặp thứ hai (for j in range(n - i - 1)) 
# duyệt qua các phần tử từ đầu đến phần tử cuối chưa được sắp xếp. Nếu phần tử arr[j] lớn hơn phần tử arr[j + 1], ta hoán đổi vị trí của hai phần tử này.

# Sau khi hoàn thành quá trình sắp xếp, ta in ra mảng đã được sắp xếp. Trong đoạn code ví dụ, mảng [64, 34, 25, 12, 22, 11, 90] đã được sắp xếp thành [11, 12, 22, 25, 34, 64, 90].