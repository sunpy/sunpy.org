
Sunpy Website Improvements
==========================

.. post:: Aug 16, 2017
   :author: Duygu KESKEK
   :tags: GSoC, Code, Fun
   :category: GSoC

Believe or not, there is only one week left to the end of GSoC!
The whole GSoC period became an unforgettable experience for me.
I still remember the first time I read the documentation of Sphinx and say “What the hell am I supposed to do now?”

The old SunPy website was a Ruby based Jekyll static website and it wasn’t consistent with the documentation theme.
The main aspect of the project is to remove the inconsistency between the website and the docs while improving UI/UX.
There are also 4 extensions of the project 

1. Implementing a registry of SunPy Affiliated packages
2. Move away from Jekyll to a Python based static site generator
3. Write a sphinx extension that maintains an up to date list on the main website of the instruments and data products supported by the SunPy library
4. Improve the content of the SunPy website

In my proposal, I mentioned that I’ll implement all the extensions and at the end of the GSoC, I can say that I’m done with all except the Sphinx extension.
Mentors also didn’t force me to do that since there was more important and never-ending issues on the list.

First Month
-----------

At the first month of the project, I spent almost 1 week to understand Sphinx and read its documentation.
This was the first time I heard about Sphinx and it was quite exciting to learn something new.
The challenge of my project was to create both the website and the docs using Sphinx.
This was discussed on Matrix channel, and even seemed impossible for some since there is always a risk that the website and the docs may break each other.
Also, using Sphinx for a website theme was so RARE ! I was sometimes like “Come on! It’s a docs generator ?!”

I used `sphinx-bootstrap-theme <https://github.com/ryan-roemer/sphinx-bootstrap-theme>`_ as a basis of my project.
I started implementing the navbar sections and put all the content in the new website.
Sphinx uses restructuredText as its markup language and I used RST for the entire website.
I added a scrolling sidebar for navigation between headlines.
At the end of the first month, the structure of the website was nicely prepared for revisions and improvements.

Second Month
------------

The second month, I started to work on the blog section and used `Ablog <https://github.com/abakan/ablog>`_ .
However, the struggle was real, Ablog was full of bugs and it was the only option for blogging with Sphinx.
Then, my mentors fixed the Ablog and did the magic.
After that, I implemented the blogging system and made it possible for someone to write their own blog posts easily.
Additionally, I integrated `DISQUS <https://disqus.com/>`_ to the blog and enabled commenting on the posts.
At the end of the 2nd month, I made a lot of meetings with my mentors and started to work on the documentation theme.

Final Month
-----------

The final month of GSoC was the most painful one for me :P
At the beginning, mentors helped me to build the current SunPy documentation theme (It took 3 days to achieve that ^^) and use our new `SunPy Sphinx theme <https://github.com/sunpy/sunpy-sphinx-theme>`_ for the docs.
After that, they opened issues on the theme repo (Have a look at this never-ending `issue list <https://github.com/sunpy/sunpy-sphinx-theme/issues>`_ 😅) and I fixed them one by one.
The worst part of working on the docs is the build time!
It takes averagely 10 min to build after a simple change 😠
By time, I got used to this also ^^ I redesigned every component of the docs and made them consistent.
There was a huge color mismatch and also lots of bugs, and I’m done with all and my mentors appreciate the work.
I’m also really happy with the docs theme. Now, there are just some minor issues and the renovated website will be replaced with the good old Jekyll one before the SunPy 0.8 release ^^
I’m really exciting for the day that everyone will see the new website with the release and get some feedbacks on it :)
In the near end of the GSoC, I can comfortably say that it makes me feel really happy to work on an open source project.
I want to contribute to the website after the GSoC ends and see how it will improve even better by time.

