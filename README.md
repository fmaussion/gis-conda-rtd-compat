# gis-conda-rtd-compat

A dummy repository to test if complex gis-related dependencies are installed
properly with conda and conda-forge on ReadTheDocs.

## Packages that should work together

On Python 3:

- IPython
- Pillow
- scickit-image
- GDAL
- Rasterio
- Geopandas
- Pyproj
- Cartopy
- matplotlib
- netCDF4
- descartes

## See if we got it right

From the directory root:

    pip install -e .
    import gis_conda_rtd_compat

## License

Public Domain