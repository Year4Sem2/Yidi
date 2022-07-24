class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
        for i in range(len(image)):
            #print(i)
            for j in range(len(image[0])):
                #print(j)
                if image[i][j] == 0:
                    #print("Okay")
                    #print(image[i])
                    image[i][j] = 1
                    #print(image[i])
                    #print(image)
                else:
                    image[i][j] = 0
        return image
        