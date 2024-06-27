from enum import Enum  
  
class ArtifactSignificance(Enum):  
    HIGH = 1  
    MEDIUM = 2  
    LOW = 3  
  
class ArtifactType(Enum):  
    SCULPTURE = 1  
    PAINTING = 2  
    DOCUMENT = 3  
  
class Artifact:  
    def __init__(self, artifact_ID, name, era, significance, type):  
        self.artifact_ID = artifact_ID  
        self.name = name  
        self.era = era  
        self.significance = ArtifactSignificance[significance.upper()]  
        self.type = ArtifactType[type.upper()]  
  
    def __repr__(self):  
        return f"Artifact(ID={self.artifact_ID}, Name={self.name}, Era={self.era}, Significance={self.significance.name}, Type={self.type.name})"  
  
    def __eq__(self, other):  
        if isinstance(other, Artifact):  
            return self.artifact_ID == other.artifact_ID  
        return False  