from enum import Enum

class OutFile(Enum):
    CSV = 1
    PARQUET = 2
    XLSX = 3
    PICKLE = 4

    def list(self):
        return [s.value for s in self]