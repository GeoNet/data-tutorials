# FITS #

The file in this folder is a Jupyter notebooks written in Python. It demonstrates some simple ways to use [GeoNet's FITS data service](https://fits.geonet.org.nz/api-docs/), typically using the Python [Pandas module](https://pandas.pydata.org/).

They apply to all data types available through FITS:
- GNSS daily positions
- volcano data collected by data logger, but not updated to the LRDCP platform (Ruapehu crater lake only)
- volcano data collected by scanDOAS spectrometer, but not available through Tilde (four Ruapehu sites only)

Other data types are available through Tilde and other applications.

FITS is the process of being replaced by [Tilde](https://tilde.geonet.org.nz/), and will later be deprecated.

## Python ##

**All notebooks use Python 3. We do not support Python 2.7.**

## Notebook ##

| Notebook | Description |
|------|-------------|
| [Data access tutorial](FITS_data_access.ipynb) | Demonstrates how to retrieve data from FITS and how to find sites and data collection methods |
