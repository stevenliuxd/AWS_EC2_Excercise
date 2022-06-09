from ec2_functions import instance_report

print("Welcome to Steven's AWS excercise!")

while True:

    print("\n1. Display ec2 instances\n2. Display ingress rules\n3. Exit\n")
    print('Please select: ')
    selection = input()

    if selection == '1':
        result = instance_report()
        print(f'\nResult:\n{result}')
    elif selection == '2':
        pass
    elif selection == '3':
        exit(1)
    else:
        print('\nWarning: Please select between options 1 to 3.')
        pass

