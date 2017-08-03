SunPy at SciPy 2013
===================

.. post:: 21 July 2013
   :author: Stuart Mumford
   :tags: scipy, talk, outreach, conference
   :category: Update

This year I was lucky enough to be able to attend the annual Scientific Python conference (SciPy 2013) in Austin, Texas.
This was very kindly supported by a sponsorship from the conference organisers and sponsors.

SciPy is a gathering of people from all over the globe who all use Python for some scientific purpose.
People there ranged from astronomers to meteorologists.
There were academics and people from industry or people who just write python in their spare time.
This diversity in people’s backgrounds and interest lead to the most diverse, interesting and friendly conference I have ever attended.

The conference this year consisted of two days of tutorials, two days of talks and two days of sprints.
The tutorials covered different levels and topics ranging from introductions to IPython, matplotlib and scikit-learn to advanced talks on Cython and NumPy.
Like with all the sessions at SciPy there are very good quality videos available online of the `tutorials <http://conference.scipy.org/scipy2013/tutorials_schedule.php>`_.

The talks were in three tracks this year, one on reproducible science, one focusing on machine learning and a general track.
In addition to this there were also a set of “domain specific mini-symposia”, covering topics such as astronomy and medical applications.

Attending SciPy as a member of the SunPy development team was also a fantastic opportunity to raise awareness of our project and talk to interested people.
I gave a presentation on SunPy and it’s development in the “Astronomy and Astrophysics mini-symposium”, the video of the talk is
`available <https://www.youtube.com/watch?v=bXPPTCkaVu8>`_ .

The last two days of the conference were full of very productive sprints, where you sit in a room with like minded people and work on code.
During the sprints, and the rest of the conference, I spent some time working on many projects including yt, astropy, ginga and scikit-image.

Ginga is a fantastic FITS file viewer written in pure Python, with surprising rendering speed and extensibility, it has a lot of potential to form the basis of a SunPy GUI.
Ginga makes use of Astropy, which is an excellent community effort to unite Python tools for astronomy.
One of the main benefits of attending SciPy was to increase the cooperation between Astropy and SunPy, there is a lot of work regarding coordinate handling as well as the migration of the PyFITS library into Astropy, which means that SunPy will be making good use of Astropy in the future.

On the last day I spent the afternoon with the scikit-image team, and had a very productive day working with them to implement a routine that warps an image to compensate for the rotation of the Sun.
This is based on various parts of SunPy to calculate the coordinates and the rotation, and then uses scikit-image to warp the solar disk.
I have written up this work and it can be found
`here <http://nbviewer.ipython.org/url/sunpy.cadair.com/diff_rot.ipynb>`_

One other project I spent some time with was the yt project.
yt is a visualisation and analysis library for astrophysical simulations.
My PhD work is numerical solar physics and this was very interesting to me.
yt has it’s own very powerful volume rendering engine as well as a very nice API to do powerful slicing and parallel computation and rendering.
I would recommended people who might be interested take a look!

