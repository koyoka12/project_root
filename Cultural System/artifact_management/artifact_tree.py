from collections import defaultdict  
from artifact import Artifact, ArtifactSignificance, ArtifactType  
  
class ArtifactTree:  
    def __init__(self):  
        self.root = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))  
  
    def add_artifact(self, artifact):  
        # 根据era, type, significance添加artifact到树中  
        pass  
  
    def remove_artifact(self, artifact_ID):  
        # 从树中移除指定artifact_ID的artifact  
        pass  
  
    def modify_artifact(self, artifact_ID, **kwargs):  
        # 根据artifact_ID修改artifact的属性  
        pass  
  
    def search_artifacts(self, type=None, significance=None):  
        # 搜索并返回指定类型和/或显著性的artifact列表  
        pass  