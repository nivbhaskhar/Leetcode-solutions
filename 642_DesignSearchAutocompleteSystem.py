#https://leetcode.com/problems/design-search-autocomplete-system/
from collections import defaultdict
class TrieNode:
    def __init__(self, is_end = False):
        self.is_end = is_end
        self.children = {}
        self.sentences = defaultdict(int)

class AutocompleteSystem:
    def __init__(self, sentences: list[str], times: list[int]):
        self.root = TrieNode()
        self.current_node = self.root
        for sentence, count in zip(sentences, times):
            self.add(sentence, count)
        self.current_sentence = []
        self.dead_end = TrieNode()


    def add(self, sentence: str, count: int)->None:
        current_node = self.root
        for i, character in enumerate(sentence):
            current_node.sentences[sentence] += count
            if character in current_node.children:
                next_node = current_node.children[character]   
            else:
                next_node = TrieNode(False)
                current_node.children[character] = next_node
            current_node = next_node
        current_node.sentences[sentence] += count
        current_node.is_end = True

        

    def input(self, c: str) -> list[str]:
        if c == "#":
            self.add("".join(self.current_sentence), 1)
            self.current_sentence = []
            self.current_node = self.root
            return []
        
        self.current_sentence.append(c)
        if c not in self.current_node.children:
            self.current_node = self.dead_end
            return []
        
        else:
            self.current_node = self.current_node.children[c]
            sentences = self.current_node.sentences
            sorted_sentences = sorted(sentences.items(), key = lambda x: (-x[1], x[0]))
            return [x for x,y in sorted_sentences[:3]]



# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)