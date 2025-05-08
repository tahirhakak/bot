print("Coder: Mohammad Tahir")
name = input("Enter Your Name: ")
print("Your Name: ",name)

# Lets verify Email 
email = input("Enter Your Email: ")
email1 = input("Verify Email: ")
if email == email1:
  print("Your Email Is VERIFIED NOW")
if email != email1:
  print("You Enter Worng email")
  exit()

# Instagram UserName 
ig_user = input("Enter Instagram UserName: ")
print("Your UserName: ",ig_user)

# Age Verification 
age = int(input("Enter Your Age: "))
if age >= 18:
  print("Welcome Sir")
if age < 18:
  print("Sorry Sir You Are Under Age")
  exit()
  
# Bot Key Verification
key = input("Enter Bot Key")
if key == 'Tahir001':
  print("Welcome Sir, Access Granted")
elif key != 'Tahir001':
  print("You Entered Worng Key")
  exit()
# Bot Starting.....
print("Type 1 to 3")
print("1. My Github Link: ")
print("2. Tools: ")
print("3. Update: ")

# Code
a = int(input("Enter: "))
if a == 1:
  print("https://github.com/tahirhakak")
  exit()
elif a == 2:
  print("Tools Coming Soon")
  exit()
elif a == 3:
  print("Latest Version")
  stop()
elif a > 3:
  print("Sorry You Entered Wrong Number")
  
