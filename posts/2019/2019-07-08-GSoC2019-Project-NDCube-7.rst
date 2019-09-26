[Week 05] — Testing out the codebase!
=====================================

.. post:: July 08, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: GSoC

|image0| Testing FTW!

    This blog post deals with the entry of tasks that I did for the 5th
    week for the project under Google Summer of Code 2019.

First evaluations are nearing!
==============================

My task for this week was cut-out; complete the testing and pass my
first evaluations. Well, it wasn’t as strict as it sounds, as my mentor
has been quite supportive, and he was more than happy to pass me for the
first evaluations for the amount of work that I had put. However, I
personally felt that delivering complete content before the first
evaluations were important, for it would unfair for anyone to pass me
for the sake of hard work. Final results matter, so I was determined to
complete off the tasks, before riding on to the next set of challenges.

Testing out the Slicing
========================

So I started out with commenting out all tests, and un-commenting each
of them one by one, and seeing if they are failing. Well, it was manual
work, but I was more than happy to do, considering the mentally draining
work that I did the week before.

Each test cases were written with a specific use case, and my code was
performing well with each one. After completing the refactoring of the
test-suite, I was mostly finished with them, with two of the tests
failing. I was not sure what was happening, so I discussed my issue with
``@Cadair`` and ``@DanRyanIrish``. They were quite happy with the
progress, and I had a telecon with them, through which I explained how I
rewrote the codebase and explained the assumptions that I took while
writing them.

Code reviews are important!
===========================

Well before I had my telecon, I was assisted with my mentors for a code
review, and boy it sounded quite intimidating. Imagine working out a
workable solution, and then get suggested by the mentors, a much simpler
and elegant solution. It was helpful and scary at the same time —
Helpful in the sense that it changed my way of approaching a paradigm of
coding, and scary because I was unsure if I met with the standards of
coding.

Telecon with my mentors
========================

After finishing up with the suggestions from my mentor, I discussed out
the two failing test cases, which was bothering me for a long time.
``@DanRyanIrish`` was away for a long time, so he asked me for a telecon
to get updated with what I have been up to this time. ``@Cadair`` also
joined me, filling out on the holes that I made throughout the
discussion, as he was quite active while I was writing and pushing my
code.

During the telecon, after closely looking through the code, ``@Cadair``
suggested that the ordering of slicing for ``WCS`` object required input
parameters in the cartesian format, opposite to what I had assumed in my
code. This sounded really scary I had written my code with that
assumption. This was really heartbreaking for me, as I didn’t expect
such a conceptual error from my side. This meant that I hadn’t read the
assumption well, and certainly threatened my progress.

Diving into the docs again
==========================

In order to fix this, I was determined to dive into the docs again, as I
wasn’t sure how the stuff was working. I mostly considered the slicing
of ``WCS`` as a black box, which was a big conceptual error from my
part. I learned how not believe certain assumptions, and the code is
written provides the concise proof of the assumptions taken — Nothing
more, nothing less.

On further brainstorming, I found that the slicing used ``NumPy``
convention(opposite of cartesian convention), and that was the result
why most of the tests were not breaking. This was a big green flag, but
I was worried about those two failing test. On close inspection, I found
that both of them used Cartesian ordering instead of NumPy ordering,
which was why it was breaking. It was sloppy from my side, as dealing
with a huge number of test-cases certainly invites a mistake or two.

I was able to get my PR merged, as Cadair was mostly impressed and
convinced about the tests passing, and asked me to focus on the next
part of the project which was plotting.

Content for the next week’s blog post
=====================================

The next week comes after my first evaluations have been done, so I plan
to document out my evals result and discuss my next target of the
coding.

Link to my previous post
========================

-  [Week 04] — Climbing the Everest — 02—
   `Link <https://medium.com/@yashrsharma44/week-04-climbing-the-everest-02-7b6aea5110d7>`__

.. |image0| image:: https://cdn-images-1.medium.com/max/1144/0*_QMGe_qrp3ihCxlh.png
