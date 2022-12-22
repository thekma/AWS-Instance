icacls.exe “ec2-key.pem” /reset #File command used to reset the permissions of the file "ec2-key.pem", can change to have the user input the pem file name

icacls.exe “ec2-key.pem” /grant:r “$($env:username):(r)” #Gives the current user reading privileges

icacls.exe “ec2-key.pem” /inheritance:r #Makes the file permanently in read-only permissions (unless changed)
