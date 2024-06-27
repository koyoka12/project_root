import csv  
from artifact_tree import ArtifactTree  
from artifact import Artifact, ArtifactSignificance, ArtifactType  
  
def load_dataset(file_path):  
    tree = ArtifactTree()  
    with open(file_path, mode='r', encoding='utf-8') as file:  
        reader = csv.DictReader(file)  
        for row in reader:  
            artifact = Artifact(  
                artifact_ID=int(row['artifact_ID']),  
                name=row['name'],  
                era=row['era'],  
                significance=row['significance'],  
                type=row['type']  
            )  
            tree.add_artifact(artifact)  # 假设add_artifact方法已经实现  
    return tree  
  
# 加载数据集并返回ArtifactTree实例