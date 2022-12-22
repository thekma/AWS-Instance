ssh -i "ec2-key.pem" ec2-user@ec2-75-101-219-134.compute-1.amazonaws.com #Using AWS example to ssh connect into the instance

sudo su #Get more commands/rights so updates or other actions can be pushed

yum update -y #Check to see what updates are available, with "-y" to give approval ahead of time

yum update -y httpd.x86_64 #Install software onto server

systemctl start httpd.service #Start up the software

systemctl enable httpd.service #Permit the software to run
