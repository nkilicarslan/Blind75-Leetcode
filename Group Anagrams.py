class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dict to store every word from strs list
        dict_of_string = {}
        # iterate over the string list
        for word in strs:
            # sort each string
            sorted_word = ''.join(sorted(word))
            # if sorted string not in the dict
            if sorted_word not in dict_of_string:
                # create a key value pair in the dict
                dict_of_string[sorted_word] = [word]
            # else, sorted string appears in the dict
            else:
                # append the orijinal string to the related key value
                dict_of_string[sorted_word].append(word)
        # return the values of the dict
        return dict_of_string.values()
