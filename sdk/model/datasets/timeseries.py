from typing import List
from dataclasses import dataclass
from sdk.model.datasets.dataset import Dataset

from .timeseriesItem import TimeSeriesItem

@dataclass
class Timeseries(Dataset):
    items: List[TimeSeriesItem]