def line(customers):
    if len(customers) == 0:
        print('The line is currently empty.')
    else:
        message = 'The line is currently:'
        for i in range(len(customers)):
            message += f' {i + 1}. {customers[i]}'
        print(message)

def take_a_number(line, customer):
    if len(line) == 0:
        print(f"Welcome, {customer}. You are number 1 in line.")
        line.append(customer)
        return line
    else:
        print(f"Welcome, {customer}. You are number {len(line) + 1} in line.")
        line.append(customer)
        return line

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {line[0]}.")
        del line[0]