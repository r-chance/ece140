# The Case of the Talking Calculator

Ted was fond of numbers. But he was also lazy. He didn't want to bother with writing numbers on paper, or
have to deal with cleaning up pencil shavings after slogging through equations.  So Ted set out to build the
worlds very first calculator that could solve simple equations that he would speak aloud.  

Your challenge, is to implement the code that answers Ted's numeric questions, based on the text translation of
the words that Ted speaks. Here are a few simple example expressions:

```
ten plus twelve
ninety nine divided by three
eight minus six
```

The equations you must handle will follow these simple rules:

1. All the spoken numbers are between 0 and 99
2. There are no negative numbers, because Ted is a positive guy
3. Only basic operators are used: 'plus', 'minus', 'times', and 'divided by'
4. Each equation will only contain a single operator 
5. In the case of an error (e.g. divide by zero or invalid input), return 'NaN'  
6. You can only rely on code you write yourself this time. Don't use libs that solve equations for you.


We've provided you the usual boiler-plate code the reads sample input from a test file, and calls your "calculate"
function to solve the expression. All you have to do is implement the calculate() function:

```
def calculate(aSpokenString):
    #your code here...
```

Need a hint?  Consider using a dictionary to define the number-words ('one','two'...) along with their numeric
value. Before you try to solve each equation, try to simplify and reduce the input string. After all, the
grammar used in the expressions are all words you know in advance.

If you're really stumped, then go ahead a look at how other programmers solve similar problems by visiting
stackoverflow.com or other online resources. Getting ideas from others is ok, but you must do your own work
and build your own unique solution.

As always, we're looking for working solutions that are simple, clear and concise. We're looking for
creative ways to articulate this algorithm. Also consider the performance of your solution.

Grading notes:
- Do not modify 'main'.
- Do not use any libraries outside the Python standard libraries.
- Your functions should be able to handle all sorts of inputs.
- When in doubt, ask.
