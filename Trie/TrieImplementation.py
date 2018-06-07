# Implementation of Trie Data structure as follows :

class TrieNode(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False


class TrieImpl(object):
    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def _charToIndex(self, ch):
        return ord(ch) - ord('a')

    def insert(self, key):
        level_up = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not level_up.children[index]:
                level_up.children[index] = self.get_node()
            level_up = level_up.children[index]
        level_up.isEndOfWord = True

    def search(self, key):
        level_up = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not level_up.children[index]:
                return False
            level_up = level_up.children[index]
        return level_up != None and level_up.isEndOfWord


def main():
    keys = ["the", "a", "there"]
    output = ["Not Present in trie", "Present in Trie"]
    t = TrieImpl()
    for key in keys:
        t.insert(key)

    print("{} -- {}".format("the", output[t.search("the")]))


if __name__ == '__main__':
    main()
