# cs50-6-readability - Summary
This is a command line application developed in Python that computes the approximate grade level needed to comprehend some input text. This is an exercise of Harvard's CS50 online course.

# Table of contents
1. [Readability](#Readability)
2. [Reading Levels](#Reading-Levels)
3. [About this program](#About-this-program)
4. [Usage](#Usage)

# Readability
This program that computes the approximate grade level needed to comprehend some text, per the below.
```
$ ./readability
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

# Reading Levels
According to Scholastic, E.B. White’s “Charlotte’s Web” is between a second and fourth grade reading level, and Lois Lowry’s “The Giver” is between an eighth grade reading level and a twelfth grade reading level. What does it mean, though, for a book to be at a “fourth grade reading level”?

Well, in many cases, a human expert might read a book and make a decision on the grade for which they think the book is most appropriate. But you could also imagine an algorithm attempting to figure out what the reading level of a text is.

So what sorts of traits are characteristic of higher reading levels? Well, longer words probably correlate with higher reading levels. Likewise, longer sentences probably correlate with higher reading levels, too. A number of “readability tests” have been developed over the years, to give a formulaic process for computing the reading level of a text.

One such readability test is the Coleman-Liau index. The Coleman-Liau index of a text is designed to output what (U.S.) grade level is needed to understand the text. The formula is:
```
index = 0.0588 * L - 0.296 * S - 15.8
```
Here, L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.

# About this program
This program first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula, written in Python.
The program counts the number of letters, words, and sentences in the text. It assumes that a letter is any lowercase character from a to z or any uppercase character from A to Z, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
The program prints as output "Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), the program outputs "Grade 16+" instead of giving the exact index number. If the index number is less than 1, the program outputs "Before Grade 1".

# Usage
You will need Python to run this application.

After cloning this repository and installing Python3, enter the project's folder through the command line and type the following to run the program:
```
python3 readability.py
```
The application will request text, where you should input the text required to be tested. It will then return the Grade reading level of that text, per the example below.
```
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

