def main(): 
    book_path = "books/frankenstein.txt"
    book = file_contents(book_path)
    words_in_book = word_count(book)
    characters_in_book = char_count(book)



    print(book)
    print("")
    print("")
    print("")
    print(f"There are {words_in_book} words in the book.")
    print("")
    print("")
    print("")
    report(book_path, words_in_book, characters_in_book)


def file_contents(path):
    with open(path) as f:
       return f.read()


def word_count(text):
    words = text.split()
    return (len(words))

def char_count(text):
    characters = {
        'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0,
'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0,
'x' : 0, 'y' : 0, 'z' : 0 }
    for char in text:
        lower = char.lower()
        if lower in characters:
            characters[lower] = characters[lower] + 1
    return characters

def report(book_path, words_in_book, characters_in_book):
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_in_book} words found in the document")
    print("")
    for char in characters_in_book:
        count = characters_in_book[char]
        print (f"The '{char}' was found {count} times ")
    print("--- End of report ---")

    

main()