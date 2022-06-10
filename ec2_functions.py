import boto3


def instance_report():

    # Pull aws instances
    try:
        aws = boto3.client('ec2') 
        reservations_ec2 = aws.describe_instances()
        instances_ec2 = reservations_ec2['Reservations']
    except Exception as e:
        print(f"\nError retrieving aws data. Please check your connection and/or configure the settings on the cli via 'aws configure'. The error: {e}\n")
        exit(1)

    try:
        # Append to readable dict
        instances_filtered = []

        # Iterate through all instances
        for instance in instances_ec2:

            # Extract required information
            sub_group = instance['Instances'][0]
            instance_id = sub_group['InstanceId']
            name = sub_group['Tags'][0]['Value']
            instance_type = sub_group['InstanceType']
            security_groups = sub_group['SecurityGroups']

            # Extract all security group IDs (in the example, there is only one per instance)
            security_group_list = []
            for security_group in security_groups:
                security_group_list.append(security_group['GroupId']) 
            
            # Convert security groups to horizontal string display (incase there is more than one, seperate with space)
            security_group_str = ''
            for security_group in security_group_list:
                security_group_str = security_group_str + security_group + '  '
            
            # Append current instance
            instances_filtered.append({'Instance ID': instance_id, 'Name': name, 'Instance Type': instance_type, 'Security Group IDs': security_group_str})
        
        # Print results in a table to the user
        str_format = "{:<22} {:<14} {:<16} {:<20}"
        print("\n----------------------------------------------------------------------------------")
        print(str_format.format('Instance ID', 'Name', 'Instance Type', 'Security Group IDs'))
        for instance in instances_filtered:
            print(str_format.format(instance['Instance ID'], instance['Name'], instance['Instance Type'], instance['Security Group IDs']))
        print("----------------------------------------------------------------------------------")

        # Return dict (for testing)
        return instances_filtered

    except Exception as e:
         print(f"\nUnknown error: {e}\n")
         exit(1)

    
def ingress_rules(security_group):
    pass
