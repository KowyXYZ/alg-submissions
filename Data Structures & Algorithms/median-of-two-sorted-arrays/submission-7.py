class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        print(nums1 + nums2)
        m  = sorted(nums1 + nums2)

        l = 0
        r = len(m) 
        k = r
        res = 0


        if len(nums1) == 0 and len(nums2) > 0 and 0 not in nums2:
             print("returned 0 from nums 1 ")
                
        if len(nums2) == 0 and len(nums1) > 0 and 0 not in nums1:
             print("returned 0 from nums 2 ")
          
            
      
        if r % 2 == 0:
            print("no middle #10")
            k = r // 2
            print(k)
            return (m[k - 1] + m[k]) / 2
        else:
            print("middle found #11")
            k = r // 2
            return float(m[k])

        return 0