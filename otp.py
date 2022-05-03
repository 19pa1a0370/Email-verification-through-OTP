from random import randint
import smtplib

#Generating OTP with the help of random(randint) module
OTP = ''
for i in range(6):
    OTP+=str(randint(0,9))
msg = OTP + ' is the OTP'


reciever = '19pa1a0338@vishnu.edu.in'
sender = 'venkateshnimmalapudi100@gmail.com'
password =  input(str('Enter password: '))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

#To login to sender's email id
server.login(sender,password)
print('Login successful')

#To send the OTP to the reciver's email id
server.sendmail(sender,reciever,msg)

#A small note
print('If not found in your indox please check your spam box')

user = input("Enter the OTP sent to your registered mail id: ")

if user == OTP:
    print("Email id verification successful")






