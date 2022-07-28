class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        try:
            k = (y1-y2) / (x1-x2)
            b = y1 - k*x1

            # equation = k * x + b
        
            for cr in coordinates:
                x, y = cr
                eq = k*x + b
                if eq != y:
                    return False
        except ZeroDivisionError:
            for cr in coordinates:
                x, y = cr
                if x != x1:
                    return False
            
        return True