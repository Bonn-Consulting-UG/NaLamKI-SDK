from dataclasses import dataclass
from sdk.model.datasets.dataset import Dataset
from typing import List

from .timeseriesItem import TimeSeriesItem

@dataclass
class Timeseries(Dataset):
    items: List[TimeSeriesItem]

    def __post_init__(self):
        self.type = "TIMESERIES"