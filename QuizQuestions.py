import math
import random

name = input("Enter your name: \n")
print("\nWelcome", name, "!!!")
choice = str(input(f"Try out our little quiz game \nPress 'yes' to start or 'no' to to back to start menu"))
while(choice.lower() != "yes" or start != "no"):
        if(choice.lower() == "yes" or start == "no"):
               break
        print("Invalid entry")
        choice = input(f"Try out our little quiz game \nPress 'yes' to start or 'no' to to back to start menu")
while(choice.lower() == "no"):
        choice = input(f"Try out our little quiz game \nPress 'yes' to start or 'no' to to back to start menu")
        if(choice.lower() == "yes"):
              break
        else: 
              print("invalid entry")
              choice = input(f"Try out our little quiz game \nPress 'yes' to start or 'no' to to back to start menu")

questions = list(range(1, 19))
random_number = random.sample(questions, k=19)
for question in random_number:

	        question1 = int(input("What's python: \n"))
      	       #	 print("(1) Snake (2) Language (3) a (4) b")
    	              if question3 == 1:
             		   print("No")
     	             elif question3 == 2:
             		  print("Wrong again")
    	             else:
            		  print("dey go your go") 

      	 question2 = int(input("Alpha and omega number is what: \n"))
      	 if question2 == 19:
             		  print("Good")
      	 else:
           		   print("No, ode")


      	 question3 = int(input("what's the product of 10 and 9: \n"))
   	 if question3 == 90:
          		  print("Correct")
   	 else:
          		  print("Wrong, olodo")


    	  question4 = int(input("What is 27 minus 7: \n"))
    	  if question4 == 20:
           		  print("Good")
     	  else:
           		  print("No")

     	 question5 = int(input("What's the division of 10 by 2"))
     	 if question5 == 5:
            		 print("Welldone!!!")
    	 else:
          		  print("Olodo")

     	  question6 = int(input("what's the product of 5 and 9: \n"))
     	  if question6 == 45:
          		   print("you gerrit")
      	 else:
         		   print("Which school u go sef")

    	  question7 = int(input("2 plus 2 is what: \n"))
   	   if question7 == 4:
          		  print("Pass")
    	  else:
      		    print ("you no no 2 plus 2???")

    	  question8 = int(input(" 8 * 8 is: \n"))
   	  if question8 == 64:
           		   print("Sure")
     	  else:
             		  print("mumu man")

     	 question9 = int(input("How many teeth has an adult man"))
     	 if question9 == 32:
             		  print("E sure for u")
     	 else:
              		print("E shock you??")


     	 question10 = int(input("What's python: \n"))
     	 #	print("(1) Snake (2) Language (3) a (4) b")
     	 if question10 == 1:
              		 print("No")
     	 elif question10 == 2:
           		   print("Wrong again")
     	 else:
           		  print("dey go your go") 

      	question11 = int(input("Alpha and omega number is what: \n"))
     	if question11 == 19:
             		  print("Good")
     	else:
            		  print("No, ode")


     	 question12 = int(input("what's the product of 10 and 9: \n"))
      	 if question12 == 90:
             		  print("Correct")
     	 else:
              		print("Wrong, olodo")


      	question13 = int(input("What is 27 minus 7: \n"))
     	 if question13 == 20:
                  	print("Good")
      	 else:
               		print("No")

     	 question14 = int(input("What's the division of 10 by 2"))
     	 if question14 == 5:
               		 print("Welldone!!!")
    	 else:
             		  print("Olodo")

     	 question15 = int(input("what's the product of 5 and 9: \n"))
     	 if question15 == 45:
             		 print("you gerrit")
     	 else:
            		  print("Which school u go sef")

     	 question16 = int(input("2 plus 2 is what: \n"))
     	 if question16 == 4:
                		    print("Pass")
    	  else:
              		 print  ("you no no 2 plus 2???")

     	 question17 = int(input(" 8 * 8 is: \n"))
     	 if question17 == 64:
                    	 print("Sure")
    	  else:
              		   print("mumu man")

     	 question18 = int(input("How many teeth has an adult man"))
     	 if question18 == 32:
	  	 print("E sure for u")
    	  else:
 		  print("E shock you??")

print("Thank you", name, "!!!")