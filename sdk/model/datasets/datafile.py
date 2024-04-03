from dataclasses import dataclass

@dataclass
class File:
    uri:str
    name:str
    type:str # NaLamKI Type (z.B. DROHNENBILD 10m)
     
    