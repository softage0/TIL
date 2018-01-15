import collections

class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # A_counts = {}
        # B_counts = {}
        # C_counts = {}
        # D_counts = {}
        # count = 0

        # for a in range(len(A)):
        #     a_sum = A[a]
        #     a_sum_count = A_counts.get(a_sum)
        #     if a_sum_count:
        #         count = count + a_sum_count
        #         continue
                
        #     a_count = 0
                
        #     for b in range(len(B)):
        #         b_sum = A[a] + B[b]
        #         b_sum_count = B_counts.get(b_sum)
        #         if b_sum_count:
        #             a_count = a_count + b_sum_count
        #             continue
                
        #         b_count = 0
                
        #         for c in range(len(C)):
        #             c_sum = A[a] + B[b] + C[c]
        #             c_sum_count = C_counts.get(c_sum)
        #             if c_sum_count:
        #                 b_count = b_count + c_sum_count
        #                 continue
                        
        #             c_count = 0

        #             for d in range(len(D)):
        #                 if A[a] + B[b] + C[c] + D[d] == 0:
        #                     c_count = c_count + 1
                    
        #             C_counts[c_sum] = c_count
        #             b_count = b_count + c_count
                    
        #         B_counts[b_sum] = b_count
        #         a_count = a_count + b_count

        #     A_counts[a_sum] = a_count
        #     count = count + a_count

        AB = collections.Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)

S = Solution()
A = list(map(int, input().strip('[').strip(']').split(',')))
B = list(map(int, input().strip('[').strip(']').split(',')))
C = list(map(int, input().strip('[').strip(']').split(',')))
D = list(map(int, input().strip('[').strip(']').split(',')))

print(S.fourSumCount(A, B, C, D))
