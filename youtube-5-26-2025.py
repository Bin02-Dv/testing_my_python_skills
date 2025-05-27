import time
import os

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for char, child in node.children.items():
            words.extend(self._collect_words(child, prefix + char))
        return words

def typing_effect(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def animate_autocomplete(trie, prefix):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Searching for words with prefix:")
    typing_effect(prefix.upper(), 0.15)
    print("\nSuggestions:\n")
    time.sleep(1)
    suggestions = trie.search_prefix(prefix)
    if suggestions:
        for word in suggestions:
            typing_effect("🔸 " + word, 0.07)
    else:
        print("No suggestions found.")

words = ['law', 'lawyer', 'lawsuit', 'legal', 'legislation', 'lecture', 'learn', 'legend']
trie = Trie()
for word in words:
    trie.insert(word)
    
user_input = input("Start writing a word: ")

animate_autocomplete(trie, user_input)