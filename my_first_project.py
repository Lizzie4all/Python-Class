#print ("Good Morning")
#try:
 #   x=int(input("Enter x: "))
 #  y=float(input("Enter y: '))
 #   print(x+y)
#except:
 #   print("invalid input")

#try:
 #   x=int(input("Enter x: "))
 #   y=int(input("Enter y: "))
 #   print("The sum of the value is")
 #   print(x+y)
 #   print(x**y)
#except:
   # print("invalid input")

#try:
    
    #grade=float(input("Enter your grade: "))

    #if grade in range(0,45) :
       #print("you Failed")
        
    #elif grade in range(45,50):
        #print("You passed with a D")
        
    #elif grade in range(50,60):
        #print("you passed with a C")
        
    #elif grade in range(60,70):
        #print("you passed with a B")

    #elif grade in range(70,100):
        #print("you passed with an A")
        
    #else:
        #print ("you are not on the grading system")
        
#except:
    #print("Invalid Input")

try:
    score = int(input("Enter your score"))
    if score>100:
        print("Your score is greater than 100!")
    elif score<0:
        print("Your score is less than 0!")
    elif score>79:
        print("Congratulation!! your grade is A")
    elif score>64:
        print("Congrats your grade is B")
    elif score>49:
        print("Congrats somehow, your grade is C")
    elif score>44:
        print("You tried, your grade is D")
    elif score>39:
        print("You failed!! your grade is E")
    else:
        print("You really failed, your grade is F")
except:
    print("Your entry is invalid")
        
    
   
