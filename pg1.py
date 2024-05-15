def collect_info(func):
    def inner():
        name = input("Enter name:")
        location = input("Enter location:")
        print(f'Name is:{name}')
        print(f'Address is : {location}')
        func()
    return inner

@collect_info
def office():
    print("Office name is Bosch")
    return 


office()

