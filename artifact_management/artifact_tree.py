from collections import defaultdict
from artifact import Artifact, ArtifactSignificance, ArtifactType

class ArtifactTree:
    def __init__(self):
        self.tree = defaultdict(lambda: defaultdict(list))

    def add_artifact(self, artifact):
        self.tree[artifact.era][artifact.type].append(artifact)

    def remove_artifact(self, artifact_ID):
        for era, types in self.tree.items():
            for type_, artifacts in types.items():
                artifacts[:] = [a for a in artifacts if a.artifact_ID != artifact_ID]

    def modify_artifact(self, artifact_ID, **kwargs):
        for era, types in self.tree.items():
            for artifacts in types.values():
                for artifact in artifacts:
                    if artifact.artifact_ID == artifact_ID:
                        for key, value in kwargs.items():
                            setattr(artifact, key, value)

    def search_artifacts(self, type=None, significance=None):
        results = []
        for era in self.tree:
            for type_, artifacts in self.tree[era].items():
                if type is not None and type_ != type:
                    continue
                for artifact in artifacts:
                    if significance is not None and artifact.significance != significance:
                        continue
                    results.append(artifact)
        return results