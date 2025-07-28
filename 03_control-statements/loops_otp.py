#otp simulation
import random
otp = random.randint(1000,9999)
print(otp)
#logic
attempts = 3
while attempts:
    user_otp = int(input("Enter OTP: "))
    if len(str(user_otp))!=4:
        print("OTP Must be 4 digit number only")
    if user_otp == otp:
        print("Correct OTP - Success")
        break
    attempts-=1
else:
    print("Maximum attempts done, try after 24 Hours") 