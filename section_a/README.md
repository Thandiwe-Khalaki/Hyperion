# Python code review for X

Hi X. This is a great start for your first attempt, I am pleased to see you understand what is required and the logic of your solution is correct. Your code is also DRY and readable which makes it fun to review.There is room for improvement and lets see how to get there. Please consider the following points when refactoring this code.

## Correctness

- This code does not run, therefore there is no way to tell if the output is correct. An indention error is raised when running this code. The error is raised on the second line.
- Use code formatter before submitting. A code formatter will save you the energy of having to take care of whitespace, indentations etc etc. Check it out [here](https://github.com/psf/black)
- Also please note the following points:
  - On line five, the built on function "sorted()" must take in an argument.

## Efficiency 

- Code is efficient if it runs faster and does not consume much memory. Knowing how to test your code performance is the best way to writing efficient code. [Here](https://www.codementor.io/@satwikkansal/python-practices-for-efficient-code-performance-memory-and-usability-aze6oiq65) is a nice article that will help with this concept.

- We use list comprehensions to make code more efficient and faster, line 3 to line 9 could be done with a list comprehension. Please see how that can be accomplished [here](https://pythonguides.com/python-list-comprehension-using-if-else/). Also search for nested list comprehension. They can be real handy if they are readable and not too long.

- Write simple code. "Simple is better than complex"_ [The Zen of Python](https://peps.python.org/pep-0020/). The same output could have achieved by using a function instead of a class. We use classes when we want to group functions, or when we want to create a template for a behavior, whereas we use functions when we want to process data, or manipulate data or create sets, I found this [here](https://stackoverflow.com/questions/18202818/classes-vs-functions#:~:text=Functions%20do%20specific%20things%2C%20classes,function%20is%20all%20you%20need.) Knowing when to use which is very important. Please create both, run the performance test and see which one is faster and uses less memory.

## Style

- We use the [PEP 8 Style Guide](https://peps.python.org/pep-0008/) to write python code. This helps us keep code consistent and clean. Please go through it and get familiar. If anything is not clear, hit me up for clarity.
- According to the style guide, the names for classes must start with a capital letter, which you did. Kudos.
- We can improve the naming on the second line from "groupAnagrams" to "group_anagrams", which is more acceptable naming convention according to the style guide
- The name "ob1" and "i" are a bit weird. Can we perhaps use a more clear, known name? A name should help the reader understand what the variable does, or what it is.Explicit variable names helps us to understand code as we revisit it.

## Documentation

- Write docstring for your public methods, classes and functions.
- The docstring should describe what the method does and what are the arguments.


**Please consider these above points and submit this task again after refactoring this code. Remember, practice makes perfect.**