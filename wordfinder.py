from random import choice
class WordFinder:
    """finds random words from a dictionary.
    """
    def __init__(self, file):
        self.file = []
        with open(file, "r") as _file:
            for line in _file:
                self.file.append(line)
        print(f"{len(self.file)} words read")
    def random(self):
        _choice = choice(self.file)
        return _choice
    
class SpecialWordFinder(WordFinder):
    """finds words from a dictionary but ignores comments and empty lines"""
    def __init__(self, file):
        self.file = []
        with open(file, "r") as _file:
            for line in _file:
                if (line[0] == "#" or line == ""):
                    continue
                self.file.append(line)
        print(f"{len(self.file)} words read")

wf = WordFinder("words.txt")
print(wf.random())


    
