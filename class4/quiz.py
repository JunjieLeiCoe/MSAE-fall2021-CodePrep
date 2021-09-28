# Title: quiz.py
# Creator: Junjie
# CreationDate: 0913-0435

'''
In this quiz, around [13] questions are going to be asked
    * Pandas 
    * List 
    * Dictionary 

Submission Format:
    * Google Form Link

Rule: 
    * Concise
    * Pesudo-code/Sudo-code
'''

# Q0;
## What is the difference between function call for *func1() and *func2() and why?
### Function definitions for func1() and func2()

def func1():
    print("Hello World!")

def func2(): 
    return "Hello World!"

# Q1;
## Standard input: A randomly generated list -- [1,10,3,4,5,65,10000]
## Standard output: @returns the *first and *last(2) value of the list


# Q2;
## Standard input: A randomly generated list -- [1,10,3,4,5,65,10000]
## Standard Output: @returns the *max, *min and *mean of the list

# Q3;
## Standard input: A dictionary; 
## Standard output: @returns the *age of the person

# my_dict = {
#         "first_name" : "Junjie",
#         "last_name"  : "Lei", 
#         "class_of"   : "2021",
#         "age"        : "25"
#         }

# Q4; 
## Standard input: A dictionary
## Standard Ouput: Append *gender_info to the dictionary

# my_dict = {
#         "first_name" : "Junjie",
#         "last_name"  : "Lei", 
#         "class_of"   : "2021",
#         "age"        : "25",
#         "Gender_info": "Male"

#         }

# Q5; 
## How to initialize an empty Pandas dataframe


# Q6;
## How to convert lists to a dataframe
## How to convert a dictionary to a dataframe

# name_lst = ["junjie", "peter"]
# age_lst = [25, ""]

# Q7
## How do I add new column to a dataframe;
## Add a gender column to the dataframe;


# Q8
## How do I select Peter from this dataframe

# Q9
## What is the difference between *loc and *iloc function in Pandas


# Q10
import pandas as pd
print(
        pd.DataFrame({
            "name": ["Junjie", "Peter"],
            "age": [25, ""],
            "gender" : ["Male", "Male"]
            "title" : ["Student", "Professor"]
            })) 

# How do I extract the name for all entries, and what is the datatype for the selected name column.
# How do I extract the name and title for all entries
# How do I select all the *professors in this dataframe -- imagine that you have all USF faculty information.

# Q11
## How do I select Non-NAN values from this dataframe
## How do I remove this nan from the dataframe;
## How do I fillnas in this dataframe

# Q12
## Standard input: A Pandas dataframe
## Standard output: @return the max and min for the *age column

# Q13
## Standard input: A Pandas datframe
## Standard output: @return the *mean age for professors & students, and etc....;
