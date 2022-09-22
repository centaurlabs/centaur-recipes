from typing import Union
from math import sqrt

import numpy as np
from imantics import Mask
from shapely.ops import transform as shapley_transform
from shapely.validation import make_valid as shapely_make_valid
from shapely.geometry import Polygon, GeometryCollection, MultiPolygon
from shapely.geometry.base import BaseGeometry, BaseMultipartGeometry

Geom = Union[BaseGeometry, BaseMultipartGeometry]
GeomOrGeoms = Union[Geom, list[Geom]]


def get_polygons_for_voxel(pixel_array: np.ndarray, focus_voxel: int) -> MultiPolygon:
    """
    Get polygons from pixel array for a particular focus voxel

    :param pixel_array: Pixel array containing polygons
    :param focus_voxel: Pixels to consider as part of a polygon in pixel array
    :return:
    """
    pa_copy = pixel_array.copy()
    pa_copy[pa_copy != focus_voxel] = 0
    coords = Mask(pa_copy).polygons().points

    return MultiPolygon(Polygon(co) for co in coords if len(co) > 2)


def get_simplified_polygon(polygon: BaseGeometry, grid_resolution) -> BaseGeometry:
    return polygon.simplify(sqrt(2) * grid_resolution)


def convert_percentage_to_coords(geom: BaseGeometry, width: int, height: int) -> BaseGeometry:
    """
    Scales coordinates for a shapely geometry from percentage units to
    absolute coordinates based off image dimensions.

    :param geom: Shapely geometry
    :param width: Image width
    :param height: Image height
    :return: Shapely geometry with scaled coordinates
    """
    def to_coords(x: float, y: float):
        return (x * width / 100), (y * height / 100)

    return shapley_transform(to_coords, geom)


def convert_coords_to_percentage(geom: BaseGeometry, width: int, height: int) -> BaseGeometry:
    """
    Scales coordinates for a shapely geometry from absolute coordinates
    to percentage units based off image dimensions.

    :param geom: Shapely geometry
    :param width: Image width
    :param height: Image height
    :return: Shapely geometry with scaled coordinates
    """

    def to_percentage(x: float, y: float):
        return (x / width) * 100, (y / height) * 100

    return shapley_transform(to_percentage, geom)


def get_polygons(geoms: GeomOrGeoms):
    """
    Recursively gets polygons from a geometry or collection of geometries.

    :param geoms: A polygon or collection of polygons.
    :return: List of polygons (possibly empty)
    """

    polygons = []

    if isinstance(geoms, BaseGeometry):
        # Polygon instance
        if isinstance(geoms, Polygon):
            polygons.append(geoms)

        # Non-empty Shapely iterable
        elif isinstance(geoms, BaseMultipartGeometry) and geoms.geoms:
            # Heterogenous geometry collection
            if isinstance(geoms, GeometryCollection):
                polygons.extend(get_polygons(geoms.geoms))

            # Homogenous collection of Polygons
            elif isinstance(geoms, MultiPolygon):
                polygons.extend(geoms.geoms)
    else:
        # Either non-shapely iterable of shapely geometries or non-geometry
        try:
            for geo in geoms:
                polygons.extend(get_polygons(geo))

        except TypeError as e:
            raise TypeError(f"Non-geometry object detected: {geoms}.\n\t Exception(s) raised: {e}\n")

    return polygons


def get_valid_polygons(geoms: GeomOrGeoms):
    """
    Makes a collection of polygons valid and returns them

    :param geoms: A shapely polygon or collection of shapely polygons.
    :return: List of valid polygons (possibly empty)
    """
    try:
        validated = shapely_make_valid(geoms)

    except AttributeError:
        # Non-shapely collection (list, set, etc.)
        try:
            validated = [shapely_make_valid(g) for g in geoms]

        except (TypeError, AttributeError):
            raise TypeError(f'Non-geometry object detected: {geoms}')

    return get_polygons(validated)


def get_polygon_wkt(polygon: Polygon) -> str:
    # The explicit wkt for empty polygons is needed since shapely<2.0
    # outputs 'GEOMETRYCOLLECTION EMPTY' for empty polygons.
    return polygon.wkt if not polygon.is_empty else 'POLYGON EMPTY'
