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
          .bd-main {
            width: 100%;
          }
          .bd-header-article {
            display: none;
          }
          .whatsnew {
            padding-top: 15px;
            font-size: 30px;
            text-align: center;
          }
          .whatsnew a {
            color: var(--sst-sunpy-logo-primary-color);
            font-weight: bold;
            text-decoration: none;
          }
          p.whatsnew{
            margin-bottom: 0;
            color: var(--sst-sunpy-darkest-gray)
          }
          #front {
            border: 1px var(--sst-sunpy-light-gray) solid;
            border-left-style: none;
            border-right-style: none;
          }
          @media only screen and (min-width: 768px) {
            .lead {
              font-size: 1.8rem;
            }
          }
          /* Override the sbt header nav hiding. */
          .bd-header label.sidebar-toggle {
            display: inherit;
          }
          /* TODO: Use flex here */
          .logo-container {
            margin-top: 2%;
            margin-bottom: 5%;
          }
        </style>
        <div class="container">
            <div class="row logo-container">
                <div class="col-md-6 center">
                    <img id="logo" class="dark-light" src="_static/img/sunpy_icon.svg" class="sunpy-logo" alt="SunPy Logo">
                </div>
                <div class="col-md-6 center">
                    <div class="text-center">
                        <p class="sunpy-icon-text">sun<span class="sunpy-icon-text-color2">py</span></p>
                    </div>
                    <p class="lead text-center always-light-theme">The community-developed, free and open-source solar data analysis environment for Python.</p>
                    <div id="front" class="text-center">
                    <p class="whatsnew always-light-theme">What's new in <a href="https://docs.sunpy.org/en/stable/whatsnew/5.0.html">sunpy 5.0?</a></p>
                    <p class="body always-light-theme">Latest stable release: <span id="version"></span></p>
                    </div>
                    <div class="grid text-center sunpy-btn-grid">
                        <a href="https://docs.sunpy.org/en/stable/tutorial/installation.html" class="btn btn-lg btn-sunpy btn-sunpy2" type="button">Install sunpy</a>
                        <a href="https://docs.sunpy.org/en/stable/tutorial/index.html" class="btn btn-lg btn-sunpy btn-sunpy1" role="button">sunpy tutorial</a>
                        <a href="https://docs.sunpy.org/en/stable/generated/gallery/index.html" class="btn btn-lg btn-sunpy btn-sunpy1" role="button">Example Gallery</a>
                        <a href="https://app.element.io/#/room/#sunpy:openastronomy.org" class="btn btn-lg btn-sunpy btn-sunpy1" role="button">Chat</a>
                        <a href="https://community.openastronomy.org/c/sunpy/5" class="btn btn-lg btn-sunpy btn-sunpy1" role="button">Forum</a>
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

   about/index
   affiliated
   help
   contribute
   blog
