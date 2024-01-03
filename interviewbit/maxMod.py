class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        size = len(A)
        max_mod = 0
        list_A = list(set(A))
        if len(list_A) == 0:
            return 0
        if len(list_A) == 1:
            return 0
        max_A = max(list_A)
        final_list = []
        for ele in list_A:
            if ele != max_A:
                final_list.append(ele)
        return max(final_list)
