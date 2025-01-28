#Python code to find Permutations

class Solution:
    def swap(self, string, i, j):
        # Helper function to swap characters in a string
        lst = list(string)
        lst[i], lst[j] = lst[j], lst[i]
        return "".join(lst)

    def findPermutation(self, s):
        def permute(string, l, r, result):
            if l == r:
                result.add(string)  # Use a set to automatically handle duplicates
            else:
                for i in range(l, r + 1):
                    string = self.swap(string, l, i)
                    permute(string, l + 1, r, result)
                    string = self.swap(string, l, i)

        result = set()  # Use a set to store unique permutations
        n = len(s)
        permute(s, 0, n - 1, result)
        return sorted(list(result))  # Convert set to list and sort the result

# Example usage:
sol = Solution()

s1 = "YHQM"
print(sol.findPermutation(s1))