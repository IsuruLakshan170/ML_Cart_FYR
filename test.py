x = 10  # global variable

def print_number():
    print(x)  # accessing global variable from within function

def increase_number():
    global x  # specifying that we want to modify the global variable
    x += 1   # modifying global variable

# print_number()  # Output: 10
# increase_number()
# print_number()  # Output: 11
