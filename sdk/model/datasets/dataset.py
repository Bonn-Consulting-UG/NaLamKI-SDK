from dataclasses import dataclass
import uuid
   

@dataclass
class Dataset:
    name: str # Unique in Feature (Reference for Dashboard Template)
    type : str
    id: uuid

    def __post_init__(self):
        self.id = uuid.uuid4()
