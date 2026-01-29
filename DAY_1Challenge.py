#I used this for checking valid or not 1==true and 0==false

a=0
b=0
c=0
d=0

Name= input("Enter Full Name: ")
EmailID= input("Enter Email ID: ")
mobileNo = input("Enter Mobile Number: ")
Age = int(input("Enter Age: "))
if Name.startswith(" ") or Name.endswith(" "):
    #print("Name Invalid should not start or end with space")
    a=0
elif not Name.__contains__(" "):
    #print("Name is Invalid must contain at least two words")
    a=0
else:
     # print(" Name is Valid")
    a=1
# check EmailID
if "@" in EmailID and "." in EmailID:
    if EmailID.startswith("@"):
         #print("EmailID must not start with @")
        b=0

    elif (" " in EmailID or
          "!" in EmailID or "#" in EmailID or "$" in EmailID or "%" in EmailID or
          "&" in EmailID or "*" in EmailID or "(" in EmailID or ")" in EmailID or
          "+" in EmailID or "=" in EmailID or "{" in EmailID or "}" in EmailID or
          "[" in EmailID or "]" in EmailID or "|" in EmailID or "\\" in EmailID or
          ":" in EmailID or ";" in EmailID or "'" in EmailID or "\"" in EmailID or
          "<" in EmailID or ">" in EmailID or "?" in EmailID or "/" in EmailID or
          "," in EmailID or "~" in EmailID or "`" in EmailID or "^" in EmailID or
          "_" in EmailID):
       # print("Invalid, EmailID must not contain special characters")
        b=0
    else:
        #print("Valid EmailID")
        b = 1
else:
    #print("Invalid EmailID: email should contain both @ and .")
    b=0


#MOBLE NUMBER CHECK

if len(mobileNo) == 10 and mobileNo.isdigit() and mobileNo[0] != '0':
    #print("valid mobile number")
    c=1
else:
     #print("Invalid moblie number Should not contain other characters")
     c=0

#age check


if 18<=Age<=60:
    #print("Age is valid")
    d=1

else:
    #print("Age is invalid")
    d=0
if a==b==c==d==1 :
    print("User profile VALID")
else:
    print("User profile INVALID")


 #changed according to testcases
