def print_hello():
    print(say_hello())
    print(say_hello('Gene'))

def say_hello(name=''):
    if (name == ''):
        return 'hello default'
    else:
        return f'hello {name}'

def list_has_even(nums):
    return get_first_even(nums) != -1

def get_first_even(nums):
    for num in nums:
        if is_even(num):
            return num
    
    return -1

def get_all_even(nums):
    evens = []
    for num in nums:
        if is_even(num):
            evens.append(num)

    return evens

def get_max(nums):
    return max(nums)

def is_even(num):
    return num % 2 == 0

def is_num(num):
    return 

# print_hello()
# num = int(input('Enter a number: '))
# print(is_even(num))
# num_list = range(1,num + 1,10)
# print(f'{num_list} is even: {list_has_even(num_list)}')

# if list_has_even(num_list):
#     print(f'{num_list} first even: {get_first_even(num_list)}')
#     print(f'all the evens are: {get_all_even(num_list)}')

# print(f'max number is {max(num_list)}')

def parse_emp_file(emp_file):
    work_hours = {}
    emp_file.seek(0)
    lines = [parse_emp_line(line) for line in emp_file.readlines()]
    for name,hours in lines:
        work_hours[name] = hours

    return work_hours

def parse_emp_line(file_line):
    lineItems = file_line.split(':')
    if len(lineItems) == 2:
        return (lineItems[0], int(lineItems[1]))
    else:
        return ('',0)

def write_emp_file(emp_file, work_hours):
    for name,hours in work_hours.items():
        if name != '' and int(hours) > 0:
            emp_file.write(f'{name}:{int(hours)}\n')


def accept_user_input(work_hours):
    is_continue = len(work_hours) == 0 or input('Update work hours?').lower == 'y'
    while is_continue:
        name = input('Enter name: ')
        hours = int(input('Enter hours: '))
        print(f'{name} worked {hours} hours.')
        retry = input('Is this correct? ')
        if retry.lower() == 'y':
            print(f'updating {name}\'s hours to {hours}')
            work_hours.update({(name,hours)})
        
        is_continue = input('Continue? ').lower() == 'y'
    
    return work_hours

def update_emp_record(file_name,work_hours):
    if len(work_hours) > 0:
        with open(file_name, 'w+') as f:
            write_emp_file(f,work_hours)
    else:
        print('no work hours')

def read_emp_record(file_name):
    work_hours = {}
    with open(file_name, 'w+') as f:
        work_hours = parse_emp_file(f)
    
    return work_hours

def print_work_hours(work_hours):
    if len(work_hours) > 0:
        for name,hours in work_hours.items():
            print(f'{name}:{hours}')
    else:
        print('no work hours')

def get_max_work_hours(work_hours):
    current_max_hours = {}
    for name,hours in work_hours.items():
        if len(current_max_hours) == 0 or int(hours) > max(current_max_hours.keys()):
            current_max_hours[hours] = [name]
        elif int(hours) == max(current_max_hours.keys()):
            current_max_hours[hours].append(name)
    
    return current_max_hours

def get_average_work_hours(work_hours):
    total_employees = len(work_hours)
    total_hours = sum(work_hours.values())
    return total_hours / total_employees


input('Press enter to start ')
file_name = input('Enter file name: ')
if file_name == '':
    file_name = 'test.txt'
print('Using file: ' + file_name)
work_hours = read_emp_record(file_name)
print('Current work hours: ')
print_work_hours(work_hours)
work_hours = accept_user_input(work_hours)
print('New work hours: ')
print_work_hours(work_hours)

update_emp_record(file_name, work_hours)

print('Updated work hours: ')
print_work_hours(read_emp_record(file_name))
max_hours = get_max_work_hours(work_hours)
for name in max_hours[max(max_hours.keys())]:
    print(f'most hours worked: {max(max_hours.keys())} by {name}')
print(f'average work hours: {get_average_work_hours(work_hours)}')