GSoC 2019: Project IRISpy 1.2
=============================

.. post:: June 23, 2019
   :author: Kris Stern
   :tags: GSoC, IRISpy, NDCube
   :category: GSoC

Four weeks have passed since the commencement of the Coding Period on May 27th, 2019 (EST). Soon our 1st evaluation will come up, which in itself is an exciting time as we will be judged on whether we will be qualified to go on to the next round. In my opinion I have done most of what have been agreed between me and my mentors. Comparing to my peers my project probably is more manageable, as an IDL version of the code already exists which provides us with a source code from which a Python-translation is written. And, the level of the project is relatively easy, so that the concepts involved are pretty basic. In this blog post, I would like to discuss about a trinity of techniques I have developed as a rookie software developer to deal with issues arising during the implementation of some new function into the broader code base. For the most up-to-date status of the PR please head to `link <https://github.com/sunpy/irispy/pull/108>`_.

Technique 1: Understanding how the new function fits into the code base — First off is to study the code base carefully in order get an idea regarding its architecture. Knowing how the chain of dependencies go can help a lot with implementing a new function. After this, review the code again to gain more insight once this first step is completed.

Technique 2: Check the chain of functions involved in the hierarchy of dependency — This is best done with some keyword search functionality of the editor-of-choice. It pays to be thorough in one’s backwards and forwards double-checking to ensure every dependency in the chain is covered.

Technique 3: Divide-and-Conquer — Dividing the task into smaller steps, in order to help both with writing the new code snippets and the testing. The first task in the process of course would be to actually write the new function to be incorporated. Then, comes the tasks of debugging, testing, and benchmarking. And then, it is to enhance the code using some algorithmic or data-structure hacks to improve its performance. Finally, we worked back up the chain of dependency to add the new elements required, in the case of my PR that would be to implement some time-dependency in the determination of some effective areas covered by the NASA IRIS satellite.

It has been a very blessed journey working with my two very knowledgeable, encouraging and caring mentors thus far. And I look forward to further collaboration with them on this and potentially other projects.
