class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = {}
        for n in strs:
            sort = "".join(sorted(n))
            if sort not in A:
                A[sort] = []

            A[sort].append(n)
            
        return list(A.values())