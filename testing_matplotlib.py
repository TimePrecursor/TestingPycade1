import arcade
import numpy as np

# Constants for the window
SCREEN_WIDTH = 920
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Arcade Line Graph Example"


class GraphWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.x_values = np.linspace(0, 10, 100)
        self.y_values = np.sin(self.x_values)

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Draw the graph
        self.draw_line_graph()

        # Draw axis labels
        arcade.draw_text("X-axis", SCREEN_WIDTH - 100, 10, arcade.color.WHITE, 14)
        arcade.draw_text("Y-axis", 10, SCREEN_HEIGHT // 2, arcade.color.WHITE, 14)
        arcade.draw_text("Sine Wave", SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 30, arcade.color.WHITE, 18)

    def draw_line_graph(self):
        """Draw a simple line graph."""
        # Scale data points to fit the window
        x_offset = SCREEN_WIDTH // 2
        y_offset = SCREEN_HEIGHT // 2
        scale_x = 50
        scale_y = 100

        # Plot each point (by drawing lines between consecutive points)
        for i in range(len(self.x_values) - 1):
            x1 = x_offset + self.x_values[i] * scale_x
            y1 = y_offset + self.y_values[i] * scale_y
            x2 = x_offset + self.x_values[i + 1] * scale_x
            y2 = y_offset + self.y_values[i + 1] * scale_y
            arcade.draw_line(x1, y1, x2, y2, arcade.color.BLUE, 2)


# Run the application
if __name__ == "__main__":
    window = GraphWindow()
    arcade.run()
