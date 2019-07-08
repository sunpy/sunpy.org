[Week 06] — First Evaluations and Completing the first half
===========================================================

.. post:: July 08, 2019
   :author: Yash Sharma
   :tags: GSoC, NDCube
   :category: GSoC

|image0| First Evaluations are Completed!

    This blog post deals with the entry of tasks that I did for the 6th
    week for the project under Google Summer of Code 2019.

First Evaluations results are out
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

So the first evaluations results are out, and fortunately, I have passed
the first evaluations. This was a mini-victory moment for me, and to top
it up, my PR regarding the first evals was merged which was sweet for
me!

I got a mail from Google, stating that I have **passed** my evaluations,
and my mentor had given positive feedback. I was overjoyed and jumping
out of happiness! I am not comfortable in sharing my mail here, but I am
happy to state a few of the comments by my mentor.

    My mentor commended the amount of hard work done and suggested me to
    improve my check-ins with the progress and keep pushing the code to
    GitHub so that how much progress I am making could be gauged.

This was imperative as it would help me in assessing my strengths and
not over-working them, and work on my shortcomings as soon as possible.
I had decided with my mentors that for the second part of the project, I
would rather break my PRs into several small parts, each of them dealing
with a small sub-task, that could be individually integrated back into
``NDCube``.

Gearing up for the next sub-part
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If any of my readers had been gauging my progress, here is a
`tab <https://github.com/sunpy/ndcube/projects/2>`__ which contains most
of the task that should be completed to check-off the task. I had
covered most of the tasks of ``NDCubeBase``. I was concerned with the
working of ``axis_world_coords``, which I had re-written earlier, and
not sure about the working of it.

I decided to add it to my later tasks, as I started with planning for
the next half of the project, the plotting. This required me to read
through the docs for understanding the plotting. I had earlier
`worked <https://github.com/sunpy/ndcube/pull/176>`__ with the plotting
earlier, so I had been familiar with the code of plotting.

The trick was to break the codebase into small portions, as the plotting
code was delegated into small methods which worked out the plotting of
``1D``, ``2D`` and ``>2D`` ``NDCube`` objects. ``@DanRyanIrish`` had
earlier advised me to break out the code into small parts, each of the
refactoring dealing with different types of ``NDCube`` objects.

Tasks for the next week
^^^^^^^^^^^^^^^^^^^^^^^

The tasks for the next week remains a bit confusing. I plan to take on
plotting, before trying out the changes that I made for the first part
of the coding. My mentor ``@Cadair`` would be out on his vacations for
around 2–3 weeks, so ``@DanRyanIrish`` would be expected to take in the
charge. I don’t expect him to be available every now and then 😛, but I
plan to make progress without pinging them every now and then.

Link to my previous post
^^^^^^^^^^^^^^^^^^^^^^^^

-  [Week 05] — Testing out the codebase! —
   `Link <https://medium.com/@yashrsharma44/week-05-testing-out-the-codebase-aaf5e804ff3a>`__

.. |image0| image:: https://cdn-images-1.medium.com/max/1144/1*BSnsYzTJ6ZurFgZPxZGvng.png

