class Valve:
    def __init__(self, id: str, flow_rate: int, neighbors: list):
        # Status 0 is closed 1 is open.
        self.status = 0
        self.id = id
        self.neighbors = neighbors
        self.flow_rate = flow_rate
