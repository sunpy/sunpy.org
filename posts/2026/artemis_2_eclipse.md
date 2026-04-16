---
blogpost: true
date: Apr 9 2026
author: Stuart Mumford, Shane Maloney, Albert Y. Shih
category: Tutorial
tags: eclipse
---

# Artemis II Solar Eclipse

The Artemis II mission launched on the 1st April 2026; this launch date allowed the crew to observe a solar eclipse on the 6th April after transiting the far side of the moon.

```{figure} ./artemis2_images/art2_eclipse_ship.jpg
  :width: 100%
  :alt: Artemis 2 Solar Eclipse with Capsule

Image credit NASA
```

We on the SunPy blog {ref}`rarely miss the opportunity <2024-04-03-eclipse>` to talk [about a solar eclipse](https://github.com/sunpy/solar-eclipse/).
So when we saw the stunning photos taken by the astronauts on Artemis II, we wanted to use SunPy to compare them to other photos of the solar corona.
I do highly recommend watching the recording of the eclipse [on YouTube](https://youtu.be/dS9qqzSF3mI?si=NFfli3b7f0tYoVDP&t=1683); the reactions and descriptions of the astronauts are worth it.

Amongst the many amazing photos downlinked during the mission was this image of the solar eclipse:

```{figure} ./artemis2_images/art002e009301~large.jpg
  :width: 100%
  :alt: Artemis 2 Solar Eclipse, showing the moon lit by Earthshine, multiple planets and a star field.

Image credit NASA
```

This image is particularly good for comparing to other solar data because the limb of the moon is clearly visible, and there are stars and planets in the image we can use as references.
These features will allow us to determine exactly where the image was pointing and the angle of the camera.
At the end of the post you will be able to see how we can overlay on this photo images taken by solar observing satellites.

## Fitting Coordinate Information

To be able to compare this image with other observations of the Sun, we need to identify where the camera was pointed and how it was rotated.
To do this we perform the following steps:

1. Extract the time information from the metadata on the camera.
1. Use the time information to know the exact position of Artemis II.
1. Fit the edge of the moon to identify the location of the center of the moon, and the size of the moon in the image.
1. Use the three planets visible in the lower right of the image to identify the rotation angle.
1. Use the planets to fit the distortion of the lens.

All the code for this example is in **the sunpy example gallery**.

### Finding the position of Artemis II

The first step is to know the time the image is taken; we can extract this from the [EXIF metadata](https://en.wikipedia.org/wiki/Exif).
Once we have this we query [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) for the position of Artemis II.

```python
from sunpy.coordinates import get_horizons_coord

artemis2_naif_id = "-1024"
artemis2_coord = get_horizons_coord(artemis2_naif_id , "2026-04-07 01:06:19")
```

We can also use the positions returned by JPL Horizons and the coordinates packages in sunpy and astropy to visualize what part of the Artemis II trajectory was in eclipse.
To see the details of how this was done see [this example in the SunPy gallery](https://sunpy--8574.org.readthedocs.build/en/8574/generated/gallery/showcase/artemis-ii-trajectory.html).

```{figure} ./artemis2-corot-traj.png
  :width: 100%
  :alt: Artemis 2 trajectory showing when the solar eclipse occurred.

Visulaisation of the Artemis II trajectory with the eclipse highlighted.
```

### Moon Limb Fitting

The next step is to find a known location in the image, a reference point.
The easiest one for us to use is the center of the moon, which we find by doing edge detection and Hough filtering, using [scikit-image](https://scikit-image.org/).

```python
import numpy as np

from skimage.feature import canny, peak_local_max
from skimage.transform import hough_circle, hough_circle_peaks

edges = canny(eclipse_image, sigma=2)

h, w = eclipse_image.shape
radii = np.arange(0.25*h, 0.4*h, 10)

hough_res = hough_circle(edges, radii)
accums, cx, cy, rad = hough_circle_peaks(hough_res, radii, total_num_peaks=1)
```

```{figure} ./artemis2_images/figure_2.svg
  :width: 100%
  :alt: A cropped image of the moon showing edge detection and Hough filtering in three panes.

  A cropped view of the Moon, showing the results of the canny edge detection algorithm and the Hough filter.
```

### Calculating Image Scale

Based on knowing where the center of the moon is and its radius in the image we can construct a coordinate system for the image.

```python
from astropy.coordinates import SkyCoord
import astropy.units as u

moon = SkyCoord(coords["moon"], observer=coords["artemis_ii"])
R_moon = 0.2725076 *  u.R_earth  # IAU mean radius
dist_moon = SkyCoord(coords["artemis_ii"]).separation_3d(moon)

moon_angular_width = np.arcsin(R_moon / dist_moon).to(u.arcsec)
im_radius = rad * u.pix
plate_scale = moon_angular_width / im_radius
```

Using this information we can build a sunpy map (see the gallery example for details).
Plotting this alongside the locations of the planets results in:

```{figure} ./artemis2_images/figure_4.svg
  :width: 100%
  :alt: Initial coordinate system fit, showing the lunar center, limb and expected locations of Mercury, Mars and Saturn, which are offset from their positions in the picture.

Initial coordinate system fit to image, notice that the locations of the highlighted planets are incorrect.
```

### Fitting Roll Angle

It's clear from the previous image that the image is rotated around the center of the moon.
We can solve for this rotation by using a peak finding algorithm to locate the planets in the image.
Doing this results in a {math}`-21.2^\circ` roll angle which we can add to our Maps metadata.

```{figure} ./artemis2_images/figure_5.svg
  :width: 100%
  :alt: Image showing the expected positions of the planets and the detected (peaks) positions of the planets.

Image showing the expected positions of the planets and the detected (peaks) positions of the planets, from which the roll angle is calculated.
```

### Fitting Lens Distortion

The final correction to apply to our fitted coordinate system is the distortion of the camera lens (a Nikkor AF 135mm f/2D DC).
This makes objects distant from the centre of the image appear even more distant than they should.
We can quantify exactly how much the image has been distorted through comparing the expect vs actual positions of Mars and Mercury.
We add this distortion to our coordinate system and our planets now appear in the correct place.

```{figure} ./artemis2_images/figure_7.svg
  :width: 100%
  :alt: Coordinate system fit with additional correction for lens distortion, the expected positions of the planets now match the image.

Coordinate system fit to with additional correction for lens distortion.
```

## Overplotting Coronagraph Images

Now that we have fit a coordinate system to the eclipse photo we can compare this observation of the corona to other data.
To do this we are going to use the coronagraph on the [Solar and Heliospheric Observatory (SOHO)](https://soho.nascom.nasa.gov/) which is located around the Sun-Earth L1 point.
We reproject (or re-grid) these images to the fitted coordinate system of the Artemis II image to compensate for differences in satellite location and point of view, and then crop them to the limb of the moon.

```{figure} ./artemis2_images/figure_8.svg
  :width: 100%
  :alt: The Artemis II solar eclipse photo with the positions of Mercury, Mars and Saturn highlighted, and coronagraph images from SOHO's LASCO instrument plotted over the disc of the moon.

The Artemis II solar eclipse photo with the positions of Mercury, Mars and Saturn highlighted, and coronagraph images from SOHO's LASCO instrument plotted over the disc of the moon.
```

We hope you have found this post interesting.
Remember, that if you are lucky enough to observe the total solar eclipse which will be visible from parts of Europe in August 2026 and you take a photo, you can try this type of analysis with your own photos!
