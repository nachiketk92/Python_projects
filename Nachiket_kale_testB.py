'''
Function that taked in two string inputs for version names compares them
'''
def version_cpmparator(str1,str2):
#Original strings are printed as they are in output
#Considering the version comparison depends only on the digits in the string
    x1=str1
    x2=str2
#returns the string with digits only
    x1 = ''.join(filter(str.isdigit, str1))
    x2 = ''.join(filter(str.isdigit, str2))
    
#Check the length of two strings 
#set a count equal to the length of smaller string
#This count will be used for while loop
    if len(str1)>len(str2):
        count=len(str2)
        
#Check if all elements in smaller string are equal to elemets in larger string and return the function if they do
#example- str1="1.2.3.4.5.6.1" and str2="1.2.3.4.5.6" then str1 is greater and function is returned
        if(str1[:len(str2)]==str2):
            print (str1 ,'This is greater version ')
            return
        
    elif len(str2)>len(str1):
        count=len(str1)

#Check if all elements in smaller string are equal to elemets in larger string and return the function if they do
#example- str1="1.2.3.4.5.6.1" and str2="1.2.3.4.5.6" then str1 is greater and function is returned
        if (str2[:len(str1)]==str1):
            print (str2 ,'This is greater version ')
            return
    else:
        count=len(str1)
# Check if both strings are equal 
    if (x1==x2):
        print ('Both versions are equal.')
#If they are not equal and are not meeting any of the abouve conditions each and every element is compared to check which one is greater
    else:
        while (count!= 0):
            for char1 in x1:
                for char2 in x2:
                    if int(char1)>int(char2):
                        print (str1 ,'This is greater version ' )
                        break
                    elif int(char1)<int(char2):
                        print (str2 ,'This is greater version ' )
                        break
                    else:
                        continue
                    break
                break
            break
#This will decrease the count by 1 in each iteration
            count-=1


str1="1"
str2="2"

version_cpmparator(str1,str2)
