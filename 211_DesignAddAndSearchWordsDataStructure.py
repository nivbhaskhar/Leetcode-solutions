#https://leetcode.com/problems/design-add-and-search-words-data-structure/description
class TrieNode:
    def __init__(self, is_end: bool):
        self.is_end = is_end
        self.children = {} # will store key:value pairs where keys = characters and value = TrieNodes

class WordDictionary:

    def __init__(self):
        self.root = TrieNode(False)
        

    def addWord(self, word: str) -> None:
        current_node = self.root
        for i, character in enumerate(word):
            if character in current_node.children:
                next_node = current_node.children[character]   
            else:
                next_node = TrieNode(False)
                current_node.children[character] = next_node
            current_node = next_node
        
        current_node.is_end = True
        
    def _search(self, characters: list[str], start_pos: int, current_node: TrieNode)-> bool:
        end_pos = len(characters)
        for pos in range(start_pos,end_pos):
            character = characters[pos]
            if character == ".":
                for next_character in current_node.children:
                    if self._search(characters, pos+1,current_node.children[next_character]):
                        return True
                else:
                    return False
            elif character in current_node.children:
                current_node = current_node.children[character]
            else:
                return False
        return current_node.is_end
        


    def search(self, word: str) -> bool:
        node = self.root
        characters = [c for c in word]
        pos = 0
        return self._search(characters, pos, node)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
