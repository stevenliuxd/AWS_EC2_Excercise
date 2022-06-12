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
        print('\nEC2 Instances:')
        print("----------------------------------------------------------------------------------")
        print(str_format.format('Instance ID', 'Name', 'Instance Type', 'Security Group IDs'))
        for instance in instances_filtered:
            print(str_format.format(instance['Instance ID'], instance['Name'], instance['Instance Type'], instance['Security Group IDs']))
        print("----------------------------------------------------------------------------------")

        # Return dict (for testing)
        return instances_filtered

    except Exception as e:
         print(f"\nUnknown error: {e}\n")
         exit(1)

def ingress_rules(user_group_raw):

    try:
        # Strip whitespaces off entry
        user_group = user_group_raw.strip()

        try:
            # Pull security group description
            aws = boto3.client('ec2') 
            describe_output = aws.describe_security_groups()
            security_group_list = describe_output["SecurityGroups"]
        except Exception as e:
            print(f"\nError retrieving aws data. Please check your connection and/or configure the settings on the cli via 'aws configure'. The error: {e}\n")
            exit(1)

        # Iterate through all security groups to find the specified one
        desired_security_group = {}
        for security_group in security_group_list:
            if security_group["GroupId"] == user_group:
                desired_security_group = security_group
        
        # Check if security group has been found
        if desired_security_group == {}:
            print(f'\nUnable to find security group {user_group}.')
            return []

        # Display the ingress rules for that security group showing the CIDR and port
        ip_permissions_list = desired_security_group["IpPermissions"]
        rules_total = []
        warn = False
        for ip_permission in ip_permissions_list:
            port = ip_permission["FromPort"]
            cidr_group = ip_permission["IpRanges"]
            for cidr_iter in cidr_group:
                cidr = cidr_iter["CidrIp"]
                rules_total.append({"Security Group ID": user_group, "port": port, "Cidr": cidr})

                # Display a warning if any of the rules in the security group allow for inbound traffic from any IP address
                if "127.0.0.0" in cidr:
                    warn = True
                elif "0.0.0.0" in cidr:
                    warn = True

        # Print Results
        print('\nIngress Rules:')
        str_format = "{:<24} {:<20} {:<10}"
        print("----------------------------------------------------------------------------------")
        print(str_format.format('Security Group ID', 'CIDR', 'Port'))
        for rule in rules_total:
            print(str_format.format(rule['Security Group ID'], rule['Cidr'], rule['port']))
        print("----------------------------------------------------------------------------------")

        # Print warning for traffic from any IP
        if warn is True:
            print("WARNING: Rule(s) in the security group allows for inbound traffic from ANY IP address.")

        # Return for testing
        return [rules_total, warn]

    except Exception as e:
        print(f"\nUnknown error: {e}\n")
        exit(1)



    