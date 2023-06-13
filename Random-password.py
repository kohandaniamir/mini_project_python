import random

lower = "abcdefghijklmnopqrstuvwxyz"

upper= lower.upper()

numbers = "1234567890"

symbol = "!@#$%^&*()[];'/|\"

length = 15

string = lower + upper + numbers +symbol

password = "".join(random.sample(string,length))

print(f"your password is : {password}")
