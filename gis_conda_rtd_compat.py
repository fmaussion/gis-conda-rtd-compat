import sys
__version__ = '0.0.1'

print("python version:", sys.version)
print("python exec:", sys.executable)

try:
    import IPython
    print("ipython: %s, %s" % (IPython.__version__, IPython.__file__))
except ImportError:
    print("no ipython")
try:
    import numpy
    print("numpy: %s, %s" % (numpy.__version__, numpy.__file__))
except ImportError:
    print("no numpy")
try:
    import scipy
    print("scipy: %s, %s" % (scipy.__version__, scipy.__file__))
except ImportError:
    print("no scipy")
try:
    import PIL
    print("PIL (Pillow): %s, %s" % (PIL.PILLOW_VERSION, PIL.__file__))
except ImportError:
    print("no PIL (Pillow)")
try:
    import pandas
    print("pandas: %s, %s" % (pandas.__version__, pandas.__file__))
except ImportError:
    print("no pandas")
try:
    import geopandas
    print("geopandas: %s, %s" % (geopandas.__version__, geopandas.__file__))
except ImportError:
    print("no geopandas")
try:
    import matplotlib
    matplotlib.use('Agg')
    print("matplotlib: %s, %s" % (matplotlib.__version__, matplotlib.__file__))
except ImportError:
    print("no matplotlib")
try:
    import rasterio
    print("rasterio: %s, %s" % (rasterio.__version__, rasterio.__file__))
except ImportError:
    print("no rasterio")
try:
    import gdal
    import osgeo.gdal
    print("gdal: %s, %s" % (osgeo.gdal.__version__, gdal.__file__))
except ImportError:
    print("no gdal")
try:
    import pyproj
    print("pyproj: %s, %s" % (pyproj.__version__, pyproj.__file__))
except ImportError:
    print("no pyproj")
try:
    import netCDF4
    print("netCDF4: %s, %s" % (netCDF4.__version__, netCDF4.__file__))
except ImportError:
    print("no netCDF4")
try:
    import skimage
    print("skimage: %s, %s" % (skimage.__version__, skimage.__file__))
except ImportError:
    print("no skimage")
