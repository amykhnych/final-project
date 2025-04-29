from manim import *

class MoveTriangle(Scene):
    def construct(self):
        # Create a triangle
        triangle = Triangle().scale(1.5)

        # Get a specific vertex (e.g., the bottom-left vertex)
        vertex_point = triangle.get_vertices()[0]

        # Define the target point to move that vertex to
        target_point = np.array([2, 1, 0])

        # Calculate the shift needed
        shift_vector = target_point - vertex_point

        # Move the triangle using shift
        self.play(triangle.animate.shift(shift_vector))

        # Keep the triangle on screen
        self.wait()
