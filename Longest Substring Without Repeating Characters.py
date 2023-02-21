class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a list to keep max counts
        keep_list_count = [0]
        # create a dict to keep subsequent string elements
        keep_subseq_elem = {}
        # create a variable to count maximum number
        max_count = 0
        # create a left pointer variable
        left_ptr = 0
        # create a right pointer variable
        right_ptr = 0
        # iterate over the string
        for i in s:
            # if new char not in the dict, store it and increase the count variable
            if i not in keep_subseq_elem:
                keep_subseq_elem[i] = 1
                max_count += 1
            # if new char not in the list
            else:
                # take the substring
                subseq_str = s[left_ptr:right_ptr]
                # find the index of the new char in the substring
                subseq_index = subseq_str.index(i)
                # adjust the left pointer
                left_ptr += subseq_index + 1
                # store the max count in the list
                keep_list_count.append(max_count)
                # calculate new substring length
                max_count = len(subseq_str) - subseq_index
                # update the dict with new substring
                keep_subseq_elem = {}
                for k in range(left_ptr,right_ptr+1):
                    keep_subseq_elem[s[k]] = 1

            # every iteration move the pointer to the right
            right_ptr += 1

        return max(max(keep_list_count),max_count)

a = Solution()
a.lengthOfLongestSubstring("abcabcaa")
