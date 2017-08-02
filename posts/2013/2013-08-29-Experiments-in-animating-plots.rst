Experiments in animating plots and saving movies in SunPy 0.3
=============================================================

.. post:: 29 August 2013
   :author: Jack Ireland
   :tags: 0.3, sunpy, movies
   :category: Update

Just over a year ago this post described a simple method for saving a movie of SunPy maps.
Since then, SunPy and matplotlib have moved on, and I’d like to describe an updated method for animating SunPy maps, and saving the results as an mp4 file.

First off, all these experiments were conducted on Ubuntu 12.04.
The code below is based on this `StackOverflow <http://stackoverflow.com/questions/18019226/matplotlib-animation>`_ question and answer (where would we be without StackOverflow???? – thanks!), and some googling around concerning Ubuntu and ffmpeg.

So, to begin, I fired up `ipython <http://ipython.org/>`_.
I tried the StackOverflow code (including the correction in the answer) and got stuck in an ipython error loop.
The solution – upgrading to ipython 1.0.0.  Trying again, the code crashed because I did not have ffmpeg installed.
Matplotlib looks for movie writers it can use, and since I had specified one that was not present, it crashed.
You can find which movie writers are present with `animation.writers.list()` (having imported the animation module as below).
I put ffmpeg capabilities on my system through sudo apt-get install libav-tools.

So, the StackOverflow code worked!
It was quite simple to adapt it plotting SunPy 0.3 maps.
I want to read in a bunch of time-ordered AIA FITS files, and make a movie of them.
A very typical use case for a solar physicist.  Here is what I managed to get to work.

::

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import os
    import sunpy

    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)

    # Get some data
    imagedir = '/home/ireland/Data/AIA_Data/'
    filenames = sorted(os.listdir(imagedir))

    fig = plt.figure("An SDO movie")
    img = []
    for x in filenames:
    print("Processing %s" % x)
    im = sunpy.Map(os.path.join(imagedir, x))
    img.append([im.plot()])

    ani = animation.ArtistAnimation(fig, img, interval=20, blit=True,repeat_delay=0)
    ani.save('output_movie.mp4', writer=writer)

The code creates a SunPy map, and then creates a list of plots of those maps for the animator to work with.
The animator then saves the animation as a movie using the ffmpeg writer.
Works quite well.
The resulting movie is `here <http://www.sunpy.org/v1/wp-content/uploads/2013/08/output2again3.mp4>`_.
As you can see the title above each image remains the same, whereas in each individual frame the titles differ (according to the observation time).  That needs fixing, and it `seems it is possible <http://stackoverflow.com/questions/17558096/animated-title-in-matplotlib>`_.

Animating a set of plots is also quite easy.
The code is almost the same as above.
Just comment out the line `matplotlib.use(‘Agg’)` and replace the line `ani.save(…)` with `plt.show()`.
A matplotlib window appears, and the animation plays in it.
The interactive zoom feature of the matplotlib window also works, and that is pretty cool.

I have not yet worked out how to animate a set of plots, and then save it as an mp4 movie.
These simple `examples <http://matplotlib.org/search.html?q=animation&check_keywords=yes&area=default>`_ are enough I think, however, to get you going with animating your own plots.
And by plots, I mean any kind of plots, not just movies of 2-d image data.
The matplotlib site has examples of how to animate line plots, for example.

Obviously it would be extremely useful to have the animation and movie saving capability baked in to the mapcube functionality of SunPy.
The code above is just an experiment, so if you have any improvements, or whole new and better methods, please let me know leave a comment below.
Thanks again to SunPy, StackOverflow and matplotlib!
