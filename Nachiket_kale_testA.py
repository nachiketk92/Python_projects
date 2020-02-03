#Check whether two lines on x- axis overlap or not
#User input for first point
while True:
    try:
#This code takes single input at a time to avoide any human error which may 
        x1=float(input('Enter the first cordinate of first line: '))
        x2=float(input('Enter the second cordinate of first line: '))
        x3=float(input('Enter the sfirst cordinate of second line: '))
        x4=float(input('Enter the second cordinate of second line: '))
        
#This code takes a tuple as a input      
        #(x1,x2)=tuple(float(x) for x in input('Enter cordinates of first line  : ').split(','))
        #(x3,x4)=tuple(float(x) for x in input('Enter cordinates of second line : ').split(','))
        break
    except:
        print("That's not a valid option!")
# Conditions to check if lines are overlaping or not
if (0>((x3-x1)/(x2-x1))>1) or (0>((x4-x1)/(x2-x1))>1):
    print('Lines are overlaping.')
else:
    print('Lines are not overlaping')
    


