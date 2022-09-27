import numpy as np
from PIL import Image
from imantics import Mask

from shapely.validation import make_valid
from shapely.geometry import shape


def extract_segmentations_from_pixel_array(image_file_path):

    image = Image.open(image_file_path)
    pixel_array = np.array(image)
    unique_pixels = np.unique(pixel_array)

    segmentations = []
    for focus_pixel in unique_pixels[unique_pixels.nonzero()]:
        pa_copy = pixel_array.copy()
        pa_copy[pa_copy != focus_pixel] = 0
        polygons = Mask(pa_copy).polygons().points

        polygon_wkts = []
        for polygon in polygons:
            polygon = shape(polygon)
            polygon = make_valid(polygon)
            polygon = polygon.simplify(tolerance=2, preserve_topology=True)

            polygon_wkts.append(polygon.wkt)

        polygon_dict = {"pixel": focus_pixel.item(), "polygons": polygon_wkts}
        segmentations.append(polygon_dict)

    return segmentations
