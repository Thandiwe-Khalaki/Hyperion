# International Standard Book Numbers

## Project Description

NB: I wanted to write this section using R programming language, but after much thought I decided to use Python although I used it on section a. I found that using python wont only be easier, but I will also get to write interesting tests and do justice to this section.

The International Standard Book Number (ISBN) is a unique identifying number given to each published book. ISBNs assigned after January 2007 are 13 digits long (ISBN-13), however books with 10-digit ISBNs are still in wide use.

Create a function that takes a string of numbers (possibly with an X at the end) and...

  1. Return "Invalid" if it is not a valid ISBN-10 or ISBN-13.
  2. Return "Valid" if it is a valid ISBN-13.
  3. If it is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.

## Installation

- First, start by cloning this repository to your local machine

``
https://github.com/Thandiwe-Khalaki/Hyperion.git
``

- I recommend installing virtualenv

``pip install virtualenv
``

- Once installed, go to the  **section_c** folder 

``cd section_c

- Create a virtual environment with the name of your choice

``python -m virtualenv venv``

- Activate the virtualenv. 

``venv/Scripts/activate``


 - Install the python dependencies on the virtual environment

``pip install -r requirements.txt``

- You can now run the main file 

`` python isbn.py``

- You can run the test file

`` python test_isbn.py``

## Limitations

Although this function works as expected, if you put in a valid ISBN-10, it does not specify if it is valid or not, however, it takes the ISBN-10 and converts it into a ISBN-13.

If the check digit(the last digit of the number) is more than 10, X is used instead.

## References

[Detail- Check Digits](https://eng.libretexts.org/Bookshelves/Electrical_Engineering/Signal_Processing_and_Modeling/Information_and_Entropy_(Penfield)/04%3A_Errors/4.09%3A_Detail-_Check_Digits)

[International Standard Book Numbers](https://edabit.com/challenge/DpFmDxcyesPfPoFMn)

### License

[MIT](https://choosealicense.com/licenses/mit/)