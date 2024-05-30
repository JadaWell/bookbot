def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = split_text(text)
    number = counter(words)
    lowered_string = convert_to_string(text)
    letter_dict = count_letters(lowered_string)
    # print(text)
    # print(words)
    # print(lowered_string)
    print(letter_dict)
    print(number)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


# Szétvágja a szöveget szavakra.
def split_text(stg):
    words = stg.split()
    return words

# Megszámolja a szavakat.
def counter(szo):
    number = 0
    for each in szo:
        number +=1
    return number

# Kisbetűket csinál mindenből.
def convert_to_string(words):
    data =""
    data = "".join(words.split("\n"))
    lowered_string = data.lower()
    return lowered_string


# Megszámolja a betűket.
def count_letters(lowered_string):
    letter_dict = {}
    for letter in lowered_string:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict
    
# Kiveszi belőle a betűket és ABC sorrendbe teszi.
    







main()
