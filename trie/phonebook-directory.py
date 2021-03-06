class Trie:
    def __init__(self):
        self.root = {}

    def add(self, name, phone_number):
        """adds a name/number to the Trie"""
        node = self.root
        for char in name:
            if char not in node:
                node[char] = {}
            node = node[char]

        node["NUMBER"] = phone_number

    def find(self, prefix):
        """returns node after consuming given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.keys():
                return None
            node = node[char]

        return node

    def list_contacts(self, prefix):
        sub_trie = self.find(prefix)
        _print(sub_trie, prefix)


def _print(subtrie, prefix):
    for key in subtrie.keys():
        if (key == "NUMBER"):
            print("{} : {}".format(prefix, subtrie[key]))
        else:
            _print(subtrie[key], prefix + key)


T = Trie()
T.add("Joe", 1234567868)
T.add("James", 4483455747)
T.add("Samantha", 4454443947)
T.list_contacts("Ja")