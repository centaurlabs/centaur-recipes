# Coordinate Converter

## Summary
This notebook demonstrates how to convert coordinates in WKT strings from **relative** space to **absolute** space and vice versa.

By **relative space** we refer to the coordinate space where each ordered-pair `(x, y)` has values in the `[0 .. 100]` closed interval, such that `(0, 0)` is the top-left corner of the image and `(100, 100)` is the bottom right.

And by **absolute space** we refer to the coordinate space where each ordered-pair `(x, y)` has values in the `[0 .. width]` and `[0 .. height]` closed intervals respectively, such that `(0, 0)` is the top-left corner of the image and `(width, height)` is the bottom right, this is also known as "pixel space".

### Installation
No special installation is required, simply follow the notebook for step-by-step instructions.
