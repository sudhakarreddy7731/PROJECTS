# INPUTS
a=0
b=0
c=0
d=0
studentID = input("Enter student ID: ")
EmailID = input("Enter email: ")
password = input("Enter password: ")
referral = input("Enter referral code: ")
#studentId check
if (len(studentID)==7 and studentID.startswith("CSE") and
        studentID[3]=="-" and studentID[4].isdigit() and
        studentID[6].isdigit() and studentID[5].isdigit()) :
   a=1
else :
   a=0

#email check

if EmailID.endswith(".edu") and "@" in EmailID and not EmailID[0]=="@" :
    if (" " in EmailID or"_" in EmailID
           or "#" in EmailID or "$" in EmailID or "%" in EmailID or
          "&" in EmailID or "*" in EmailID or "(" in EmailID or ")" in EmailID or"{" in EmailID or
          "+" in EmailID  or"=" in EmailID  or "}" in EmailID or
          "[" in EmailID or "]" in EmailID or "|" in EmailID or "\\" in EmailID or
          ":" in EmailID or ";" in EmailID or "'" in EmailID or "\"" in EmailID or
          "<" in EmailID or ">" in EmailID or "?" in EmailID or "/" in EmailID or
          "," in EmailID or "~" in EmailID or "`" in EmailID or "^" in EmailID or
          "!" in EmailID) :
        b=0
    else :
        b=1
else :
    b=0

#password check
if len(password)==8:
    if  (password[0]=="A" or password[0]=="B" or password[0]=="C" or password[0]=="D" or password[0]=="E" or
    password[0]=="F" or password[0]=="G" or password[0]=="H" or password[0]=="I" or password[0]=="J" or
    password[0]=="K" or password[0]=="L" or password[0]=="M" or password[0]=="N" or password[0]=="O" or
    password[0]=="P" or password[0]=="Q" or password[0]=="Y" or password[0]=="S" or password[0]=="T" or
    password[0]=="U" or password[0]=="V" or password[0]=="X" or password[0]=="W" or password[0]=="R" or
    password[0]=="Z") and ( password[0].isdigit() or password[1].isdigit() or password[2].isdigit() or
        password[3].isdigit() or password[4].isdigit() or password[5].isdigit() or
        password[6].isdigit() or password[7].isdigit()) :
        c=1

    else:
         c=0

# Refferalcode check

if len(referral)==6:
    if referral.startswith("REF") and referral[3].isdigit() and referral[4].isdigit() and referral[5] == "@" :
        d=1
    else :
        d=0

if a==b==c==d==1 :
    print("APPROVED")
else :
    print("REJECTED")