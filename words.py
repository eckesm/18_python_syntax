def print_upper_words_ORIGINAL(words, must_start_with={"h", "y"}):
    """Converts a list of words to printed words on separate lines all in upper-case"""
    for word in words:

        for letter in must_start_with:

            if word.startswith(letter):

                cap_word = ''
                for char in word:
                    cap_word += char.capitalize()
                print(cap_word)


def print_upper_words(words):

    # suggested solution 1:
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
