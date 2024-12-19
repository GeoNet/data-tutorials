# Working with Volcano Data 

The files in this folder are Jupyter notebooks written in Python. They demonstrate some simple ways to access and use volcano data. Most data access is via [GeoNet's Tilde Time Series API](https://tilde.geonet.org.nz/) using the [Python programming language](https://www.python.org/). Because there is a wide variety of volcano data types, we have provided specialised tutorials.

## Python ##

**All notebooks use Python 3. We do not support Python 2.7.**

## The Tilde API ## 
When using Tilde, the volcano-specific notebooks only use the Tilde Data Endpoint. Refer to the [Tilde README file](../Tilde/README.md) for a more complete description of Tilde endpoints and response messages.

## Notebooks ##

| File | Description |
|------|-------------|
| [Envirosensor](./Volcano_data_envirosensor.ipynb) | Demonstrates how to retrieve and graph multiGas data, fumarole and water temperature data, water level data, self potential and ground temperature data, wind data, and rainfall data.|
| [GNSS](./Volcano_data_gnss.ipynb) | Demonstrates how to retrieve and graph GNSS data. These data are currently delivered by [FITS](https://fits.geonet.org.nz/api-docs/) but will move to Tilde |
| [Manually collected](./Volcano_data_manualcollect.ipynb) | Demonstrates how to retrieve and graph water chemistry data, airborne gas emission rate data, soil gas data, lake levelling (Lake Taupō) data, and how to create spreadsheet-like output files for water chemistry data.|
| [ScanDOAS](./Volcano_data_scandoas.ipynb) | Demonstrates how to retrieve and graph scanDOAS data, including working with data from multiple sensors.|
| [Data aggregation](./Volcano_data_aggregation.ipynb) | Demonstrates how to use Tilde's data aggregation functions with volcano data.|
| [Multi-domain data](./Volcano_data_multidomain.ipynb) | Demonstrates how to retrieve and graph data from more than one data domain. Covers Tilde data with [Volcanic Alert Level data](https://doi.org/10.21420/we5s-1n52), and Tilde data with [historic volcanic activity data](https://doi.org/10.21420/bw31-2x60).|
