import datetime
import urllib.request

import astropy.units as u

# the following functions will help us get GPS data from the EXIF data if it exists
def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degress in float format
    :param value:
    :type value: exifread.utils.Ratio
    :rtype: float
    """
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)

    return d + (m / 60.0) + (s / 3600.0)
    
def get_exif_location(exif_data):
    """
    Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)
    """
    lat = None
    lon = None

    gps_latitude = exif_data.get('GPS GPSLatitude', None)
    gps_latitude_ref = exif_data.get('GPS GPSLatitudeRef', None)
    gps_longitude = exif_data.get('GPS GPSLongitude', None)
    gps_longitude_ref = exif_data.get('GPS GPSLongitudeRef', None)

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref.values[0] != 'N':
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref.values[0] != 'E':
            lon = 0 - lon

    return lat, lon

def get_camera_metadata(tags):
    camera_metadata = {}
    if "EXIF ExposureTime" in tags:
        exposure_tag = tags['EXIF ExposureTime']
        camera_metadata["exposure_time"] = exposure_tag.values[0].num / exposure_tag.values[0].den * u.s
    if "Image Artist" in tags:
        camera_metadata["author"] = tags['Image Artist'].values
    if "EXIF DateTimeOriginal" in tags:
        datetime_str = tags['EXIF DateTimeOriginal'].values.replace(' ', ':').split(':')
        camera_metadata["time"] = datetime.datetime(int(datetime_str[0]), int(datetime_str[1]), 
                                                    int(datetime_str[2]), int(datetime_str[3]),
                                                    int(datetime_str[4]), int(datetime_str[5]))
    if "Image Model" in tags:
        camera_metadata["camera_model"] = tags['Image Model'].values
        
    lat, lon = get_exif_location(tags)
    if ((lat != None) and (lon != None)):
        camera_metadata["gps"] = [lat, lon] * u.deg
    return camera_metadata

solar_eclipse_image = "total_solar_eclipse2017.jpg"