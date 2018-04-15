class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sorted_dict = sorted(dict, key=lambda i: len(i))
        splited_words = sentence.split()
        replaced_word = []
        
        for word in splited_words:
            for root in sorted_dict:
                if root in word:
                    replaced_word.append(root)
                    break;
                elif root == sorted_dict[-1]:
                    replaced_word.append(word)

        return " ".join(replaced_word)
