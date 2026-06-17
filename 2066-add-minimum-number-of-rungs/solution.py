class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        current_height = 0
        additional_rungs = 0
        for rung in rungs:
            if rung - current_height > dist:
                additional_rungs += (rung - current_height - 1) // dist
            current_height = rung
        return additional_rungs
