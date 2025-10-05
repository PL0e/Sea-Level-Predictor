# This entrypoint file to be used in development. Start by reading README.md
import sea_level_predictor
from unittest import main

# Draw the plot
sea_level_predictor.draw_plot()

# Run unit tests automatically
main(module='test_module', exit=False)
