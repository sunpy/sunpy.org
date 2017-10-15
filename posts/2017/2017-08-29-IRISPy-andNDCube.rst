IRISPy and NDCube
=================

.. post:: Aug 29, 2017
   :author: Ankit Baruah
   :tags: GSoC, Code, Fun
   :category: GSoC

GSoC has come to an end, it was one of the best summer experience I had.  In
this summer I had to create a new affiliated package IRISPy but during this
project making a base package for multi-dimensional contiguious and
non-contiguious spatially aware arrays (from readme.md of NDCube) was a natural
step so ended up developing another repository NDCube.  This was initially
a part of sunpycube but after breaking and burning everything we ended up with
ndcube :P.

NDCube
------
`NDCube <https://github.com/sunpy/ndcube>`_.

`PR10 <https://github.com/abit2/cube/pull/10>`_.

The NDCube has two container objects:

1. NDCube which can handle n-dimensional data containing WCS objects and metadata.
This has different methods such as:

The basic slicing i.e ``__getitem__`` of N-dimensional objects like numpy.array
and this also handle the slicing of WCS objects.  Suppose we are dropping
a axis, this is handled by setting the WCS value to one for that axis.

::

    In [4]: cube2.dimensions
    Out[4]: DimensionPair(shape=<Quantity [ 2., 3., 4.] pix>, axis_types=['HPLN-TAN', 'HPLT-TAN', 'WAVE'])
    In [5]: cube2
    Out[5]: 
    Sunpy NDCube
    ---------------------
    WCS Keywords
    Number of WCS axes: 3
    CTYPE : 'WAVE'  'HPLT-TAN'  'HPLN-TAN'  
    CRVAL : 1.0000000000000001e-09  0.5  1.0  
    CRPIX : 0.0  2.0  2.0  
    PC1_1 PC1_2 PC1_3  : 1.0  0.0  0.0  
    PC2_1 PC2_2 PC2_3  : 0.0  1.0  0.0  
    PC3_1 PC3_2 PC3_3  : 0.0  0.0  1.0  
    CDELT : 2.0000000000000002e-11  0.5  0.40000000000000002  
    NAXIS : 4  3  2
    ---------------------
    Length of NDCube: [ 2.  3.  4.] pix
    Axis Types of NDCube: ['HPLN-TAN', 'HPLT-TAN', 'WAVE']
    In [6]: cube2[0, :, :]
    Out[6]: 
    Sunpy NDCube
    ---------------------
    WCS Keywords
    Number of WCS axes: 3
    CTYPE : 'WAVE'  'HPLT-TAN'  'HPLN-TAN'  
    CRVAL : 1.0000000000000001e-09  0.5  1.0  
    CRPIX : 0.0  2.0  2.0  
    PC1_1 PC1_2 PC1_3  : 1.0  0.0  0.0  
    PC2_1 PC2_2 PC2_3  : 0.0  1.0  0.0  
    PC3_1 PC3_2 PC3_3  : 0.0  0.0  1.0  
    CDELT : 2.0000000000000002e-11  0.5  0.40000000000000002  
    NAXIS : 4  3  1
    ---------------------
    Length of NDCube: [ 3.  4.] pix
    Axis Types of NDCube: ['HPLT-TAN', 'WAVE']
    In [7]: cube2[0, :, :].dimensions
    Out[7]: DimensionPair(shape=<Quantity [ 3., 4.] pix>, axis_types=['HPLT-TAN', 'WAVE'])

``plot()`` method that animates if dimension is greater than 2, else if dimension less than equal to 2 than plots images, this animations uses the WCS data for the axis.

``world_to_pixel()`` method converts world coordinates to pixel coordinates, this method is unit aware.

``pixel_to_world()`` method converts pixel coordinates to world coordinates, this method is unit aware.

``to_sunpy()`` this method automates the conversion of present NDCube instance to sunpy instance is it satisfies all the necessary requirements. Presently it supports Map and work is going on in TimeSeries.

2. ``NDCubeSequence`` which handles a list of NDCube object, this also handles extra coordinate axis which is parallel to one of the data axis.
This has methods such as:

``plot()`` method that creates a animation using the data of the WCS for the axis.

``__getitem__`` method that slices the sequence like a list containing NDCubes which also handles slicing of WCS objects.

``index_as_cube()`` this method handles the slicing of sequence as a single N-dimensional object. 
Example: if the dimension of NDCube objects inside the list of NDCubeSequence is 3 then this method will treat slicing of sequence as single 3 dimensional object by concatenating all the cubes.
So this makes the dimensions as ``(len(list_inside_cubesequence)*NDCube[1st dimension], NDCube[2nd dimension], NDCube[3rd dimension])``.

``explode_along_axis()`` method that slices NDCube object along that axis.
This is useful to reduce the dimension of NDCube’s inside the sequence list.
This will create a new sequence as this break the cube along one axis.

``to_sunpy()`` method it creates a new Sunpy instance if it satisfies the requirements.
Presently only mapcube is implemented.


IRISPy
------
`PR3 <https://github.com/abit2/irispy/pull/3>`_.

IRISPy class was a easy implementation after the useful and challenging NDCube repository was alive.
This made creating a new class such as IRISSpectrograph a rather simple task.
This was done in a clean and neat way.

So this class object has all the inherent methods and properties of NDCubeSequence as it uses this as it’s base class.

Future work includes making changes to ``IRISSpectrograph`` to include the recently added changes such as 
SpectrographSequence, so this is a new sequence which is using the ``NDCubeSequence`` as it’s parent class. Making the
iris tools working properly with the new IRISSpectrograph. Developing NDCube's and NDCubeSequence's ``to_sunpy`` method
to handle all the sunpy objects.
