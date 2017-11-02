def word_count(filename,the_word):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except IOError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        the_word_count = str(contents.lower().count(the_word))
        print("The file " + filename + " has about " + str(num_words) +
              " words.")
        print("It contains " + the_word_count + " '" + the_word + "' in it.")


filename_1 = 'known_to_the_police.txt'
the_word_1 = 'the'
word_count(filename_1, the_word_1)
