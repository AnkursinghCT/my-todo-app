def get_todos(filepath="todos.txt"):
    """ reads a text files and return the list
    of to do items.
    """
    with open(filepath, 'r') as file_type:
        todos_local = file_type.readlines()
    return todos_local

def write_todos(todos_arg ,filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos())

text = """hello guys just a text to understand 
rt is awseome
fight the war
"""
print(text)