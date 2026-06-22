todo = []
todo.append("task1")
todo.append("task2")
todo.append("task3")
todo.insert(1, "newtask")
last = todo.pop(-1)
print(last, todo)
try:
    todo.remove("task14")
except ValueError:
    print("Task doesn't exist.")
print(todo)