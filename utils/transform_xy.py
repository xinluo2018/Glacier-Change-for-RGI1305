### ----- 
# author: luo xin, 
# creat: 2021.6.15, modify: 2021.6.23 
# des: image location transform between different coordinate systems 
# -----

from code import interact
import pyproj
import numpy as np

def coor2coor(srs_from, srs_to, x, y):
    """
    Transform coordinates from srs_from to srs_to
    input:
        srs_from and srs_to, are EPSG number (e.g., 4326, 3031)
        x and y are x-coord and y-coord corresponding to srs_from and srs_to    
    return:
        x-coord and y-coord in srs_to 
    """
    transformer = pyproj.Transformer.from_crs(int(srs_from), int(srs_to), always_xy=True)
    return transformer.transform(x,y)

def geo2imagexy(x, y, gdal_trans, integer=True):
    '''
    des: from georeferenced location (i.e., lon, lat) to image location(col,row).
    input:
        x: project or georeferenced x, i.e.,lon
        y: project or georeferenced y, i.e., lat
        gdal_trans: wgs84 coordinate systems of the specific image, 
                    obtained by gdal.Open() and .GetGeoTransform(), or by geotif_io.readTiff()['geotrans']
    return: 
        image col and row corresponding to the georeferenced location.
    '''
    a = np.array([[gdal_trans[1], gdal_trans[2]], [gdal_trans[4], gdal_trans[5]]])
    b = np.array([x - gdal_trans[0], y - gdal_trans[3]])
    col_img, row_img = np.linalg.solve(a, b)
    if integer:
        col_img, row_img = np.floor(col_img).astype('int'), np.floor(row_img).astype('int')
    return row_img, col_img

def imagexy2geo(row, col, gdal_trans):
    '''
    input: 
        img_gdal: GDAL data (read by gdal.Open()
        row and col are corresponding to input image (dataset)
    :return:  
        geographical coordinates (pixel center)
    '''
    x = gdal_trans[0] + col * gdal_trans[1] + row * gdal_trans[2]
    y = gdal_trans[3] + col * gdal_trans[4] + row * gdal_trans[5]
    return x, y