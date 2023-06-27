from collections import deque
class Queue:
    def __init__(self):
        self.items = deque()
    def is_empty(self):
        return len(self.items) == 0
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    def size(self):
        return len(self.items)
# Sử dụng queue
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Kích thước của queue:", queue.size())
print("Phần tử đầu tiên của queue:", queue.peek())
print("Phần tử lấy ra từ queue:", queue.dequeue())
print("Kích thước của queue sau khi dequeue:", queue.size())
# Queue:
# 	Queue là một cấu trúc dữ liệu tuân theo nguyên tắc "FIFO" (First In, First Out), có nghĩa là phần tử đầu tiên được thêm vào là phần tử đầu tiên được lấy ra.
# 	Để triển khai queue trong Python, chúng ta có thể sử dụng module collections và lớp deque để tạo một hàng đợi. Lớp deque cung cấp các phương thức như append (thêm phần tử vào cuối hàng đợi) và popleft (lấy phần tử từ đầu hàng đợi).
