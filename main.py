
def get_content(file):
    "Returns File Contents as single string"
    with open(file, 'r') as f:
        file_contents = f.read()
    return file_contents


def count_words(string):
    "Returns number of words in string"
    word_list = string.split()
    return len(word_list)

def count_chars(string):
    "Returns a dictionary of all characters and their count"
    letters = {}
    for char in string.lower():
        if char not in letters.keys():
            letters[ char ] = 1
        else:
            letters[ char ] += 1
    
    return  letters

def get_report(file):
    "Prints a report of file's word count and letter count"
    content = get_content(file)
    words = count_words(content)
    chars = count_chars(content)

    # Remove unnecessary characters from character count dictionary
    letters = { char : chars[ char ] for char in chars.keys() if char.isalpha() }
    count_list = list(letters.values())

    # Sort count by largest first
    count_list.sort(reverse=True)

    print(f"--- Begin Report of {file} ---\n")
    print(f"{words} words found in the document\n")

    # Inefficient... but works :)
    for count in count_list:
        # Get index location of count to find key 
        index = list(letters.values()).index(count)
        key = list(letters.keys())[index]

        # Prints letter and count
        print(f"The letter '{key}' was found {count} times")

        # Removes the key-value pair to prevent duplicate letters (if any)
        del letters[key]

    print("---End Report---")

if __name__ == "__main__":
    import os
    script_location = os.path.dirname(os.path.abspath(__file__))
    book_dir = os.path.join(script_location, 'books')
    if not os.path.exists(book_dir):
        print("No Book directory... Creating Book Directory...")
        os.makedirs(book_dir)
        print("Done. Please Place your books in the 'book' directory to get a report of each book.")
        print("Each book MUST be in .txt format")
    books = [ book for book in os.listdir(book_dir) if book.endswith('.txt') ]
    for book in books:
        book_path = os.path.relpath( os.path.join(book_dir, book), script_location)
        get_report(book_path)

