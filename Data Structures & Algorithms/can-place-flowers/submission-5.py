class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed)==1 and n ==0:
            return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                
                # Check left neighbor
                left = (i == 0 or flowerbed[i - 1] == 0)
                
                # Check right neighbor
                right = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if left and right:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True
                

        return False