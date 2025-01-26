# Fake-News-Detector

This project is a Python-based Fake News Detector that helps identify potentially fake news headlines or article snippets. The program checks user input against a predefined list of fake news phrases and offers similarity-based detection using the fuzzywuzzy library.

## Working

The user enter the headline of snippet or news.
The program compares the user input against already stored list of fake news phrases in a JSON file or dictionary.
If the input contains any exact or similarity-based matches, the program displays: "This might be fake news!"
If no matches are found, it displays: "This seems legitimate."

### Libraries used
**fuzzywuzzy**: The fuzzywuzzy library is used for string matching and similarity measurement.
**json**: The json module is part of Python’s standard library and is used for reading and writing data in JSON format.
**difflib**: The difflib module, part of Python’s standard library, is used for comparing sequences.
