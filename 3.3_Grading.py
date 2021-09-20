'''
Grading PROGRAM
---------------
Create a program that asks the user for their semester grade, final exam grade, 
and final exam worth and then calculates the overall final grade. 
Ask your instructor if you don't know how to calculate weighted averages.
You don't have to print out the letter grade. We will do that in the next chapter.

Test with the following:

Sem Grade: 86   Final Exam: 52   Exam worth: 15%    Overall: 80.9
Sem Grade: 95   Final Exam: 32   Exam worth: 10%    Overall: 88.7
Sem Grade: 72   Final Exam: 100   Exam worth: 20%    Overall: 77.6
'''
sem= float(input("What's your grade for this semester?"))
exa= float(input("What's did you get on finals?"))
exv= float(input("How much did the exam impact your grade?"))
overall= (exa*exv)+(sem)*(1-exv)
print ("Your overall grade for the class was",overall,"!")