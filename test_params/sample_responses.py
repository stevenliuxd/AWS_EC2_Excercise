instance_response = [{'Instance ID': 'i-0e85d4a77301ec602', 'Name': 'webserver 1', 'Instance Type': 't1.micro', 
'Security Group IDs': 'sg-0d86fb90a180ef0aa  '}, {'Instance ID': 'i-047ae0eea184a32a8', 
'Name': 'database', 'Instance Type': 't1.micro', 'Security Group IDs': 'sg-00a99efae992dbd6e  '}]

rule_one_response = [{'Security Group ID': 'sg-00a99efae992dbd6e', 'port': 22, 'Cidr': '127.0.0.0/32'}]
rule_two_response = [{'Security Group ID': 'sg-0d86fb90a180ef0aa', 'port': 22, 'Cidr': '50.66.186.96/32'}, {'Security Group ID': 'sg-0d86fb90a180ef0aa', 'port': 443, 'Cidr': '50.66.186.96/32'}]