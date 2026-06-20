class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        K=celsius+273.15
        f=celsius*1.80+32
        return[K,f]
