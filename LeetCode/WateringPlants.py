# https://leetcode.com/problems/watering-plants/

class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        water = capacity
        steps = 0
        for i, c in enumerate(plants):
            if water >= c:
                water -= c
                steps += 1
            else:
                water = capacity - c
                steps += i + 1 + i
        return steps
            
        