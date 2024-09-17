import re
import requests
import random

def get_synonyms_and_antonyms(word):
    url = f"https://www.merriam-webster.com/thesaurus/{word}"

    response = requests.get(url)
    if response.status_code != 200:
        possible_case = 'The word "{word}" doesn\'t have any synonyms or antonyms'
        print(f"ERR_MSG: {possible_case.format(word=word)} \nFailed to fetch data. Status code: {response.status_code}. ")
        return None, None


    html_content = response.content.decode('utf-8') # Decode the response content to text
    meta_pattern = r'<meta name="description" content="([^"]+)">' # Regex pattern to extract the content of the meta description tag
    meta_match = re.search(meta_pattern, html_content)

    if not meta_match:
        print("Meta description not found.")
        return None, None

    meta_content = meta_match.group(1)

    # Regex to extract synonyms and antonyms from the meta description content
    synonyms_pattern = r'Synonyms for \w+: ([\w\s,]+);'
    antonyms_pattern = r'Antonyms of \w+: ([\w\s,]+)'

    synonyms_match = re.search(synonyms_pattern, meta_content)
    antonyms_match = re.search(antonyms_pattern, meta_content)

    synonyms = [syn.strip() for syn in synonyms_match.group(1).split(',')] if synonyms_match else None
    antonyms = [ant.strip() for ant in antonyms_match.group(1).split(',')] if antonyms_match else None

    return synonyms, antonyms

# Explanation of the game and user is prompted to enter a word
print("----------------------------------------")
print("Welcome to the Word Quiz Game!")
print("----------------------------------------\n")
print("This app will help you learn synonyms and antonyms for words.")
print("We use the Merriam-Webster dictionary for the data.\n")

user_word = input("Enter a word to start the quiz game: ")

# Scrape data from dictionary website (or placeholder functon)
synonyms, antonyms = get_synonyms_and_antonyms(user_word)

# Easter egg error messages
error_easter = ["in another language", "too complicated", "is in Elvish", "is a Dwarf rune", "£@$!*?(&%}.", "hmm... idk"]

# Function responsible for the quiz game related to the inputted word
def play_quiz_game(user_word):
    print("\n----------------------------------------")
    print("Quiz: Input Synonyms and Antonyms!")
    print("----------------------------------------\n")
    user_synonym = input("Enter synonyms (separated by commas):\n")
    user_antonym = input("Enter antonyms (separated by commas):\n")

    # Parse user input
    user_synonym = [word.strip().lower() for word in user_synonym.split(",")]
    user_antonym = [word.strip().lower() for word in user_antonym.split(",")]

    match_synonym = [word for word in user_synonym if word in synonyms]
    match_antonym = [word for word in user_antonym if word in antonyms]

    # Output the result
    print("\n----------------------------------------")
    print("Results: Your Matches")
    print("----------------------------------------")
    print(f"Synonyms you got right: {match_synonym}")
    print(f"Antonyms you got right: {match_antonym}")

    print("\n----------------------------------------")
    print(f"Full List of Synonyms and Antonyms for '{user_word}'")
    print("----------------------------------------")
    print(f"Synonyms: {', '.join(synonyms)}")
    print(f"Antonyms: {', '.join(antonyms)}\n")

    user_check = input("\nDo you want to try a scrambled word quiz? (y/n): ")
    if user_check.lower() == "y":
        scrambled_word_quiz(synonyms, antonyms)
    else:
        print("Thank you for playing!")

# Function responsible for the scrambled word quiz
def scrambled_word_quiz(synonyms, antonyms):
    print("\n----------------------------------------")
    print("Scrambled Word Quiz!")
    print("----------------------------------------\n")

    combined = synonyms + antonyms
    quiz_word = random.choice(combined)
    quiz_word_list = list(quiz_word)
    random.shuffle(quiz_word_list)
    quiz_word_randomized = "".join(quiz_word_list)

    while True:
        guess = input(f"Guess the word from scrambled letters '{quiz_word_randomized}': ")
        if guess.lower() == quiz_word:
            print("Congrats! You guessed the word correctly!")
            break
        else:
            print("Oops! That's not right. Try again!")

# Check if scraping was successful
if not synonyms and not antonyms:
    print(f"Oops! Seems like your word is {random.choice(error_easter)}")
else:
    play_quiz_game(user_word)
