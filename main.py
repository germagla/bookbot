def main():
    text = get_book_text('books/frankenstein.txt')
    print(wordcount(text))
    print(charcount(text))
    report(text)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def wordcount(text):
    return len(text.split())


def charcount(text):
    count_dict = {}
    for char in text:
        if char.lower() in count_dict.keys():
            count_dict[char.lower()] += 1
        else:
            count_dict[char.lower()] = 1
    return dict(sorted(count_dict.items()))


def report(text):
    print('------------ BEGIN REPORT ------------')
    print(f'{wordcount(text)} were found in this book. \n')
    countdict = charcount(text)
    for letter in countdict.keys():
        if letter.isalpha():
            print(f'The "{letter}" character was found {countdict[letter]} times')
    print('------------ END REPORT ------------')

main()
