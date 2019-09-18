Part 6: Reaching the Summit
---------------------------

.. post:: August 5, 2019
   :author: Vatsalya Chaubey
   :tags: GSoC, Sunpy, Sunkit-image
   :category: GSoC

If I describe my journey through Google Summer of Code as an arduous
mountain climbing adventure then finally I have reached a point from
where the **summit**\ is within reach.

But as they say — > # “The last stretch is the most difficult!!”

The past few weeks have been such a delight — they involved everything
from episodes of frustration to moments of great joy!! I really have to
thank my mentors — Nabil and Jack, for the level of confidence they have
shown in me.

If you have been following my previous posts then you are very well
aware of the one thing about which I have been talking, i.e. the
**Fourier Local Correlation Tracking.**\ This has been the longest part
of my project and it took me almost a month to conclude it (though it is
still not merged). So, the last time when I left you we were searching
for a bug in the wrapper code. But to our amazement, we could not find
anyone in the wrapper code rather it was lurking in the most unexpected
of places.

The C code had some IDL I/O routines involved with it to read and write
binary “dat” files. We were aware that the IDL and C codes will read the
arrays differently owing to the order in which they store arrays. IDL is
column-major and C and Python are row-major. We thought that it can be
taken care of by transposing the arrays but it was found that this was
not the solution because both the codes were reading different values
from the binary files and this was really baffling!!

Later, we realized that this was actually due to the order of
operations. IDL was reading the binary file in column-major, unlike C
which produced different results. So to fix this I wrote a few more
Python functions wrapping the C read codes and also providing an option
by which arrays read by IDL can also be used. This finally completed our
code for FLCT and only the documentation and examples were left, which
were later added.

On a separate note, I passed the second evaluation but after reading the
above, I presume you already got to know about it ;-)

The most exciting part of this journey still awaits and I hope with the
team with which I have been working with we will surely **reach the
summit**. I hope you enjoyed this and would surely join us next time to
see the conclusion of this saga. Until then, ciao!!!
