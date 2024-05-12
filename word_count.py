def count_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    print("The number of words in your sentence is:", len(words))

count_words()