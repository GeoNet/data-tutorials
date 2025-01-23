# Working with Tilde and it's Data 

The files in this folder are Jupyter notebooks written in Python. They demonstrate some simple ways to use [GeoNet's Tilde Time Series API](https://tilde.geonet.org.nz/) using the [Python programming language](https://www.python.org/).

They apply to all data domains available through Tilde:
- [coastal tsunami gauge](#section_tsun)
- [DART](#section_dart)
- [envirosensor](#section_envi)
- [GNSS](#section_gnss)

Other data types are available through other applications.

## Python ##

**All notebooks use Python 3. We do not support Python 2.7.**

## The Tilde API ## 
The notebooks use [version 3](https://tilde.geonet.org.nz/) of the Tilde API. If you have Python scripts that use version 1 or 2, we recommend that you upgrade to gain optimal functionality. You can check the differences between versions using the API documentation for [version 1](https://tilde.geonet.org.nz/v1/api-docs/), [version 2](https://tilde.geonet.org.nz/v2/api-docs/), and [version 3](https://tilde.geonet.org.nz/).

The Tilde API has three endpoints, each delivers a different kind of data:
- `data` delivers time series data
- `dataSummary` delivers information about what data are available
- `stats` delivers basic statistics about data

We have a Jupyter notebook for each API endpoint.

## Endpoints ##

### Data ###
The notebook makes a data request using a URL. We read the returned data into a [Pandas](https://pandas.pydata.org/) dataframe, from which data can be analysed and graphed.

We show how to :
- make a basic time-series graph of data
- do the same for aggregated data
- formatting data so it can be analysed using [ObsPy](https://github.com/obspy/obspy/wiki/); probably only useful for 15 sec DART data

By default, the API returns JSON. To get CSV, which is easier for time-series analysis, we need to use the [requests module](https://pypi.org/project/requests/), specifically `requests.get`. A response status code says whether we were successful in getting the data requested and why not if we were unsuccessful:
- 200 -- everything went okay, and the result has been returned (if any)
- 301 -- the server is redirecting you to a different endpoint. This can happen when a company switches domain names, or an endpoint name is changed.
- 400 -- the server thinks you made a bad request. This can happen when you don't send along the right data, among other things.
- 404 -- the resource you tried to access wasn't found on the server.

### DataSummary ###
The notebook makes a data request using a URL with data returned in JSON format that goes into a Python dictionary.

We show how to :
- get summary data for each data domain from the dictionary
- get a list of observation stations and their locations and to map them
- graph data availability, including time ranges with data

### Stats ###
The notebook makes a data request using a URL with data returned in JSON format that goes into a Python dictionary.

We show how to :
- get summary statistics for data from stations and how you can present those tidily
- graphically depict the data statistics

## Notebooks ##

| File | Description |
|------|-------------|
| [Data Endpoint](./Tilde_endpoint02-data.ipynb) | Demonstrates how to retrieve and graph data.|
| [Data-Summary Endpoint](./Tilde_endpoint01-dataSummary.ipynb) | Demonstrates how to find what data exists, and show that as a table, map, or graph. |
| [Statistics Endpoint](./Tilde_endpoint03-stats.ipynb) | Demonstrates how to get different statistics from a data set.|

## Accessing the Tilde API using Bash ##
A markdown file also shows a few examples of how to access the Tilde API using bash scripting. This can be found here: [Bash Tutorial](Bash_Tilde_Access.md).

## Data Domains ##

The following data domains are available through the Tilde API, and can be interrogated and analysed using the Jupyter notebooks.

### Coastal tsunami gauge network ### <a id="section_tsun"></a>

GeoNet operates 18 tsunami gauges on the coast. Tilde contains a 15 second down-sampled verion of the original 1 second sampled data. Data are available as water-height and water-height-detided, which has had the effects of tides removed.

### DART ### <a id="section_dart"></a>

GeoNet uses the 12 DART stations deployed offshore New Zealand and around the Southwestern Pacific Ocean to monitor ocean height. When a change has been detected of a certain magnitude, the DART will "trigger" and go into a heightened detection mode. The DARTs have two operational reporting modes; standard and event. When in standard reporting mode, the BPR (bottom pressure recorder) and buoy system send four six-hour bundles of 15 minute water height values. When in event reporting mode, BPR data are sampled at 15 second intervals and are sent more frequently. The buoy surface location (latitude and longitude) will also be sent daily.

Tilde provides access to the 15 minutes and 15 second sampled data, and `raw` 15 second data retrieved when a DART is serviced. As part of the `raw` BPR data, `water-temperature` and `water-pressure` data is also available after a DART has been serviced. DART data are available showing water-height and water-height after the effect of tidal chnages have been removed. You can replace `water-height` with `water-height-detided` in any tutorial to get detided data.

For more DART information see the GeoNet page: https://www.geonet.org.nz/tsunami/dart

Please use the following Digital Object Identifiers https://doi.org/10.21420/8TCZ-TV02 when using DART data.

### Envirosensor network <a id="section_envi"></a>

GeoNet envirosensor network measure various factors related to volcanic activity, and factors that influence the movement of landslides at a rate of one observation every 10 minutes. These include measuring: fumarole temperature, temperature and height of volcanic lakes and springs, rainfall, soil moisture, and displacement across cracks in landslides. Most of these sites measure 2-3 of these factors. Different aspects can also be selected if there are more than one similar measure at a site, for example there is a south-vent and an east-vent aspect for fumarole temperature at site TO006 at Mt Tongariro, and soil moisture is measured by a single sensor at eight different depths at a site at Fox Glacier.

### GNSS <a id="section_gnss"></a>

GeoNet has a network of two hundreds GNSS stations deployed all around New Zealand to monitor ground deformation. The position of every station is computed on daily basis and provided in the form of time series of diplacement from a reference position in the `north`, `east` and `up` directions in meters.

Tilde provides access to the `displacement` data which has not been corrected for any natural or antropogenic effects.

For more GNSS information see the GeoNet page: https://www.geonet.org.nz/data/types/geodetic.

Please use the follow DOI https://doi.org/10.21420/30F4-1A55?x=y when using GNSS time series data.