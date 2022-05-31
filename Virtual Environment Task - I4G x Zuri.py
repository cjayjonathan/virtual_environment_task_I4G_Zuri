#!/usr/bin/env python
# coding: utf-8

# In[1]:



pip install --user ipykernel


# In[ ]:


# I experienced issues adding my virtual environment to my Jupyter Noteboook.
# This has stalled my trying to show my work but I was successful at the end of the day.
# I copied all my steps which are codes basically from my Anaconda Prompt to show how it went. 


# In[14]:


pip install --user ipykernel


# In[ ]:



(base) C:\Users\ALH.YAHYA>conda -V
conda 4.12.0

(base) C:\Users\ALH.YAHYA>conda update conda
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\ProgramData\Anaconda3

  added / updated specs:
    - conda


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    conda-4.13.0               |   py39haa95532_0         923 KB
    conda-package-handling-1.8.1|   py39h8cc25b3_0         729 KB
    ------------------------------------------------------------
                                           Total:         1.6 MB

The following packages will be REMOVED:

  xmltodict-0.12.0-pyhd3eb1b0_0

The following packages will be UPDATED:

  conda                               4.12.0-py39haa95532_0 --> 4.13.0-py39haa95532_0
  conda-package-han~                   1.7.3-py39h8cc25b3_1 --> 1.8.1-py39h8cc25b3_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
conda-4.13.0         | 923 KB    | ############################################################################ | 100%
conda-package-handli | 729 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: failed

EnvironmentNotWritableError: The current user does not have write permissions to the target environment.
  environment location: C:\ProgramData\Anaconda3



(base) C:\Users\ALH.YAHYA>conda search "^python$"
Loading channels: done
# Name                       Version           Build  Channel
python                        2.7.13     h1b6d89f_16  pkgs/main
python                        2.7.13     h9912b81_15  pkgs/main
python                        2.7.13     hb034564_12  pkgs/main
python                        2.7.14     h2765ee6_18  pkgs/main
python                        2.7.14     h3e68818_15  pkgs/main
python                        2.7.14     h4084c39_22  pkgs/main
python                        2.7.14     h4a10d90_30  pkgs/main
python                        2.7.14     h4a10d90_31  pkgs/main
python                        2.7.14     h59f5a59_20  pkgs/main
python                        2.7.14     h819644d_16  pkgs/main
python                        2.7.14     h8c3f1cb_23  pkgs/main
python                        2.7.15      h2880e7c_2  pkgs/main
python                        2.7.15      h2880e7c_3  pkgs/main
python                        2.7.15      h2880e7c_4  pkgs/main
python                        2.7.15     hcb6e200_15  pkgs/main
python                        2.7.15      hcb6e200_5  pkgs/main
python                        2.7.15      hcb6e200_7  pkgs/main
python                        2.7.15      he216670_0  pkgs/main
python                        2.7.16      hcb6e200_0  pkgs/main
python                        2.7.17      h930f6bb_0  pkgs/main
python                        2.7.18      hcb6e200_0  pkgs/main
python                        2.7.18      hfb89ab9_0  pkgs/main
python                         3.5.4     h1357f44_23  pkgs/main
python                         3.5.4     hc495aa9_21  pkgs/main
python                         3.5.4     hd3c4935_11  pkgs/main
python                         3.5.4     hdec4e59_20  pkgs/main
python                         3.5.4     hedc2606_15  pkgs/main
python                         3.5.5      h0c2934d_0  pkgs/main
python                         3.5.5      h0c2934d_1  pkgs/main
python                         3.5.5      h0c2934d_2  pkgs/main
python                         3.5.6      he025d50_0  pkgs/main
python                         3.6.2     h09676a0_15  pkgs/main
python                         3.6.2     h6679aeb_11  pkgs/main
python                         3.6.3      h210ce5f_2  pkgs/main
python                         3.6.3      h3389d20_0  pkgs/main
python                         3.6.3      h3b118a2_4  pkgs/main
python                         3.6.3      h9e2ca53_1  pkgs/main
python                         3.6.4      h0c2934d_2  pkgs/main
python                         3.6.4      h0c2934d_3  pkgs/main
python                         3.6.4      h6538335_0  pkgs/main
python                         3.6.4      h6538335_1  pkgs/main
python                         3.6.5      h0c2934d_0  pkgs/main
python                         3.6.6      hea74fb7_0  pkgs/main
python                         3.6.7      h33f27b4_0  pkgs/main
python                         3.6.7      h33f27b4_1  pkgs/main
python                         3.6.7      h9f7ef89_2  pkgs/main
python                         3.6.8      h9f7ef89_0  pkgs/main
python                         3.6.8      h9f7ef89_1  pkgs/main
python                         3.6.8      h9f7ef89_7  pkgs/main
python                         3.6.9      h5500b2f_0  pkgs/main
python                        3.6.10      h9f7ef89_0  pkgs/main
python                        3.6.10      h9f7ef89_1  pkgs/main
python                        3.6.10      h9f7ef89_2  pkgs/main
python                        3.6.12      h5500b2f_2  pkgs/main
python                        3.6.13      h3758d61_0  pkgs/main
python                         3.7.0      hea74fb7_0  pkgs/main
python                         3.7.1      h33f27b4_3  pkgs/main
python                         3.7.1      h33f27b4_4  pkgs/main
python                         3.7.1      h8c8aaf0_6  pkgs/main
python                         3.7.1      he44a216_5  pkgs/main
python                         3.7.2      h8c8aaf0_0  pkgs/main
python                         3.7.2     h8c8aaf0_10  pkgs/main
python                         3.7.2      h8c8aaf0_2  pkgs/main
python                         3.7.3      h8c8aaf0_0  pkgs/main
python                         3.7.3      h8c8aaf0_1  pkgs/main
python                         3.7.4      h5263a28_0  pkgs/main
python                         3.7.5      h8c8aaf0_0  pkgs/main
python                         3.7.6      h60c2a47_2  pkgs/main
python                         3.7.7 h60c2a47_0_cpython  pkgs/main
python                         3.7.7      h60c2a47_2  pkgs/main
python                         3.7.7      h81c818b_4  pkgs/main
python                         3.7.9      h60c2a47_0  pkgs/main
python                        3.7.10      h6244533_0  pkgs/main
python                        3.7.11      h6244533_0  pkgs/main
python                        3.7.13      h6244533_0  pkgs/main
python                         3.8.0      hff0d562_0  pkgs/main
python                         3.8.0      hff0d562_1  pkgs/main
python                         3.8.0      hff0d562_2  pkgs/main
python                         3.8.1      h5fd99cc_1  pkgs/main
python                         3.8.1 h5fd99cc_8_cpython  pkgs/main
python                         3.8.1 he1778fa_7_cpython  pkgs/main
python                         3.8.2      h5fd99cc_0  pkgs/main
python                         3.8.2     h5fd99cc_11  pkgs/main
python                         3.8.2     he1778fa_13  pkgs/main
python                         3.8.3      he1778fa_0  pkgs/main
python                         3.8.3      he1778fa_2  pkgs/main
python                         3.8.5      h5fd99cc_1  pkgs/main
python                         3.8.5      he1778fa_0  pkgs/main
python                         3.8.8      hdbf39b2_4  pkgs/main
python                         3.8.8      hdbf39b2_5  pkgs/main
python                        3.8.10      hdbf39b2_7  pkgs/main
python                        3.8.11      h6244533_1  pkgs/main
python                        3.8.12      h6244533_0  pkgs/main
python                        3.8.13      h6244533_0  pkgs/main
python                         3.9.0      h6244533_2  pkgs/main
python                         3.9.0      h8aef87e_1  pkgs/main
python                         3.9.1      h6244533_2  pkgs/main
python                         3.9.2      h6244533_0  pkgs/main
python                         3.9.4      h6244533_0  pkgs/main
python                         3.9.5      h6244533_3  pkgs/main
python                         3.9.6      h6244533_0  pkgs/main
python                         3.9.6      h6244533_1  pkgs/main
python                         3.9.7      h6244533_1  pkgs/main
python                        3.9.11      h6244533_1  pkgs/main
python                        3.9.11      h6244533_2  pkgs/main
python                        3.9.12      h6244533_0  pkgs/main
python                        3.10.0      h96c0403_3  pkgs/main
python                        3.10.0      hbb2ffb3_0  pkgs/main
python                        3.10.0      hbb2ffb3_1  pkgs/main
python                        3.10.0      hbb2ffb3_2  pkgs/main
python                        3.10.3      hbb2ffb3_5  pkgs/main
python                        3.10.4      hbb2ffb3_0  pkgs/main

(base) C:\Users\ALH.YAHYA>conda create -n ceejayenv python=3.9.7 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done


==> WARNING: A newer version of conda exists. <==
  current version: 4.12.0
  latest version: 4.13.0

Please update conda by running

    $ conda update -n base -c defaults conda



## Package Plan ##

  environment location: C:\Users\ALH.YAHYA\.conda\envs\ceejayenv

  added / updated specs:
    - anaconda
    - python=3.9.7


