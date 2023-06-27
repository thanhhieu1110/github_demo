class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

# Sử dụng stack
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Kích thước của stack:", stack.size())
print("Phần tử đầu tiên của stack:", stack.peek())
print("Phần tử lấy ra từ stack:", stack.pop())
print("Kích thước của stack sau khi pop:", stack.size())
# Stack:
# Stack là một cấu trúc dữ liệu tuân theo nguyên tắc "LIFO" (Last In, First Out), có nghĩa là phần tử cuối cùng được thêm vào là phần tử đầu tiên được lấy ra.
# Để triển khai stack trong Python, chúng ta có thể sử dụng danh sách (list) và sử dụng các phương thức của list để thực hiện các thao tác stack như push (thêm phần tử vào đỉnh stack) và pop (lấy phần tử ở đỉnh stack).
