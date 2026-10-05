import cv2
import numpy as np

def blur(gray: np.ndarray, kernel_size: int = 5) -> np.ndarray:
    return cv2.GaussianBlur(gray, (kernel_size, kernel_size), 0)

def threshold_otsu(gray: np.ndarray) -> np.ndarray:
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return binary