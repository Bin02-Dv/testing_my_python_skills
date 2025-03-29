# import re

# user_input = input("Enter a sentence to find duplicates: ")

# cleaned_user_input = re.sub(r'[^\w\s]', '', user_input.lower())

# words = cleaned_user_input.strip().split()

# words_count = {}

# for word in words:
#     words_count[word] = words_count.get(word, 0) + 1

# sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)


# print("Duplicates Detector:")
# print("\n")

# for word, count in sorted_words:
#     if count > 1:
#         print(f"{word} was detected {count} times")

import re


sentence_input_by_user = input("Enter a sentence to find the most frequency word(s): ")

cleaned_text = re.sub(r'[^\w\s]', '', sentence_input_by_user.lower())

words = cleaned_text.strip().split()

words_count = {}

stop_words = {"the", "is", "and"}

for word in words:
    if word not in stop_words:
        words_count[word] = words_count.get(word, 0) + 1

# sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)

max_frequency = max(words_count.values())

print("The Most fequency word(s):")

for word, count in words_count.items():
    if count == max_frequency:
        print(f"{word} was detected {count} times")