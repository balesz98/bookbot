def main():    
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #print(type(file_contents))
        print("--- Begin report of books/frankenstein.txt ---")
        print(word_count(file_contents), " words found in the document")
        charFreq=char_count(file_contents)
        #print(charFreq)
        for dict_key, dict_value in charFreq.items():
            print("The", dict_key, "character was found", dict_value, "times")
        print("--- End report ---")

def char_count(book):
    book=book.lower()
    freq = {}
    for char in book:
        if char in freq and char.isalpha():
            freq[char] += 1
        elif char.isalpha():
            freq[char] = 1
    return freq

def word_count(book):
    words = book.split()
    return len(words)


if __name__ == "__main__":
    main()