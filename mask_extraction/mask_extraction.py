import numpy as np
from PIL import Image

from geometry_processing import (
    get_polygons_for_voxel,
    get_simplified_polygon,
    convert_coords_to_percentage,
    get_valid_polygons,
    get_polygon_wkt,
)
from file_utilities import PathLike


def get_pixel_arrays_from_image(image_path: PathLike) -> np.ndarray:
    image = Image.open(image_path)
    return np.array(image)


def extract_segmentations_from_pixel_array(
    image_file_path: PathLike,
    pixel_array: np.ndarray,
    simplify_polygons: bool = False,
    grid_resolution: int = 1
) -> dict:
    """
    Extracts all segmentations from a pixel array for each unique voxel
    found in the pixel array.

    :param image_file_path: Path to image file
    :param pixel_array: Pixel array representation of image
    :param simplify_polygons: Whether to simplofy polygon or not.
        Default is false.
    :param grid_resolution: Grid resolution to simplify polygon by.
        Only meaningful if simplify_polygons is true.
    :return: Dictionary containing image path, width, height and the
        segmentations found in the pixel array for each voxel.
    """

    width, height = pixel_array.shape
    unique_voxels = np.unique(pixel_array)

    segmentations = []
    for focus_voxel in unique_voxels[unique_voxels.nonzero()]:
        polygons = get_polygons_for_voxel(pixel_array, focus_voxel)

        if simplify_polygons:
            polygons = get_simplified_polygon(polygons, grid_resolution)

        polygons = convert_coords_to_percentage(polygons, width, height)
        polygons = get_valid_polygons(polygons)

        polygon_wkts = [get_polygon_wkt(polygon) for polygon in polygons]

        polygon_dict = {"voxel": focus_voxel.item(), "polygons": polygon_wkts}
        segmentations.append(polygon_dict)

    image_data = {
        "image_path": str(image_file_path),
        "width": width,
        "height": height,
        "segmentations": segmentations,
    }

    return image_data
