import boto3

ec2_client = boto3.client("ec2")

sgn = "new-group"
connect = ec2_client.create_security_group(GroupName=sgn,
                                        Description="new-vpc",
                                        VpcId="vpc-01e42630fd956d4f5")

security_group_id = connect["GroupId"]

security_group_config = ec2_client.authorize_security_group_ingress(
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

print(security_group_id)