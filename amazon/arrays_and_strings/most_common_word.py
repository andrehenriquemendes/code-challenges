# https://leetcode.com/problems/most-common-word/

class Solution(object):

    def getWordList(self, paragraph):
        normalized_paragraph =  ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        return normalized_paragraph.split()

    def getWordList(self, paragraph):
        words = []
        word = ''
        for i, c in enumerate(paragraph):
            if c not in [' ', '!', '?', "'", ',', ';', '.']:
                word = word + c
            else:
                if word != '':
                    words.append(word.lower())
                    word = ''
        if word != '':
            words.append(word.lower())
        return words


    def getBannedWordsDictionary(self, banned):
        banned_words = {}
        for word in banned:
            banned_words[word] = 1
        return banned_words

    def countWordOccurences(self, word_list, banned_words):
        dictionary = {}
        for word in word_list:
            if word not in banned_words:
                if word not in dictionary:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1
        return dictionary

    def getMostCommonWord(self, dictionary):
        count_most_common = 0
        most_common_word = None
        for word, count in dictionary.items():
            if count > count_most_common:
                count_most_common = count
                most_common_word = word
        return most_common_word

    def mostCommonWord(self, paragraph, banned):
        banned_words = self.getBannedWordsDictionary(banned)
        word_list = self.getWordList(paragraph)
        dictionary = self.countWordOccurences(word_list, banned_words)
        return self.getMostCommonWord(dictionary)


sol = Solution()
text = "Bob hit a ball, the hit BALL flew far after it was hit."
banneds = ["hit"]
print(sol.mostCommonWord(text, banneds))