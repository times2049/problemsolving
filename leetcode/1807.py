class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        class Default(dict): 
            def __missing__(self, key): return '?'
        return s.replace('(',"{").replace(')',"}").format_map(Default(dict(knowledge)))
