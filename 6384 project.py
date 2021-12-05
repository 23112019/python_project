##WRITE A PYTHON PROGRAM FOR CREATING OWN REPORT CARD DISPLAY UR GRADE AND DISPLAY (SUBJECT TOPPER)………
print("                                  " ," 🙏 Welcome to 🙏 ","              ")

print("***********************************************************************")


print("                        ","!.....","Mahatma Education Society's"," .....! ")

print("                     ","🌻🌻🌻🌻  Pillai Institute of Information Technology  🌻🌻🌻")
print("***********************************************************************")


print("                                  ","ENTER CLASS STUDENT DETAILS","                    ")






n = int(input("PLEASE ENTER THE TOTAL NO.OF STUDENTS:"))

all_students = []

sub1=[]
sub2=[]
sub3=[]
name=[]
for i in range(0, n):
    stud_name = input('ENTER THE NAME OF STUDENT: ')
    print (stud_name)
    name.append(stud_name)

    stud_rollno = input('ENTER THE ROLL NO. OF STUDENT: ')
    print (stud_rollno)

    mark1 = int(input('ENTER THE MARKS OF SUBJECT1 OUT OF 100: '))
    print (mark1)
    sub1.append(mark1)

    mark2 = int(input('ENTER THE MARKS OF SUBJECT2 OUT OF 100:: '))
    print (mark2)
    sub2.append(mark2)

    mark3 = int(input('ENTER THE MARKS OF SUBJECT3 OUT OF 100: '))
    print (mark3)
    sub3.append(mark3)

    total = (mark1+mark2+mark3)
    avg = total / 3
    print( "AVERAGE OF YOUR MARKS :", avg)
    print("***************************************************************************")
    if(avg>=90):            
         print("Grade: A+")
         print("CONGRATS YOUR PROMOTED TO NEXT CLASS")
    elif(avg>=80):
         print("Grade: A")
         print("CONGRATS YOUR PROMOTED TO NEXT CLASS")
    elif(avg>=70):  
         print("Grade: B+")
         print("CONGRATS YOUR PROMOTED TO NEXT CLASS")
    elif(avg>=60):
         print("Grade: B")
         print("CONGRATS YOUR PROMOTED TO NEXT CLASS")
    elif(avg>=50):
         print("Grade: C+")
         print("CONGRATS YOUR PROMOTED TO NEXT CLASS")
    elif(avg>=40):
         print("Grade: C")
         print("CONGRATS YOUR PROMOTED TO NEXT CLASS")
    elif(avg>=35):
         print("YOU ARE GRACED PASS")
         print("Grade: D")    
    else:
         print("YOU ARE FAILED,TRY HARDER NEXT TIME")
         print("Grade: F")
    print("THANK YOU")    
    print("***************************************************************************")
           

    
    
    all_students.append({
                            'NAME:-': stud_name,
                            'ROLL NO:-': stud_rollno,
                            'SUBJECT1:-': mark1,
                            'SUBJECT2:-': mark2,
                            'SUBJECT3:-': mark3,
                            'TOTAL MARKS OBTAINED OUT OF 300': total,
                            'AVERAGE OF YOUR MARKS': avg
                            })
print("***************************************************************************")
print('')
print('RESULTS')
print("---------")
for student in all_students:
    print( '\n')
    print("***************************************************************************")    
    for key, value in student.items():
        print ('{0}: {1}'.format(key, value))
print('')
print("***************************************************************************")
print('SUBJECTWISE TOPPERS 2019-20 OF OUR CLASS:- ')
print("***************************************************************************")
print('')
print('CONRATULATIONS....')
print("***************************************************************************")
print("***************************************************************************")
print('')
print('Highest marks in SUBJECT1:-',max(sub1))
print('SCORED BY:-',name[sub1.index(max(sub1))])
print('')
print("***************************************************************************")
print('Highest marks in SUBJECT2:-',max(sub2))
print('SCORED BY:-',name[sub2.index(max(sub2))])
print('')
print("***************************************************************************")
print('Highest marks in SUBJECT3:-',max(sub3))
print('SCORED BY:-',name[sub3.index(max(sub3))])

print("                            "," 🙏 THANK YOU 🙏")


print("***********************************************************************")


