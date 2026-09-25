import string

class Solution(object):
    def mapWordWeights(self, words, weights):
        """
        :type words: List[str]
        :type weights: List[int]
        :rtype: str
        """

        mapped = ""
        for word in words:
            weight_sum = 0
            for letter in word:
                weight_sum += weights[string.lowercase.index(letter)]
            
            index = (weight_sum % 26)
            mapped += string.lowercase[25 - index]
        
        return mapped
        