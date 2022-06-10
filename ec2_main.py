from ec2_functions import instance_report, ingress_rules

print("\nWelcome to Steven's AWS excercise!")

while True:

    print("\n1. Display ec2 instances\n2. Display ingress rules\n3. Exit\n")
    print('Please select: ')
    selection = input()

    if selection == '1':
        instance_report()
    elif selection == '2':
        print('\nEnter the security group ID: ')
        security_group = input()
        ingress_rules(security_group)
    elif selection == '3':
        exit(1)
    else:
        print('\nWarning: Please select between options 1 to 3.')
        pass



