# RANDOM PASSWORD GENERATION
import random

lower = ("abcdefghijklmnopqrstuvwxyz")
upper = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
number = ("12345678909")
symbol = ("!@#$%^&*()[]'.")

string = lower+upper+upper+number+symbol
length = 10

password = "".join(random.sample(string, length))
print("your new password is-- "+password)
