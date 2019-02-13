SIZE = 100
stack = [0] * SIZE
top = -1
def push(item):
    global top, stack
    if top >= SIZE - 1:
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top, stack
    if top == -1:
        print("Stack is Empty!")
        return 0
    else:
        result = stack[top]
        # stack[top] = 0 하지않고 다음에 push할때 값이 변경 (지우는거x)
        # 다른 값으로 바뀌기 전까지는 복구 가능
        top -= 1
        return result

push(1)
push(2)
push(3)
item = pop()
print(f"pop item => {item}")
item = pop()
print(f"pop item => {item}")
item = pop()
print(f"pop item => {item}")
print(top, stack)