The following NEW packages will be INSTALLED:

  alabaster          pkgs/main/noarch::alabaster-0.7.12-pyhd3eb1b0_0
  anaconda           pkgs/main/win-64::anaconda-2021.11-py39_0
  anaconda-client    pkgs/main/win-64::anaconda-client-1.9.0-py39haa95532_0
  anaconda-project   pkgs/main/noarch::anaconda-project-0.10.1-pyhd3eb1b0_0
  anyio              pkgs/main/win-64::anyio-2.2.0-py39haa95532_2
  appdirs            pkgs/main/noarch::appdirs-1.4.4-pyhd3eb1b0_0
  argh               pkgs/main/win-64::argh-0.26.2-py39haa95532_0
  argon2-cffi        pkgs/main/win-64::argon2-cffi-20.1.0-py39h2bbff1b_1
  arrow              pkgs/main/win-64::arrow-0.13.1-py39haa95532_0
  asn1crypto         pkgs/main/noarch::asn1crypto-1.4.0-py_0
  astroid            pkgs/main/win-64::astroid-2.6.6-py39haa95532_0
  astropy            pkgs/main/win-64::astropy-4.3.1-py39hc7d831d_0
  async_generator    pkgs/main/noarch::async_generator-1.10-pyhd3eb1b0_0
  atomicwrites       pkgs/main/noarch::atomicwrites-1.4.0-py_0
  attrs              pkgs/main/noarch::attrs-21.2.0-pyhd3eb1b0_0
  autopep8           pkgs/main/noarch::autopep8-1.5.7-pyhd3eb1b0_0
  babel              pkgs/main/noarch::babel-2.9.1-pyhd3eb1b0_0
  backcall           pkgs/main/noarch::backcall-0.2.0-pyhd3eb1b0_0
  backports          pkgs/main/noarch::backports-1.0-pyhd3eb1b0_2
  backports.shutil_~ pkgs/main/noarch::backports.shutil_get_terminal_size-1.0.0-pyhd3eb1b0_3
  bcrypt             pkgs/main/win-64::bcrypt-3.2.0-py39h196d8e1_0
  beautifulsoup4     pkgs/main/noarch::beautifulsoup4-4.10.0-pyh06a4308_0
  binaryornot        pkgs/main/noarch::binaryornot-0.4.4-pyhd3eb1b0_1
  bitarray           pkgs/main/win-64::bitarray-2.3.0-py39h2bbff1b_1
  bkcharts           pkgs/main/win-64::bkcharts-0.2-py39haa95532_0
  black              pkgs/main/noarch::black-19.10b0-py_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  bleach             pkgs/main/noarch::bleach-4.0.0-pyhd3eb1b0_0
  blosc              pkgs/main/win-64::blosc-1.21.0-h19a0ad4_0
  bokeh              pkgs/main/win-64::bokeh-2.4.1-py39haa95532_0
  boto               pkgs/main/win-64::boto-2.49.0-py39haa95532_0
  bottleneck         pkgs/main/win-64::bottleneck-1.3.2-py39h7cc1a96_1
  brotli             pkgs/main/win-64::brotli-1.0.9-ha925a31_2
  brotlipy           pkgs/main/win-64::brotlipy-0.7.0-py39h2bbff1b_1003
  bzip2              pkgs/main/win-64::bzip2-1.0.8-he774522_0
  ca-certificates    pkgs/main/win-64::ca-certificates-2021.10.26-haa95532_2
  cached-property    pkgs/main/noarch::cached-property-1.5.2-py_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_0
  cffi               pkgs/main/win-64::cffi-1.14.6-py39h2bbff1b_0
  cfitsio            pkgs/main/win-64::cfitsio-3.470-he774522_6
  chardet            pkgs/main/win-64::chardet-4.0.0-py39haa95532_1003
  charls             pkgs/main/win-64::charls-2.2.0-h6c2663c_0
  charset-normalizer pkgs/main/noarch::charset-normalizer-2.0.4-pyhd3eb1b0_0
  click              pkgs/main/noarch::click-8.0.3-pyhd3eb1b0_0
  cloudpickle        pkgs/main/noarch::cloudpickle-2.0.0-pyhd3eb1b0_0
  clyent             pkgs/main/win-64::clyent-1.2.2-py39haa95532_1
  colorama           pkgs/main/noarch::colorama-0.4.4-pyhd3eb1b0_0
  comtypes           pkgs/main/win-64::comtypes-1.1.10-py39haa95532_1002
  conda              pkgs/main/win-64::conda-4.13.0-py39haa95532_0
  conda-content-tru~ pkgs/main/noarch::conda-content-trust-0.1.1-pyhd3eb1b0_0
  conda-pack         pkgs/main/noarch::conda-pack-0.6.0-pyhd3eb1b0_0
  conda-package-han~ pkgs/main/win-64::conda-package-handling-1.8.1-py39h8cc25b3_0
  conda-token        pkgs/main/noarch::conda-token-0.3.0-pyhd3eb1b0_0
  console_shortcut   pkgs/main/win-64::console_shortcut-0.1.1-4
  contextlib2        pkgs/main/noarch::contextlib2-0.6.0.post1-pyhd3eb1b0_0
  cookiecutter       pkgs/main/noarch::cookiecutter-1.7.2-pyhd3eb1b0_0
  cryptography       pkgs/main/win-64::cryptography-3.4.8-py39h71e12ea_0
  curl               pkgs/main/win-64::curl-7.78.0-h86230a5_0
  cycler             pkgs/main/win-64::cycler-0.10.0-py39haa95532_0
  cython             pkgs/main/win-64::cython-0.29.24-py39h604cdb4_0
  cytoolz            pkgs/main/win-64::cytoolz-0.11.0-py39h2bbff1b_0
  daal4py            pkgs/main/win-64::daal4py-2021.3.0-py39h757b272_0
  dal                pkgs/main/win-64::dal-2021.3.0-haa95532_564
  dask               pkgs/main/noarch::dask-2021.10.0-pyhd3eb1b0_0
  dask-core          pkgs/main/noarch::dask-core-2021.10.0-pyhd3eb1b0_0
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7
  debugpy            pkgs/main/win-64::debugpy-1.4.1-py39hd77b12b_0
  decorator          pkgs/main/noarch::decorator-5.1.0-pyhd3eb1b0_0
  defusedxml         pkgs/main/noarch::defusedxml-0.7.1-pyhd3eb1b0_0
  diff-match-patch   pkgs/main/noarch::diff-match-patch-20200713-pyhd3eb1b0_0
  distributed        pkgs/main/win-64::distributed-2021.10.0-py39haa95532_0
  docutils           pkgs/main/win-64::docutils-0.17.1-py39haa95532_1
  entrypoints        pkgs/main/win-64::entrypoints-0.3-py39haa95532_0
  et_xmlfile         pkgs/main/win-64::et_xmlfile-1.1.0-py39haa95532_0
  fastcache          pkgs/main/win-64::fastcache-1.1.0-py39h196d8e1_0
  filelock           pkgs/main/noarch::filelock-3.3.1-pyhd3eb1b0_1
  flake8             pkgs/main/noarch::flake8-3.9.2-pyhd3eb1b0_0
  flask              pkgs/main/noarch::flask-1.1.2-pyhd3eb1b0_0
  fonttools          pkgs/main/noarch::fonttools-4.25.0-pyhd3eb1b0_0
  freetype           pkgs/main/win-64::freetype-2.10.4-hd328e21_0
  fsspec             pkgs/main/noarch::fsspec-2021.10.1-pyhd3eb1b0_0
  get_terminal_size  pkgs/main/win-64::get_terminal_size-1.0.0-h38e98db_0
  gevent             pkgs/main/win-64::gevent-21.8.0-py39h2bbff1b_1
  giflib             pkgs/main/win-64::giflib-5.2.1-h62dcd97_0
  glob2              pkgs/main/noarch::glob2-0.7-pyhd3eb1b0_0
  greenlet           pkgs/main/win-64::greenlet-1.1.1-py39hd77b12b_0
  h5py               pkgs/main/win-64::h5py-3.2.1-py39h3de5c98_0
  hdf5               pkgs/main/win-64::hdf5-1.10.6-h7ebc959_0
  heapdict           pkgs/main/noarch::heapdict-1.0.1-pyhd3eb1b0_0
  html5lib           pkgs/main/noarch::html5lib-1.1-pyhd3eb1b0_0
  icc_rt             pkgs/main/win-64::icc_rt-2019.0.0-h0cc432a_1
  icu                pkgs/main/win-64::icu-58.2-ha925a31_3
  idna               pkgs/main/noarch::idna-3.2-pyhd3eb1b0_0
  imagecodecs        pkgs/main/win-64::imagecodecs-2021.8.26-py39ha1f97ea_0
  imageio            pkgs/main/noarch::imageio-2.9.0-pyhd3eb1b0_0
  imagesize          pkgs/main/noarch::imagesize-1.2.0-pyhd3eb1b0_0
  importlib-metadata pkgs/main/win-64::importlib-metadata-4.8.1-py39haa95532_0
  importlib_metadata pkgs/main/noarch::importlib_metadata-4.8.1-hd3eb1b0_0
  inflection         pkgs/main/win-64::inflection-0.5.1-py39haa95532_0
  iniconfig          pkgs/main/noarch::iniconfig-1.1.1-pyhd3eb1b0_0
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  intervaltree       pkgs/main/noarch::intervaltree-3.1.0-pyhd3eb1b0_0
  ipykernel          pkgs/main/win-64::ipykernel-6.4.1-py39haa95532_1
  ipython            pkgs/main/win-64::ipython-7.29.0-py39hd4e2768_0
  ipython_genutils   pkgs/main/noarch::ipython_genutils-0.2.0-pyhd3eb1b0_1
  ipywidgets         pkgs/main/noarch::ipywidgets-7.6.5-pyhd3eb1b0_1
  isort              pkgs/main/noarch::isort-5.9.3-pyhd3eb1b0_0
  itsdangerous       pkgs/main/noarch::itsdangerous-2.0.1-pyhd3eb1b0_0
  jdcal              pkgs/main/noarch::jdcal-1.4.1-pyhd3eb1b0_0
  jedi               pkgs/main/win-64::jedi-0.18.0-py39haa95532_1
  jinja2             pkgs/main/noarch::jinja2-2.11.3-pyhd3eb1b0_0
  jinja2-time        pkgs/main/noarch::jinja2-time-0.2.0-pyhd3eb1b0_2
  joblib             pkgs/main/noarch::joblib-1.1.0-pyhd3eb1b0_0
  jpeg               pkgs/main/win-64::jpeg-9d-h2bbff1b_0
  json5              pkgs/main/noarch::json5-0.9.6-pyhd3eb1b0_0
  jsonschema         pkgs/main/noarch::jsonschema-3.2.0-pyhd3eb1b0_2
  jupyter            pkgs/main/win-64::jupyter-1.0.0-py39haa95532_7
  jupyter_client     pkgs/main/noarch::jupyter_client-6.1.12-pyhd3eb1b0_0
  jupyter_console    pkgs/main/noarch::jupyter_console-6.4.0-pyhd3eb1b0_0
  jupyter_core       pkgs/main/win-64::jupyter_core-4.8.1-py39haa95532_0
  jupyter_server     pkgs/main/win-64::jupyter_server-1.4.1-py39haa95532_0
  jupyterlab         pkgs/main/noarch::jupyterlab-3.2.1-pyhd3eb1b0_1
  jupyterlab_pygmen~ pkgs/main/noarch::jupyterlab_pygments-0.1.2-py_0
  jupyterlab_server  pkgs/main/noarch::jupyterlab_server-2.8.2-pyhd3eb1b0_0
  jupyterlab_widgets pkgs/main/noarch::jupyterlab_widgets-1.0.0-pyhd3eb1b0_1
  keyring            pkgs/main/win-64::keyring-23.1.0-py39haa95532_0
  kiwisolver         pkgs/main/win-64::kiwisolver-1.3.1-py39hd77b12b_0
  krb5               pkgs/main/win-64::krb5-1.19.2-h5b6d351_0
  lazy-object-proxy  pkgs/main/win-64::lazy-object-proxy-1.6.0-py39h2bbff1b_0
  lcms2              pkgs/main/win-64::lcms2-2.12-h83e58a3_0
  lerc               pkgs/main/win-64::lerc-3.0-hd77b12b_0
  libaec             pkgs/main/win-64::libaec-1.0.4-h33f27b4_1
  libarchive         pkgs/main/win-64::libarchive-3.4.2-h5e25573_0
  libcurl            pkgs/main/win-64::libcurl-7.78.0-h86230a5_0
  libdeflate         pkgs/main/win-64::libdeflate-1.8-h2bbff1b_5
  libiconv           pkgs/main/win-64::libiconv-1.15-h1df5818_7
  liblief            pkgs/main/win-64::liblief-0.10.1-hd77b12b_1
  libpng             pkgs/main/win-64::libpng-1.6.37-h2a8f88b_0
  libspatialindex    pkgs/main/win-64::libspatialindex-1.9.3-h6c2663c_0
  libssh2            pkgs/main/win-64::libssh2-1.9.0-h7a1dbc1_1
  libtiff            pkgs/main/win-64::libtiff-4.2.0-hd0e1b90_0
  libwebp            pkgs/main/win-64::libwebp-1.2.0-h2bbff1b_0
  libxml2            pkgs/main/win-64::libxml2-2.9.12-h0ad7f3c_0
  libxslt            pkgs/main/win-64::libxslt-1.1.34-he774522_0
  libzopfli          pkgs/main/win-64::libzopfli-1.0.3-ha925a31_0
  llvmlite           pkgs/main/win-64::llvmlite-0.37.0-py39h23ce68f_1
  locket             pkgs/main/win-64::locket-0.2.1-py39haa95532_1
  lxml               pkgs/main/win-64::lxml-4.6.3-py39h9b66d53_0
  lz4-c              pkgs/main/win-64::lz4-c-1.9.3-h2bbff1b_1
  lzo                pkgs/main/win-64::lzo-2.10-he774522_2
  m2w64-gcc-libgfor~ pkgs/msys2/win-64::m2w64-gcc-libgfortran-5.3.0-6
  m2w64-gcc-libs     pkgs/msys2/win-64::m2w64-gcc-libs-5.3.0-7
  m2w64-gcc-libs-co~ pkgs/msys2/win-64::m2w64-gcc-libs-core-5.3.0-7
  m2w64-gmp          pkgs/msys2/win-64::m2w64-gmp-6.1.0-2
  m2w64-libwinpthre~ pkgs/msys2/win-64::m2w64-libwinpthread-git-5.0.0.4634.697f757-2
  markupsafe         pkgs/main/win-64::markupsafe-1.1.1-py39h2bbff1b_0
  matplotlib         pkgs/main/win-64::matplotlib-3.4.3-py39haa95532_0
  matplotlib-base    pkgs/main/win-64::matplotlib-base-3.4.3-py39h49ac443_0
  matplotlib-inline  pkgs/main/noarch::matplotlib-inline-0.1.2-pyhd3eb1b0_2
  mccabe             pkgs/main/win-64::mccabe-0.6.1-py39haa95532_1
  menuinst           pkgs/main/win-64::menuinst-1.4.18-py39h59b6b97_0
  mistune            pkgs/main/win-64::mistune-0.8.4-py39h2bbff1b_1000
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  mock               pkgs/main/noarch::mock-4.0.3-pyhd3eb1b0_0
  more-itertools     pkgs/main/noarch::more-itertools-8.10.0-pyhd3eb1b0_0
  mpmath             pkgs/main/win-64::mpmath-1.2.1-py39haa95532_0
  msgpack-python     pkgs/main/win-64::msgpack-python-1.0.2-py39h59b6b97_1
  msys2-conda-epoch  pkgs/msys2/win-64::msys2-conda-epoch-20160418-1
  multipledispatch   pkgs/main/win-64::multipledispatch-0.6.0-py39haa95532_0
  munkres            pkgs/main/noarch::munkres-1.1.4-py_0
  mypy_extensions    pkgs/main/win-64::mypy_extensions-0.4.3-py39haa95532_0
  nbclassic          pkgs/main/noarch::nbclassic-0.2.6-pyhd3eb1b0_0
  nbclient           pkgs/main/noarch::nbclient-0.5.3-pyhd3eb1b0_0
  nbconvert          pkgs/main/win-64::nbconvert-6.1.0-py39haa95532_0
  nbformat           pkgs/main/noarch::nbformat-5.1.3-pyhd3eb1b0_0
  nest-asyncio       pkgs/main/noarch::nest-asyncio-1.5.1-pyhd3eb1b0_0
  networkx           pkgs/main/noarch::networkx-2.6.3-pyhd3eb1b0_0
  nltk               pkgs/main/noarch::nltk-3.6.5-pyhd3eb1b0_0
  nose               pkgs/main/noarch::nose-1.3.7-pyhd3eb1b0_1006
  notebook           pkgs/main/win-64::notebook-6.4.5-py39haa95532_0
  numba              pkgs/main/win-64::numba-0.54.1-py39hf11a4ad_0
  numexpr            pkgs/main/win-64::numexpr-2.7.3-py39hb80d3ca_1
  numpy              pkgs/main/win-64::numpy-1.20.3-py39ha4e8547_0
  numpy-base         pkgs/main/win-64::numpy-base-1.20.3-py39hc2deb75_0
  numpydoc           pkgs/main/noarch::numpydoc-1.1.0-pyhd3eb1b0_1
  olefile            pkgs/main/noarch::olefile-0.46-pyhd3eb1b0_0
  openjpeg           pkgs/main/win-64::openjpeg-2.4.0-h4fc8c34_0
  openpyxl           pkgs/main/noarch::openpyxl-3.0.9-pyhd3eb1b0_0
  openssl            pkgs/main/win-64::openssl-1.1.1l-h2bbff1b_0
  packaging          pkgs/main/noarch::packaging-21.0-pyhd3eb1b0_0
  pandas             pkgs/main/win-64::pandas-1.3.4-py39h6214cd6_0
  pandocfilters      pkgs/main/win-64::pandocfilters-1.4.3-py39haa95532_1
  paramiko           pkgs/main/noarch::paramiko-2.7.2-py_0
  parso              pkgs/main/noarch::parso-0.8.2-pyhd3eb1b0_0
  partd              pkgs/main/noarch::partd-1.2.0-pyhd3eb1b0_0
  path               pkgs/main/win-64::path-16.0.0-py39haa95532_0
  path.py            pkgs/main/noarch::path.py-12.5.0-hd3eb1b0_0
  pathlib2           pkgs/main/win-64::pathlib2-2.3.6-py39haa95532_2
  pathspec           pkgs/main/noarch::pathspec-0.7.0-py_0
  patsy              pkgs/main/win-64::patsy-0.5.2-py39haa95532_0
  pep8               pkgs/main/win-64::pep8-1.7.1-py39haa95532_0
  pexpect            pkgs/main/noarch::pexpect-4.8.0-pyhd3eb1b0_3
  pickleshare        pkgs/main/noarch::pickleshare-0.7.5-pyhd3eb1b0_1003
  pillow             pkgs/main/win-64::pillow-8.4.0-py39hd45dc43_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  pkginfo            pkgs/main/win-64::pkginfo-1.7.1-py39haa95532_0
  pluggy             pkgs/main/win-64::pluggy-0.13.1-py39haa95532_0
  ply                pkgs/main/win-64::ply-3.11-py39haa95532_0
  powershell_shortc~ pkgs/main/win-64::powershell_shortcut-0.0.1-3
  poyo               pkgs/main/noarch::poyo-0.5.0-pyhd3eb1b0_0
  prometheus_client  pkgs/main/noarch::prometheus_client-0.11.0-pyhd3eb1b0_0
  prompt-toolkit     pkgs/main/noarch::prompt-toolkit-3.0.20-pyhd3eb1b0_0
  prompt_toolkit     pkgs/main/noarch::prompt_toolkit-3.0.20-hd3eb1b0_0
  psutil             pkgs/main/win-64::psutil-5.8.0-py39h2bbff1b_1
  ptyprocess         pkgs/main/noarch::ptyprocess-0.7.0-pyhd3eb1b0_2
  py                 pkgs/main/noarch::py-1.10.0-pyhd3eb1b0_0
  py-lief            pkgs/main/win-64::py-lief-0.10.1-py39hd77b12b_1
  pycodestyle        pkgs/main/noarch::pycodestyle-2.7.0-pyhd3eb1b0_0
  pycosat            pkgs/main/win-64::pycosat-0.6.3-py39h2bbff1b_0
  pycparser          pkgs/main/noarch::pycparser-2.20-py_2
  pycurl             pkgs/main/win-64::pycurl-7.44.1-py39hcd4344a_1
  pydocstyle         pkgs/main/noarch::pydocstyle-6.1.1-pyhd3eb1b0_0
  pyerfa             pkgs/main/win-64::pyerfa-2.0.0-py39h2bbff1b_0
  pyflakes           pkgs/main/noarch::pyflakes-2.3.1-pyhd3eb1b0_0
  pygments           pkgs/main/noarch::pygments-2.10.0-pyhd3eb1b0_0
  pylint             pkgs/main/win-64::pylint-2.9.6-py39haa95532_1
  pyls-spyder        pkgs/main/noarch::pyls-spyder-0.4.0-pyhd3eb1b0_0
  pynacl             pkgs/main/win-64::pynacl-1.4.0-py39hbd8134f_1
  pyodbc             pkgs/main/win-64::pyodbc-4.0.31-py39hd77b12b_0
  pyopenssl          pkgs/main/noarch::pyopenssl-21.0.0-pyhd3eb1b0_1
  pyparsing          pkgs/main/noarch::pyparsing-3.0.4-pyhd3eb1b0_0
  pyqt               pkgs/main/win-64::pyqt-5.9.2-py39hd77b12b_6
  pyreadline         pkgs/main/win-64::pyreadline-2.1-py39haa95532_1
  pyrsistent         pkgs/main/win-64::pyrsistent-0.18.0-py39h196d8e1_0
  pysocks            pkgs/main/win-64::pysocks-1.7.1-py39haa95532_0
  pytables           pkgs/main/win-64::pytables-3.6.1-py39h56d22b6_1
  pytest             pkgs/main/win-64::pytest-6.2.4-py39haa95532_2
  python             pkgs/main/win-64::python-3.9.7-h6244533_1
  python-dateutil    pkgs/main/noarch::python-dateutil-2.8.2-pyhd3eb1b0_0
  python-libarchive~ pkgs/main/noarch::python-libarchive-c-2.9-pyhd3eb1b0_1
  python-lsp-black   pkgs/main/noarch::python-lsp-black-1.0.0-pyhd3eb1b0_0
  python-lsp-jsonrpc pkgs/main/noarch::python-lsp-jsonrpc-1.0.0-pyhd3eb1b0_0
  python-lsp-server  pkgs/main/noarch::python-lsp-server-1.2.4-pyhd3eb1b0_0
  python-slugify     pkgs/main/noarch::python-slugify-5.0.2-pyhd3eb1b0_0
  pytz               pkgs/main/noarch::pytz-2021.3-pyhd3eb1b0_0
  pywavelets         pkgs/main/win-64::pywavelets-1.1.1-py39h080aedc_4
  pywin32            pkgs/main/win-64::pywin32-228-py39he774522_0
  pywin32-ctypes     pkgs/main/win-64::pywin32-ctypes-0.2.0-py39haa95532_1000
  pywinpty           pkgs/main/win-64::pywinpty-0.5.7-py39haa95532_0
  pyyaml             pkgs/main/win-64::pyyaml-6.0-py39h2bbff1b_1
  pyzmq              pkgs/main/win-64::pyzmq-22.2.1-py39hd77b12b_1
  qdarkstyle         pkgs/main/noarch::qdarkstyle-3.0.2-pyhd3eb1b0_0
  qstylizer          pkgs/main/noarch::qstylizer-0.1.10-pyhd3eb1b0_0
  qt                 pkgs/main/win-64::qt-5.9.7-vc14h73c81de_0
  qtawesome          pkgs/main/noarch::qtawesome-1.0.2-pyhd3eb1b0_0
  qtconsole          pkgs/main/noarch::qtconsole-5.1.1-pyhd3eb1b0_0
  qtpy               pkgs/main/noarch::qtpy-1.10.0-pyhd3eb1b0_0
  regex              pkgs/main/win-64::regex-2021.8.3-py39h2bbff1b_0
  requests           pkgs/main/noarch::requests-2.26.0-pyhd3eb1b0_0
  rope               pkgs/main/noarch::rope-0.19.0-pyhd3eb1b0_0
  rtree              pkgs/main/win-64::rtree-0.9.7-py39h2eaa2aa_1
  ruamel_yaml        pkgs/main/win-64::ruamel_yaml-0.15.100-py39h2bbff1b_0
  scikit-image       pkgs/main/win-64::scikit-image-0.18.3-py39hf11a4ad_0
  scikit-learn       pkgs/main/win-64::scikit-learn-0.24.2-py39hf11a4ad_1
  scikit-learn-inte~ pkgs/main/win-64::scikit-learn-intelex-2021.3.0-py39haa95532_0
  scipy              pkgs/main/win-64::scipy-1.7.1-py39hbe87c03_2
  seaborn            pkgs/main/noarch::seaborn-0.11.2-pyhd3eb1b0_0
  send2trash         pkgs/main/noarch::send2trash-1.8.0-pyhd3eb1b0_1
  setuptools         pkgs/main/win-64::setuptools-58.0.4-py39haa95532_0
  simplegeneric      pkgs/main/win-64::simplegeneric-0.8.1-py39haa95532_2
  singledispatch     pkgs/main/noarch::singledispatch-3.7.0-pyhd3eb1b0_1001
  sip                pkgs/main/win-64::sip-4.19.13-py39hd77b12b_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_0
  snappy             pkgs/main/win-64::snappy-1.1.8-h33f27b4_0
  sniffio            pkgs/main/win-64::sniffio-1.2.0-py39haa95532_1
  snowballstemmer    pkgs/main/noarch::snowballstemmer-2.1.0-pyhd3eb1b0_0
  sortedcollections  pkgs/main/noarch::sortedcollections-2.1.0-pyhd3eb1b0_0
  sortedcontainers   pkgs/main/noarch::sortedcontainers-2.4.0-pyhd3eb1b0_0
  soupsieve          pkgs/main/noarch::soupsieve-2.2.1-pyhd3eb1b0_0
  sphinx             pkgs/main/noarch::sphinx-4.2.0-pyhd3eb1b0_1
  sphinxcontrib      pkgs/main/win-64::sphinxcontrib-1.0-py39haa95532_1
  sphinxcontrib-app~ pkgs/main/noarch::sphinxcontrib-applehelp-1.0.2-pyhd3eb1b0_0
  sphinxcontrib-dev~ pkgs/main/noarch::sphinxcontrib-devhelp-1.0.2-pyhd3eb1b0_0
  sphinxcontrib-htm~ pkgs/main/noarch::sphinxcontrib-htmlhelp-2.0.0-pyhd3eb1b0_0
  sphinxcontrib-jsm~ pkgs/main/noarch::sphinxcontrib-jsmath-1.0.1-pyhd3eb1b0_0
  sphinxcontrib-qth~ pkgs/main/noarch::sphinxcontrib-qthelp-1.0.3-pyhd3eb1b0_0
  sphinxcontrib-ser~ pkgs/main/noarch::sphinxcontrib-serializinghtml-1.1.5-pyhd3eb1b0_0
  sphinxcontrib-web~ pkgs/main/noarch::sphinxcontrib-websupport-1.2.4-py_0
  spyder             pkgs/main/win-64::spyder-5.1.5-py39haa95532_1
  spyder-kernels     pkgs/main/win-64::spyder-kernels-2.1.3-py39haa95532_0
  sqlalchemy         pkgs/main/win-64::sqlalchemy-1.4.22-py39h2bbff1b_0
  sqlite             pkgs/main/win-64::sqlite-3.36.0-h2bbff1b_0
  statsmodels        pkgs/main/win-64::statsmodels-0.12.2-py39h2bbff1b_0
  sympy              pkgs/main/win-64::sympy-1.9-py39haa95532_0
  tbb                pkgs/main/win-64::tbb-2021.4.0-h59b6b97_0
  tbb4py             pkgs/main/win-64::tbb4py-2021.4.0-py39h59b6b97_0
  tblib              pkgs/main/noarch::tblib-1.7.0-pyhd3eb1b0_0
  terminado          pkgs/main/win-64::terminado-0.9.4-py39haa95532_0
  testpath           pkgs/main/noarch::testpath-0.5.0-pyhd3eb1b0_0
  text-unidecode     pkgs/main/noarch::text-unidecode-1.3-pyhd3eb1b0_0
  textdistance       pkgs/main/noarch::textdistance-4.2.1-pyhd3eb1b0_0
  threadpoolctl      pkgs/main/noarch::threadpoolctl-2.2.0-pyh0d69192_0
  three-merge        pkgs/main/noarch::three-merge-0.1.1-pyhd3eb1b0_0
  tifffile           pkgs/main/noarch::tifffile-2021.7.2-pyhd3eb1b0_2
  tinycss            pkgs/main/noarch::tinycss-0.4-pyhd3eb1b0_1002
  tk                 pkgs/main/win-64::tk-8.6.11-h2bbff1b_0
  toml               pkgs/main/noarch::toml-0.10.2-pyhd3eb1b0_0
  toolz              pkgs/main/noarch::toolz-0.11.1-pyhd3eb1b0_0
  tornado            pkgs/main/win-64::tornado-6.1-py39h2bbff1b_0
  tqdm               pkgs/main/noarch::tqdm-4.62.3-pyhd3eb1b0_1
  traitlets          pkgs/main/noarch::traitlets-5.1.0-pyhd3eb1b0_0
  typed-ast          pkgs/main/win-64::typed-ast-1.4.3-py39h2bbff1b_1
  typing_extensions  pkgs/main/noarch::typing_extensions-3.10.0.2-pyh06a4308_0
  tzdata             pkgs/main/noarch::tzdata-2021e-hda174b7_0
  ujson              pkgs/main/win-64::ujson-4.0.2-py39hd77b12b_0
  unicodecsv         pkgs/main/win-64::unicodecsv-0.14.1-py39haa95532_0
  unidecode          pkgs/main/noarch::unidecode-1.2.0-pyhd3eb1b0_0
  urllib3            pkgs/main/noarch::urllib3-1.26.7-pyhd3eb1b0_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  watchdog           pkgs/main/win-64::watchdog-2.1.3-py39haa95532_0
  wcwidth            pkgs/main/noarch::wcwidth-0.2.5-pyhd3eb1b0_0
  webencodings       pkgs/main/win-64::webencodings-0.5.1-py39haa95532_1
  werkzeug           pkgs/main/noarch::werkzeug-2.0.2-pyhd3eb1b0_0
  wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
  whichcraft         pkgs/main/noarch::whichcraft-0.6.1-pyhd3eb1b0_0
  widgetsnbextension pkgs/main/win-64::widgetsnbextension-3.5.1-py39haa95532_0
  win_inet_pton      pkgs/main/win-64::win_inet_pton-1.1.0-py39haa95532_0
  win_unicode_conso~ pkgs/main/win-64::win_unicode_console-0.5-py39haa95532_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2
  winpty             pkgs/main/win-64::winpty-0.4.3-4
  wrapt              pkgs/main/win-64::wrapt-1.12.1-py39h196d8e1_1
  xlrd               pkgs/main/noarch::xlrd-2.0.1-pyhd3eb1b0_0
  xlsxwriter         pkgs/main/noarch::xlsxwriter-3.0.1-pyhd3eb1b0_0
  xlwings            pkgs/main/win-64::xlwings-0.24.9-py39haa95532_0
  xlwt               pkgs/main/win-64::xlwt-1.3.0-py39haa95532_0
  xz                 pkgs/main/win-64::xz-5.2.5-h62dcd97_0
  yaml               pkgs/main/win-64::yaml-0.2.5-he774522_0
  yapf               pkgs/main/noarch::yapf-0.31.0-pyhd3eb1b0_0
  zfp                pkgs/main/win-64::zfp-0.5.5-hd77b12b_6
  zict               pkgs/main/noarch::zict-2.0.0-pyhd3eb1b0_0
  zipp               pkgs/main/noarch::zipp-3.6.0-pyhd3eb1b0_0
  zlib               pkgs/main/win-64::zlib-1.2.11-h62dcd97_4
  zope               pkgs/main/win-64::zope-1.0-py39haa95532_1
  zope.event         pkgs/main/win-64::zope.event-4.5.0-py39haa95532_0
  zope.interface     pkgs/main/win-64::zope.interface-5.4.0-py39h2bbff1b_0
  zstd               pkgs/main/win-64::zstd-1.4.9-h19a0ad4_0


Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: -

    Windows 64-bit packages of scikit-learn can be accelerated using scikit-learn-intelex.
    More details are available here: https://intel.github.io/scikit-learn-intelex

    For example:

        $ conda install scikit-learn-intelex
        $ python -m sklearnex my_application.py


done
#
# To activate this environment, use
#
#     $ conda activate ceejayenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\ALH.YAHYA>conda activate ceejayenv

(ceejayenv) C:\Users\ALH.YAHYA>conda install -c anaconda django
Collecting package metadata (current_repodata.json): failed

CondaHTTPError: HTTP 502 BAD GATEWAY for url <https://repo.anaconda.com/pkgs/main/win-64/current_repodata.json>
Elapsed: 00:02.894575
CF-RAY: 713a915fedf4c4ec-LOS

A remote server error occurred when trying to retrieve this URL.

A 500-type error (e.g. 500, 501, 502, 503, etc.) indicates the server failed to
fulfill a valid request.  The problem may be spurious, and will resolve itself if you
try your request again.  If the problem persists, consider notifying the maintainer
of the remote server.



(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv puthon=3.6 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): failed

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/r/win-64/repodata.json>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

If your current network has https://www.anaconda.com blocked, please file
a support request with your network engineering team.

'https//repo.anaconda.com/pkgs/r/win-64'



