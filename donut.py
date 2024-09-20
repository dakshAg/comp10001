import numpy as np
import matplotlib.pyplot as plt
from time import time, sleep, perf_counter

# torus
theta_spacing = 0.025
phi_spacing = 0.065
R1 = 1.0
R2 = 2.0

# rotation
rotX_rate = 0.07
rotY_rate = 0.0
rotZ_rate = 0.02

# projection
camera_z = -5.0
proj_distance = -camera_z * 3 / (4 * (R1 + R2))

# lighting
light_strength = 0.72
light_direction = np.array([0.0, 1.0, -1.0])

# rendering
screen_size: int = 40
maxfps = 30.0


def illumination(value: np.ndarray) -> np.ndarray:
    """Map an array of brightness values to ascii characters"""
    illumination_chars = np.fromiter(" .,-~:;=!*#$@", dtype="<U1")
    value = (len(illumination_chars) - 1) * np.clip(value, 0.0, 1.0)
    return illumination_chars[value.astype(int)]


def rotX(theta: float) -> np.ndarray:
    """
    Construct a 3×3 matrix representing a counter-clockwise rotation
    about the X axis
    """
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    return np.array([
        [1, 0, 0],
        [0, cos_theta, sin_theta],
        [0, -sin_theta, cos_theta],
    ])


def rotY(theta: float) -> np.ndarray:
    """
    Construct a 3×3 matrix representing a counter-clockwise rotation
    about the Y axis
    """
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    return np.array([
        [cos_theta, 0, -sin_theta],
        [0, 1, 0],
        [sin_theta, 0, cos_theta],
    ])


def rotZ(theta: float) -> np.ndarray:
    """
    Construct a 3×3 matrix representing a counter-clockwise rotation
    about the Z axis
    """
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    return np.array([
        [cos_theta, -sin_theta, 0],
        [sin_theta, cos_theta, 0],
        [0, 0, 1],
    ])


def generate_torus(
        r1: float,
        r2: float,
        dphi: float,
        dtheta: float
) -> tuple[np.ndarray, np.ndarray]:
    """Generate points and surface normals on a torus."""
    phis = np.arange(0, 2 * np.pi, dphi)
    thetas = np.arange(0, 2 * np.pi, dtheta)

    points = np.array([
        rotZ(theta) @ ([r2, 0, 0] + rotY(phi) @ [r1, 0, 0])
        for phi in phis
        for theta in thetas
    ]).T  # (2, num points)

    normals = np.array([
        rotZ(theta) @ rotY(phi) @ [1, 0, 0]
        for phi in phis
        for theta in thetas
    ]).T  # (2, num points)

    return points, normals


def render_points(
        output: np.ndarray,
        points: np.ndarray,
        zs: np.ndarray,
        brightness: np.ndarray
) -> None:
    chars = illumination(brightness)

    zbuffer = np.zeros_like(output, dtype='float')
    zbuffer.fill(np.inf)
    for xp, yp, z, char in zip(points[0], points[1], zs, chars):
        if z < zbuffer[yp, xp]:
            zbuffer[yp, xp] = z
            output[yp, xp] = char


def pprint(array: np.ndarray) -> None:
    """Pretty print the frame."""
    print(*[" ".join(row) for row in array], sep="\n")


if __name__ == "__main__":
    points_all, normals_all = generate_torus(R1, R2, phi_spacing, theta_spacing)

    rotation = rotZ(rotZ_rate) @ rotY(rotY_rate) @ rotX(rotX_rate)
    proj = np.array([[1, 0, 0], [0, -1, 0]])
    R = rotX(0)

    for _ in range(int(10 * maxfps)):
        frame_start = time()

        output = np.full((screen_size, screen_size), " ")

        R = rotation @ R

        points = R @ points_all
        normals = R @ normals_all

        # cull points that are facing away from the camera
        mask = normals[2] <= 0
        points = points[:, mask]
        normals = normals[:, mask]

        # project from world coordinates to screen coordinates
        projection_scaling = proj_distance / (points[2] - camera_z)
        points_screen = proj @ points * projection_scaling

        # remove points that are offscreen
        mask = (np.abs(points_screen[0]) < 1) & (np.abs(points_screen[1]) < 1)
        points_screen = points_screen[:, mask]
        points = points[:, mask]
        normals = normals[:, mask]

        # convert from screen coordinates to pixel coordinates
        points_pixel = (screen_size / 2 * (1 + points_screen)).astype(int)

        # calculate illumination
        Ls = light_strength * light_direction.T @ normals

        render_points(output, points_pixel, points[2], Ls)

        # framerate limiter
        sleep_time = frame_start + 1 / maxfps - time()
        if sleep_time > 0:
            sleep(sleep_time)

        print("\x1b[H")
        pprint(output)
