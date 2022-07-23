class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set_candy = set(candyType)
        if len(set_candy) < len(candyType)/2:
            return len(set_candy)
        else:
            return int(len(candyType)/2)
        