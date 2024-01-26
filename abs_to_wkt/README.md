# Absolute Pixel Coordinates to WKT (Well-known text) representation 

![Ex. Image information in absolute pixel format](example/input/example_image.jpg?raw=false "Ex. Image information in absolute pixel format") 

Image width: 668
Image height 640

In a JSON file:
image_points:  {'x': 450, 'y': 234}, {'x': 335, 'y': 234},{'x': 356, 'y': 385}, {'x': 215, 'y': 385}

## Summary
The code snippet in the notebook can be used to convert geometries stored in “absolute” format (x/y coordinates in pixel values) to WKT format (0->100) before uploading. The script takes in an image and a json file with the geometry pixel coordinates as an input. 

### Installation
No special installation steps required. Follow the virtual environment setup on
[the main repository page](../README.md#installation) and then follow the steps in the notebook.