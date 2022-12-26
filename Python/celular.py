# Welcome to the Python coding playground. 
# Pattern to output:


# Type your code here:
'''x = 0
for x in range(0,6) :
    print(x * '*')
    x = x + 1'''

# Welcome to the Python coding playground. 
# Example Input:
# 3
# Example Output:
# It is Thursday

# Type your code here:
week = {0:'monday', 1:'thursday', 2:'wednesday', 3:'thuesday', 4:'friday', 5:'saturday', 6:'sunday'}

def days_of_week(x=None):
  if x < 7:
    print ('It is: ' + week[x])
  else:
    print('try again')

num_day = input('enter a number of a day: ')
days_of_week(int(num_day))