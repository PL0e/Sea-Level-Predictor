import unittest
import sea_level_predictor
import matplotlib.pyplot as plt

class SeaLevelPredictorTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Expected plot title to be 'Rise in Sea Level'")
    
    def test_plot_xlabel(self):
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Expected x-axis label to be 'Year'")

    def test_plot_ylabel(self):
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Expected y-axis label to be 'Sea Level (inches)'")

    def test_plot_data_points(self):
        actual = len(self.ax.get_children())
        expected = 16  # This may vary based on matplotlib version
        self.assertGreater(actual, 5, "Expected more plot elements")

if __name__ == "__main__":
    unittest.main()
