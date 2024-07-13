python
import unittest
import subprocess

class TestScripts(unittest.TestCase):
    
    def test_train_model(self):
        result = subprocess.run(["python", "scripts/train_model.py", "--config=config/config.yaml"], capture_output=True, text=True)
        self.assertIn("Training with configuration", result.stdout)
    
    def test_interact_with_model(self):
        result = subprocess.run(["python", "scripts/interact_with_model.py"], capture_output=True, text=True)
        self.assertIn("Starting interactive session with the model", result.stdout)
    
    def test_deploy_model(self):
        result = subprocess.run(["python", "scripts/deploy_model.py", "--config=config/deploy_config.yaml"], capture_output=True, text=True)
        self.assertIn("Deploying model with configuration", result.stdout)

if __name__ == "__main__":
    unittest.main()
