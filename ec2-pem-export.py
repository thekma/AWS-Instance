import boto3 #Have this to access AWS on Python

r_ec2 = boto3.resource("ec2") #Higher-level abstraction, necessary for this part

outf = open("ec2-key.pem","w") #Variable to write a file as "ec2-key.pem"

key_pair = r_ec2.create_key_pair(KeyName="ec2-key") #Stating the Key Name on the Key Pairing

KeyPairOut = str(key_pair.key_material) #Set up the key, in string format

outf.write(KeyPairOut) #Export, writing the file
