import csv
from artifact import Artifact, ArtifactSignificance, ArtifactType
from artifact_tree import ArtifactTree

def load_dataset(file_path):
    tree = ArtifactTree()
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                artifact = Artifact(
                    artifact_ID=int(row['artifact_ID']),
                    name=row['name'],
                    era=row['era'],
                    significance=row['significance'],
                    type=row['type']
                )
                tree.add_artifact(artifact)
            except ValueError as e:
                print(f"Error loading artifact {row}: {e}")
    return tree