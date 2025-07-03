def total_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    count_dictionary = {}
    for char in text:
            if char in count_dictionary:
                count_dictionary[char] += 1
            else:
                count_dictionary[char] = 1
    return count_dictionary

def sort_on(items):
     return items["num"]

def sort_char_dictionary(dictionary):
    dictionary_list = []
    for key, value in dictionary.items():
          if key.isalpha():
            dictionary_list.append({"char": key, "num": value})
    dictionary_list.sort(reverse=True, key=sort_on)
    #sorted_dictionary = {}
    #for item in dictionary_list:
     #   sorted_dictionary[item["char"]] = item["num"]
     #^ignore this, I was trying to fix my output and thought I needed to use a dictionary instead of a list.
    return dictionary_list