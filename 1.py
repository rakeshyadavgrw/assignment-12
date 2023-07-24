#***************Q1***************#
# python3
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
		# Here is the better way, we only need to search once, and then enlarge the border pointers to find what we want
		right = bisect_left(arr,x)
        left = right-1
        for _ in range(k):
            if left < 0: right += 1
            elif right >= len(arr): left -= 1
            else:
                if x-arr[left] <= arr[right]-x: left -= 1
                else: right += 1
        return arr[left+1:right]

#***************Q2****************#
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return -1
        heap = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                nextVal = -matrix[row][col]
                if len(heap) < k:
                    heapq.heappush(heap, nextVal)
                elif nextVal > heap[0]:
                    heapq.heappushpop(heap, nextVal)
        return -heap[0]
    
#****************Q3****************#
        from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt=defaultdict(lambda :[0,""])
        for i in words:
            cnt[i]=[cnt[i][0]-1,i]
        lst=list(cnt.values())
        heapq.heapify(lst)
        lst=heapq.nsmallest(k,lst)
        ans=[]
        for i in lst:
            ans.append(i[1])
        return ans
    
    #***************Q4***************#
    class Solution:
    def __init__(self):
	    self.diameter = 0  # stores the maximum diameter calculated
	
    def depth(self, node: Optional[TreeNode]) -> int:
        """
        This function needs to do the following:
            1. Calculate the maximum depth of the left and right sides of the given node
            2. Determine the diameter at the given node and check if its the maximum
        """
        # Calculate maximum depth
        left = self.depth(node.left) if node.left else 0
        right = self.depth(node.right) if node.right else 0
        # Calculate diameter
        if left + right > self.diameter:
            self.diameter = left + right
        # Make sure the parent node(s) get the correct depth from this node
        return 1 + (left if left > right else right)
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        self.depth(root)  # root is guaranteed to be a TreeNode object
        return self.diameter
    
    #************Q5***************#
    class Solution(object):
    def isSymmetric(self, root):
        # Special case...
        if not root:
            return true;
        # Return the function recursively...
        return self.isSame(root.left, root.right)
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
    

    #*********************Q6******************#
    from functools import cmp_to_key
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sorter(x, y):
            n, m = len(x), len(y)
            if n != m:
                return -1 if n < m else 1 # when n > m
            else:
                return -1 if x < y else 1 if x > y else 0
            
        key = cmp_to_key(sorter)
        nums.sort(key=key, reverse=True)
        return nums[k-1]
    
    #****************Q7***************#
    class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #Base Case
            return root
        self.invertTree(root.left) #Call the left substree
        self.invertTree(root.right)  #Call the right substree
        # Swap the nodes
        root.left, root.right = root.right, root.left
        return root # Return the root
    
    #****************Q8****************#
    class Solution:
    # 28 ms, 92.33%. Time: O(N). Space: O(H)
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_depth(node):
            if not node: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1
        
        def insert_value(node, lo, hi, depth=0):
            if not node: return
            mid = (lo + hi) // 2
            output[depth][mid] = str(node.val)
            insert_value(node.left, lo, mid, depth + 1)
            insert_value(node.right, mid, hi, depth + 1)

        depth = get_depth(root)
        output = [[""] * (2**depth - 1) for _ in range(depth)]
        
        insert_value(root, 0, 2**depth - 1)
        return output