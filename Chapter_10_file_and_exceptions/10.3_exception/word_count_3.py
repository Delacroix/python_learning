def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

    except IOError:
        pass
    else:
        # count how many words in the file
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " +str(num_words) +
              " words.")


filenames = ['alice.txt', 'siddharta.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)
