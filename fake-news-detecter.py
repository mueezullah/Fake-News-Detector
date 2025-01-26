import difflib
from random import choice
from fuzzywuzzy import fuzz
import json

from sqlalchemy import values

#Load the fake news phrases from file
FAKE_NEWS_FILE = "fake_news_phrases.json"

#Function to load fake news from Json file
def load_fake_news_phrases():
    try:
        with open(FAKE_NEWS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return[]

#Function to save fake news to JSON file
def save_fake_news_phrases(phrases):
    with open(FAKE_NEWS_FILE, 'w') as file:
        json.dump(phrases, file, indent=4)

#Fucntion to check if input text matches the fake news phrases
def check_fake_news(input_text, fake_news_phrases):
    for phrase in fake_news_phrases:
        if phrase.lower() in input_text.lower():
            return True
    #Similarity check using fuzzywuzzy
    for phrase in fake_news_phrases:
        similarity = fuzz.partial_ratio(input_text.lower(), phrase.lower())
        if similarity > 80:
            return True

    return False

#Main function
def main():
    fake_news_phrases = load_fake_news_phrases()

    while True:
        #Display menu options
        print("\nFake News Detecter!")
        print("1. Check news headline/article")
        print("2. View fake news phrases")
        print("3. Add fake news phrases")
        print("4. Delete news")
        print("5. Exit")

        #User's choice
        choice = input("Enter your choice: ")

        #Check the news article or headline
        if choice == '1':
            input_text = input("Enter the news headline or article snippet: ")
            if check_fake_news(input_text, fake_news_phrases):
                print("This might be fake news!")

            else:
                print("This seems legitimate.")

        #View the list of fake news
        elif choice == '2':
            print("\nFake News phrases: ")
            for idx, phrase in enumerate(fake_news_phrases, start=1):
                print(f"{idx}. {phrase}")

        #Add fake news
        elif choice == '3':
            new_phrase = input("Enter the fake news phrase to add: ")
            if new_phrase not in fake_news_phrases:
                fake_news_phrases.append(new_phrase)
                save_fake_news_phrases(fake_news_phrases)
                print("Phrase added successfully.")
            else:
                print("Phrase already exists.")

        #Remove the news
        elif choice == '4':
            print("\nFake News:")
            for idx, phrase in enumerate(fake_news_phrases, start=1):
                #Display phrases with numbering
                print(f"{idx}. {phrase}")
            try:
                phrase_index = int(input("Enter the number of news you want to delete: ")) - 1
                if 0 <= phrase_index < len(fake_news_phrases):
                    removed_phrase = fake_news_phrases.pop(phrase_index)
                    save_fake_news_phrases(fake_news_phrases)
                    print(f"Phrase '{removed_phrase}' deleted successfully")

                else:
                    print("Invalid number. Please try again.")

            except valueError:
                print("Invalid input. Please enter a valid number.")

        #Exit the program
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        #Handling the invalid input
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()