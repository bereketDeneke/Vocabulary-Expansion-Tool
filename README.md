# Week 2 Homework - Vocabulary Expansion Tool

## Overview
This project is a **Vocabulary Expansion Tool** that helps users practice and expand their vocabulary by introducing them to a variety of synonyms and antonyms. The goal of this tool is to make communication more engaging by offering alternatives to frequently used words. Users can input a word and receive a list of synonyms and antonyms, then test their knowledge in a fun quiz game.

### Features
- Scrapes synonyms and antonyms for a user-provided word.
- Offers a quiz game for users to input their own guesses for synonyms and antonyms.
- Includes an additional scrambled word quiz for more fun!
- Data is sourced from the Merriam-Webster online thesaurus.

## Data Source
The tool retrieves synonyms and antonyms from [Merriam-Webster Thesaurus](https://www.merriam-webster.com/thesaurus/). This website was chosen due to its comprehensive and reliable database of English vocabulary, offering accurate information for both common and rare words.

## How to Run

To run the project locally:

1. **Clone the repository**
2. **Run**: pip install -r requirements.txt
3. **Run main.py**

## Notes
- Some words may not have direct antonyms or synonyms (e.g., words like "penguin" or "walk").
- The program may return humorous error messages if the word isn't found or if scraping fails.

