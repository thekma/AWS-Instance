import boto3

ec2_r = boto3.resource("ec2")

instance = ec2_r.Instance("i-0c500a69946d45924") #The EC2 uses 'Instance' function to recognize the instance ID, put into variable

instance.terminate() #Destroys the EC2 server respective to the instance ID

instance.wait_until_terminated() #Continues to run until the termination finishes completely
