def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Sử dụng hàm quicksort
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quicksort(arr, 0, n - 1)
print("Mảng đã được sắp xếp:")
print(arr)
# Hàm partition(arr, low, high) được sử dụng để chia mảng thành hai phần, với một phần chứa các phần tử nhỏ hơn hoặc bằng pivot và phần còn lại chứa các phần tử lớn hơn pivot. Trong đó, low và high là chỉ số của phần tử đầu và cuối của mảng cần sắp xếp. Ban đầu, ta gán i = low - 1 và chọn pivot là phần tử cuối cùng của mảng (arr[high]). Sau đó, vòng lặp for duyệt qua các phần tử từ low đến high - 1. Nếu phần tử arr[j] nhỏ hơn hoặc bằng pivot, ta tăng chỉ số i lên 1 và hoán đổi vị trí của arr[i] và arr[j] để đưa phần tử nhỏ hơn pivot vào phần đầu mảng.

# Sau khi kết thúc vòng lặp, ta hoán đổi vị trí của pivot (phần tử cuối cùng của mảng) với phần tử đầu tiên của phần lớn hơn pivot. Quá trình này chia mảng thành hai phần, với các phần tử nhỏ hơn pivot nằm bên trái và các phần tử lớn hơn pivot nằm bên phải.

# Hàm quicksort(arr, low, high) thực hiện việc đệ quy để sắp xếp các phần tử trong mảng. Đầu tiên, ta kiểm tra điều kiện low < high để đảm bảo rằng mảng có nhiều hơn một phần tử. Sau đó, ta sử dụng hàm partition để chia mảng thành hai phần và lấy chỉ số pi của pivot sau khi đã được sắp xếp đúng vị trí. Tiếp theo, ta gọi đệ quy hàm quicksort cho phần tử nhỏ hơn pivot (từ low đến pi - 1) và cho phần tử lớn hơn pivot (từ pi + 1 đến high).

# Cuối cùng, ta sử dụng hàm quicksort để sắp xếp mảng arr từ vị trí đầu (0) đến vị trí cuối (n - 1, với n là độ dài của mảng). Sau khi hoàn thành quá trình sắp xếp, ta in ra mảng đã được sắp xếp. 