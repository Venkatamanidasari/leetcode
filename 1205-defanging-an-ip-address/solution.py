class Solution:
    def defangIPaddr(self, address: str) -> str:
        list1=address.split(".")
        return "[.]".join(list1)
        
