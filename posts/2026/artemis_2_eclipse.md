---
blogpost: true
date: Apr 9 2026
author: Stuart Mumford, Shane Maloney, Albert Y. Shih
category: Tutorial
tags: eclipse
---

# Artemis II Solar Eclipse

The Artemis II mission launched on the 1st April 2026, this launch date (or the window on the 2nd) allowed the crew to observe a solar eclipse on the 6th April after transiting the far side of the moon.

```{figure} ./art2_eclipse_ship.jpg
  :width: 66%
  :alt: Artemis 2 Solar Eclipse with Capsule

Image credit NASA
```

We on the SunPy blog {ref}`rarely miss the opportunity <2024-04-03-eclipse>` to talk [about a solar eclipse](https://github.com/sunpy/solar-eclipse/).
So when we saw the stunning photos taken by the astronaughts on Artemis II, we loaded them with SunPy.
I do highly recommend watching the recording of the eclipse [on YouTube](https://youtu.be/dS9qqzSF3mI?si=NFfli3b7f0tYoVDP&t=1683).

## Fitting Coordinate Information

To be able to compare this image with other observations of the Sun, we need to identify where the camera was pointed and how it was rotated.
To do this we perform the following steps, all the code for this example is in **the sunpy example gallery**.

1. Extract the time information from the metadata on the camera.
1. Use the time information to know the exact position of Artemis 2.
1. Fit the edge of the moon to identify the location of the center of the moon, and the size of the moon in the image.
1. Use the three planets visible in the lower right of the image to identify the rotation angle.
1. Use the planets to fit the distortion of the lens.
