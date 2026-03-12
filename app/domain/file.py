from dataclasses import dataclass

@dataclass
class MediaFile:
    name: str
    size: int
    path: str