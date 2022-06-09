import boto3
import json

def instance_report():
    # Pull aws instances
    aws = boto3.client('ec2') 
    reservations_ec2 = aws.describe_instances()
    instances_ec2 = reservations_ec2['Reservations']

    # Append to readable dict
    instances_filtered = {'instances': []}

    # Iterate through all instances
    for instance in instances_ec2:

        # Extract required information
        sub_group = instance['Instances'][0]
        instance_id = sub_group['InstanceId']
        name = sub_group['Tags'][0]['Value']
        instance_type = sub_group['InstanceType']
        security_groups = sub_group['SecurityGroups']

        # Extract all security group IDs 
        security_group_list = []
        for security_group in security_groups:
            security_group_list.append(security_group['GroupId']) 
        
        instances_filtered['instances'].append({'Instance ID': instance_id, 'Name': name, 'Instance Type': instance_type, 'Security Group IDs': security_group_list})
    
    # Convert to JSON and return response
    response = json.dumps(instances_filtered, indent=4)
    return response


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

