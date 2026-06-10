class revstring:
    def reverse_words(self, text):
        return " ".join(text.split()[::-1])


reverser = revstring()

sentence = input("Enter a sentence: ")
print(reverser.reverse_words(sentence))