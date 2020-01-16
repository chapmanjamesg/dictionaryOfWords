"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
word_definitions["fun"]= "enjoyment, amusement, or lighthearted pleasure."
word_definitions["bored"] = "feeling weary because one is unoccupied or lacks interest in one's current activity."
word_definitions["rage"] = "feel or express violent uncontrollable anger."
word_definitions["willpower"] = "control exerted to do something or restrain impulses."

# print(word_definitions.keys())

for key, values in word_definitions.items():
    print(f"The definition of {key} is {values}")