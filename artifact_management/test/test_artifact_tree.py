import unittest
from artifact_tree import ArtifactTree
from dataset_loader import load_dataset

class TestArtifactTree(unittest.TestCase):
    def setUp(self):
        self.tree = load_dataset('cultural_heritage_artifacts.csv')

    def test_add_artifact(self):
        new_artifact = Artifact(11, 'New Artifact', 'Modern', 'HIGH', 'SCULPTURE')
        self.tree.add_artifact(new_artifact)
        self.assertIn(new_artifact, self.tree.search_artifacts(era='Modern'))

    def test_remove_artifact(self):
        self.tree.remove_artifact(1)
        self.assertNotIn(1, [a.artifact_ID for a in self.tree.search_artifacts(era='Ancient')])

    def test_modify_artifact(self):
        self.tree.modify_artifact(2, name='Modified Venus de Milo')
        self.assertEqual(self.tree.search_artifacts(name='Modified Venus de Milo'), [Artifact(2, 'Modified Venus de Milo', 'Ancient', 'HIGH', 'SCULPTURE')])

    def test_search_artifacts(self):
        high_significance_artifacts = self.tree.search_artifacts(significance=ArtifactSignificance.HIGH)
        self.assertTrue(all(a.significance == ArtifactSignificance.HIGH for a in high_significance_artifacts))

    def test_search_artifacts_by_type(self):
        sculptures = self.tree.search_artifacts(type=ArtifactType.SCULPTURE)
        self.assertTrue(all(a.type == ArtifactType.SCULPTURE for a in sculptures))

if __name__ == '__main__':
    unittest.main()