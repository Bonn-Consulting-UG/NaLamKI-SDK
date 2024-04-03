from dataclasses import dataclass, field
import uuid
from sdk.model.datasets.dataset import Dataset
from typing import List

@dataclass
class GeoFeatureProperty:
    type: str
    elevation: float = None # Elevation over 0 
    roiID: uuid = None
    datasets: List[Dataset] = field(default_factory=list)

    def __post_init__(self):
        self.roiID = uuid.uuid4()