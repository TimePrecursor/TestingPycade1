import arcade
import numpy as np

# Constants for the window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Slithering Sine Wave"


class GraphWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Initial X and Y values of the sine wave (this will oscillate horizontally and vertically)
        self.x_values = np.linspace(0, 2 * np.pi, 100)  # X values range from 0 to 2π
        self.y_values = np.sin(self.x_values)  # Initial sine wave values for Y

        # Create the text objects for axis and title
        self.x_axis_label = arcade.Text("X-axis", SCREEN_WIDTH - 100, 10, arcade.color.WHITE, 14)
        self.y_axis_label = arcade.Text("Y-axis", 10, SCREEN_HEIGHT // 2, arcade.color.WHITE, 14)
        self.title = arcade.Text("Slithering Sine Wave", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT - 30,
                                 arcade.color.WHITE, 18)

    def on_draw(self):
        """Render the screen."""
        self.clear()

        # Draw the graph
        self.draw_line_graph()

        # Draw the text labels
        self.x_axis_label.draw()
        self.y_axis_label.draw()
        self.title.draw()

    def on_update(self, delta_time):
        """Update the graph in real time."""
        # Update the Y values to animate the sine wave slithering
        self.y_values = np.sin(self.x_values + self.time * 2)  # Animate sine wave vertically

    def draw_line_graph(self):
        """Draw a simple line graph."""
        # Set the x_offset to 100 to start the graph 100 pixels from the left
        x_offset = 100  # Start the graph 100 pixels from the left side
        y_offset = SCREEN_HEIGHT // 2  # Keep y_offset centered vertically in the window

        # Scaling factors to fit the graph within the screen dimensions
        scale_x = SCREEN_WIDTH // 10  # 10 units per screen width
        scale_y = SCREEN_HEIGHT // 4  # 4 units per screen height (sine wave amplitude)

        # Plot each point by drawing lines between consecutive points
        for i in range(len(self.x_values) - 1):
            x1 = x_offset + self.x_values[i] * scale_x
            y1 = y_offset + self.y_values[i] * scale_y
            x2 = x_offset + self.x_values[i + 1] * scale_x
            y2 = y_offset + self.y_values[i + 1] * scale_y

            # Draw the line connecting two points (form the graph)
            arcade.draw_line(x1, y1, x2, y2, arcade.color.BLUE, 2)


# Run the application
if __name__ == "__main__":
    window = GraphWindow()
    arcade.run()
