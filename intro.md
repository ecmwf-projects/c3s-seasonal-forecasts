![logo](LogoLine_horizon_C3S.png)

# C3S seasonal forecast applications and workflows

This Jupyter Book contains a collection of Jupyter Notebooks related to the C3S seasonal forecast service. This compliments the data tutorials available in the C3S training Jupyter Book, by showing how some of the data or graphical products are created, as well as by exploring some additional properties of the data.

1. [Workflows related to graphical products](workflows/prod_workflows.md)
2. [Additional analysis using C3S seasonal data](workflows/extra_analysis.md)

## Running the Notebooks

This Jupyter Book provides practical examples of data processing of C3S seasonal data available from the CDS. The workflows and examples are in the form of [Jupyter Notebooks](https://jupyter.org/). You may use a selection of cloud-based services to run, edit, export or create new notebooks, although some may exceed the free compute resources allocate by those platforms. These include the following:

|Binder|Kaggle|Colab|
|:-:|:-:|:-:|
|[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/)|[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/code)|[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)|
|Binder may take some time to load, so please be patient!                                           |Requires (free) registration with Kaggle. Once in, "switch on the internet" via settings           |Requires Google account, and installation of some libraries, such as Cartopy `!pip install cartopy`|

[WEkEo](https://www.wekeo.eu/computing), funded by Copernicus, also offers free compute services which could also be used for this purpose.

If you would like to run these notebooks in your own environment, we suggest you install [Anaconda](https://docs.anaconda.com/anaconda/install/), which contains most of the libraries you will need. You will also need to install [Xarray](http://xarray.pydata.org/en/stable/) for working with multidimensional data in netcdf files, and the CDS API (`pip install cdsapi`) for downloading data programmatically from the CDS.

```{note}
 [Earthkit](https://github.com/ecmwf/earthkit), currently under development at ECMWF, aims to simplify accessing, processing and plotting climate and weather data in a format agnostic manner, but is not extensively used here to be as explicit and transparent in the code as possible. However, some hints may be given on how Earthkit can be used. 
```
