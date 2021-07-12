SunPy
=====

.. raw:: html

    <style>
        body{
            background-color: none !important;
            background-image: url("_static/img/sunpy-bg.jpg");
            background-repeat: no-repeat;
            background-position: center center;
            background-attachment: fixed;
            background-size: cover;
            }
          h1 {
           display : none;
          }
        </style>
        <div class="container">
            <div class="row logo-container">
                <div class="col-md-6 center">
                    <img id="logo" src="_static/img/sunpy_icon.svg" class="sunpy-logo" alt="SunPy Logo">
                </div>
                <div class="col-md-6 center">
                    <div class="icon-text">
                        <p>sun<span class="icon-text color2">py</span></p>
                    </div>
                    <p class="lead">The community-developed, free and open-source solar data analysis environment for Python.</p>
                    <div id="front" class="border">
                    <p class="whatsnew">What's new in <a href="https://docs.sunpy.org/en/stable/whatsnew/3.0.html">sunpy 3.0?</a></p>
                    <p class="body">Latest stable release: <span id="version"></span></p>
                    </div>
                    <div>
                        <a href="https://docs.sunpy.org/en/stable/guide/installation.html" class="btn btn-default btn2" role="button">Install SunPy</a>
                        <a href="https://docs.sunpy.org/en/stable/guide/tour.html" class="btn btn-default btn1" role="button">Tour of SunPy</a>
                        <a href="https://docs.sunpy.org/en/stable/generated/gallery/index.html" class="btn btn-default btn1" role="button">Example Gallery</a>
                    </div>
                </div>
            </div>
        </div>
        <script>
        const d = new Date();
        if (d.getMonth() == 5){
            document.getElementById("logo").src = "_static/img/pride/sunpy_icon.svg";
        }
        </script>

.. toctree::
   :maxdepth: 0
   :hidden:

   about
   blog
   help
   project/index
   contribute
   coc
