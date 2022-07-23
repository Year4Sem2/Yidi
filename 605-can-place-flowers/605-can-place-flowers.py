class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 >= n
            else:
                return 0 >= n


        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i+1] != 1:
                        cnt+=1
                        flowerbed[i] = 1
                elif i == len(flowerbed)-1:
                    if flowerbed[i-1] != 1:
                        cnt+=1
                        flowerbed[i] = 1
                else:
                    if flowerbed[i-1] != 1 and flowerbed[i+1] != 1:
                        cnt += 1
                        flowerbed[i] = 1
                #print(flowerbed)
                #print(cnt)
        return cnt >= n
