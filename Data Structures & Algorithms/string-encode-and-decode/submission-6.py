class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#"
        
        
        str_encoded = "+".join(s.encode("utf-8").hex() for s in strs)
        
        return str_encoded
        

    def decode(self, s: str) -> List[str]:

        if s == "#":
            return []


        if s == "":
            return [""]
        
        hex_segments = s.split("+")

        str_decoded = [bytes.fromhex(hex_seg).decode("utf-8") for hex_seg in hex_segments]
        


        return str_decoded
