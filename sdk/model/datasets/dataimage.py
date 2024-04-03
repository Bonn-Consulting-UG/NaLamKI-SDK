from dataclasses import dataclass
from sdk.model.datasets.dataset import Dataset
import uuid
from datetime import datetime
from .datavalue import DataValue
from .datafile import File
from sdk.model.annotations.bbox import BoundingBox

@dataclass
class Image(File):
    bbox: BoundingBox = None
    