def main() :
    path_to_file = "./books/frankenstein.txt"
    words = read_book_content(path_to_file)
    num_words = count_total_words(words.split())
    print(f"{num_words} words found in the document")

    words_dict = count_words(words)

    print(f"--- Begin report of {path_to_file} ---")
    report_list = filter_alphabet(words_dict)
    for element in report_list:
        print(f"The '{element['letter']}' character was found '{element['num']}' times")

    print("--- End report ---")


def read_book_content(path_to_file) :
    with open(path_to_file) as f:
        file_contents = f.read()

    words = file_contents.lower()
    return words

def count_total_words(words) :
    word_count = 0
    for word in words:
        word_count += 1

    return word_count

def count_words(words) :
    num_of_words = {}
    for word in words:
        if word in num_of_words:
            num_of_words[word] += 1
        else:
            num_of_words[word] = 1
    return num_of_words

def sort_value(dict):
    return dict["num"]

def filter_alphabet(dict) :
    list_of_characters = []
    for key, item in dict.items():
        if key.isalpha():
            list_of_characters.append({"letter": key, "num": item})

    list_of_characters.sort(reverse=True, key=sort_value)
    return list_of_characters

main()