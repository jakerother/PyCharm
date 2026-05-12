# test_pycharmplugin.py
"""
Tests for PyCharmPlugin module.
"""

import unittest
from pycharmplugin import PyCharmPlugin

class TestPyCharmPlugin(unittest.TestCase):
    """Test cases for PyCharmPlugin class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PyCharmPlugin()
        self.assertIsInstance(instance, PyCharmPlugin)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PyCharmPlugin()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
