from dataclasses import dataclass
import uuid
from sdk.model.datasets.dataset import Dataset
from typing import List

@dataclass
class GeoFeatureProperty:
    roiID: uuid
    type: str
    elevation: float # Elevation over 0 
    datasets: List[Dataset]

    def __post_init__(self):
        self.roiID = uuid.uuid4()