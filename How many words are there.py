def word_count(words):
    number_words = len(words.split())
    if number_words < 0:
        return "Less than Zero"
    if number_words == 0:
        return "Zero"
    if number_words == 1:
        return "One"
    if number_words == 2:
        return "Two"
    if number_words == 3:
        return "Three"
    if number_words == 4:
        return "Four"
    if number_words == 5:
        return "Five"
    if number_words == 6:
        return "Six"
    if number_words == 7:
        return "Seven"
    if number_words == 8:
        return "Eight"
    if number_words == 9:
        return "Nine"
    if number_words == 10:
        return "Ten"
    if number_words > 10:
        return "More than ten"
    return None

print(word_count(input("Insert the phrase and this will count the words. > ",)))
