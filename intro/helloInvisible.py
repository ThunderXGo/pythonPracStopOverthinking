"""
You have decided to start a career as a magician.

Write a program to help you come up with your stage name.

It should work like this:

What name? Gizmo
The Amazing Gizmo
​
We've given you some example code to start with. You will need to modify it to solve this problem.

1.
The program has a variable named animal. That's not a very good variable name for our new program!

Change it to be name instead.

2.
Update the input prompt to: What name?

Remember to keep a space after the question mark.

3.
Change the print statement so that it prints The Amazing followed by the name the user entered.

Make sure you have an f at the beginning of the f-string, and put the name variable inside curly braces.

4.
Run your program and try it with Gizmo.

5.
Your program should also work with other names.

Run your program again and this time try Frank.

What name? Frank
The Amazing Frank
​
6.
Now try out your own examples! When you're happy mark your program to check it.

"""


name = input('What name? ')
print(f'The Amazing {name}')