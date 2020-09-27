#Needed library
import random

#Strings for passwords
lowerChars = "abcdefghijklmnopqrstuvwxyz"
upperChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
specialChars = "abcdefghijklmnopqrstuvwxyz!@#$%^&*"
lowerCharsNum = "abcdefghijklmnopqrstuvwxyz1234567890"
upperCharsNum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
specialCharsNum = "abcdefghijklmnopqrstuvwxyz!@#$%^&*1234567890"
allChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
allCharsNum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^*1234567890"

#The actual password
password = ''

#Gets size of password
print("What is the length of your password? (8, 16, 24 or 32 characters):")
length = int(input())
while (length != 8 and length != 16 and length != 24 and length != 32):
   print("Length must be 8, 16, 24 or 32 characters")
   length = int(input())

#These are all additives for uppercase, numbers, and special characters
print("Do you want to include uppercase letters? (y/n):")
uppercase = input()
uppercase = uppercase.lower()
while (uppercase != "y" and uppercase != "n"):
   print("Please respond with y (Yes) or n (No):")
   uppercase = input()
if uppercase == "y":
   uppercase = True
else:
   uppercase = False

print("Do you want to include numbers? (y/n):")
numbers = input()
numbers = numbers.lower()
while (numbers != "y" and numbers != "n"):
   print("Please respond with y (Yes) or n (No):")
   numbers = input()
if numbers == "y":
   numbers = True
else:
   numbers = False

print("Do you want to include special characters? (y/n):")
specialChar = input()
specialChar = specialChar.lower()
while (specialChar != "y" and specialChar != "n"):
   print("Please respond with y (Yes) or n (No):")
   specialChar = input()
if specialChar == "y":
   specialChar = True
else:
   specialChar = False

#Conditions to determine the type of password that needs to be generated
if uppercase and not numbers and not specialChar:
   for c in range(length):
      password += random.choice(upperChars)
elif uppercase and numbers and not specialChar:
   for c in range(length):
      password += random.choice(upperCharsNum)
elif uppercase and not numbers and specialChar:
   for c in range(length):
      password += random.choice(allChars)
elif not uppercase and numbers and specialChar:
   for c in range(length):
      password += random.choice(specialCharsNum)
elif not uppercase and not numbers and specialChar:
   for c in range(length):
      password += random.choice(specialChars)
elif not uppercase and numbers and not specialChar:
   for c in range(length):
      password += random.choice(lowerCharsNum)
elif uppercase and numbers and specialChar:
   for c in range(length):
      password += random.choice(allCharsNum)
else:
   for c in range(length):
      password += random.choice(lowerChars)

#prints the password
print()
print("Password:", password)