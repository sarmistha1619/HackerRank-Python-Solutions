'''
without creating any funtion
first = input()
last = input()
print(f"Hello {first} {last}! You just delved into python.")
'''

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)