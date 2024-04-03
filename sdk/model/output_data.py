from dataclasses import dataclass
import uuid

from datetime import datetime
from typing import List

from sdk.model.geojson.feature import GeoFeature
from sdk.model.geojson.geometry import GeoGeometry
from sdk.model.geojson.coordinates import GeoCoordinates
from sdk.model.geojson.property import GeoFeatureProperty

from sdk.model.datasets.dataset import Dataset
from sdk.model.datasets.timeseries import Timeseries
from sdk.model.datasets.timeseriesItem import TimeSeriesItem
from sdk.model.datasets.datavalue import DataValue
from sdk.model.datasets.datafile import File
from sdk.model.datasets.dataimage import Image

from sdk.model.datasets.dataset import Dataset

@dataclass
class OutputData: 
    type: str
    
@dataclass
class GeoOutputData(OutputData):
    features: List[GeoFeature]

@dataclass
class Datasets(OutputData):
    dataset: List[Dataset]
