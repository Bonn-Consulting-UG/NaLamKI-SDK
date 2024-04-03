from dataclasses import dataclass

@dataclass
class BoundingBox():
    x:int
    y:int
    h:int
    w:int
    classification: str = None
    accuracy: int = None
    