(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv puthon=3.6 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - puthon=3.6

Current channels:

  - https://repo.anaconda.com/pkgs/main/win-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/win-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/msys2/win-64
  - https://repo.anaconda.com/pkgs/msys2/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.



(ceejayenv) C:\Users\ALH.YAHYA>conda activate djangoenv

EnvironmentNameNotFound: Could not find conda environment: djangoenv
You can list all discoverable environments with `conda info --envs`.



(ceejayenv) C:\Users\ALH.YAHYA>conda info --envs
# conda environments:
#
                         C:\ProgramData\Anaconda3
base                  *  C:\Users\ALH.YAHYA\.conda\envs\ceejayenv
wordcloud                C:\Users\ALH.YAHYA\.conda\envs\wordcloud


(ceejayenv) C:\Users\ALH.YAHYA>conda activate djangoenv

EnvironmentNameNotFound: Could not find conda environment: djangoenv
You can list all discoverable environments with `conda info --envs`.



(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv puthon=3.6 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - puthon=3.6

Current channels:

  - https://repo.anaconda.com/pkgs/main/win-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/win-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/msys2/win-64
  - https://repo.anaconda.com/pkgs/msys2/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.



(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv puthon=3.9.7 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - puthon=3.9.7

Current channels:

  - https://repo.anaconda.com/pkgs/main/win-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/win-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/msys2/win-64
  - https://repo.anaconda.com/pkgs/msys2/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.



(ceejayenv) C:\Users\ALH.YAHYA>conda info

     active environment : base
    active env location : C:\Users\ALH.YAHYA\.conda\envs\ceejayenv
            shell level : 2
       user config file : C:\Users\ALH.YAHYA\.condarc
 populated config files : C:\Users\ALH.YAHYA\.condarc
          conda version : 4.13.0
    conda-build version : not installed
         python version : 3.9.7.final.0
       virtual packages : __win=0=0
                          __archspec=1=x86_64
       base environment : C:\Users\ALH.YAHYA\.conda\envs\ceejayenv  (writable)
      conda av data dir : C:\Users\ALH.YAHYA\.conda\envs\ceejayenv\etc\conda
  conda av metadata url : None
           channel URLs : https://repo.anaconda.com/pkgs/main/win-64
                          https://repo.anaconda.com/pkgs/main/noarch
                          https://repo.anaconda.com/pkgs/r/win-64
                          https://repo.anaconda.com/pkgs/r/noarch
                          https://repo.anaconda.com/pkgs/msys2/win-64
                          https://repo.anaconda.com/pkgs/msys2/noarch
          package cache : C:\Users\ALH.YAHYA\.conda\envs\ceejayenv\pkgs
                          C:\Users\ALH.YAHYA\.conda\pkgs
                          C:\Users\ALH.YAHYA\AppData\Local\conda\conda\pkgs
       envs directories : C:\Users\ALH.YAHYA\.conda\envs\ceejayenv\envs
                          C:\Users\ALH.YAHYA\.conda\envs
                          C:\Users\ALH.YAHYA\AppData\Local\conda\conda\envs
               platform : win-64
             user-agent : conda/4.13.0 requests/2.26.0 CPython/3.9.7 Windows/10 Windows/10.0.19044
          administrator : False
             netrc file : None
           offline mode : False


(ceejayenv) C:\Users\ALH.YAHYA>pip install scp
Collecting scp
  Downloading scp-0.14.4-py2.py3-none-any.whl (8.6 kB)
Requirement already satisfied: paramiko in c:\users\alh.yahya\.conda\envs\ceejayenv\lib\site-packages (from scp) (2.7.2)
Requirement already satisfied: pynacl>=1.0.1 in c:\users\alh.yahya\.conda\envs\ceejayenv\lib\site-packages (from paramiko->scp) (1.4.0)
Requirement already satisfied: bcrypt>=3.1.3 in c:\users\alh.yahya\.conda\envs\ceejayenv\lib\site-packages (from paramiko->scp) (3.2.0)
Requirement already satisfied: cryptography>=2.5 in c:\users\alh.yahya\.conda\envs\ceejayenv\lib\site-packages (from paramiko->scp) (3.4.8)
Requirement already satisfied: six>=1.4.1 in c:\users\alh.yahya\.conda\envs\ceejayenv\lib\site-packages (from bcrypt>=3.1.3->paramiko->scp) (1.16.0)
Requirement already satisfied: cffi>=1.1 in c:\users\alh.yahya\.conda\envs\ceejayenv\lib\site-packages (from bcrypt>=3.1.3->paramiko->scp) (1.14.6)
Requirement already satisfied: pycparser in c:\users\alh.yahya\.conda\envs\ceejayenv\lib\site-packages (from cffi>=1.1->bcrypt>=3.1.3->paramiko->scp) (2.20)
Installing collected packages: scp
Successfully installed scp-0.14.4

(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv puthon=3.9.7 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - puthon=3.9.7

Current channels:

  - https://repo.anaconda.com/pkgs/main/win-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/win-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/msys2/win-64
  - https://repo.anaconda.com/pkgs/msys2/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.



(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv python=3.9.7 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\ALH.YAHYA\.conda\envs\ceejayenv\envs\djangoenv

  added / updated specs:
    - anaconda
    - python=3.9.7


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    alabaster-0.7.12           |     pyhd3eb1b0_0          16 KB
    anaconda-2021.11           |           py39_0          18 KB
    anaconda-client-1.9.0      |   py39haa95532_0         170 KB
    anaconda-project-0.10.1    |     pyhd3eb1b0_0         218 KB
    anyio-2.2.0                |   py39haa95532_2         125 KB
    appdirs-1.4.4              |     pyhd3eb1b0_0          12 KB
    argh-0.26.2                |   py39haa95532_0          36 KB
    argon2-cffi-20.1.0         |   py39h2bbff1b_1          49 KB
    arrow-0.13.1               |   py39haa95532_0          83 KB
    asn1crypto-1.4.0           |             py_0          80 KB
    astroid-2.6.6              |   py39haa95532_0         313 KB
    astropy-4.3.1              |   py39hc7d831d_0         6.1 MB
    async_generator-1.10       |     pyhd3eb1b0_0          23 KB
    atomicwrites-1.4.0         |             py_0          11 KB
    attrs-21.2.0               |     pyhd3eb1b0_0          46 KB
    autopep8-1.5.7             |     pyhd3eb1b0_0          43 KB
    babel-2.9.1                |     pyhd3eb1b0_0         5.5 MB
    backcall-0.2.0             |     pyhd3eb1b0_0          13 KB
    backports-1.0              |     pyhd3eb1b0_2         210 KB
    backports.shutil_get_terminal_size-1.0.0|     pyhd3eb1b0_3          10 KB
    bcrypt-3.2.0               |   py39h196d8e1_0         139 KB
    beautifulsoup4-4.10.0      |     pyh06a4308_0          85 KB
    binaryornot-0.4.4          |     pyhd3eb1b0_1         351 KB
    bitarray-2.3.0             |   py39h2bbff1b_1         142 KB
    bkcharts-0.2               |   py39haa95532_0         133 KB
    black-19.10b0              |             py_0          86 KB
    blas-1.0                   |              mkl           6 KB
    bleach-4.0.0               |     pyhd3eb1b0_0         113 KB
    blosc-1.21.0               |       h19a0ad4_0         139 KB
    bokeh-2.4.1                |   py39haa95532_0         7.6 MB
    boto-2.49.0                |   py39haa95532_0         1.5 MB
    bottleneck-1.3.2           |   py39h7cc1a96_1         107 KB
    brotli-1.0.9               |       ha925a31_2         332 KB
    brotlipy-0.7.0             |py39h2bbff1b_1003         411 KB
    bzip2-1.0.8                |       he774522_0         113 KB
    ca-certificates-2021.10.26 |       haa95532_2         115 KB
    cached-property-1.5.2      |             py_0          11 KB
    certifi-2021.10.8          |   py39haa95532_0         152 KB
    cffi-1.14.6                |   py39h2bbff1b_0         224 KB
    cfitsio-3.470              |       he774522_6         512 KB
    chardet-4.0.0              |py39haa95532_1003         212 KB
    charls-2.2.0               |       h6c2663c_0          82 KB
    charset-normalizer-2.0.4   |     pyhd3eb1b0_0          35 KB
    click-8.0.3                |     pyhd3eb1b0_0          79 KB
    cloudpickle-2.0.0          |     pyhd3eb1b0_0          32 KB
    clyent-1.2.2               |   py39haa95532_1          21 KB
    colorama-0.4.4             |     pyhd3eb1b0_0          21 KB
    comtypes-1.1.10            |py39haa95532_1002         239 KB
    conda-content-trust-0.1.1  |     pyhd3eb1b0_0          56 KB
    conda-pack-0.6.0           |     pyhd3eb1b0_0          29 KB
    conda-token-0.3.0          |     pyhd3eb1b0_0          10 KB
    console_shortcut-0.1.1     |                4         277 KB
    contextlib2-0.6.0.post1    |     pyhd3eb1b0_0          13 KB
    cookiecutter-1.7.2         |     pyhd3eb1b0_0          86 KB
    cryptography-3.4.8         |   py39h71e12ea_0         638 KB
    curl-7.78.0                |       h86230a5_0         132 KB
    cycler-0.10.0              |   py39haa95532_0          16 KB
    cython-0.29.24             |   py39h604cdb4_0         1.8 MB
    cytoolz-0.11.0             |   py39h2bbff1b_0         294 KB
    daal4py-2021.3.0           |   py39h757b272_0         7.6 MB
    dal-2021.3.0               |     haa95532_564        24.4 MB
    dask-2021.10.0             |     pyhd3eb1b0_0          19 KB
    dask-core-2021.10.0        |     pyhd3eb1b0_0         718 KB
    dataclasses-0.8            |     pyh6d0b6a4_7           8 KB
    debugpy-1.4.1              |   py39hd77b12b_0         2.6 MB
    decorator-5.1.0            |     pyhd3eb1b0_0          14 KB
    defusedxml-0.7.1           |     pyhd3eb1b0_0          23 KB
    diff-match-patch-20200713  |     pyhd3eb1b0_0          35 KB
    distributed-2021.10.0      |   py39haa95532_0        1013 KB
    docutils-0.17.1            |   py39haa95532_1         693 KB
    entrypoints-0.3            |   py39haa95532_0          12 KB
    et_xmlfile-1.1.0           |   py39haa95532_0          10 KB
    fastcache-1.1.0            |   py39h196d8e1_0          57 KB
    filelock-3.3.1             |     pyhd3eb1b0_1          12 KB
    flake8-3.9.2               |     pyhd3eb1b0_0         129 KB
    flask-1.1.2                |     pyhd3eb1b0_0          70 KB
    fonttools-4.25.0           |     pyhd3eb1b0_0         632 KB
    freetype-2.10.4            |       hd328e21_0         466 KB
    fsspec-2021.10.1           |     pyhd3eb1b0_0          96 KB
    get_terminal_size-1.0.0    |       h38e98db_0           3 KB
    gevent-21.8.0              |   py39h2bbff1b_1         1.4 MB
    giflib-5.2.1               |       h62dcd97_0          81 KB
    glob2-0.7                  |     pyhd3eb1b0_0          12 KB
    greenlet-1.1.1             |   py39hd77b12b_0          82 KB
    h5py-3.2.1                 |   py39h3de5c98_0         872 KB
    hdf5-1.10.6                |       h7ebc959_0         7.9 MB
    heapdict-1.0.1             |     pyhd3eb1b0_0           8 KB
    html5lib-1.1               |     pyhd3eb1b0_0          91 KB
    icc_rt-2019.0.0            |       h0cc432a_1         6.0 MB
    icu-58.2                   |       ha925a31_3         9.4 MB
    idna-3.2                   |     pyhd3eb1b0_0          48 KB
    imagecodecs-2021.8.26      |   py39ha1f97ea_0         6.2 MB
    imageio-2.9.0              |     pyhd3eb1b0_0         3.0 MB
    imagesize-1.2.0            |     pyhd3eb1b0_0           9 KB
    importlib-metadata-4.8.1   |   py39haa95532_0          39 KB
    importlib_metadata-4.8.1   |       hd3eb1b0_0          11 KB
    inflection-0.5.1           |   py39haa95532_0          12 KB
    iniconfig-1.1.1            |     pyhd3eb1b0_0           8 KB
    intel-openmp-2021.4.0      |    haa95532_3556         2.2 MB
    intervaltree-3.1.0         |     pyhd3eb1b0_0          25 KB
    ipykernel-6.4.1            |   py39haa95532_1         195 KB
    ipython-7.29.0             |   py39hd4e2768_0         1.0 MB
    ipython_genutils-0.2.0     |     pyhd3eb1b0_1          27 KB
    ipywidgets-7.6.5           |     pyhd3eb1b0_1         105 KB
    isort-5.9.3                |     pyhd3eb1b0_0          83 KB
    itsdangerous-2.0.1         |     pyhd3eb1b0_0          18 KB
    jdcal-1.4.1                |     pyhd3eb1b0_0          10 KB
    jedi-0.18.0                |   py39haa95532_1         912 KB
    jinja2-2.11.3              |     pyhd3eb1b0_0         101 KB
    jinja2-time-0.2.0          |     pyhd3eb1b0_2          17 KB
    joblib-1.1.0               |     pyhd3eb1b0_0         211 KB
    jpeg-9d                    |       h2bbff1b_0         283 KB
    json5-0.9.6                |     pyhd3eb1b0_0          21 KB
    jsonschema-3.2.0           |     pyhd3eb1b0_2          47 KB
    jupyter-1.0.0              |   py39haa95532_7           8 KB
    jupyter_client-6.1.12      |     pyhd3eb1b0_0          88 KB
    jupyter_console-6.4.0      |     pyhd3eb1b0_0          23 KB
    jupyter_core-4.8.1         |   py39haa95532_0          91 KB
    jupyter_server-1.4.1       |   py39haa95532_0         328 KB
    jupyterlab-3.2.1           |     pyhd3eb1b0_1         3.6 MB
    jupyterlab_pygments-0.1.2  |             py_0           8 KB
    jupyterlab_server-2.8.2    |     pyhd3eb1b0_0          46 KB
    jupyterlab_widgets-1.0.0   |     pyhd3eb1b0_1         109 KB
    keyring-23.1.0             |   py39haa95532_0          78 KB
    kiwisolver-1.3.1           |   py39hd77b12b_0          52 KB
    krb5-1.19.2                |       h5b6d351_0         697 KB
    lazy-object-proxy-1.6.0    |   py39h2bbff1b_0          31 KB
    lcms2-2.12                 |       h83e58a3_0         454 KB
    lerc-3.0                   |       hd77b12b_0         120 KB
    libaec-1.0.4               |       h33f27b4_1          31 KB
    libarchive-3.4.2           |       h5e25573_0         1.7 MB
    libcurl-7.78.0             |       h86230a5_0         294 KB
    libdeflate-1.8             |       h2bbff1b_5          46 KB
    libiconv-1.15              |       h1df5818_7         626 KB
    liblief-0.10.1             |       hd77b12b_1         1.6 MB
    libpng-1.6.37              |       h2a8f88b_0         333 KB
    libspatialindex-1.9.3      |       h6c2663c_0         351 KB
    libssh2-1.9.0              |       h7a1dbc1_1         215 KB
    libtiff-4.2.0              |       hd0e1b90_0         786 KB
    libwebp-1.2.0              |       h2bbff1b_0         643 KB
    libxml2-2.9.12             |       h0ad7f3c_0         1.5 MB
    libxslt-1.1.34             |       he774522_0         399 KB
    libzopfli-1.0.3            |       ha925a31_0         176 KB
    llvmlite-0.37.0            |   py39h23ce68f_1        13.3 MB
    locket-0.2.1               |   py39haa95532_1          10 KB
    lxml-4.6.3                 |   py39h9b66d53_0         978 KB
    lz4-c-1.9.3                |       h2bbff1b_1         132 KB
    lzo-2.10                   |       he774522_2         142 KB
    m2w64-gcc-libgfortran-5.3.0|                6         340 KB
    m2w64-gcc-libs-5.3.0       |                7         518 KB
    m2w64-gcc-libs-core-5.3.0  |                7         213 KB
    m2w64-gmp-6.1.0            |                2         689 KB
    m2w64-libwinpthread-git-5.0.0.4634.697f757|                2          30 KB
    markupsafe-1.1.1           |   py39h2bbff1b_0          56 KB
    matplotlib-3.4.3           |   py39haa95532_0          29 KB
    matplotlib-base-3.4.3      |   py39h49ac443_0         5.5 MB
    matplotlib-inline-0.1.2    |     pyhd3eb1b0_2          12 KB
    mccabe-0.6.1               |   py39haa95532_1          16 KB
    menuinst-1.4.18            |   py39h59b6b97_0          96 KB
    mistune-0.8.4              |py39h2bbff1b_1000          57 KB
    mkl-2021.4.0               |     haa95532_640       114.9 MB
    mkl-service-2.4.0          |   py39h2bbff1b_0          51 KB
    mkl_fft-1.3.1              |   py39h277e83a_0         139 KB
    mkl_random-1.2.2           |   py39hf11a4ad_0         225 KB
    mock-4.0.3                 |     pyhd3eb1b0_0          29 KB
    more-itertools-8.10.0      |     pyhd3eb1b0_0          47 KB
    mpmath-1.2.1               |   py39haa95532_0         773 KB
    msgpack-python-1.0.2       |   py39h59b6b97_1          76 KB
    msys2-conda-epoch-20160418 |                1           2 KB
    multipledispatch-0.6.0     |   py39haa95532_0          24 KB
    munkres-1.1.4              |             py_0          13 KB
    mypy_extensions-0.4.3      |   py39haa95532_0          10 KB
    nbclassic-0.2.6            |     pyhd3eb1b0_0          19 KB
    nbclient-0.5.3             |     pyhd3eb1b0_0          62 KB
    nbconvert-6.1.0            |   py39haa95532_0         501 KB
    nbformat-5.1.3             |     pyhd3eb1b0_0          44 KB
    nest-asyncio-1.5.1         |     pyhd3eb1b0_0          10 KB
    networkx-2.6.3             |     pyhd3eb1b0_0         1.3 MB
    nltk-3.6.5                 |     pyhd3eb1b0_0         979 KB
    nose-1.3.7                 |  pyhd3eb1b0_1006         128 KB
    notebook-6.4.5             |   py39haa95532_0         4.5 MB
    numba-0.54.1               |   py39hf11a4ad_0         3.3 MB
    numexpr-2.7.3              |   py39hb80d3ca_1         126 KB
    numpy-1.20.3               |   py39ha4e8547_0          23 KB
    numpy-base-1.20.3          |   py39hc2deb75_0         4.2 MB
    numpydoc-1.1.0             |     pyhd3eb1b0_1          42 KB
    olefile-0.46               |     pyhd3eb1b0_0          34 KB
    openjpeg-2.4.0             |       h4fc8c34_0         219 KB
    openpyxl-3.0.9             |     pyhd3eb1b0_0         164 KB
    openssl-1.1.1l             |       h2bbff1b_0         4.8 MB
    packaging-21.0             |     pyhd3eb1b0_0          36 KB
    pandas-1.3.4               |   py39h6214cd6_0         8.6 MB
    pandocfilters-1.4.3        |   py39haa95532_1          14 KB
    paramiko-2.7.2             |             py_0         143 KB
    parso-0.8.2                |     pyhd3eb1b0_0          69 KB
    partd-1.2.0                |     pyhd3eb1b0_0          19 KB
    path-16.0.0                |   py39haa95532_0          38 KB
    path.py-12.5.0             |       hd3eb1b0_0           4 KB
    pathlib2-2.3.6             |   py39haa95532_2          37 KB
    pathspec-0.7.0             |             py_0          26 KB
    patsy-0.5.2                |   py39haa95532_0         274 KB
    pep8-1.7.1                 |   py39haa95532_0          71 KB
    pexpect-4.8.0              |     pyhd3eb1b0_3          53 KB
    pickleshare-0.7.5          |  pyhd3eb1b0_1003          13 KB
    pillow-8.4.0               |   py39hd45dc43_0         906 KB
    pip-21.2.4                 |   py39haa95532_0         1.8 MB
    pkginfo-1.7.1              |   py39haa95532_0          60 KB
    pluggy-0.13.1              |   py39haa95532_0          34 KB
    ply-3.11                   |   py39haa95532_0          81 KB
    powershell_shortcut-0.0.1  |                3         277 KB
    poyo-0.5.0                 |     pyhd3eb1b0_0          17 KB
    prometheus_client-0.11.0   |     pyhd3eb1b0_0          47 KB
    prompt-toolkit-3.0.20      |     pyhd3eb1b0_0         259 KB
    prompt_toolkit-3.0.20      |       hd3eb1b0_0          12 KB
    psutil-5.8.0               |   py39h2bbff1b_1         348 KB
    ptyprocess-0.7.0           |     pyhd3eb1b0_2          17 KB
    py-1.10.0                  |     pyhd3eb1b0_0          76 KB
    py-lief-0.10.1             |   py39hd77b12b_1         1.1 MB
    pycodestyle-2.7.0          |     pyhd3eb1b0_0          41 KB
    pycosat-0.6.3              |   py39h2bbff1b_0          75 KB
    pycparser-2.20             |             py_2          94 KB
    pycurl-7.44.1              |   py39hcd4344a_1          68 KB
    pydocstyle-6.1.1           |     pyhd3eb1b0_0          36 KB
    pyerfa-2.0.0               |   py39h2bbff1b_0         359 KB
    pyflakes-2.3.1             |     pyhd3eb1b0_0          60 KB
    pygments-2.10.0            |     pyhd3eb1b0_0         725 KB
    pylint-2.9.6               |   py39haa95532_1         505 KB
    pyls-spyder-0.4.0          |     pyhd3eb1b0_0          11 KB
    pynacl-1.4.0               |   py39hbd8134f_1         1.3 MB
    pyodbc-4.0.31              |   py39hd77b12b_0          68 KB
    pyopenssl-21.0.0           |     pyhd3eb1b0_1          49 KB
    pyparsing-3.0.4            |     pyhd3eb1b0_0          81 KB
    pyqt-5.9.2                 |   py39hd77b12b_6         3.3 MB
    pyreadline-2.1             |   py39haa95532_1         146 KB
    pyrsistent-0.18.0          |   py39h196d8e1_0          90 KB
    pysocks-1.7.1              |   py39haa95532_0          55 KB
    pytables-3.6.1             |   py39h56d22b6_1         1.1 MB
    pytest-6.2.4               |   py39haa95532_2         445 KB
    python-3.9.7               |       h6244533_1        16.5 MB
    python-dateutil-2.8.2      |     pyhd3eb1b0_0         233 KB
    python-libarchive-c-2.9    |     pyhd3eb1b0_1          47 KB
    python-lsp-black-1.0.0     |     pyhd3eb1b0_0           8 KB
    python-lsp-jsonrpc-1.0.0   |     pyhd3eb1b0_0          10 KB
    python-lsp-server-1.2.4    |     pyhd3eb1b0_0          41 KB
    python-slugify-5.0.2       |     pyhd3eb1b0_0          13 KB
    pytz-2021.3                |     pyhd3eb1b0_0         171 KB
    pywavelets-1.1.1           |   py39h080aedc_4         3.4 MB
    pywin32-228                |   py39he774522_0         5.6 MB
    pywin32-ctypes-0.2.0       |py39haa95532_1000          40 KB
    pywinpty-0.5.7             |   py39haa95532_0          51 KB
    pyyaml-6.0                 |   py39h2bbff1b_1         145 KB
    pyzmq-22.2.1               |   py39hd77b12b_1         620 KB
    qdarkstyle-3.0.2           |     pyhd3eb1b0_0         337 KB
    qstylizer-0.1.10           |     pyhd3eb1b0_0          17 KB
    qt-5.9.7                   |   vc14h73c81de_0        72.5 MB
    qtawesome-1.0.2            |     pyhd3eb1b0_0         760 KB
    qtconsole-5.1.1            |     pyhd3eb1b0_0          98 KB
    qtpy-1.10.0                |     pyhd3eb1b0_0          35 KB
    regex-2021.8.3             |   py39h2bbff1b_0         301 KB
    requests-2.26.0            |     pyhd3eb1b0_0          59 KB
    rope-0.19.0                |     pyhd3eb1b0_0         126 KB
    rtree-0.9.7                |   py39h2eaa2aa_1          49 KB
    ruamel_yaml-0.15.100       |   py39h2bbff1b_0         273 KB
    scikit-image-0.18.3        |   py39hf11a4ad_0         9.1 MB
    scikit-learn-0.24.2        |   py39hf11a4ad_1         4.9 MB
    scikit-learn-intelex-2021.3.0|   py39haa95532_0          38 KB
    scipy-1.7.1                |   py39hbe87c03_2        13.8 MB
    seaborn-0.11.2             |     pyhd3eb1b0_0         218 KB
    send2trash-1.8.0           |     pyhd3eb1b0_1          19 KB
    setuptools-58.0.4          |   py39haa95532_0         778 KB
    simplegeneric-0.8.1        |   py39haa95532_2          11 KB
    singledispatch-3.7.0       |  pyhd3eb1b0_1001          12 KB
    sip-4.19.13                |   py39hd77b12b_0         262 KB
    six-1.16.0                 |     pyhd3eb1b0_0          18 KB
    snappy-1.1.8               |       h33f27b4_0          80 KB
    sniffio-1.2.0              |   py39haa95532_1          15 KB
    snowballstemmer-2.1.0      |     pyhd3eb1b0_0          62 KB
    sortedcollections-2.1.0    |     pyhd3eb1b0_0          12 KB
    sortedcontainers-2.4.0     |     pyhd3eb1b0_0          26 KB
    soupsieve-2.2.1            |     pyhd3eb1b0_0          32 KB
    sphinx-4.2.0               |     pyhd3eb1b0_1         1.2 MB
    sphinxcontrib-1.0          |   py39haa95532_1         218 KB
    sphinxcontrib-applehelp-1.0.2|     pyhd3eb1b0_0          29 KB
    sphinxcontrib-devhelp-1.0.2|     pyhd3eb1b0_0          23 KB
    sphinxcontrib-htmlhelp-2.0.0|     pyhd3eb1b0_0          32 KB
    sphinxcontrib-jsmath-1.0.1 |     pyhd3eb1b0_0           8 KB
    sphinxcontrib-qthelp-1.0.3 |     pyhd3eb1b0_0          26 KB
    sphinxcontrib-serializinghtml-1.1.5|     pyhd3eb1b0_0          25 KB
    sphinxcontrib-websupport-1.2.4|             py_0          34 KB
    spyder-5.1.5               |   py39haa95532_1         9.4 MB
    spyder-kernels-2.1.3       |   py39haa95532_0         112 KB
    sqlalchemy-1.4.22          |   py39h2bbff1b_0         1.8 MB
    sqlite-3.36.0              |       h2bbff1b_0         780 KB
    statsmodels-0.12.2         |   py39h2bbff1b_0         8.2 MB
    sympy-1.9                  |   py39haa95532_0         9.2 MB
    tbb-2021.4.0               |       h59b6b97_0         148 KB
    tbb4py-2021.4.0            |   py39h59b6b97_0          72 KB
    tblib-1.7.0                |     pyhd3eb1b0_0          15 KB
    terminado-0.9.4            |   py39haa95532_0          26 KB
    testpath-0.5.0             |     pyhd3eb1b0_0          81 KB
    text-unidecode-1.3         |     pyhd3eb1b0_0          65 KB
    textdistance-4.2.1         |     pyhd3eb1b0_0          29 KB
    threadpoolctl-2.2.0        |     pyh0d69192_0          16 KB
    three-merge-0.1.1          |     pyhd3eb1b0_0          10 KB
    tifffile-2021.7.2          |     pyhd3eb1b0_2         135 KB
    tinycss-0.4                |  pyhd3eb1b0_1002          39 KB
    tk-8.6.11                  |       h2bbff1b_0         3.3 MB
    toml-0.10.2                |     pyhd3eb1b0_0          20 KB
    toolz-0.11.1               |     pyhd3eb1b0_0          46 KB
    tornado-6.1                |   py39h2bbff1b_0         598 KB
    tqdm-4.62.3                |     pyhd3eb1b0_1          83 KB
    traitlets-5.1.0            |     pyhd3eb1b0_0          89 KB
    typed-ast-1.4.3            |   py39h2bbff1b_1         137 KB
    typing_extensions-3.10.0.2 |     pyh06a4308_0          31 KB
    tzdata-2021e               |       hda174b7_0         112 KB
    ujson-4.0.2                |   py39hd77b12b_0          46 KB
    unicodecsv-0.14.1          |   py39haa95532_0          28 KB
    unidecode-1.2.0            |     pyhd3eb1b0_0         155 KB
    urllib3-1.26.7             |     pyhd3eb1b0_0         111 KB
    vc-14.2                    |       h21ff451_1           8 KB
    vs2015_runtime-14.27.29016 |       h5e58377_2        1007 KB
    watchdog-2.1.3             |   py39haa95532_0         109 KB
    wcwidth-0.2.5              |     pyhd3eb1b0_0          26 KB
    webencodings-0.5.1         |   py39haa95532_1          20 KB
    werkzeug-2.0.2             |     pyhd3eb1b0_0         224 KB
    wheel-0.37.0               |     pyhd3eb1b0_1          33 KB
    whichcraft-0.6.1           |     pyhd3eb1b0_0          11 KB
    widgetsnbextension-3.5.1   |   py39haa95532_0         867 KB
    win_inet_pton-1.1.0        |   py39haa95532_0          35 KB
    win_unicode_console-0.5    |   py39haa95532_0          35 KB
    wincertstore-0.2           |   py39haa95532_2          15 KB
    winpty-0.4.3               |                4         678 KB
    wrapt-1.12.1               |   py39h196d8e1_1          73 KB
    xlrd-2.0.1                 |     pyhd3eb1b0_0          90 KB
    xlsxwriter-3.0.1           |     pyhd3eb1b0_0         111 KB
    xlwings-0.24.9             |   py39haa95532_0         894 KB
    xlwt-1.3.0                 |   py39haa95532_0         160 KB
    xz-5.2.5                   |       h62dcd97_0         244 KB
    yaml-0.2.5                 |       he774522_0          62 KB
    yapf-0.31.0                |     pyhd3eb1b0_0         126 KB
    zfp-0.5.5                  |       hd77b12b_6         139 KB
    zict-2.0.0                 |     pyhd3eb1b0_0          10 KB
    zipp-3.6.0                 |     pyhd3eb1b0_0          17 KB
    zlib-1.2.11                |       h62dcd97_4         113 KB
    zope-1.0                   |   py39haa95532_1         218 KB
    zope.event-4.5.0           |   py39haa95532_0         223 KB
    zope.interface-5.4.0       |   py39h2bbff1b_0         304 KB
    zstd-1.4.9                 |       h19a0ad4_0         478 KB
    ------------------------------------------------------------
                                           Total:       477.4 MB

The following NEW packages will be INSTALLED:

  alabaster          pkgs/main/noarch::alabaster-0.7.12-pyhd3eb1b0_0
  anaconda           pkgs/main/win-64::anaconda-2021.11-py39_0
  anaconda-client    pkgs/main/win-64::anaconda-client-1.9.0-py39haa95532_0
  anaconda-project   pkgs/main/noarch::anaconda-project-0.10.1-pyhd3eb1b0_0
  anyio              pkgs/main/win-64::anyio-2.2.0-py39haa95532_2
  appdirs            pkgs/main/noarch::appdirs-1.4.4-pyhd3eb1b0_0
  argh               pkgs/main/win-64::argh-0.26.2-py39haa95532_0
  argon2-cffi        pkgs/main/win-64::argon2-cffi-20.1.0-py39h2bbff1b_1
  arrow              pkgs/main/win-64::arrow-0.13.1-py39haa95532_0
  asn1crypto         pkgs/main/noarch::asn1crypto-1.4.0-py_0
  astroid            pkgs/main/win-64::astroid-2.6.6-py39haa95532_0
  astropy            pkgs/main/win-64::astropy-4.3.1-py39hc7d831d_0
  async_generator    pkgs/main/noarch::async_generator-1.10-pyhd3eb1b0_0
  atomicwrites       pkgs/main/noarch::atomicwrites-1.4.0-py_0
  attrs              pkgs/main/noarch::attrs-21.2.0-pyhd3eb1b0_0
  autopep8           pkgs/main/noarch::autopep8-1.5.7-pyhd3eb1b0_0
  babel              pkgs/main/noarch::babel-2.9.1-pyhd3eb1b0_0
  backcall           pkgs/main/noarch::backcall-0.2.0-pyhd3eb1b0_0
  backports          pkgs/main/noarch::backports-1.0-pyhd3eb1b0_2
  backports.shutil_~ pkgs/main/noarch::backports.shutil_get_terminal_size-1.0.0-pyhd3eb1b0_3
  bcrypt             pkgs/main/win-64::bcrypt-3.2.0-py39h196d8e1_0
  beautifulsoup4     pkgs/main/noarch::beautifulsoup4-4.10.0-pyh06a4308_0
  binaryornot        pkgs/main/noarch::binaryornot-0.4.4-pyhd3eb1b0_1
  bitarray           pkgs/main/win-64::bitarray-2.3.0-py39h2bbff1b_1
  bkcharts           pkgs/main/win-64::bkcharts-0.2-py39haa95532_0
  black              pkgs/main/noarch::black-19.10b0-py_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  bleach             pkgs/main/noarch::bleach-4.0.0-pyhd3eb1b0_0
  blosc              pkgs/main/win-64::blosc-1.21.0-h19a0ad4_0
  bokeh              pkgs/main/win-64::bokeh-2.4.1-py39haa95532_0
  boto               pkgs/main/win-64::boto-2.49.0-py39haa95532_0
  bottleneck         pkgs/main/win-64::bottleneck-1.3.2-py39h7cc1a96_1
  brotli             pkgs/main/win-64::brotli-1.0.9-ha925a31_2
  brotlipy           pkgs/main/win-64::brotlipy-0.7.0-py39h2bbff1b_1003
  bzip2              pkgs/main/win-64::bzip2-1.0.8-he774522_0
  ca-certificates    pkgs/main/win-64::ca-certificates-2021.10.26-haa95532_2
  cached-property    pkgs/main/noarch::cached-property-1.5.2-py_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_0
  cffi               pkgs/main/win-64::cffi-1.14.6-py39h2bbff1b_0
  cfitsio            pkgs/main/win-64::cfitsio-3.470-he774522_6
  chardet            pkgs/main/win-64::chardet-4.0.0-py39haa95532_1003
  charls             pkgs/main/win-64::charls-2.2.0-h6c2663c_0
  charset-normalizer pkgs/main/noarch::charset-normalizer-2.0.4-pyhd3eb1b0_0
  click              pkgs/main/noarch::click-8.0.3-pyhd3eb1b0_0
  cloudpickle        pkgs/main/noarch::cloudpickle-2.0.0-pyhd3eb1b0_0
  clyent             pkgs/main/win-64::clyent-1.2.2-py39haa95532_1
  colorama           pkgs/main/noarch::colorama-0.4.4-pyhd3eb1b0_0
  comtypes           pkgs/main/win-64::comtypes-1.1.10-py39haa95532_1002
  conda              pkgs/main/win-64::conda-4.13.0-py39haa95532_0
  conda-content-tru~ pkgs/main/noarch::conda-content-trust-0.1.1-pyhd3eb1b0_0
  conda-pack         pkgs/main/noarch::conda-pack-0.6.0-pyhd3eb1b0_0
  conda-package-han~ pkgs/main/win-64::conda-package-handling-1.8.1-py39h8cc25b3_0
  conda-token        pkgs/main/noarch::conda-token-0.3.0-pyhd3eb1b0_0
  console_shortcut   pkgs/main/win-64::console_shortcut-0.1.1-4
  contextlib2        pkgs/main/noarch::contextlib2-0.6.0.post1-pyhd3eb1b0_0
  cookiecutter       pkgs/main/noarch::cookiecutter-1.7.2-pyhd3eb1b0_0
  cryptography       pkgs/main/win-64::cryptography-3.4.8-py39h71e12ea_0
  curl               pkgs/main/win-64::curl-7.78.0-h86230a5_0
  cycler             pkgs/main/win-64::cycler-0.10.0-py39haa95532_0
  cython             pkgs/main/win-64::cython-0.29.24-py39h604cdb4_0
  cytoolz            pkgs/main/win-64::cytoolz-0.11.0-py39h2bbff1b_0
  daal4py            pkgs/main/win-64::daal4py-2021.3.0-py39h757b272_0
  dal                pkgs/main/win-64::dal-2021.3.0-haa95532_564
  dask               pkgs/main/noarch::dask-2021.10.0-pyhd3eb1b0_0
  dask-core          pkgs/main/noarch::dask-core-2021.10.0-pyhd3eb1b0_0
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7
  debugpy            pkgs/main/win-64::debugpy-1.4.1-py39hd77b12b_0
  decorator          pkgs/main/noarch::decorator-5.1.0-pyhd3eb1b0_0
  defusedxml         pkgs/main/noarch::defusedxml-0.7.1-pyhd3eb1b0_0
  diff-match-patch   pkgs/main/noarch::diff-match-patch-20200713-pyhd3eb1b0_0
  distributed        pkgs/main/win-64::distributed-2021.10.0-py39haa95532_0
  docutils           pkgs/main/win-64::docutils-0.17.1-py39haa95532_1
  entrypoints        pkgs/main/win-64::entrypoints-0.3-py39haa95532_0
  et_xmlfile         pkgs/main/win-64::et_xmlfile-1.1.0-py39haa95532_0
  fastcache          pkgs/main/win-64::fastcache-1.1.0-py39h196d8e1_0
  filelock           pkgs/main/noarch::filelock-3.3.1-pyhd3eb1b0_1
  flake8             pkgs/main/noarch::flake8-3.9.2-pyhd3eb1b0_0
  flask              pkgs/main/noarch::flask-1.1.2-pyhd3eb1b0_0
  fonttools          pkgs/main/noarch::fonttools-4.25.0-pyhd3eb1b0_0
  freetype           pkgs/main/win-64::freetype-2.10.4-hd328e21_0
  fsspec             pkgs/main/noarch::fsspec-2021.10.1-pyhd3eb1b0_0
  get_terminal_size  pkgs/main/win-64::get_terminal_size-1.0.0-h38e98db_0
  gevent             pkgs/main/win-64::gevent-21.8.0-py39h2bbff1b_1
  giflib             pkgs/main/win-64::giflib-5.2.1-h62dcd97_0
  glob2              pkgs/main/noarch::glob2-0.7-pyhd3eb1b0_0
  greenlet           pkgs/main/win-64::greenlet-1.1.1-py39hd77b12b_0
  h5py               pkgs/main/win-64::h5py-3.2.1-py39h3de5c98_0
  hdf5               pkgs/main/win-64::hdf5-1.10.6-h7ebc959_0
  heapdict           pkgs/main/noarch::heapdict-1.0.1-pyhd3eb1b0_0
  html5lib           pkgs/main/noarch::html5lib-1.1-pyhd3eb1b0_0
  icc_rt             pkgs/main/win-64::icc_rt-2019.0.0-h0cc432a_1
  icu                pkgs/main/win-64::icu-58.2-ha925a31_3
  idna               pkgs/main/noarch::idna-3.2-pyhd3eb1b0_0
  imagecodecs        pkgs/main/win-64::imagecodecs-2021.8.26-py39ha1f97ea_0
  imageio            pkgs/main/noarch::imageio-2.9.0-pyhd3eb1b0_0
  imagesize          pkgs/main/noarch::imagesize-1.2.0-pyhd3eb1b0_0
  importlib-metadata pkgs/main/win-64::importlib-metadata-4.8.1-py39haa95532_0
  importlib_metadata pkgs/main/noarch::importlib_metadata-4.8.1-hd3eb1b0_0
  inflection         pkgs/main/win-64::inflection-0.5.1-py39haa95532_0
  iniconfig          pkgs/main/noarch::iniconfig-1.1.1-pyhd3eb1b0_0
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  intervaltree       pkgs/main/noarch::intervaltree-3.1.0-pyhd3eb1b0_0
  ipykernel          pkgs/main/win-64::ipykernel-6.4.1-py39haa95532_1
  ipython            pkgs/main/win-64::ipython-7.29.0-py39hd4e2768_0
  ipython_genutils   pkgs/main/noarch::ipython_genutils-0.2.0-pyhd3eb1b0_1
  ipywidgets         pkgs/main/noarch::ipywidgets-7.6.5-pyhd3eb1b0_1
  isort              pkgs/main/noarch::isort-5.9.3-pyhd3eb1b0_0
  itsdangerous       pkgs/main/noarch::itsdangerous-2.0.1-pyhd3eb1b0_0
  jdcal              pkgs/main/noarch::jdcal-1.4.1-pyhd3eb1b0_0
  jedi               pkgs/main/win-64::jedi-0.18.0-py39haa95532_1
  jinja2             pkgs/main/noarch::jinja2-2.11.3-pyhd3eb1b0_0
  jinja2-time        pkgs/main/noarch::jinja2-time-0.2.0-pyhd3eb1b0_2
  joblib             pkgs/main/noarch::joblib-1.1.0-pyhd3eb1b0_0
  jpeg               pkgs/main/win-64::jpeg-9d-h2bbff1b_0
  json5              pkgs/main/noarch::json5-0.9.6-pyhd3eb1b0_0
  jsonschema         pkgs/main/noarch::jsonschema-3.2.0-pyhd3eb1b0_2
  jupyter            pkgs/main/win-64::jupyter-1.0.0-py39haa95532_7
  jupyter_client     pkgs/main/noarch::jupyter_client-6.1.12-pyhd3eb1b0_0
  jupyter_console    pkgs/main/noarch::jupyter_console-6.4.0-pyhd3eb1b0_0
  jupyter_core       pkgs/main/win-64::jupyter_core-4.8.1-py39haa95532_0
  jupyter_server     pkgs/main/win-64::jupyter_server-1.4.1-py39haa95532_0
  jupyterlab         pkgs/main/noarch::jupyterlab-3.2.1-pyhd3eb1b0_1
  jupyterlab_pygmen~ pkgs/main/noarch::jupyterlab_pygments-0.1.2-py_0
  jupyterlab_server  pkgs/main/noarch::jupyterlab_server-2.8.2-pyhd3eb1b0_0
  jupyterlab_widgets pkgs/main/noarch::jupyterlab_widgets-1.0.0-pyhd3eb1b0_1
  keyring            pkgs/main/win-64::keyring-23.1.0-py39haa95532_0
  kiwisolver         pkgs/main/win-64::kiwisolver-1.3.1-py39hd77b12b_0
  krb5               pkgs/main/win-64::krb5-1.19.2-h5b6d351_0
  lazy-object-proxy  pkgs/main/win-64::lazy-object-proxy-1.6.0-py39h2bbff1b_0
  lcms2              pkgs/main/win-64::lcms2-2.12-h83e58a3_0
  lerc               pkgs/main/win-64::lerc-3.0-hd77b12b_0
  libaec             pkgs/main/win-64::libaec-1.0.4-h33f27b4_1
  libarchive         pkgs/main/win-64::libarchive-3.4.2-h5e25573_0
  libcurl            pkgs/main/win-64::libcurl-7.78.0-h86230a5_0
  libdeflate         pkgs/main/win-64::libdeflate-1.8-h2bbff1b_5
  libiconv           pkgs/main/win-64::libiconv-1.15-h1df5818_7
  liblief            pkgs/main/win-64::liblief-0.10.1-hd77b12b_1
  libpng             pkgs/main/win-64::libpng-1.6.37-h2a8f88b_0
  libspatialindex    pkgs/main/win-64::libspatialindex-1.9.3-h6c2663c_0
  libssh2            pkgs/main/win-64::libssh2-1.9.0-h7a1dbc1_1
  libtiff            pkgs/main/win-64::libtiff-4.2.0-hd0e1b90_0
  libwebp            pkgs/main/win-64::libwebp-1.2.0-h2bbff1b_0
  libxml2            pkgs/main/win-64::libxml2-2.9.12-h0ad7f3c_0
  libxslt            pkgs/main/win-64::libxslt-1.1.34-he774522_0
  libzopfli          pkgs/main/win-64::libzopfli-1.0.3-ha925a31_0
  llvmlite           pkgs/main/win-64::llvmlite-0.37.0-py39h23ce68f_1
  locket             pkgs/main/win-64::locket-0.2.1-py39haa95532_1
  lxml               pkgs/main/win-64::lxml-4.6.3-py39h9b66d53_0
  lz4-c              pkgs/main/win-64::lz4-c-1.9.3-h2bbff1b_1
  lzo                pkgs/main/win-64::lzo-2.10-he774522_2
  m2w64-gcc-libgfor~ pkgs/msys2/win-64::m2w64-gcc-libgfortran-5.3.0-6
  m2w64-gcc-libs     pkgs/msys2/win-64::m2w64-gcc-libs-5.3.0-7
  m2w64-gcc-libs-co~ pkgs/msys2/win-64::m2w64-gcc-libs-core-5.3.0-7
  m2w64-gmp          pkgs/msys2/win-64::m2w64-gmp-6.1.0-2
  m2w64-libwinpthre~ pkgs/msys2/win-64::m2w64-libwinpthread-git-5.0.0.4634.697f757-2
  markupsafe         pkgs/main/win-64::markupsafe-1.1.1-py39h2bbff1b_0
  matplotlib         pkgs/main/win-64::matplotlib-3.4.3-py39haa95532_0
  matplotlib-base    pkgs/main/win-64::matplotlib-base-3.4.3-py39h49ac443_0
  matplotlib-inline  pkgs/main/noarch::matplotlib-inline-0.1.2-pyhd3eb1b0_2
  mccabe             pkgs/main/win-64::mccabe-0.6.1-py39haa95532_1
  menuinst           pkgs/main/win-64::menuinst-1.4.18-py39h59b6b97_0
  mistune            pkgs/main/win-64::mistune-0.8.4-py39h2bbff1b_1000
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  mock               pkgs/main/noarch::mock-4.0.3-pyhd3eb1b0_0
  more-itertools     pkgs/main/noarch::more-itertools-8.10.0-pyhd3eb1b0_0
  mpmath             pkgs/main/win-64::mpmath-1.2.1-py39haa95532_0
  msgpack-python     pkgs/main/win-64::msgpack-python-1.0.2-py39h59b6b97_1
  msys2-conda-epoch  pkgs/msys2/win-64::msys2-conda-epoch-20160418-1
  multipledispatch   pkgs/main/win-64::multipledispatch-0.6.0-py39haa95532_0
  munkres            pkgs/main/noarch::munkres-1.1.4-py_0
  mypy_extensions    pkgs/main/win-64::mypy_extensions-0.4.3-py39haa95532_0
  nbclassic          pkgs/main/noarch::nbclassic-0.2.6-pyhd3eb1b0_0
  nbclient           pkgs/main/noarch::nbclient-0.5.3-pyhd3eb1b0_0
  nbconvert          pkgs/main/win-64::nbconvert-6.1.0-py39haa95532_0
  nbformat           pkgs/main/noarch::nbformat-5.1.3-pyhd3eb1b0_0
  nest-asyncio       pkgs/main/noarch::nest-asyncio-1.5.1-pyhd3eb1b0_0
  networkx           pkgs/main/noarch::networkx-2.6.3-pyhd3eb1b0_0
  nltk               pkgs/main/noarch::nltk-3.6.5-pyhd3eb1b0_0
  nose               pkgs/main/noarch::nose-1.3.7-pyhd3eb1b0_1006
  notebook           pkgs/main/win-64::notebook-6.4.5-py39haa95532_0
  numba              pkgs/main/win-64::numba-0.54.1-py39hf11a4ad_0
  numexpr            pkgs/main/win-64::numexpr-2.7.3-py39hb80d3ca_1
  numpy              pkgs/main/win-64::numpy-1.20.3-py39ha4e8547_0
  numpy-base         pkgs/main/win-64::numpy-base-1.20.3-py39hc2deb75_0
  numpydoc           pkgs/main/noarch::numpydoc-1.1.0-pyhd3eb1b0_1
  olefile            pkgs/main/noarch::olefile-0.46-pyhd3eb1b0_0
  openjpeg           pkgs/main/win-64::openjpeg-2.4.0-h4fc8c34_0
  openpyxl           pkgs/main/noarch::openpyxl-3.0.9-pyhd3eb1b0_0
  openssl            pkgs/main/win-64::openssl-1.1.1l-h2bbff1b_0
  packaging          pkgs/main/noarch::packaging-21.0-pyhd3eb1b0_0
  pandas             pkgs/main/win-64::pandas-1.3.4-py39h6214cd6_0
  pandocfilters      pkgs/main/win-64::pandocfilters-1.4.3-py39haa95532_1
  paramiko           pkgs/main/noarch::paramiko-2.7.2-py_0
  parso              pkgs/main/noarch::parso-0.8.2-pyhd3eb1b0_0
  partd              pkgs/main/noarch::partd-1.2.0-pyhd3eb1b0_0
  path               pkgs/main/win-64::path-16.0.0-py39haa95532_0
  path.py            pkgs/main/noarch::path.py-12.5.0-hd3eb1b0_0
  pathlib2           pkgs/main/win-64::pathlib2-2.3.6-py39haa95532_2
  pathspec           pkgs/main/noarch::pathspec-0.7.0-py_0
  patsy              pkgs/main/win-64::patsy-0.5.2-py39haa95532_0
  pep8               pkgs/main/win-64::pep8-1.7.1-py39haa95532_0
  pexpect            pkgs/main/noarch::pexpect-4.8.0-pyhd3eb1b0_3
  pickleshare        pkgs/main/noarch::pickleshare-0.7.5-pyhd3eb1b0_1003
  pillow             pkgs/main/win-64::pillow-8.4.0-py39hd45dc43_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  pkginfo            pkgs/main/win-64::pkginfo-1.7.1-py39haa95532_0
  pluggy             pkgs/main/win-64::pluggy-0.13.1-py39haa95532_0
  ply                pkgs/main/win-64::ply-3.11-py39haa95532_0
  powershell_shortc~ pkgs/main/win-64::powershell_shortcut-0.0.1-3
  poyo               pkgs/main/noarch::poyo-0.5.0-pyhd3eb1b0_0
  prometheus_client  pkgs/main/noarch::prometheus_client-0.11.0-pyhd3eb1b0_0
  prompt-toolkit     pkgs/main/noarch::prompt-toolkit-3.0.20-pyhd3eb1b0_0
  prompt_toolkit     pkgs/main/noarch::prompt_toolkit-3.0.20-hd3eb1b0_0
  psutil             pkgs/main/win-64::psutil-5.8.0-py39h2bbff1b_1
  ptyprocess         pkgs/main/noarch::ptyprocess-0.7.0-pyhd3eb1b0_2
  py                 pkgs/main/noarch::py-1.10.0-pyhd3eb1b0_0
  py-lief            pkgs/main/win-64::py-lief-0.10.1-py39hd77b12b_1
  pycodestyle        pkgs/main/noarch::pycodestyle-2.7.0-pyhd3eb1b0_0
  pycosat            pkgs/main/win-64::pycosat-0.6.3-py39h2bbff1b_0
  pycparser          pkgs/main/noarch::pycparser-2.20-py_2
  pycurl             pkgs/main/win-64::pycurl-7.44.1-py39hcd4344a_1
  pydocstyle         pkgs/main/noarch::pydocstyle-6.1.1-pyhd3eb1b0_0
  pyerfa             pkgs/main/win-64::pyerfa-2.0.0-py39h2bbff1b_0
  pyflakes           pkgs/main/noarch::pyflakes-2.3.1-pyhd3eb1b0_0
  pygments           pkgs/main/noarch::pygments-2.10.0-pyhd3eb1b0_0
  pylint             pkgs/main/win-64::pylint-2.9.6-py39haa95532_1
  pyls-spyder        pkgs/main/noarch::pyls-spyder-0.4.0-pyhd3eb1b0_0
  pynacl             pkgs/main/win-64::pynacl-1.4.0-py39hbd8134f_1
  pyodbc             pkgs/main/win-64::pyodbc-4.0.31-py39hd77b12b_0
  pyopenssl          pkgs/main/noarch::pyopenssl-21.0.0-pyhd3eb1b0_1
  pyparsing          pkgs/main/noarch::pyparsing-3.0.4-pyhd3eb1b0_0
  pyqt               pkgs/main/win-64::pyqt-5.9.2-py39hd77b12b_6
  pyreadline         pkgs/main/win-64::pyreadline-2.1-py39haa95532_1
  pyrsistent         pkgs/main/win-64::pyrsistent-0.18.0-py39h196d8e1_0
  pysocks            pkgs/main/win-64::pysocks-1.7.1-py39haa95532_0
  pytables           pkgs/main/win-64::pytables-3.6.1-py39h56d22b6_1
  pytest             pkgs/main/win-64::pytest-6.2.4-py39haa95532_2
  python             pkgs/main/win-64::python-3.9.7-h6244533_1
  python-dateutil    pkgs/main/noarch::python-dateutil-2.8.2-pyhd3eb1b0_0
  python-libarchive~ pkgs/main/noarch::python-libarchive-c-2.9-pyhd3eb1b0_1
  python-lsp-black   pkgs/main/noarch::python-lsp-black-1.0.0-pyhd3eb1b0_0
  python-lsp-jsonrpc pkgs/main/noarch::python-lsp-jsonrpc-1.0.0-pyhd3eb1b0_0
  python-lsp-server  pkgs/main/noarch::python-lsp-server-1.2.4-pyhd3eb1b0_0
  python-slugify     pkgs/main/noarch::python-slugify-5.0.2-pyhd3eb1b0_0
  pytz               pkgs/main/noarch::pytz-2021.3-pyhd3eb1b0_0
  pywavelets         pkgs/main/win-64::pywavelets-1.1.1-py39h080aedc_4
  pywin32            pkgs/main/win-64::pywin32-228-py39he774522_0
  pywin32-ctypes     pkgs/main/win-64::pywin32-ctypes-0.2.0-py39haa95532_1000
  pywinpty           pkgs/main/win-64::pywinpty-0.5.7-py39haa95532_0
  pyyaml             pkgs/main/win-64::pyyaml-6.0-py39h2bbff1b_1
  pyzmq              pkgs/main/win-64::pyzmq-22.2.1-py39hd77b12b_1
  qdarkstyle         pkgs/main/noarch::qdarkstyle-3.0.2-pyhd3eb1b0_0
  qstylizer          pkgs/main/noarch::qstylizer-0.1.10-pyhd3eb1b0_0
  qt                 pkgs/main/win-64::qt-5.9.7-vc14h73c81de_0
  qtawesome          pkgs/main/noarch::qtawesome-1.0.2-pyhd3eb1b0_0
  qtconsole          pkgs/main/noarch::qtconsole-5.1.1-pyhd3eb1b0_0
  qtpy               pkgs/main/noarch::qtpy-1.10.0-pyhd3eb1b0_0
  regex              pkgs/main/win-64::regex-2021.8.3-py39h2bbff1b_0
  requests           pkgs/main/noarch::requests-2.26.0-pyhd3eb1b0_0
  rope               pkgs/main/noarch::rope-0.19.0-pyhd3eb1b0_0
  rtree              pkgs/main/win-64::rtree-0.9.7-py39h2eaa2aa_1
  ruamel_yaml        pkgs/main/win-64::ruamel_yaml-0.15.100-py39h2bbff1b_0
  scikit-image       pkgs/main/win-64::scikit-image-0.18.3-py39hf11a4ad_0
  scikit-learn       pkgs/main/win-64::scikit-learn-0.24.2-py39hf11a4ad_1
  scikit-learn-inte~ pkgs/main/win-64::scikit-learn-intelex-2021.3.0-py39haa95532_0
  scipy              pkgs/main/win-64::scipy-1.7.1-py39hbe87c03_2
  seaborn            pkgs/main/noarch::seaborn-0.11.2-pyhd3eb1b0_0
  send2trash         pkgs/main/noarch::send2trash-1.8.0-pyhd3eb1b0_1
  setuptools         pkgs/main/win-64::setuptools-58.0.4-py39haa95532_0
  simplegeneric      pkgs/main/win-64::simplegeneric-0.8.1-py39haa95532_2
  singledispatch     pkgs/main/noarch::singledispatch-3.7.0-pyhd3eb1b0_1001
  sip                pkgs/main/win-64::sip-4.19.13-py39hd77b12b_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_0
  snappy             pkgs/main/win-64::snappy-1.1.8-h33f27b4_0
  sniffio            pkgs/main/win-64::sniffio-1.2.0-py39haa95532_1
  snowballstemmer    pkgs/main/noarch::snowballstemmer-2.1.0-pyhd3eb1b0_0
  sortedcollections  pkgs/main/noarch::sortedcollections-2.1.0-pyhd3eb1b0_0
  sortedcontainers   pkgs/main/noarch::sortedcontainers-2.4.0-pyhd3eb1b0_0
  soupsieve          pkgs/main/noarch::soupsieve-2.2.1-pyhd3eb1b0_0
  sphinx             pkgs/main/noarch::sphinx-4.2.0-pyhd3eb1b0_1
  sphinxcontrib      pkgs/main/win-64::sphinxcontrib-1.0-py39haa95532_1
  sphinxcontrib-app~ pkgs/main/noarch::sphinxcontrib-applehelp-1.0.2-pyhd3eb1b0_0
  sphinxcontrib-dev~ pkgs/main/noarch::sphinxcontrib-devhelp-1.0.2-pyhd3eb1b0_0
  sphinxcontrib-htm~ pkgs/main/noarch::sphinxcontrib-htmlhelp-2.0.0-pyhd3eb1b0_0
  sphinxcontrib-jsm~ pkgs/main/noarch::sphinxcontrib-jsmath-1.0.1-pyhd3eb1b0_0
  sphinxcontrib-qth~ pkgs/main/noarch::sphinxcontrib-qthelp-1.0.3-pyhd3eb1b0_0
  sphinxcontrib-ser~ pkgs/main/noarch::sphinxcontrib-serializinghtml-1.1.5-pyhd3eb1b0_0
  sphinxcontrib-web~ pkgs/main/noarch::sphinxcontrib-websupport-1.2.4-py_0
  spyder             pkgs/main/win-64::spyder-5.1.5-py39haa95532_1
  spyder-kernels     pkgs/main/win-64::spyder-kernels-2.1.3-py39haa95532_0
  sqlalchemy         pkgs/main/win-64::sqlalchemy-1.4.22-py39h2bbff1b_0
  sqlite             pkgs/main/win-64::sqlite-3.36.0-h2bbff1b_0
  statsmodels        pkgs/main/win-64::statsmodels-0.12.2-py39h2bbff1b_0
  sympy              pkgs/main/win-64::sympy-1.9-py39haa95532_0
  tbb                pkgs/main/win-64::tbb-2021.4.0-h59b6b97_0
  tbb4py             pkgs/main/win-64::tbb4py-2021.4.0-py39h59b6b97_0
  tblib              pkgs/main/noarch::tblib-1.7.0-pyhd3eb1b0_0
  terminado          pkgs/main/win-64::terminado-0.9.4-py39haa95532_0
  testpath           pkgs/main/noarch::testpath-0.5.0-pyhd3eb1b0_0
  text-unidecode     pkgs/main/noarch::text-unidecode-1.3-pyhd3eb1b0_0
  textdistance       pkgs/main/noarch::textdistance-4.2.1-pyhd3eb1b0_0
  threadpoolctl      pkgs/main/noarch::threadpoolctl-2.2.0-pyh0d69192_0
  three-merge        pkgs/main/noarch::three-merge-0.1.1-pyhd3eb1b0_0
  tifffile           pkgs/main/noarch::tifffile-2021.7.2-pyhd3eb1b0_2
  tinycss            pkgs/main/noarch::tinycss-0.4-pyhd3eb1b0_1002
  tk                 pkgs/main/win-64::tk-8.6.11-h2bbff1b_0
  toml               pkgs/main/noarch::toml-0.10.2-pyhd3eb1b0_0
  toolz              pkgs/main/noarch::toolz-0.11.1-pyhd3eb1b0_0
  tornado            pkgs/main/win-64::tornado-6.1-py39h2bbff1b_0
  tqdm               pkgs/main/noarch::tqdm-4.62.3-pyhd3eb1b0_1
  traitlets          pkgs/main/noarch::traitlets-5.1.0-pyhd3eb1b0_0
  typed-ast          pkgs/main/win-64::typed-ast-1.4.3-py39h2bbff1b_1
  typing_extensions  pkgs/main/noarch::typing_extensions-3.10.0.2-pyh06a4308_0
  tzdata             pkgs/main/noarch::tzdata-2021e-hda174b7_0
  ujson              pkgs/main/win-64::ujson-4.0.2-py39hd77b12b_0
  unicodecsv         pkgs/main/win-64::unicodecsv-0.14.1-py39haa95532_0
  unidecode          pkgs/main/noarch::unidecode-1.2.0-pyhd3eb1b0_0
  urllib3            pkgs/main/noarch::urllib3-1.26.7-pyhd3eb1b0_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  watchdog           pkgs/main/win-64::watchdog-2.1.3-py39haa95532_0
  wcwidth            pkgs/main/noarch::wcwidth-0.2.5-pyhd3eb1b0_0
  webencodings       pkgs/main/win-64::webencodings-0.5.1-py39haa95532_1
  werkzeug           pkgs/main/noarch::werkzeug-2.0.2-pyhd3eb1b0_0
  wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
  whichcraft         pkgs/main/noarch::whichcraft-0.6.1-pyhd3eb1b0_0
  widgetsnbextension pkgs/main/win-64::widgetsnbextension-3.5.1-py39haa95532_0
  win_inet_pton      pkgs/main/win-64::win_inet_pton-1.1.0-py39haa95532_0
  win_unicode_conso~ pkgs/main/win-64::win_unicode_console-0.5-py39haa95532_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2
  winpty             pkgs/main/win-64::winpty-0.4.3-4
  wrapt              pkgs/main/win-64::wrapt-1.12.1-py39h196d8e1_1
  xlrd               pkgs/main/noarch::xlrd-2.0.1-pyhd3eb1b0_0
  xlsxwriter         pkgs/main/noarch::xlsxwriter-3.0.1-pyhd3eb1b0_0
  xlwings            pkgs/main/win-64::xlwings-0.24.9-py39haa95532_0
  xlwt               pkgs/main/win-64::xlwt-1.3.0-py39haa95532_0
  xz                 pkgs/main/win-64::xz-5.2.5-h62dcd97_0
  yaml               pkgs/main/win-64::yaml-0.2.5-he774522_0
  yapf               pkgs/main/noarch::yapf-0.31.0-pyhd3eb1b0_0
  zfp                pkgs/main/win-64::zfp-0.5.5-hd77b12b_6
  zict               pkgs/main/noarch::zict-2.0.0-pyhd3eb1b0_0
  zipp               pkgs/main/noarch::zipp-3.6.0-pyhd3eb1b0_0
  zlib               pkgs/main/win-64::zlib-1.2.11-h62dcd97_4
  zope               pkgs/main/win-64::zope-1.0-py39haa95532_1
  zope.event         pkgs/main/win-64::zope.event-4.5.0-py39haa95532_0
  zope.interface     pkgs/main/win-64::zope.interface-5.4.0-py39h2bbff1b_0
  zstd               pkgs/main/win-64::zstd-1.4.9-h19a0ad4_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
openjpeg-2.4.0       | 219 KB    | ############################################################################ | 100%
msgpack-python-1.0.2 | 76 KB     | ############################################################################ | 100%
idna-3.2             | 48 KB     | ############################################################################ | 100%
snowballstemmer-2.1. | 62 KB     | ############################################################################ | 100%
typing_extensions-3. | 31 KB     | ############################################################################ | 100%
ipykernel-6.4.1      | 195 KB    | ############################################################################ | 100%
icu-58.2             | 9.4 MB    | ############################################################################ | 100%
charset-normalizer-2 | 35 KB     | ############################################################################ | 100%
jedi-0.18.0          | 912 KB    | ############################################################################ | 100%
pycparser-2.20       | 94 KB     | ############################################################################ | 100%
python-slugify-5.0.2 | 13 KB     | ############################################################################ | 100%
itsdangerous-2.0.1   | 18 KB     | ############################################################################ | 100%
pep8-1.7.1           | 71 KB     | ############################################################################ | 100%
backcall-0.2.0       | 13 KB     | ############################################################################ | 100%
jupyterlab_widgets-1 | 109 KB    | ############################################################################ | 100%
python-lsp-black-1.0 | 8 KB      | ############################################################################ | 100%
ipython_genutils-0.2 | 27 KB     | ############################################################################ | 100%
regex-2021.8.3       | 301 KB    | ############################################################################ | 100%
requests-2.26.0      | 59 KB     | ############################################################################ | 100%
greenlet-1.1.1       | 82 KB     | ############################################################################ | 100%
pywin32-228          | 5.6 MB    | ############################################################################ | 100%
cached-property-1.5. | 11 KB     | ############################################################################ | 100%
pywinpty-0.5.7       | 51 KB     | ############################################################################ | 100%
cfitsio-3.470        | 512 KB    | ############################################################################ | 100%
partd-1.2.0          | 19 KB     | ############################################################################ | 100%
tbb4py-2021.4.0      | 72 KB     | ############################################################################ | 100%
m2w64-gmp-6.1.0      | 689 KB    | ############################################################################ | 100%
win_unicode_console- | 35 KB     | ############################################################################ | 100%
black-19.10b0        | 86 KB     | ############################################################################ | 100%
jupyterlab-3.2.1     | 3.6 MB    | ############################################################################ | 100%
numba-0.54.1         | 3.3 MB    | ############################################################################ | 100%
yaml-0.2.5           | 62 KB     | ############################################################################ | 100%
defusedxml-0.7.1     | 23 KB     | ############################################################################ | 100%
mock-4.0.3           | 29 KB     | ############################################################################ | 100%
arrow-0.13.1         | 83 KB     | ############################################################################ | 100%
pexpect-4.8.0        | 53 KB     | ############################################################################ | 100%
libwebp-1.2.0        | 643 KB    | ############################################################################ | 100%
imagesize-1.2.0      | 9 KB      | ############################################################################ | 100%
nbformat-5.1.3       | 44 KB     | ############################################################################ | 100%
icc_rt-2019.0.0      | 6.0 MB    | ############################################################################ | 100%
sip-4.19.13          | 262 KB    | ############################################################################ | 100%
html5lib-1.1         | 91 KB     | ############################################################################ | 100%
bokeh-2.4.1          | 7.6 MB    | ############################################################################ | 100%
mkl-service-2.4.0    | 51 KB     | ############################################################################ | 100%
xlrd-2.0.1           | 90 KB     | ############################################################################ | 100%
bitarray-2.3.0       | 142 KB    | ############################################################################ | 100%
zlib-1.2.11          | 113 KB    | ############################################################################ | 100%
text-unidecode-1.3   | 65 KB     | ############################################################################ | 100%
hdf5-1.10.6          | 7.9 MB    | ############################################################################ | 100%
libzopfli-1.0.3      | 176 KB    | ############################################################################ | 100%
json5-0.9.6          | 21 KB     | ############################################################################ | 100%
pathspec-0.7.0       | 26 KB     | ############################################################################ | 100%
tornado-6.1          | 598 KB    | ############################################################################ | 100%
intel-openmp-2021.4. | 2.2 MB    | ############################################################################ | 100%
paramiko-2.7.2       | 143 KB    | ############################################################################ | 100%
libspatialindex-1.9. | 351 KB    | ############################################################################ | 100%
widgetsnbextension-3 | 867 KB    | ############################################################################ | 100%
zstd-1.4.9           | 478 KB    | ############################################################################ | 100%
rope-0.19.0          | 126 KB    | ############################################################################ | 100%
jdcal-1.4.1          | 10 KB     | ############################################################################ | 100%
cloudpickle-2.0.0    | 32 KB     | ############################################################################ | 100%
unidecode-1.2.0      | 155 KB    | ############################################################################ | 100%
python-3.9.7         | 16.5 MB   | ############################################################################ | 100%
wincertstore-0.2     | 15 KB     | ############################################################################ | 100%
singledispatch-3.7.0 | 12 KB     | ############################################################################ | 100%
anaconda-project-0.1 | 218 KB    | ############################################################################ | 100%
certifi-2021.10.8    | 152 KB    | ############################################################################ | 100%
libiconv-1.15        | 626 KB    | ############################################################################ | 100%
anaconda-2021.11     | 18 KB     | ############################################################################ | 100%
markupsafe-1.1.1     | 56 KB     | ############################################################################ | 100%
numpy-1.20.3         | 23 KB     | ############################################################################ | 100%
pycurl-7.44.1        | 68 KB     | ############################################################################ | 100%
libarchive-3.4.2     | 1.7 MB    | ############################################################################ | 100%
tblib-1.7.0          | 15 KB     | ############################################################################ | 100%
pynacl-1.4.0         | 1.3 MB    | ############################################################################ | 100%
qtpy-1.10.0          | 35 KB     | ############################################################################ | 100%
sphinxcontrib-htmlhe | 32 KB     | ############################################################################ | 100%
numexpr-2.7.3        | 126 KB    | ############################################################################ | 100%
openssl-1.1.1l       | 4.8 MB    | ############################################################################ | 100%
wcwidth-0.2.5        | 26 KB     | ############################################################################ | 100%
networkx-2.6.3       | 1.3 MB    | ############################################################################ | 100%
argon2-cffi-20.1.0   | 49 KB     | ############################################################################ | 100%
send2trash-1.8.0     | 19 KB     | ############################################################################ | 100%
pyopenssl-21.0.0     | 49 KB     | ############################################################################ | 100%
webencodings-0.5.1   | 20 KB     | ############################################################################ | 100%
pillow-8.4.0         | 906 KB    | ############################################################################ | 100%
flask-1.1.2          | 70 KB     | ############################################################################ | 100%
path.py-12.5.0       | 4 KB      | ############################################################################ | 100%
sqlalchemy-1.4.22    | 1.8 MB    | ############################################################################ | 100%
tbb-2021.4.0         | 148 KB    | ############################################################################ | 100%
powershell_shortcut- | 277 KB    | ############################################################################ | 100%
scipy-1.7.1          | 13.8 MB   | ############################################################################ | 100%
lz4-c-1.9.3          | 132 KB    | ############################################################################ | 100%
clyent-1.2.2         | 21 KB     | ############################################################################ | 100%
diff-match-patch-202 | 35 KB     | ############################################################################ | 100%
m2w64-libwinpthread- | 30 KB     | ############################################################################ | 100%
bzip2-1.0.8          | 113 KB    | ############################################################################ | 100%
statsmodels-0.12.2   | 8.2 MB    | ############################################################################ | 100%
cffi-1.14.6          | 224 KB    | ############################################################################ | 100%
sphinxcontrib-jsmath | 8 KB      | ############################################################################ | 100%
toolz-0.11.1         | 46 KB     | ############################################################################ | 100%
patsy-0.5.2          | 274 KB    | ############################################################################ | 100%
libaec-1.0.4         | 31 KB     | ############################################################################ | 100%
pip-21.2.4           | 1.8 MB    | ############################################################################ | 100%
pycosat-0.6.3        | 75 KB     | ############################################################################ | 100%
dal-2021.3.0         | 24.4 MB   | ############################################################################ | 100%
simplegeneric-0.8.1  | 11 KB     | ############################################################################ | 100%
anaconda-client-1.9. | 170 KB    | ############################################################################ | 100%
pywavelets-1.1.1     | 3.4 MB    | ############################################################################ | 100%
pyqt-5.9.2           | 3.3 MB    | ################################################3                            |  64%
appdirs-1.4.4        | 12 KB     | ############################################################################ | 100%
parso-0.8.2          | 69 KB     | ############################################################################ | 100%
brotlipy-0.7.0       | 411 KB    | ############################################################################ | 100%
python-lsp-jsonrpc-1 | 10 KB     | ############################################################################ | 100%
pyflakes-2.3.1       | 60 KB     | ############################################################################ | 100%
sphinxcontrib-devhel | 23 KB     | ############################################################################ | 100%
matplotlib-inline-0. | 12 KB     | ############################################################################ | 100%
fastcache-1.1.0      | 57 KB     | ############################################################################ | 100%
jsonschema-3.2.0     | 47 KB     | ############################################################################ | 100%
kiwisolver-1.3.1     | 52 KB     | ############################################################################ | 100%
chardet-4.0.0        | 212 KB    | ############################################################################ | 100%
tqdm-4.62.3          | 83 KB     | ############################################################################ | 100%
prompt_toolkit-3.0.2 | 12 KB     | ############################################################################ | 100%
jpeg-9d              | 283 KB    | ############################################################################ | 100%
zope.interface-5.4.0 | 304 KB    | ############################################################################ | 100%
contextlib2-0.6.0.po | 13 KB     | ############################################################################ | 100%
m2w64-gcc-libgfortra | 340 KB    | ############################################################################ | 100%
sympy-1.9            | 9.2 MB    | ############################################################################ | 100%
more-itertools-8.10. | 47 KB     | ############################################################################ | 100%
openpyxl-3.0.9       | 164 KB    | ############################################################################ | 100%
qstylizer-0.1.10     | 17 KB     | ############################################################################ | 100%
xlwt-1.3.0           | 160 KB    | ############################################################################ | 100%
intervaltree-3.1.0   | 25 KB     | ############################################################################ | 100%
conda-token-0.3.0    | 10 KB     | ############################################################################ | 100%
boto-2.49.0          | 1.5 MB    | ############################################################################ | 100%
pickleshare-0.7.5    | 13 KB     | ############################################################################ | 100%
urllib3-1.26.7       | 111 KB    | ############################################################################ | 100%
nbclient-0.5.3       | 62 KB     | ############################################################################ | 100%
pathlib2-2.3.6       | 37 KB     | ############################################################################ | 100%
pandocfilters-1.4.3  | 14 KB     | ############################################################################ | 100%
qdarkstyle-3.0.2     | 337 KB    | ############################################################################ | 100%
sphinxcontrib-serial | 25 KB     | ############################################################################ | 100%
gevent-21.8.0        | 1.4 MB    | ############################################################################ | 100%
tzdata-2021e         | 112 KB    | ############################################################################ | 100%
scikit-learn-0.24.2  | 4.9 MB    | ############################################################################ | 100%
typed-ast-1.4.3      | 137 KB    | ############################################################################ | 100%
attrs-21.2.0         | 46 KB     | ############################################################################ | 100%
pyls-spyder-0.4.0    | 11 KB     | ############################################################################ | 100%
threadpoolctl-2.2.0  | 16 KB     | ############################################################################ | 100%
three-merge-0.1.1    | 10 KB     | ############################################################################ | 100%
fsspec-2021.10.1     | 96 KB     | ############################################################################ | 100%
bleach-4.0.0         | 113 KB    |                                                                              |   0%
imagecodecs-2021.8.2 | 6.2 MB    |                                                                              |   0%
astropy-4.3.1        | 6.1 MB    |                                                                              |   0%
watchdog-2.1.3       | 109 KB    |                                                                              |   0%
textdistance-4.2.1   | 29 KB     |                                                                              |   0%
autopep8-1.5.7       | 43 KB     |                                                                              |   0%
alabaster-0.7.12     | 16 KB     |                                                                              |   0%
qtawesome-1.0.2      | 760 KB    |                                                                              |   0%
pysocks-1.7.1        | 55 KB     |                                                                              |   0%
six-1.16.0           | 18 KB     |                                                                              |   0%
scikit-image-0.18.3  | 9.1 MB    |                                                                              |   0%
cookiecutter-1.7.2   | 86 KB     |                                                                              |   0%
lxml-4.6.3           | 978 KB    |                                                                              |   0%
keyring-23.1.0       | 78 KB     |                                                                              |   0%
backports-1.0        | 210 KB    |                                                                              |   0%
matplotlib-base-3.4. | 5.5 MB    |                                                                              |   0%
zict-2.0.0           | 10 KB     |                                                                              |   0%
sphinxcontrib-1.0    | 218 KB    |                                                                              |   0%
sphinxcontrib-qthelp | 26 KB     |                                                                              |   0%
pygments-2.10.0      | 725 KB    |                                                                              |   0%
filelock-3.3.1       | 12 KB     |                                                                              |   0%
poyo-0.5.0           | 17 KB     |                                                                              |   0%
bcrypt-3.2.0         | 139 KB    |                                                                              |   0%
libssh2-1.9.0        | 215 KB    |                                                                              |   0%
python-libarchive-c- | 47 KB     |                                                                              |   0%
asn1crypto-1.4.0     | 80 KB     |                                                                              |   0%
krb5-1.19.2          | 697 KB    |                                                                              |   0%
libxslt-1.1.34       | 399 KB    |                                                                              |   0%
pyzmq-22.2.1         | 620 KB    |                                                                              |   0%
libtiff-4.2.0        | 786 KB    |                                                                              |   0%
zfp-0.5.5            | 139 KB    |                                                                              |   0%
packaging-21.0       | 36 KB     |                                                                              |   0%
anyio-2.2.0          | 125 KB    |                                                                              |   0%
vs2015_runtime-14.27 | 1007 KB   | ############################################################################ | 100%
scikit-learn-intelex | 38 KB     | ############################################################################ | 100%
mccabe-0.6.1         | 16 KB     | ############################################################################ | 100%
mkl_fft-1.3.1        | 139 KB    | ############################################################################ | 100%
dataclasses-0.8      | 8 KB      | ############################################################################ | 100%
pkginfo-1.7.1        | 60 KB     | ############################################################################ | 100%
liblief-0.10.1       | 1.6 MB    | ############################################################################ | 100%
comtypes-1.1.10      | 239 KB    | ############################################################################ | 100%
pywin32-ctypes-0.2.0 | 40 KB     | ############################################################################ | 100%
rtree-0.9.7          | 49 KB     | ############################################################################ | 100%
xlwings-0.24.9       | 894 KB    | ############################################################################ | 100%
nltk-3.6.5           | 979 KB    | ############################################################################ | 100%
win_inet_pton-1.1.0  | 35 KB     | ############################################################################ | 100%
terminado-0.9.4      | 26 KB     | ############################################################################ | 100%
prompt-toolkit-3.0.2 | 259 KB    | ############################################################################ | 100%
daal4py-2021.3.0     | 7.6 MB    | ############################################################################ | 100%
beautifulsoup4-4.10. | 85 KB     | ############################################################################ | 100%
glob2-0.7            | 12 KB     | ############################################################################ | 100%
locket-0.2.1         | 10 KB     | ############################################################################ | 100%
pandas-1.3.4         | 8.6 MB    | ############################################################################ | 100%
brotli-1.0.9         | 332 KB    | ############################################################################ | 100%
blosc-1.21.0         | 139 KB    | ############################################################################ | 100%
debugpy-1.4.1        | 2.6 MB    | ############################################################################ | 100%
pytest-6.2.4         | 445 KB    | ############################################################################ | 100%
jinja2-2.11.3        | 101 KB    | ############################################################################ | 100%
astroid-2.6.6        | 313 KB    | ############################################################################ | 100%
ptyprocess-0.7.0     | 17 KB     | ############################################################################ | 100%
heapdict-1.0.1       | 8 KB      | ############################################################################ | 100%
jupyterlab_pygments- | 8 KB      | ############################################################################ | 100%
fonttools-4.25.0     | 632 KB    | ############################################################################ | 100%
h5py-3.2.1           | 872 KB    | ############################################################################ | 100%
cryptography-3.4.8   | 638 KB    | ############################################################################ | 100%
lzo-2.10             | 142 KB    | ############################################################################ | 100%
entrypoints-0.3      | 12 KB     | ############################################################################ | 100%
importlib_metadata-4 | 11 KB     | ############################################################################ | 100%
giflib-5.2.1         | 81 KB     | ############################################################################ | 100%
python-lsp-server-1. | 41 KB     | ############################################################################ | 100%
py-lief-0.10.1       | 1.1 MB    | ############################################################################ | 100%
zipp-3.6.0           | 17 KB     | ############################################################################ | 100%
setuptools-58.0.4    | 778 KB    | ############################################################################ | 100%
ply-3.11             | 81 KB     | ############################################################################ | 100%
mypy_extensions-0.4. | 10 KB     | ############################################################################ | 100%
lazy-object-proxy-1. | 31 KB     | ############################################################################ | 100%
zope-1.0             | 218 KB    | ############################################################################ | 100%
flake8-3.9.2         | 129 KB    | ############################################################################ | 100%
docutils-0.17.1      | 693 KB    | ############################################################################ | 100%
libdeflate-1.8       | 46 KB     | ############################################################################ | 100%
jupyter_core-4.8.1   | 91 KB     | ############################################################################ | 100%
sqlite-3.36.0        | 780 KB    | ############################################################################ | 100%
nbconvert-6.1.0      | 501 KB    | ############################################################################ | 100%
charls-2.2.0         | 82 KB     | ############################################################################ | 100%
zope.event-4.5.0     | 223 KB    | ############################################################################ | 100%
pyerfa-2.0.0         | 359 KB    | ############################################################################ | 100%
imageio-2.9.0        | 3.0 MB    | ############################################################################ | 100%
soupsieve-2.2.1      | 32 KB     | ############################################################################ | 100%
yapf-0.31.0          | 126 KB    | ############################################################################ | 100%
pylint-2.9.6         | 505 KB    | ############################################################################ | 100%
tinycss-0.4          | 39 KB     | ############################################################################ | 100%
snappy-1.1.8         | 80 KB     | ############################################################################ | 100%
spyder-5.1.5         | 9.4 MB    | ############################################################################ | 100%
munkres-1.1.4        | 13 KB     | ############################################################################ | 100%
pytables-3.6.1       | 1.1 MB    | ############################################################################ | 100%
traitlets-5.1.0      | 89 KB     | ############################################################################ | 100%
jupyterlab_server-2. | 46 KB     | ############################################################################ | 100%
unicodecsv-0.14.1    | 28 KB     | ############################################################################ | 100%
libcurl-7.78.0       | 294 KB    | ############################################################################ | 100%
mpmath-1.2.1         | 773 KB    | ############################################################################ | 100%
libpng-1.6.37        | 333 KB    | ############################################################################ | 100%
olefile-0.46         | 34 KB     | ############################################################################ | 100%
babel-2.9.1          | 5.5 MB    | ###6                                                                         |   5%
psutil-5.8.0         | 348 KB    |                                                                              |   0%
prometheus_client-0. | 47 KB     |                                                                              |   0%
ujson-4.0.2          | 46 KB     |                                                                              |   0%
dask-2021.10.0       | 19 KB     |                                                                              |   0%
pyparsing-3.0.4      | 81 KB     | ############################################################################ | 100%
spyder-kernels-2.1.3 | 112 KB    | ############################################################################ | 100%
pydocstyle-6.1.1     | 36 KB     | ############################################################################ | 100%
pytz-2021.3          | 171 KB    | ############################################################################ | 100%
curl-7.78.0          | 132 KB    | ############################################################################ | 100%
jupyter_client-6.1.1 | 88 KB     | ############################################################################ | 100%
lerc-3.0             | 120 KB    | ############################################################################ | 100%
libxml2-2.9.12       | 1.5 MB    | ############################################################################ | 100%
jupyter_console-6.4. | 23 KB     | ############################################################################ | 100%
wrapt-1.12.1         | 73 KB     | ############################################################################ | 100%
inflection-0.5.1     | 12 KB     | ############################################################################ | 100%
menuinst-1.4.18      | 96 KB     | ############################################################################ | 100%
atomicwrites-1.4.0   | 11 KB     | ############################################################################ | 100%
conda-pack-0.6.0     | 29 KB     | ############################################################################ | 100%
cytoolz-0.11.0       | 294 KB    | ############################################################################ | 100%
blas-1.0             | 6 KB      | ############################################################################ | 100%
qtconsole-5.1.1      | 98 KB     | ############################################################################ | 100%
mkl-2021.4.0         | 114.9 MB  | ############################################################################ | 100%
seaborn-0.11.2       | 218 KB    | ############################################################################ | 100%
wheel-0.37.0         | 33 KB     | ############################################################################ | 100%
bottleneck-1.3.2     | 107 KB    | ############################################################################ | 100%
nest-asyncio-1.5.1   | 10 KB     | ############################################################################ | 100%
lcms2-2.12           | 454 KB    | ############################################################################ | 100%
xz-5.2.5             | 244 KB    | ############################################################################ | 100%
pyrsistent-0.18.0    | 90 KB     | ############################################################################ | 100%
python-dateutil-2.8. | 233 KB    | ############################################################################ | 100%
mistune-0.8.4        | 57 KB     | ############################################################################ | 100%
notebook-6.4.5       | 4.5 MB    | ############################################################################ | 100%
iniconfig-1.1.1      | 8 KB      | ############################################################################ | 100%
m2w64-gcc-libs-5.3.0 | 518 KB    | ############################################################################ | 100%
argh-0.26.2          | 36 KB     | ############################################################################ | 100%
sphinxcontrib-websup | 34 KB     | ############################################################################ | 100%
tifffile-2021.7.2    | 135 KB    | ############################################################################ | 100%
importlib-metadata-4 | 39 KB     | ############################################################################ | 100%
binaryornot-0.4.4    | 351 KB    | ############################################################################ | 100%
vc-14.2              | 8 KB      | ############################################################################ | 100%
sniffio-1.2.0        | 15 KB     | ############################################################################ | 100%
pyreadline-2.1       | 146 KB    | ############################################################################ | 100%
mkl_random-1.2.2     | 225 KB    | ############################################################################ | 100%
sphinxcontrib-appleh | 29 KB     | ############################################################################ | 100%
cycler-0.10.0        | 16 KB     | ############################################################################ | 100%
ipywidgets-7.6.5     | 105 KB    | ############################################################################ | 100%
pluggy-0.13.1        | 34 KB     | ############################################################################ | 100%
pyodbc-4.0.31        | 68 KB     | ############################################################################ | 100%
freetype-2.10.4      | 466 KB    | ############################################################################ | 100%
jinja2-time-0.2.0    | 17 KB     | ############################################################################ | 100%
jupyter_server-1.4.1 | 328 KB    | ############################################################################ | 100%
get_terminal_size-1. | 3 KB      | ############################################################################ | 100%
click-8.0.3          | 79 KB     | ############################################################################ | 100%
conda-content-trust- | 56 KB     | ############################################################################ | 100%
ipython-7.29.0       | 1.0 MB    | ############################################################################ | 100%
decorator-5.1.0      | 14 KB     | ############################################################################ | 100%
pyyaml-6.0           | 145 KB    | ############################################################################ | 100%
dask-core-2021.10.0  | 718 KB    | ############################################################################ | 100%
sphinx-4.2.0         | 1.2 MB    | ############################################################################ | 100%
et_xmlfile-1.1.0     | 10 KB     | ############################################################################ | 100%
sortedcontainers-2.4 | 26 KB     | ############################################################################ | 100%
qt-5.9.7             | 72.5 MB   | ############################################################################ | 100%
bkcharts-0.2         | 133 KB    | ############################################################################ | 100%
colorama-0.4.4       | 21 KB     | ############################################################################ | 100%
ca-certificates-2021 | 115 KB    | ############################################################################ | 100%
numpydoc-1.1.0       | 42 KB     | ############################################################################ | 100%
sortedcollections-2. | 12 KB     | ############################################################################ | 100%
distributed-2021.10. | 1013 KB   | ############################################################################ | 100%
llvmlite-0.37.0      | 13.3 MB   | ############################################################################ | 100%
pycodestyle-2.7.0    | 41 KB     | ############################################################################ | 100%
numpy-base-1.20.3    | 4.2 MB    | ############################################################################ | 100%
multipledispatch-0.6 | 24 KB     | ############################################################################ | 100%
nbclassic-0.2.6      | 19 KB     | ############################################################################ | 100%
jupyter-1.0.0        | 8 KB      | ############################################################################ | 100%
matplotlib-3.4.3     | 29 KB     | ############################################################################ | 100%
winpty-0.4.3         | 678 KB    | ############################################################################ | 100%
msys2-conda-epoch-20 | 2 KB      | ############################################################################ | 100%
async_generator-1.10 | 23 KB     | ############################################################################ | 100%
console_shortcut-0.1 | 277 KB    | ############################################################################ | 100%
xlsxwriter-3.0.1     | 111 KB    | ############################################################################ | 100%
backports.shutil_get | 10 KB     | ############################################################################ | 100%
joblib-1.1.0         | 211 KB    | ############################################################################ | 100%
cython-0.29.24       | 1.8 MB    | ############################################################################ | 100%
nose-1.3.7           | 128 KB    | ############################################################################ | 100%
tk-8.6.11            | 3.3 MB    | ############################################################################ | 100%
py-1.10.0            | 76 KB     | ############################################################################ | 100%
path-16.0.0          | 38 KB     | ############################################################################ | 100%
m2w64-gcc-libs-core- | 213 KB    | ############################################################################ | 100%
ruamel_yaml-0.15.100 | 273 KB    | ############################################################################ | 100%
testpath-0.5.0       | 81 KB     | ############################################################################ | 100%
whichcraft-0.6.1     | 11 KB     | ############################################################################ | 100%
toml-0.10.2          | 20 KB     | ############################################################################ | 100%
werkzeug-2.0.2       | 224 KB    | ############################################################################ | 100%
isort-5.9.3          | 83 KB     | ############################################################################ | 100%

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/pyqt-5.9.2-py39hd77b12b_6.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/bleach-4.0.0-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/imagecodecs-2021.8.26-py39ha1f97ea_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/astropy-4.3.1-py39hc7d831d_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/watchdog-2.1.3-py39haa95532_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/textdistance-4.2.1-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/autopep8-1.5.7-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/alabaster-0.7.12-pyhd3eb1b0_0.tar.bz2>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/qtawesome-1.0.2-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/pysocks-1.7.1-py39haa95532_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/six-1.16.0-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/scikit-image-0.18.3-py39hf11a4ad_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/cookiecutter-1.7.2-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/lxml-4.6.3-py39h9b66d53_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/keyring-23.1.0-py39haa95532_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/backports-1.0-pyhd3eb1b0_2.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/matplotlib-base-3.4.3-py39h49ac443_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/zict-2.0.0-pyhd3eb1b0_0.tar.bz2>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/sphinxcontrib-1.0-py39haa95532_1.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/sphinxcontrib-qthelp-1.0.3-pyhd3eb1b0_0.tar.bz2>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/pygments-2.10.0-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/filelock-3.3.1-pyhd3eb1b0_1.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/poyo-0.5.0-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/bcrypt-3.2.0-py39h196d8e1_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/libssh2-1.9.0-h7a1dbc1_1.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/python-libarchive-c-2.9-pyhd3eb1b0_1.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/asn1crypto-1.4.0-py_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/krb5-1.19.2-h5b6d351_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/libxslt-1.1.34-he774522_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/pyzmq-22.2.1-py39hd77b12b_1.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/libtiff-4.2.0-hd0e1b90_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/zfp-0.5.5-hd77b12b_6.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/packaging-21.0-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/anyio-2.2.0-py39haa95532_2.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/babel-2.9.1-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/psutil-5.8.0-py39h2bbff1b_1.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/prometheus_client-0.11.0-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/win-64/ujson-4.0.2-py39hd77b12b_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.

CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://repo.anaconda.com/pkgs/main/noarch/dask-2021.10.0-pyhd3eb1b0_0.conda>
Elapsed: -

An HTTP error occurred when trying to retrieve this URL.
HTTP errors are often intermittent, and a simple retry will get you on your way.



(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv puthon=3.9.7 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: failed

PackagesNotFoundError: The following packages are not available from current channels:

  - puthon=3.9.7

Current channels:

  - https://repo.anaconda.com/pkgs/main/win-64
  - https://repo.anaconda.com/pkgs/main/noarch
  - https://repo.anaconda.com/pkgs/r/win-64
  - https://repo.anaconda.com/pkgs/r/noarch
  - https://repo.anaconda.com/pkgs/msys2/win-64
  - https://repo.anaconda.com/pkgs/msys2/noarch

To search for alternate channels that may provide the conda package you're
looking for, navigate to

    https://anaconda.org

and use the search bar at the top of the page.



(ceejayenv) C:\Users\ALH.YAHYA>conda create -n djangoenv python=3.9.7 anaconda
Collecting package metadata (current_repodata.json): done
Solving environment: failed with repodata from current_repodata.json, will retry with next repodata source.
Collecting package metadata (repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\ALH.YAHYA\.conda\envs\ceejayenv\envs\djangoenv

  added / updated specs:
    - anaconda
    - python=3.9.7


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    alabaster-0.7.12           |     pyhd3eb1b0_0          16 KB
    anyio-2.2.0                |   py39haa95532_2         125 KB
    asn1crypto-1.4.0           |             py_0          80 KB
    astropy-4.3.1              |   py39hc7d831d_0         6.1 MB
    autopep8-1.5.7             |     pyhd3eb1b0_0          43 KB
    babel-2.9.1                |     pyhd3eb1b0_0         5.5 MB
    backports-1.0              |     pyhd3eb1b0_2         210 KB
    bcrypt-3.2.0               |   py39h196d8e1_0         139 KB
    bleach-4.0.0               |     pyhd3eb1b0_0         113 KB
    cookiecutter-1.7.2         |     pyhd3eb1b0_0          86 KB
    dask-2021.10.0             |     pyhd3eb1b0_0          19 KB
    filelock-3.3.1             |     pyhd3eb1b0_1          12 KB
    imagecodecs-2021.8.26      |   py39ha1f97ea_0         6.2 MB
    keyring-23.1.0             |   py39haa95532_0          78 KB
    krb5-1.19.2                |       h5b6d351_0         697 KB
    libssh2-1.9.0              |       h7a1dbc1_1         215 KB
    libtiff-4.2.0              |       hd0e1b90_0         786 KB
    libxslt-1.1.34             |       he774522_0         399 KB
    lxml-4.6.3                 |   py39h9b66d53_0         978 KB
    matplotlib-base-3.4.3      |   py39h49ac443_0         5.5 MB
    packaging-21.0             |     pyhd3eb1b0_0          36 KB
    poyo-0.5.0                 |     pyhd3eb1b0_0          17 KB
    prometheus_client-0.11.0   |     pyhd3eb1b0_0          47 KB
    psutil-5.8.0               |   py39h2bbff1b_1         348 KB
    pygments-2.10.0            |     pyhd3eb1b0_0         725 KB
    pyqt-5.9.2                 |   py39hd77b12b_6         3.3 MB
    pysocks-1.7.1              |   py39haa95532_0          55 KB
    python-libarchive-c-2.9    |     pyhd3eb1b0_1          47 KB
    pyzmq-22.2.1               |   py39hd77b12b_1         620 KB
    qtawesome-1.0.2            |     pyhd3eb1b0_0         760 KB
    scikit-image-0.18.3        |   py39hf11a4ad_0         9.1 MB
    six-1.16.0                 |     pyhd3eb1b0_0          18 KB
    sphinxcontrib-1.0          |   py39haa95532_1         218 KB
    sphinxcontrib-qthelp-1.0.3 |     pyhd3eb1b0_0          26 KB
    textdistance-4.2.1         |     pyhd3eb1b0_0          29 KB
    ujson-4.0.2                |   py39hd77b12b_0          46 KB
    watchdog-2.1.3             |   py39haa95532_0         109 KB
    zfp-0.5.5                  |       hd77b12b_6         139 KB
    zict-2.0.0                 |     pyhd3eb1b0_0          10 KB
    ------------------------------------------------------------
                                           Total:        42.8 MB

The following NEW packages will be INSTALLED:

  alabaster          pkgs/main/noarch::alabaster-0.7.12-pyhd3eb1b0_0
  anaconda           pkgs/main/win-64::anaconda-2021.11-py39_0
  anaconda-client    pkgs/main/win-64::anaconda-client-1.9.0-py39haa95532_0
  anaconda-project   pkgs/main/noarch::anaconda-project-0.10.1-pyhd3eb1b0_0
  anyio              pkgs/main/win-64::anyio-2.2.0-py39haa95532_2
  appdirs            pkgs/main/noarch::appdirs-1.4.4-pyhd3eb1b0_0
  argh               pkgs/main/win-64::argh-0.26.2-py39haa95532_0
  argon2-cffi        pkgs/main/win-64::argon2-cffi-20.1.0-py39h2bbff1b_1
  arrow              pkgs/main/win-64::arrow-0.13.1-py39haa95532_0
  asn1crypto         pkgs/main/noarch::asn1crypto-1.4.0-py_0
  astroid            pkgs/main/win-64::astroid-2.6.6-py39haa95532_0
  astropy            pkgs/main/win-64::astropy-4.3.1-py39hc7d831d_0
  async_generator    pkgs/main/noarch::async_generator-1.10-pyhd3eb1b0_0
  atomicwrites       pkgs/main/noarch::atomicwrites-1.4.0-py_0
  attrs              pkgs/main/noarch::attrs-21.2.0-pyhd3eb1b0_0
  autopep8           pkgs/main/noarch::autopep8-1.5.7-pyhd3eb1b0_0
  babel              pkgs/main/noarch::babel-2.9.1-pyhd3eb1b0_0
  backcall           pkgs/main/noarch::backcall-0.2.0-pyhd3eb1b0_0
  backports          pkgs/main/noarch::backports-1.0-pyhd3eb1b0_2
  backports.shutil_~ pkgs/main/noarch::backports.shutil_get_terminal_size-1.0.0-pyhd3eb1b0_3
  bcrypt             pkgs/main/win-64::bcrypt-3.2.0-py39h196d8e1_0
  beautifulsoup4     pkgs/main/noarch::beautifulsoup4-4.10.0-pyh06a4308_0
  binaryornot        pkgs/main/noarch::binaryornot-0.4.4-pyhd3eb1b0_1
  bitarray           pkgs/main/win-64::bitarray-2.3.0-py39h2bbff1b_1
  bkcharts           pkgs/main/win-64::bkcharts-0.2-py39haa95532_0
  black              pkgs/main/noarch::black-19.10b0-py_0
  blas               pkgs/main/win-64::blas-1.0-mkl
  bleach             pkgs/main/noarch::bleach-4.0.0-pyhd3eb1b0_0
  blosc              pkgs/main/win-64::blosc-1.21.0-h19a0ad4_0
  bokeh              pkgs/main/win-64::bokeh-2.4.1-py39haa95532_0
  boto               pkgs/main/win-64::boto-2.49.0-py39haa95532_0
  bottleneck         pkgs/main/win-64::bottleneck-1.3.2-py39h7cc1a96_1
  brotli             pkgs/main/win-64::brotli-1.0.9-ha925a31_2
  brotlipy           pkgs/main/win-64::brotlipy-0.7.0-py39h2bbff1b_1003
  bzip2              pkgs/main/win-64::bzip2-1.0.8-he774522_0
  ca-certificates    pkgs/main/win-64::ca-certificates-2021.10.26-haa95532_2
  cached-property    pkgs/main/noarch::cached-property-1.5.2-py_0
  certifi            pkgs/main/win-64::certifi-2021.10.8-py39haa95532_0
  cffi               pkgs/main/win-64::cffi-1.14.6-py39h2bbff1b_0
  cfitsio            pkgs/main/win-64::cfitsio-3.470-he774522_6
  chardet            pkgs/main/win-64::chardet-4.0.0-py39haa95532_1003
  charls             pkgs/main/win-64::charls-2.2.0-h6c2663c_0
  charset-normalizer pkgs/main/noarch::charset-normalizer-2.0.4-pyhd3eb1b0_0
  click              pkgs/main/noarch::click-8.0.3-pyhd3eb1b0_0
  cloudpickle        pkgs/main/noarch::cloudpickle-2.0.0-pyhd3eb1b0_0
  clyent             pkgs/main/win-64::clyent-1.2.2-py39haa95532_1
  colorama           pkgs/main/noarch::colorama-0.4.4-pyhd3eb1b0_0
  comtypes           pkgs/main/win-64::comtypes-1.1.10-py39haa95532_1002
  conda              pkgs/main/win-64::conda-4.13.0-py39haa95532_0
  conda-content-tru~ pkgs/main/noarch::conda-content-trust-0.1.1-pyhd3eb1b0_0
  conda-pack         pkgs/main/noarch::conda-pack-0.6.0-pyhd3eb1b0_0
  conda-package-han~ pkgs/main/win-64::conda-package-handling-1.8.1-py39h8cc25b3_0
  conda-token        pkgs/main/noarch::conda-token-0.3.0-pyhd3eb1b0_0
  console_shortcut   pkgs/main/win-64::console_shortcut-0.1.1-4
  contextlib2        pkgs/main/noarch::contextlib2-0.6.0.post1-pyhd3eb1b0_0
  cookiecutter       pkgs/main/noarch::cookiecutter-1.7.2-pyhd3eb1b0_0
  cryptography       pkgs/main/win-64::cryptography-3.4.8-py39h71e12ea_0
  curl               pkgs/main/win-64::curl-7.78.0-h86230a5_0
  cycler             pkgs/main/win-64::cycler-0.10.0-py39haa95532_0
  cython             pkgs/main/win-64::cython-0.29.24-py39h604cdb4_0
  cytoolz            pkgs/main/win-64::cytoolz-0.11.0-py39h2bbff1b_0
  daal4py            pkgs/main/win-64::daal4py-2021.3.0-py39h757b272_0
  dal                pkgs/main/win-64::dal-2021.3.0-haa95532_564
  dask               pkgs/main/noarch::dask-2021.10.0-pyhd3eb1b0_0
  dask-core          pkgs/main/noarch::dask-core-2021.10.0-pyhd3eb1b0_0
  dataclasses        pkgs/main/noarch::dataclasses-0.8-pyh6d0b6a4_7
  debugpy            pkgs/main/win-64::debugpy-1.4.1-py39hd77b12b_0
  decorator          pkgs/main/noarch::decorator-5.1.0-pyhd3eb1b0_0
  defusedxml         pkgs/main/noarch::defusedxml-0.7.1-pyhd3eb1b0_0
  diff-match-patch   pkgs/main/noarch::diff-match-patch-20200713-pyhd3eb1b0_0
  distributed        pkgs/main/win-64::distributed-2021.10.0-py39haa95532_0
  docutils           pkgs/main/win-64::docutils-0.17.1-py39haa95532_1
  entrypoints        pkgs/main/win-64::entrypoints-0.3-py39haa95532_0
  et_xmlfile         pkgs/main/win-64::et_xmlfile-1.1.0-py39haa95532_0
  fastcache          pkgs/main/win-64::fastcache-1.1.0-py39h196d8e1_0
  filelock           pkgs/main/noarch::filelock-3.3.1-pyhd3eb1b0_1
  flake8             pkgs/main/noarch::flake8-3.9.2-pyhd3eb1b0_0
  flask              pkgs/main/noarch::flask-1.1.2-pyhd3eb1b0_0
  fonttools          pkgs/main/noarch::fonttools-4.25.0-pyhd3eb1b0_0
  freetype           pkgs/main/win-64::freetype-2.10.4-hd328e21_0
  fsspec             pkgs/main/noarch::fsspec-2021.10.1-pyhd3eb1b0_0
  get_terminal_size  pkgs/main/win-64::get_terminal_size-1.0.0-h38e98db_0
  gevent             pkgs/main/win-64::gevent-21.8.0-py39h2bbff1b_1
  giflib             pkgs/main/win-64::giflib-5.2.1-h62dcd97_0
  glob2              pkgs/main/noarch::glob2-0.7-pyhd3eb1b0_0
  greenlet           pkgs/main/win-64::greenlet-1.1.1-py39hd77b12b_0
  h5py               pkgs/main/win-64::h5py-3.2.1-py39h3de5c98_0
  hdf5               pkgs/main/win-64::hdf5-1.10.6-h7ebc959_0
  heapdict           pkgs/main/noarch::heapdict-1.0.1-pyhd3eb1b0_0
  html5lib           pkgs/main/noarch::html5lib-1.1-pyhd3eb1b0_0
  icc_rt             pkgs/main/win-64::icc_rt-2019.0.0-h0cc432a_1
  icu                pkgs/main/win-64::icu-58.2-ha925a31_3
  idna               pkgs/main/noarch::idna-3.2-pyhd3eb1b0_0
  imagecodecs        pkgs/main/win-64::imagecodecs-2021.8.26-py39ha1f97ea_0
  imageio            pkgs/main/noarch::imageio-2.9.0-pyhd3eb1b0_0
  imagesize          pkgs/main/noarch::imagesize-1.2.0-pyhd3eb1b0_0
  importlib-metadata pkgs/main/win-64::importlib-metadata-4.8.1-py39haa95532_0
  importlib_metadata pkgs/main/noarch::importlib_metadata-4.8.1-hd3eb1b0_0
  inflection         pkgs/main/win-64::inflection-0.5.1-py39haa95532_0
  iniconfig          pkgs/main/noarch::iniconfig-1.1.1-pyhd3eb1b0_0
  intel-openmp       pkgs/main/win-64::intel-openmp-2021.4.0-haa95532_3556
  intervaltree       pkgs/main/noarch::intervaltree-3.1.0-pyhd3eb1b0_0
  ipykernel          pkgs/main/win-64::ipykernel-6.4.1-py39haa95532_1
  ipython            pkgs/main/win-64::ipython-7.29.0-py39hd4e2768_0
  ipython_genutils   pkgs/main/noarch::ipython_genutils-0.2.0-pyhd3eb1b0_1
  ipywidgets         pkgs/main/noarch::ipywidgets-7.6.5-pyhd3eb1b0_1
  isort              pkgs/main/noarch::isort-5.9.3-pyhd3eb1b0_0
  itsdangerous       pkgs/main/noarch::itsdangerous-2.0.1-pyhd3eb1b0_0
  jdcal              pkgs/main/noarch::jdcal-1.4.1-pyhd3eb1b0_0
  jedi               pkgs/main/win-64::jedi-0.18.0-py39haa95532_1
  jinja2             pkgs/main/noarch::jinja2-2.11.3-pyhd3eb1b0_0
  jinja2-time        pkgs/main/noarch::jinja2-time-0.2.0-pyhd3eb1b0_2
  joblib             pkgs/main/noarch::joblib-1.1.0-pyhd3eb1b0_0
  jpeg               pkgs/main/win-64::jpeg-9d-h2bbff1b_0
  json5              pkgs/main/noarch::json5-0.9.6-pyhd3eb1b0_0
  jsonschema         pkgs/main/noarch::jsonschema-3.2.0-pyhd3eb1b0_2
  jupyter            pkgs/main/win-64::jupyter-1.0.0-py39haa95532_7
  jupyter_client     pkgs/main/noarch::jupyter_client-6.1.12-pyhd3eb1b0_0
  jupyter_console    pkgs/main/noarch::jupyter_console-6.4.0-pyhd3eb1b0_0
  jupyter_core       pkgs/main/win-64::jupyter_core-4.8.1-py39haa95532_0
  jupyter_server     pkgs/main/win-64::jupyter_server-1.4.1-py39haa95532_0
  jupyterlab         pkgs/main/noarch::jupyterlab-3.2.1-pyhd3eb1b0_1
  jupyterlab_pygmen~ pkgs/main/noarch::jupyterlab_pygments-0.1.2-py_0
  jupyterlab_server  pkgs/main/noarch::jupyterlab_server-2.8.2-pyhd3eb1b0_0
  jupyterlab_widgets pkgs/main/noarch::jupyterlab_widgets-1.0.0-pyhd3eb1b0_1
  keyring            pkgs/main/win-64::keyring-23.1.0-py39haa95532_0
  kiwisolver         pkgs/main/win-64::kiwisolver-1.3.1-py39hd77b12b_0
  krb5               pkgs/main/win-64::krb5-1.19.2-h5b6d351_0
  lazy-object-proxy  pkgs/main/win-64::lazy-object-proxy-1.6.0-py39h2bbff1b_0
  lcms2              pkgs/main/win-64::lcms2-2.12-h83e58a3_0
  lerc               pkgs/main/win-64::lerc-3.0-hd77b12b_0
  libaec             pkgs/main/win-64::libaec-1.0.4-h33f27b4_1
  libarchive         pkgs/main/win-64::libarchive-3.4.2-h5e25573_0
  libcurl            pkgs/main/win-64::libcurl-7.78.0-h86230a5_0
  libdeflate         pkgs/main/win-64::libdeflate-1.8-h2bbff1b_5
  libiconv           pkgs/main/win-64::libiconv-1.15-h1df5818_7
  liblief            pkgs/main/win-64::liblief-0.10.1-hd77b12b_1
  libpng             pkgs/main/win-64::libpng-1.6.37-h2a8f88b_0
  libspatialindex    pkgs/main/win-64::libspatialindex-1.9.3-h6c2663c_0
  libssh2            pkgs/main/win-64::libssh2-1.9.0-h7a1dbc1_1
  libtiff            pkgs/main/win-64::libtiff-4.2.0-hd0e1b90_0
  libwebp            pkgs/main/win-64::libwebp-1.2.0-h2bbff1b_0
  libxml2            pkgs/main/win-64::libxml2-2.9.12-h0ad7f3c_0
  libxslt            pkgs/main/win-64::libxslt-1.1.34-he774522_0
  libzopfli          pkgs/main/win-64::libzopfli-1.0.3-ha925a31_0
  llvmlite           pkgs/main/win-64::llvmlite-0.37.0-py39h23ce68f_1
  locket             pkgs/main/win-64::locket-0.2.1-py39haa95532_1
  lxml               pkgs/main/win-64::lxml-4.6.3-py39h9b66d53_0
  lz4-c              pkgs/main/win-64::lz4-c-1.9.3-h2bbff1b_1
  lzo                pkgs/main/win-64::lzo-2.10-he774522_2
  m2w64-gcc-libgfor~ pkgs/msys2/win-64::m2w64-gcc-libgfortran-5.3.0-6
  m2w64-gcc-libs     pkgs/msys2/win-64::m2w64-gcc-libs-5.3.0-7
  m2w64-gcc-libs-co~ pkgs/msys2/win-64::m2w64-gcc-libs-core-5.3.0-7
  m2w64-gmp          pkgs/msys2/win-64::m2w64-gmp-6.1.0-2
  m2w64-libwinpthre~ pkgs/msys2/win-64::m2w64-libwinpthread-git-5.0.0.4634.697f757-2
  markupsafe         pkgs/main/win-64::markupsafe-1.1.1-py39h2bbff1b_0
  matplotlib         pkgs/main/win-64::matplotlib-3.4.3-py39haa95532_0
  matplotlib-base    pkgs/main/win-64::matplotlib-base-3.4.3-py39h49ac443_0
  matplotlib-inline  pkgs/main/noarch::matplotlib-inline-0.1.2-pyhd3eb1b0_2
  mccabe             pkgs/main/win-64::mccabe-0.6.1-py39haa95532_1
  menuinst           pkgs/main/win-64::menuinst-1.4.18-py39h59b6b97_0
  mistune            pkgs/main/win-64::mistune-0.8.4-py39h2bbff1b_1000
  mkl                pkgs/main/win-64::mkl-2021.4.0-haa95532_640
  mkl-service        pkgs/main/win-64::mkl-service-2.4.0-py39h2bbff1b_0
  mkl_fft            pkgs/main/win-64::mkl_fft-1.3.1-py39h277e83a_0
  mkl_random         pkgs/main/win-64::mkl_random-1.2.2-py39hf11a4ad_0
  mock               pkgs/main/noarch::mock-4.0.3-pyhd3eb1b0_0
  more-itertools     pkgs/main/noarch::more-itertools-8.10.0-pyhd3eb1b0_0
  mpmath             pkgs/main/win-64::mpmath-1.2.1-py39haa95532_0
  msgpack-python     pkgs/main/win-64::msgpack-python-1.0.2-py39h59b6b97_1
  msys2-conda-epoch  pkgs/msys2/win-64::msys2-conda-epoch-20160418-1
  multipledispatch   pkgs/main/win-64::multipledispatch-0.6.0-py39haa95532_0
  munkres            pkgs/main/noarch::munkres-1.1.4-py_0
  mypy_extensions    pkgs/main/win-64::mypy_extensions-0.4.3-py39haa95532_0
  nbclassic          pkgs/main/noarch::nbclassic-0.2.6-pyhd3eb1b0_0
  nbclient           pkgs/main/noarch::nbclient-0.5.3-pyhd3eb1b0_0
  nbconvert          pkgs/main/win-64::nbconvert-6.1.0-py39haa95532_0
  nbformat           pkgs/main/noarch::nbformat-5.1.3-pyhd3eb1b0_0
  nest-asyncio       pkgs/main/noarch::nest-asyncio-1.5.1-pyhd3eb1b0_0
  networkx           pkgs/main/noarch::networkx-2.6.3-pyhd3eb1b0_0
  nltk               pkgs/main/noarch::nltk-3.6.5-pyhd3eb1b0_0
  nose               pkgs/main/noarch::nose-1.3.7-pyhd3eb1b0_1006
  notebook           pkgs/main/win-64::notebook-6.4.5-py39haa95532_0
  numba              pkgs/main/win-64::numba-0.54.1-py39hf11a4ad_0
  numexpr            pkgs/main/win-64::numexpr-2.7.3-py39hb80d3ca_1
  numpy              pkgs/main/win-64::numpy-1.20.3-py39ha4e8547_0
  numpy-base         pkgs/main/win-64::numpy-base-1.20.3-py39hc2deb75_0
  numpydoc           pkgs/main/noarch::numpydoc-1.1.0-pyhd3eb1b0_1
  olefile            pkgs/main/noarch::olefile-0.46-pyhd3eb1b0_0
  openjpeg           pkgs/main/win-64::openjpeg-2.4.0-h4fc8c34_0
  openpyxl           pkgs/main/noarch::openpyxl-3.0.9-pyhd3eb1b0_0
  openssl            pkgs/main/win-64::openssl-1.1.1l-h2bbff1b_0
  packaging          pkgs/main/noarch::packaging-21.0-pyhd3eb1b0_0
  pandas             pkgs/main/win-64::pandas-1.3.4-py39h6214cd6_0
  pandocfilters      pkgs/main/win-64::pandocfilters-1.4.3-py39haa95532_1
  paramiko           pkgs/main/noarch::paramiko-2.7.2-py_0
  parso              pkgs/main/noarch::parso-0.8.2-pyhd3eb1b0_0
  partd              pkgs/main/noarch::partd-1.2.0-pyhd3eb1b0_0
  path               pkgs/main/win-64::path-16.0.0-py39haa95532_0
  path.py            pkgs/main/noarch::path.py-12.5.0-hd3eb1b0_0
  pathlib2           pkgs/main/win-64::pathlib2-2.3.6-py39haa95532_2
  pathspec           pkgs/main/noarch::pathspec-0.7.0-py_0
  patsy              pkgs/main/win-64::patsy-0.5.2-py39haa95532_0
  pep8               pkgs/main/win-64::pep8-1.7.1-py39haa95532_0
  pexpect            pkgs/main/noarch::pexpect-4.8.0-pyhd3eb1b0_3
  pickleshare        pkgs/main/noarch::pickleshare-0.7.5-pyhd3eb1b0_1003
  pillow             pkgs/main/win-64::pillow-8.4.0-py39hd45dc43_0
  pip                pkgs/main/win-64::pip-21.2.4-py39haa95532_0
  pkginfo            pkgs/main/win-64::pkginfo-1.7.1-py39haa95532_0
  pluggy             pkgs/main/win-64::pluggy-0.13.1-py39haa95532_0
  ply                pkgs/main/win-64::ply-3.11-py39haa95532_0
  powershell_shortc~ pkgs/main/win-64::powershell_shortcut-0.0.1-3
  poyo               pkgs/main/noarch::poyo-0.5.0-pyhd3eb1b0_0
  prometheus_client  pkgs/main/noarch::prometheus_client-0.11.0-pyhd3eb1b0_0
  prompt-toolkit     pkgs/main/noarch::prompt-toolkit-3.0.20-pyhd3eb1b0_0
  prompt_toolkit     pkgs/main/noarch::prompt_toolkit-3.0.20-hd3eb1b0_0
  psutil             pkgs/main/win-64::psutil-5.8.0-py39h2bbff1b_1
  ptyprocess         pkgs/main/noarch::ptyprocess-0.7.0-pyhd3eb1b0_2
  py                 pkgs/main/noarch::py-1.10.0-pyhd3eb1b0_0
  py-lief            pkgs/main/win-64::py-lief-0.10.1-py39hd77b12b_1
  pycodestyle        pkgs/main/noarch::pycodestyle-2.7.0-pyhd3eb1b0_0
  pycosat            pkgs/main/win-64::pycosat-0.6.3-py39h2bbff1b_0
  pycparser          pkgs/main/noarch::pycparser-2.20-py_2
  pycurl             pkgs/main/win-64::pycurl-7.44.1-py39hcd4344a_1
  pydocstyle         pkgs/main/noarch::pydocstyle-6.1.1-pyhd3eb1b0_0
  pyerfa             pkgs/main/win-64::pyerfa-2.0.0-py39h2bbff1b_0
  pyflakes           pkgs/main/noarch::pyflakes-2.3.1-pyhd3eb1b0_0
  pygments           pkgs/main/noarch::pygments-2.10.0-pyhd3eb1b0_0
  pylint             pkgs/main/win-64::pylint-2.9.6-py39haa95532_1
  pyls-spyder        pkgs/main/noarch::pyls-spyder-0.4.0-pyhd3eb1b0_0
  pynacl             pkgs/main/win-64::pynacl-1.4.0-py39hbd8134f_1
  pyodbc             pkgs/main/win-64::pyodbc-4.0.31-py39hd77b12b_0
  pyopenssl          pkgs/main/noarch::pyopenssl-21.0.0-pyhd3eb1b0_1
  pyparsing          pkgs/main/noarch::pyparsing-3.0.4-pyhd3eb1b0_0
  pyqt               pkgs/main/win-64::pyqt-5.9.2-py39hd77b12b_6
  pyreadline         pkgs/main/win-64::pyreadline-2.1-py39haa95532_1
  pyrsistent         pkgs/main/win-64::pyrsistent-0.18.0-py39h196d8e1_0
  pysocks            pkgs/main/win-64::pysocks-1.7.1-py39haa95532_0
  pytables           pkgs/main/win-64::pytables-3.6.1-py39h56d22b6_1
  pytest             pkgs/main/win-64::pytest-6.2.4-py39haa95532_2
  python             pkgs/main/win-64::python-3.9.7-h6244533_1
  python-dateutil    pkgs/main/noarch::python-dateutil-2.8.2-pyhd3eb1b0_0
  python-libarchive~ pkgs/main/noarch::python-libarchive-c-2.9-pyhd3eb1b0_1
  python-lsp-black   pkgs/main/noarch::python-lsp-black-1.0.0-pyhd3eb1b0_0
  python-lsp-jsonrpc pkgs/main/noarch::python-lsp-jsonrpc-1.0.0-pyhd3eb1b0_0
  python-lsp-server  pkgs/main/noarch::python-lsp-server-1.2.4-pyhd3eb1b0_0
  python-slugify     pkgs/main/noarch::python-slugify-5.0.2-pyhd3eb1b0_0
  pytz               pkgs/main/noarch::pytz-2021.3-pyhd3eb1b0_0
  pywavelets         pkgs/main/win-64::pywavelets-1.1.1-py39h080aedc_4
  pywin32            pkgs/main/win-64::pywin32-228-py39he774522_0
  pywin32-ctypes     pkgs/main/win-64::pywin32-ctypes-0.2.0-py39haa95532_1000
  pywinpty           pkgs/main/win-64::pywinpty-0.5.7-py39haa95532_0
  pyyaml             pkgs/main/win-64::pyyaml-6.0-py39h2bbff1b_1
  pyzmq              pkgs/main/win-64::pyzmq-22.2.1-py39hd77b12b_1
  qdarkstyle         pkgs/main/noarch::qdarkstyle-3.0.2-pyhd3eb1b0_0
  qstylizer          pkgs/main/noarch::qstylizer-0.1.10-pyhd3eb1b0_0
  qt                 pkgs/main/win-64::qt-5.9.7-vc14h73c81de_0
  qtawesome          pkgs/main/noarch::qtawesome-1.0.2-pyhd3eb1b0_0
  qtconsole          pkgs/main/noarch::qtconsole-5.1.1-pyhd3eb1b0_0
  qtpy               pkgs/main/noarch::qtpy-1.10.0-pyhd3eb1b0_0
  regex              pkgs/main/win-64::regex-2021.8.3-py39h2bbff1b_0
  requests           pkgs/main/noarch::requests-2.26.0-pyhd3eb1b0_0
  rope               pkgs/main/noarch::rope-0.19.0-pyhd3eb1b0_0
  rtree              pkgs/main/win-64::rtree-0.9.7-py39h2eaa2aa_1
  ruamel_yaml        pkgs/main/win-64::ruamel_yaml-0.15.100-py39h2bbff1b_0
  scikit-image       pkgs/main/win-64::scikit-image-0.18.3-py39hf11a4ad_0
  scikit-learn       pkgs/main/win-64::scikit-learn-0.24.2-py39hf11a4ad_1
  scikit-learn-inte~ pkgs/main/win-64::scikit-learn-intelex-2021.3.0-py39haa95532_0
  scipy              pkgs/main/win-64::scipy-1.7.1-py39hbe87c03_2
  seaborn            pkgs/main/noarch::seaborn-0.11.2-pyhd3eb1b0_0
  send2trash         pkgs/main/noarch::send2trash-1.8.0-pyhd3eb1b0_1
  setuptools         pkgs/main/win-64::setuptools-58.0.4-py39haa95532_0
  simplegeneric      pkgs/main/win-64::simplegeneric-0.8.1-py39haa95532_2
  singledispatch     pkgs/main/noarch::singledispatch-3.7.0-pyhd3eb1b0_1001
  sip                pkgs/main/win-64::sip-4.19.13-py39hd77b12b_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_0
  snappy             pkgs/main/win-64::snappy-1.1.8-h33f27b4_0
  sniffio            pkgs/main/win-64::sniffio-1.2.0-py39haa95532_1
  snowballstemmer    pkgs/main/noarch::snowballstemmer-2.1.0-pyhd3eb1b0_0
  sortedcollections  pkgs/main/noarch::sortedcollections-2.1.0-pyhd3eb1b0_0
  sortedcontainers   pkgs/main/noarch::sortedcontainers-2.4.0-pyhd3eb1b0_0
  soupsieve          pkgs/main/noarch::soupsieve-2.2.1-pyhd3eb1b0_0
  sphinx             pkgs/main/noarch::sphinx-4.2.0-pyhd3eb1b0_1
  sphinxcontrib      pkgs/main/win-64::sphinxcontrib-1.0-py39haa95532_1
  sphinxcontrib-app~ pkgs/main/noarch::sphinxcontrib-applehelp-1.0.2-pyhd3eb1b0_0
  sphinxcontrib-dev~ pkgs/main/noarch::sphinxcontrib-devhelp-1.0.2-pyhd3eb1b0_0
  sphinxcontrib-htm~ pkgs/main/noarch::sphinxcontrib-htmlhelp-2.0.0-pyhd3eb1b0_0
  sphinxcontrib-jsm~ pkgs/main/noarch::sphinxcontrib-jsmath-1.0.1-pyhd3eb1b0_0
  sphinxcontrib-qth~ pkgs/main/noarch::sphinxcontrib-qthelp-1.0.3-pyhd3eb1b0_0
  sphinxcontrib-ser~ pkgs/main/noarch::sphinxcontrib-serializinghtml-1.1.5-pyhd3eb1b0_0
  sphinxcontrib-web~ pkgs/main/noarch::sphinxcontrib-websupport-1.2.4-py_0
  spyder             pkgs/main/win-64::spyder-5.1.5-py39haa95532_1
  spyder-kernels     pkgs/main/win-64::spyder-kernels-2.1.3-py39haa95532_0
  sqlalchemy         pkgs/main/win-64::sqlalchemy-1.4.22-py39h2bbff1b_0
  sqlite             pkgs/main/win-64::sqlite-3.36.0-h2bbff1b_0
  statsmodels        pkgs/main/win-64::statsmodels-0.12.2-py39h2bbff1b_0
  sympy              pkgs/main/win-64::sympy-1.9-py39haa95532_0
  tbb                pkgs/main/win-64::tbb-2021.4.0-h59b6b97_0
  tbb4py             pkgs/main/win-64::tbb4py-2021.4.0-py39h59b6b97_0
  tblib              pkgs/main/noarch::tblib-1.7.0-pyhd3eb1b0_0
  terminado          pkgs/main/win-64::terminado-0.9.4-py39haa95532_0
  testpath           pkgs/main/noarch::testpath-0.5.0-pyhd3eb1b0_0
  text-unidecode     pkgs/main/noarch::text-unidecode-1.3-pyhd3eb1b0_0
  textdistance       pkgs/main/noarch::textdistance-4.2.1-pyhd3eb1b0_0
  threadpoolctl      pkgs/main/noarch::threadpoolctl-2.2.0-pyh0d69192_0
  three-merge        pkgs/main/noarch::three-merge-0.1.1-pyhd3eb1b0_0
  tifffile           pkgs/main/noarch::tifffile-2021.7.2-pyhd3eb1b0_2
  tinycss            pkgs/main/noarch::tinycss-0.4-pyhd3eb1b0_1002
  tk                 pkgs/main/win-64::tk-8.6.11-h2bbff1b_0
  toml               pkgs/main/noarch::toml-0.10.2-pyhd3eb1b0_0
  toolz              pkgs/main/noarch::toolz-0.11.1-pyhd3eb1b0_0
  tornado            pkgs/main/win-64::tornado-6.1-py39h2bbff1b_0
  tqdm               pkgs/main/noarch::tqdm-4.62.3-pyhd3eb1b0_1
  traitlets          pkgs/main/noarch::traitlets-5.1.0-pyhd3eb1b0_0
  typed-ast          pkgs/main/win-64::typed-ast-1.4.3-py39h2bbff1b_1
  typing_extensions  pkgs/main/noarch::typing_extensions-3.10.0.2-pyh06a4308_0
  tzdata             pkgs/main/noarch::tzdata-2021e-hda174b7_0
  ujson              pkgs/main/win-64::ujson-4.0.2-py39hd77b12b_0
  unicodecsv         pkgs/main/win-64::unicodecsv-0.14.1-py39haa95532_0
  unidecode          pkgs/main/noarch::unidecode-1.2.0-pyhd3eb1b0_0
  urllib3            pkgs/main/noarch::urllib3-1.26.7-pyhd3eb1b0_0
  vc                 pkgs/main/win-64::vc-14.2-h21ff451_1
  vs2015_runtime     pkgs/main/win-64::vs2015_runtime-14.27.29016-h5e58377_2
  watchdog           pkgs/main/win-64::watchdog-2.1.3-py39haa95532_0
  wcwidth            pkgs/main/noarch::wcwidth-0.2.5-pyhd3eb1b0_0
  webencodings       pkgs/main/win-64::webencodings-0.5.1-py39haa95532_1
  werkzeug           pkgs/main/noarch::werkzeug-2.0.2-pyhd3eb1b0_0
  wheel              pkgs/main/noarch::wheel-0.37.0-pyhd3eb1b0_1
  whichcraft         pkgs/main/noarch::whichcraft-0.6.1-pyhd3eb1b0_0
  widgetsnbextension pkgs/main/win-64::widgetsnbextension-3.5.1-py39haa95532_0
  win_inet_pton      pkgs/main/win-64::win_inet_pton-1.1.0-py39haa95532_0
  win_unicode_conso~ pkgs/main/win-64::win_unicode_console-0.5-py39haa95532_0
  wincertstore       pkgs/main/win-64::wincertstore-0.2-py39haa95532_2
  winpty             pkgs/main/win-64::winpty-0.4.3-4
  wrapt              pkgs/main/win-64::wrapt-1.12.1-py39h196d8e1_1
  xlrd               pkgs/main/noarch::xlrd-2.0.1-pyhd3eb1b0_0
  xlsxwriter         pkgs/main/noarch::xlsxwriter-3.0.1-pyhd3eb1b0_0
  xlwings            pkgs/main/win-64::xlwings-0.24.9-py39haa95532_0
  xlwt               pkgs/main/win-64::xlwt-1.3.0-py39haa95532_0
  xz                 pkgs/main/win-64::xz-5.2.5-h62dcd97_0
  yaml               pkgs/main/win-64::yaml-0.2.5-he774522_0
  yapf               pkgs/main/noarch::yapf-0.31.0-pyhd3eb1b0_0
  zfp                pkgs/main/win-64::zfp-0.5.5-hd77b12b_6
  zict               pkgs/main/noarch::zict-2.0.0-pyhd3eb1b0_0
  zipp               pkgs/main/noarch::zipp-3.6.0-pyhd3eb1b0_0
  zlib               pkgs/main/win-64::zlib-1.2.11-h62dcd97_4
  zope               pkgs/main/win-64::zope-1.0-py39haa95532_1
  zope.event         pkgs/main/win-64::zope.event-4.5.0-py39haa95532_0
  zope.interface     pkgs/main/win-64::zope.interface-5.4.0-py39h2bbff1b_0
  zstd               pkgs/main/win-64::zstd-1.4.9-h19a0ad4_0


Proceed ([y]/n)? y


Downloading and Extracting Packages
pyqt-5.9.2           | 3.3 MB    | ############################################################################ | 100%
bleach-4.0.0         | 113 KB    | ############################################################################ | 100%
dask-2021.10.0       | 19 KB     | ############################################################################ | 100%
pysocks-1.7.1        | 55 KB     | ############################################################################ | 100%
filelock-3.3.1       | 12 KB     | ############################################################################ | 100%
qtawesome-1.0.2      | 760 KB    | ############################################################################ | 100%
watchdog-2.1.3       | 109 KB    | ############################################################################ | 100%
imagecodecs-2021.8.2 | 6.2 MB    | ############################################################################ | 100%
textdistance-4.2.1   | 29 KB     | ############################################################################ | 100%
lxml-4.6.3           | 978 KB    | ############################################################################ | 100%
matplotlib-base-3.4. | 5.5 MB    | ############################################################################ | 100%
astropy-4.3.1        | 6.1 MB    | ############################################################################ | 100%
libxslt-1.1.34       | 399 KB    | ############################################################################ | 100%
zict-2.0.0           | 10 KB     | ############################################################################ | 100%
psutil-5.8.0         | 348 KB    | ############################################################################ | 100%
babel-2.9.1          | 5.5 MB    | ############################################################################ | 100%
prometheus_client-0. | 47 KB     | ############################################################################ | 100%
ujson-4.0.2          | 46 KB     | ############################################################################ | 100%
cookiecutter-1.7.2   | 86 KB     | ############################################################################ | 100%
scikit-image-0.18.3  | 9.1 MB    | ############################################################################ | 100%
anyio-2.2.0          | 125 KB    | ############################################################################ | 100%
autopep8-1.5.7       | 43 KB     | ############################################################################ | 100%
libtiff-4.2.0        | 786 KB    | ############################################################################ | 100%
poyo-0.5.0           | 17 KB     | ############################################################################ | 100%
pygments-2.10.0      | 725 KB    | ############################################################################ | 100%
six-1.16.0           | 18 KB     | ############################################################################ | 100%
sphinxcontrib-qthelp | 26 KB     | ############################################################################ | 100%
sphinxcontrib-1.0    | 218 KB    | ############################################################################ | 100%
python-libarchive-c- | 47 KB     | ############################################################################ | 100%
packaging-21.0       | 36 KB     | ############################################################################ | 100%
pyzmq-22.2.1         | 620 KB    | ############################################################################ | 100%
alabaster-0.7.12     | 16 KB     | ############################################################################ | 100%
keyring-23.1.0       | 78 KB     | ############################################################################ | 100%
asn1crypto-1.4.0     | 80 KB     | ############################################################################ | 100%
zfp-0.5.5            | 139 KB    | ############################################################################ | 100%
libssh2-1.9.0        | 215 KB    | ############################################################################ | 100%
krb5-1.19.2          | 697 KB    | ############################################################################ | 100%
bcrypt-3.2.0         | 139 KB    | ############################################################################ | 100%
backports-1.0        | 210 KB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: |

    Windows 64-bit packages of scikit-learn can be accelerated using scikit-learn-intelex.
    More details are available here: https://intel.github.io/scikit-learn-intelex

    For example:

        $ conda install scikit-learn-intelex
        $ python -m sklearnex my_application.py

()
\ menuinst called from non-root env C:\Users\ALH.YAHYA\.conda\envs\ceejayenv
done
#
# To activate this environment, use
#
#     $ conda activate djangoenv
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(ceejayenv) C:\Users\ALH.YAHYA>conda activate djangoenv

(djangoenv) C:\Users\ALH.YAHYA>conda install -c anaconda django
Collecting package metadata (current_repodata.json): done
Solving environment: done

## Package Plan ##

  environment location: C:\Users\ALH.YAHYA\.conda\envs\ceejayenv\envs\djangoenv

  added / updated specs:
    - django


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    asgiref-3.4.1              |     pyhd3eb1b0_0          23 KB  anaconda
    ca-certificates-2021.10.26 |       haa95532_2         151 KB  anaconda
    certifi-2021.10.8          |   py39haa95532_0         155 KB  anaconda
    django-3.2.5               |     pyhd3eb1b0_0         3.8 MB  anaconda
    libpq-12.9                 |       hb652d5d_1         3.7 MB  anaconda
    openssl-1.1.1l             |       h2bbff1b_0         5.7 MB  anaconda
    psycopg2-2.8.6             |   py39hcd4344a_1         170 KB  anaconda
    sqlparse-0.4.1             |             py_0          34 KB  anaconda
    ------------------------------------------------------------
                                           Total:        13.7 MB

The following NEW packages will be INSTALLED:

  asgiref            anaconda/noarch::asgiref-3.4.1-pyhd3eb1b0_0
  django             anaconda/noarch::django-3.2.5-pyhd3eb1b0_0
  libpq              anaconda/win-64::libpq-12.9-hb652d5d_1
  psycopg2           anaconda/win-64::psycopg2-2.8.6-py39hcd4344a_1
  sqlparse           anaconda/noarch::sqlparse-0.4.1-py_0

The following packages will be SUPERSEDED by a higher-priority channel:

  ca-certificates                                 pkgs/main --> anaconda
  certifi                                         pkgs/main --> anaconda
  openssl                                         pkgs/main --> anaconda


Proceed ([y]/n)? y


Downloading and Extracting Packages
libpq-12.9           | 3.7 MB    | ############################################################################ | 100%
certifi-2021.10.8    | 155 KB    | ############################################################################ | 100%
asgiref-3.4.1        | 23 KB     | ############################################################################ | 100%
django-3.2.5         | 3.8 MB    | ############################################################################ | 100%
psycopg2-2.8.6       | 170 KB    | ############################################################################ | 100%
ca-certificates-2021 | 151 KB    | ############################################################################ | 100%
sqlparse-0.4.1       | 34 KB     | ############################################################################ | 100%
openssl-1.1.1l       | 5.7 MB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(djangoenv) C:\Users\ALH.YAHYA>django-admin startproject chukwumajonathan

(djangoenv) C:\Users\ALH.YAHYA>python manage.py runserver
python: can't open file 'C:\Users\ALH.YAHYA\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA>ipython manage.py runserver
[TerminalIPythonApp] WARNING | File 'manage.py' doesn't exist

(djangoenv) C:\Users\ALH.YAHYA>python manage.py runserver
python: can't open file 'C:\Users\ALH.YAHYA\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA>python manage.py runserver
C:\Users\ALH.YAHYA\.conda\envs\ceejayenv\envs\djangoenv\python.exe: can't find '__main__' module in 'C:\\Users\\ALH.YAHYA\\manage.py'

(djangoenv) C:\Users\ALH.YAHYA>python manage.py runserver
python: can't open file 'C:\Users\ALH.YAHYA\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA>mkdir django_projects
A subdirectory or file django_projects already exists.

(djangoenv) C:\Users\ALH.YAHYA>cd django_projects

(djangoenv) C:\Users\ALH.YAHYA\django_projects>mkdir django-admin

(djangoenv) C:\Users\ALH.YAHYA\django_projects>startproject
'startproject' is not recognized as an internal or external command,
operable program or batch file.

(djangoenv) C:\Users\ALH.YAHYA\django_projects>mkdir django-admin
A subdirectory or file django-admin already exists.

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject
usage: django-admin startproject [-h] [--template TEMPLATE] [--extension EXTENSIONS] [--name FILES] [--version]
                                 [-v {0,1,2,3}] [--settings SETTINGS] [--pythonpath PYTHONPATH] [--traceback]
                                 [--no-color] [--force-color]
                                 name [directory]
django-admin startproject: error: You must provide a project name.

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject chukwumajonathan

(djangoenv) C:\Users\ALH.YAHYA\django_projects>py manage.py startap catalog
C:\Users\ALH.YAHYA\AppData\Local\Programs\Python\Python39\python.exe: can't open file 'C:\Users\ALH.YAHYA\django_projects\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py runserver
python: can't open file 'C:\Users\ALH.YAHYA\django_projects\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject chukwumajonathan
CommandError: 'C:\Users\ALH.YAHYA\django_projects\chukwumajonathan' already exists

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject chukwumaajonathan

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py runserver
python: can't open file 'C:\Users\ALH.YAHYA\django_projects\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject setup

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py runserver
python: can't open file 'C:\Users\ALH.YAHYA\django_projects\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py startapp zuri
python: can't open file 'C:\Users\ALH.YAHYA\django_projects\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py startapp chukwumajonathan
python: can't open file 'C:\Users\ALH.YAHYA\django_projects\manage.py': [Errno 2] No such file or directory

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject cjjonathan

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject setup
CommandError: 'C:\Users\ALH.YAHYA\django_projects\setup' already exists

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject cjjonathan .

(djangoenv) C:\Users\ALH.YAHYA\django_projects>django-admin startproject setup
CommandError: 'C:\Users\ALH.YAHYA\django_projects\setup' already exists

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py startapp chukwumajonathan
CommandError: 'chukwumajonathan' conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name.

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py startapp cjjonathan
CommandError: 'cjjonathan' conflicts with the name of an existing Python module and cannot be used as an app name. Please try another name.

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py startapp chukwumajonathann

(djangoenv) C:\Users\ALH.YAHYA\django_projects>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
May 31, 2022 - 12:10:15
Django version 3.2.5, using settings 'cjjonathan.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
[31/May/2022 12:11:15] "GET / HTTP/1.1" 200 10697
[31/May/2022 12:11:17] "GET /static/admin/css/fonts.css HTTP/1.1" 200 423
[31/May/2022 12:11:20] "GET /static/admin/fonts/Roboto-Regular-webfont.woff HTTP/1.1" 200 85876
[31/May/2022 12:11:20] "GET /static/admin/fonts/Roboto-Bold-webfont.woff HTTP/1.1" 200 86184
[31/May/2022 12:11:21] "GET /static/admin/fonts/Roboto-Light-webfont.woff HTTP/1.1" 200 85692
Not Found: /favicon.ico
[31/May/2022 12:11:24] "GET /favicon.ico HTTP/1.1" 404 2114
[31/May/2022 12:27:45] "GET / HTTP/1.1" 200 10697

