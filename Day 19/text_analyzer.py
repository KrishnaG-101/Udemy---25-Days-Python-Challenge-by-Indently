# This file contains the code for text analyzer project.

from collections import Counter
import re

def analyze(path : str) -> None:
    with open(path, "r", encoding="utf-8") as file:
        text : str = file.read()
    
    # list of words
    words : list[str] = re.findall(r"\b\w+\b", text.lower()) 
    # count of words
    word_count : int = len(words)
    # count of characters
    char_count_with_space : int = len(text)
    # count of white space and punctuation
    # we haven't applied .strip() to text so spaces before and after will be counted too.
    char_counter : Counter[str] = Counter(text)
    # count of white spaces
    # sum(c.isspace for c in text) -> 136 as it counts "\n" too, but text.count(" ") -> 118 as count of white spaces.
    white_space_count : int = char_counter[" "]
    # 3 most common words
    three_most_common_words : list[tuple[str, int]] = Counter(words).most_common(3)
    
    # display
    print("-" * 30)
    print(f"Number of characters in the text: {char_count_with_space}")
    print(f"Number of white spaces in the text: {white_space_count}")
    print(f"Number of words in the text: {word_count}")
    
    # count of each punctuation [",", ".", ";", ":", "'", "-", "!"]
    print("\nPunctuation count:")
    for punctuation in [",", ".", "-", ";", ":", "'", "!"]:
        print(f"=> {punctuation} : {char_counter[punctuation]}")
    
    print("\nThree most common words in our text:")
    # Well I am a bit confused on how the code below works absolutely correctly.
    # Because the three_most_common_words contains tuples inside which we have the values
    # I mean it should be for tuple_ in variable: and we access "tuple_[0]" for word and "tuple_[1]" for frequency. right?
    for word, frequency in three_most_common_words:
        print(f"=> {word} : {frequency}")
    print("-" * 30)

def main() -> None:
    analyze("Day 19/sample.txt")

if __name__ == "__main__":
    main()