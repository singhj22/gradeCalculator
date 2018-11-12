'''
Created on Nov 12, 2018

@author: Jugat Singh
Grade Calculator
'''

grade= float(input('Please enter the points earned on the assignment: '))
total= float(input('Please enter the total number of points: '))

percent = (grade/total)*100 

print("\nYour grade is a ", format(percent, '.2f'), '%')

if percent>=90:
    print("You got an A")
elif percent>=80:
    print('You got a B')
elif percent>=70:
    print('You got a C')
elif percent>=60:
    print('You got a D')
elif percent>=50:
    print('You got an E')
else:
    print('You got lower than an E. Oof!')