class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        return s.replace('(',"{").replace(')',"}").format_map(defaultdict(lambda: '?', knowledge))
