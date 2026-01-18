
from src.persistence.interfaces import IGraphGenerator


class GraphGenerator(IGraphGenerator):
    async def gen_graph(self, code:str) -> bool:
        ...