**Part 1: The Community Bonding Period**
========================================

.. post:: May 26, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC

In this series of posts, I describe my journey as a Google Summer of
Code student. These posts would mostly include my work during the weeks
and the experience I gained from it. Such posts would come up every two
weeks from now so stay tuned.

--------------

The official coding period of Google Summer of Code is preceded by
almost a month-long **“Community Bonding Period.”**\ During this period
a student is expected to interact with the community and understand what
is expected of him/her during the summer. It is a very crucial period,
during which plan for the entire summer is laid out.

|image0|

I am working with the SunPy organization on their sunkit-image project
which is an image processing library for solar images. The sunpy
community is great, made up of an awesome bunch of people. Everyone is
working hard and just by observing them I learned a lot.

|image1| SunPy Logo

I had some interactions with them before being selected for the program
but after the results came out they have increased and will go on
increasing further. The first piece of information which I received
after being selected was from **Open Astronomy** which the umbrella
organization for sunpy. The mail had all the guidelines which needed to
be followed throughout the summer.

I also contacted my mentors, **Nabil Freji**\ and **Jack Ireland**\ to
discuss how things should proceed and we decided to stick to our earlier
timeline. Though I have been unable to talk to them directly over a
video call due to some unavoidable circumstances, I will soon make up
for it as our weekly video calls will begin soon as the coding period
starts.

During the coding period, I mainly focused on completing the tests for a
function which I had previously written but it proved quite challenging.
I wrote a few completely new tests and for the others, I did some
modifications (adding a radial profile to the test data). First of all,
I had never done unit testing before so writing tests and making them
run was something I found tricky. I still have not figured it out
completely but I am still working on it. I learned about **tox**, for
unit testing in python and how continuous integration works. One major
mistake which I had committed earlier and because of which my code
failed on continuous integration was not keeping up my local sunpy in
sync with the sunpy master. This problem never came to my notice and it
was only after Nabil pointed it out that I realized it. This made me
understand how interconnected sunpy is with sunkit-image, which I had
failed to grasp upon previously.

Thankfully, all the above fiasco occurred in the bonding period which
helped me realize my mistakes. I learnt how important is to be working
on the latest development version and the power of unit testing and
continuous integration. It taught me that no code should be pushed
before thoroughly testing it and so making good tests is extremely
important.

--------------

I look forward to the coding period where I can put to use whatever I
learned during the bonding period, it really has been an eye-opener. I
hope that I can contribute to sunkit-image and the final results of this
summer would be fruitful.

-  `Gsoc <https://medium.com/tag/gsoc?source=post>`__
-  `Open Source <https://medium.com/tag/open-source?source=post>`__
-  `Programming <https://medium.com/tag/programming?source=post>`__
-  `Sunpy <https://medium.com/tag/sunpy?source=post>`__

`Vatsalya Chaubey <https://medium.com/@vatsalyachaubey19980>`__
---------------------------------------------------------------

.. |image0| image:: https://cdn-images-1.medium.com/max/1000/1*g5RBYeGe0VLB6t_ZsvO_wQ.png
.. |image1| image:: https://cdn-images-1.medium.com/max/1000/0*ym9QvtbkCfiyIwMi
