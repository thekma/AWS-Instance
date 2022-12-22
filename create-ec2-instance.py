import boto3

r_ec2 = boto3.resource('ec2')
ec2_client = boto3.client("ec2") #Client, like resource, used to allow configuration of AWS

sgn = "new-group" #Setting the name, can be made open to ask user for a specific name

connect = ec2_client.create_security_group(GroupName=sgn, #Making the details of the security group for the instance
                                        Description="new-vpc",
                                        VpcId="vpc-01e42630fd956d4f5")

security_group_id = connect["GroupId"] #Using the details to create the security group ID

security_group_config = ec2_client.authorize_security_group_ingress( #Allow editing of the security group, with specific ports
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': "tcp",
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': "0.0.0.0/0"}]
        },
        {
            'IpProtocol': "tcp",
            'FromPort': 443,
            'ToPort': 443,
            'IpRanges': [{'CidrIp': "0.0.0.0/0"}]
        },
        {
            'IpProtocol': "tcp",
            'FromPort': 80,
            'ToPort': 80,
            'IpRanges': [{'CidrIp': "0.0.0.0/0"}]
        }
    ]
)

response = r_ec2.create_instances(InstanceType="t2.micro", #Creating an instance on AWS using the following data
                                MaxCount=1,
                                MinCount=1,
                                ImageId="ami-0b0dcb5067f052a63",
                                KeyName="ec2-key",
                                TagSpecifications=[
                                    {
                                        'ResourceType': 'instance',
                                        'Tags': [
                                                {
                                                    'Key': 'Name',
                                                    'Value': 'ServerA'
                                                },
                                            ]
                                        },
                                ],
                                SecurityGroupIds=[security_group_id],
                                SubnetId="subnet-020556bb1f4e249c7"
                                )
