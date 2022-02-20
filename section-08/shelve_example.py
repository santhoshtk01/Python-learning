# Program to read and write file using shelve module same as dictionary
import shelve

# Global declarations
fruits = ['apple', 'orange', 'grape', 'strawberry']

with shelve.open('example') as values:
    for fruit in fruits:
        values[fruit] = 'It is a eatable thing..'

    # Printing them out
    for key, value in values.items():
        print(key, value)

