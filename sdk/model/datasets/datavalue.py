
from dataclasses import dataclass
from sdk.model.datasets.dataset import Dataset
import uuid

@dataclass
class DataValue:
    value: any
    unit: str = None
    type: str = None