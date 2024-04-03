from dataclasses import dataclass
import uuid
from sdk.model.datasets.dataset import Dataset
from typing import List

@dataclass
class GeoFeatureProperty:
    type:str
    datasets: List[Dataset]