import astropy.units as u
from sunpy.time import parse_time

SOLAR_ECLIPSE_IMAGE = "total_solar_eclipse2017.jpg"


def _convert_to_degress(value):
    """
    Helper function to convert the GPS coordinates stored in the EXIF to degrees
    """
    d = value.values[0].num / value.values[0].den * u.degree
    m = value.values[1].num / value.values[1].den * u.arcminute
    s = value.values[2].num / value.values[2].den * u.arcsec

    return d + m + s


def get_exif_location(exif_data):
    """
    Returns the latitude, longitude, and altitude, if available, from the provided exif_data
    """
    lat = None
    lon = None
    alt = None

    gps_latitude = exif_data.get("GPS GPSLatitude", None)
    gps_latitude_ref = exif_data.get("GPS GPSLatitudeRef", None)
    gps_longitude = exif_data.get("GPS GPSLongitude", None)
    gps_longitude_ref = exif_data.get("GPS GPSLongitudeRef", None)
    gps_altitude = exif_data.get("GPS GPSAltitude", None)

    if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
        lat = _convert_to_degress(gps_latitude)
        if gps_latitude_ref.values[0] != "N":
            lat = 0 - lat

        lon = _convert_to_degress(gps_longitude)
        if gps_longitude_ref.values[0] != "E":
            lon = 0 - lon

    if gps_altitude:
        alt = gps_altitude.values[0].num / gps_altitude.values[0].den * u.m

    return lat, lon, alt


def get_camera_metadata(tags):
    camera_metadata = {}
    if "EXIF ExposureTime" in tags:
        exposure_tag = tags["EXIF ExposureTime"]
        camera_metadata["exposure_time"] = (
            exposure_tag.values[0].num / exposure_tag.values[0].den * u.s
        )
    if "Image Artist" in tags:
        camera_metadata["author"] = tags["Image Artist"].values
    if "EXIF DateTimeOriginal" in tags:
        datetime_str = tags["EXIF DateTimeOriginal"].values.replace(" ", ":").split(":")
        camera_metadata["time"] = parse_time(
            f"{'-'.join(datetime_str[:3])} {':'.join(datetime_str[3:])}"
        )
    if "Image Model" in tags:
        camera_metadata["camera_model"] = tags["Image Model"].values

    camera_metadata["gps"] = get_exif_location(tags)

    return camera_metadata
