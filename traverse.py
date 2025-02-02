# -*- coding: utf-8 -*-
"""Traverse
"""

def traverse_complex_space(z0, steps, angles, scales):
    """
    Traverse the complex space starting from z0.

    Parameters:
    - z0: Initial complex number
    - steps: Number of steps to traverse
    - angles: List of angles for each step
    - scales: List of scaling factors for each step

    Returns:
    - List of complex numbers representing the path
    """
    path = [z0]
    z = z0

    for k in range(steps):
        theta = angles[k % len(angles)]
        a = scales[k % len(scales)]
        z = a * z * cmath.exp(1j * theta)
        path.append(z)

    return path

# Example usage
import cmath

z0 = 1 + 0j  # Starting point in the complex plane
steps = 100  # Number of steps to traverse
angles = [cmath.pi / cmath.e, cmath.e / cmath.pi]  # Angles using transcendental numbers
scales = [1, 1]  # No scaling for simplicity

path = traverse_complex_space(z0, steps, angles, scales)
print(path)
