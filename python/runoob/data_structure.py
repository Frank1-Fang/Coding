# 1. Stack 将列表当做栈使用
# 栈是一种后进先出（LIFO, Last-In-First-Out）数据结构，意味着最后添加的元素最先被移除
# 用 append() 方法可以把一个元素添加到栈顶
# 用不指定索引的 pop() 方法可以把一个元素从栈顶释放出来

# Stack operations 栈操作
# 压入（Push）: 将一个元素添加到栈的顶端。
# 弹出（Pop）: 移除并返回栈顶元素。
# 查看栈顶元素（Peek/Top）: 返回栈顶元素而不移除它。
# 检查是否为空（IsEmpty）: 检查栈是否为空。
# 获取栈的大小（Size）: 获取栈中元素的数量。

class Stack:
    def __init__(self):             # 创建一个空栈（初始化）
        self.stack = []

    def push(self, item):           # 压入（Push）操作
        self.stack.append(item)     # 使用 append() 方法将元素添加到栈的顶端

    def pop(self):                  # 弹出（Pop）操作
        if not self.is_empty():     
            return self.stack.pop() # 使用 pop() 方法移除并返回栈顶元素
        else:
            raise IndexError("pop from empty stack")

    def peek(self):                 # 查看栈顶元素（Peek/Top）
        if not self.is_empty():
            return self.stack[-1]   # 直接访问列表的最后一个元素（不移除）
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):             # 检查是否为空（IsEmpty）
        return len(self.stack) == 0 # 检查列表是否为空

    def size(self):                 # 获取栈的大小（Size）
        return len(self.stack)      # 使用 len() 函数获取栈中元素的数量

# 使用示例
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("栈顶元素:", stack.peek())        # 输出: 栈顶元素: 3
print("栈大小:", stack.size())          # 输出: 栈大小: 3

print("弹出元素:", stack.pop())         # 输出: 弹出元素: 3
print("栈是否为空:", stack.is_empty())  # 输出: 栈是否为空: False
print("栈大小:", stack.size())          # 输出: 栈大小: 2

# 2. Queue 队列
# 队列是一种先进先出（FIFO, First-In-First-Out）的数据结构，意味着最早添加的元素最先被移除
# 使用列表时，如果频繁地在列表的开头插入或删除元素，性能会受到影响，因为这些操作的时间复杂度是 O(n)
# 为了解决这个问题，Python 提供了 collections.deque，它是双端队列，可以在两端高效地添加和删除元素
from collections import deque

# 创建一个空队列
queue = deque()

# 向队尾添加元素
queue.append('a')
queue.append('b')
queue.append('c')

print("队列状态:", queue)            # 输出: 队列状态: deque(['a', 'b', 'c'])

# 从队首移除元素
first_element = queue.popleft()
print("移除的元素:", first_element)  # 输出: 移除的元素: a
print("队列状态:", queue)            # 输出: 队列状态: deque(['b', 'c'])

# 查看队首元素（不移除）
front_element = queue[0]
print("队首元素:", front_element)    # 输出: 队首元素: b

# 检查队列是否为空
is_empty = len(queue) == 0
print("队列是否为空:", is_empty)     # 输出: 队列是否为空: False

# 获取队列大小
size = len(queue)
print("队列大小:", size)             # 输出: 队列大小: 2