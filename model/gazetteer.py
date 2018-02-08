 # -*- coding: utf-8 -*-


class Gazetteer:
    def __init__(self, gazetteerPath):
        self.gazetteer = {}
        self.gazetteerFile = open(gazetteerPath, 'r', encoding="utf-8")
        for line in self.gazetteerFile:
            l = line.split()
            tag = l.pop()
            word = " "
            if(tag == "person"):
                for w in l:
                    self.gazetteer[w] = tag
            else:
                self.gazetteer[word.join(l)] = tag

    def lookup_tags(self, words, tags):
        for i, word in enumerate(words):
            if word in self.gazetteer:
                print(word)
                print(self.gazetteer[word])
                tags[i] = self.gazetteer[word]
        return tags
            