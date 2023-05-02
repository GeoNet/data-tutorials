# GeoNet Data distributed via AWS Open Data Program

## <a name="introduction"></a>Introduction
A copy of much of GeoNet's raw data is held by [Amazon Web Services (AWS) Open Data Program](https://registry.opendata.aws/geonet/).

This document provides examples of simple commands to access GeoNet data through the AWS Open Data Program. It also summarises each of the data sets and how they are structured.

### Data sets
The [GeoNet](https://www.geonet.org.nz) sensor network is a geophysical network used to monitor earthquakes, volcanoes, tsunami, and landslides in New Zealand.
The sensor network is made up of different types of equipments, and raw data are collected and made available for scientific research and geohazards monitoring.
The AWS Open Data dataset currently provides:
- [Camera images](#camera)
- [Coastal gauge data](#coastal)
- [GNSS data](#gnss)
- [Seismic data products](#seismoprod)
- [Digital waveform data](#waveform)
- [Time Series data](#tseries)

With plans to add further data types in the future.

## Data access commands
The simplest way to access data from GeoNet's AWS Open Data storage is to use the [AWS command line interface (CLI)](https://aws.amazon.com/cli/). There are [install instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) for the CLI for the three common operating systems.

### A. To list the top level data "folders"

`aws s3 --no-sign-request ls s3://geonet-open-data/`
- `aws s3` says we want to issue a aws command that acts on S3 bucket storage
- `--no-sign-request` is required as users do not need to sign in to access AWS Open Data
- `ls` says list the files and directories
- `s3://geonet-open-data/` identifies to GeoNet's data in AWS Open Data
Producing the following output:
```
PRE camera/
PRE coastal/
PRE gnss/
PRE seismic-products/
PRE time-series/
PRE waveforms/
```

### B. Download data "folders"
This command uses AWS CLI's `sync` command to "download" a month's worth of data from one "folder".
`aws s3 --no-sign-request sync s3://geonet-open-data/time-series/tilde/v3/domain=coastal/station=AUCT/name=water-height/sensorcode=40/method=15s/aspect=nil/start=2023-01-01/ scratch`
- `aws s3` says we want to issue a aws command that acts on S3 bucket storage
- `--no-sign-request` is required as users do not need to sign in to access AWS Open Data
- `sync` says synchronise the folder, effectively this copies it to your local computer
- `s3://geonet-open-data/` identifies to GeoNet's data in AWS Open Data
- `time-series/tilde/v3/domain=coastal/station=AUCT/name=water-height/sensorcode=40/method=15s/aspect=nil/start=2023-01-01/` identifies the resources (folder) to synchronise
- `scratch` is where to store the folder on your local computer
There will be no error messages, but no output will be written to the terminal. A file `coastal.AUCT.water-height.40.15s.nil.m.m.2023-01-01T00:00:00Z.csv.gz` will be generated.

## Data description ##
### <a name="camera"></a>Camera images
Camera images recorded at webcams installed to monitor active New Zealand volcanoes. The dataset also include data from three webcams that documented the Christchurch rebuild from 2011 to 2019.

Camera data include images in jpg format.

Additional information around this dataset can be found on the [GeoNet camera images website page](https://www.geonet.org.nz/data/types/camera).

All camera images are available under the bucket and prefix `s3://geonet-open-data/camera/`.

prefix | content
-- | --
`camera/building/` | camera images recorded at 10 minutes intervals installed in Christchurch between 2011 and 2019
`camera/volcano/` | camera images recorded at 10 minutes intervals installed around active volcanoes

Data are organized by site code and date, and objects' prefixes are formed as:

`camera/[building|volcano]/images/[yyyy]/[SITE]/[SITE].[VC]/[yyyy].[doy]/[yyyy].[doy].[hhmm].[ss].[SITE].[VC].jpg`, where:
  - `yyyy` is year (four digits)
  - `doy` is day of year (three digits)
  - `hhmm` is the hour and minute (four digits)
  - `ss` is the second (two digits, generally `00`)
  - `SITE` is the camera station 4 character code, upper case
  - `VC` is camera view code (two digits)

### <a name="coastal"></a>Coastal gauge data
Relative coastal sea level data measured by tsunami monitoring gauges around New Zealand coastlines. Data are in Character form for the Representation and EXchange of meteorological data (CREX) format. The network is operated in partnership with [LINZ](http://linz.govt.nz).

Coastal data include two sets of daily files containing measurements and quality control data.

Additional information around this dataset can be found on the [GeoNet Tide Gauge website page](https://www.geonet.org.nz/data/types/tidal_gauges).

All coastal data are available under the bucket and prefix `s3://geonet-open-data/coastal/`

prefix | content
-- | --
`coastal/crex/` | 24 hours long, 1 minute sampled relative sea level and quality control data in CREX format

Data are organized by date, and objects' prefixes are formed as:

  `coastal/crex/[yyyy]/[yyyy].[doy]/[SITE].TG/[yyyy].[doy].[SITE].[40|41]-CRX.TG.[ext]`, where:
  - `yyyy` is year (four digits)
  - `doy` is day of year (three digits)
  - `SITE` is the Tsunami gauge station 4 character code, upper case
  - `[40|41]` is the tsunami monitoring gauge code, 40 for the primary gauge, 41 for the backup gauge
  - `ext` is the file extension, `D` for relative sea level data, `D.qc` for quality data

Please use the following Digital Object Identifiers https://doi.org/10.21420/4RAS-J272 when using coastal gauge data.

### <a name="gnss"></a>GNSS data
Global Navigation Satellite System data recorded by the [New Zealand continuous GNSS ground network](https://www.geonet.org.nz/data/gnss/map) made by the GeoNet and [PositioNZ](http://linz.govt.nz) GNSS networks, with contribution from [Otago University](http://www.otago.ac.nz/surveying) and [NIWA](https://www.niwa.co.nz/).
GNSS data include:
- [raw data in RINEX format](#gnssrinex)
- [raw data in proprietary format](#gnssraw)
- [high rate GNSS data for significant geohazard events](#gnssevent)
- [GNSS station metadata](#gnssmeta)
- [local tie-in survey conducted during equipment changes](#gnsstie)

Additional information around these datasets can be found on the [GeoNet GNSS data website page](https://www.geonet.org.nz/data/types/geodetic).

All GNSS data are available under the bucket and prefix `s3://geonet-open-data/gnss/`

Please use the following Digital Object Identifiers https://doi.org/10.21420/RXKE-AZ44 when using GNSS data.

#### <a name="gnssrinex"></a>Raw data in RINEX format
The primary dataset of this collection is made by raw data in Receiver INdependent EXchange format (RINEX).

RINEX data are provided in version 2.11 and available as:

prefix | content
-- | --
`gnss/rinex/` | 24 hours long, 30 second sampled compressed RINEX
`gnss/rinexhourly/` | 1 hour long, 30 second sampled compressed RINEX
`gnss/rinex1Hz/` | 15 minutes long, 1 second sampled uncompressed RINEX (for the last 2 months and 20% of the stations)

- 30 second sampled data are organized by date, and object prefix are formed as:
  `gnss/[rinex|rinexhourly]/yyyy/doy/[site][doy][0|a-x].[yy]o.gz`, where:
  - `yyyy` is year (four digits)
  - `doy` is day of year (three digits)
  - `site` is the GNSS station 4 character code, lower case
  - `[0|a-x]` indicate the start time of the observation period. `0` for daily files, a lower-case letter for hourly files with letter `[a-x]` indicating the n-th hour in the day, e.g. `a` for `00:00 to 00:59`, `b` for `01:00 to 01:59`, and so on.
  - `yy` is last two digits of the year

- 1 second sampled, 15 minutes long data are organized by date, and objects' prefix are formed as:
  `gnss/rinex1Hz/yyyy/doy/[SITE][doy][A-X][MM].[yy]O`, where:
  - `yyyy` is year (four digits)
  - `doy` is day of year (three digits)
  - `SITE` is the GNSS station 4 character code, upper case
  - `[A-X]` indicate the start time of the observation period. Upper case letter `[A-X]` for the n-th hour in the day `*`
  - `MM` is the minutes of the n-th hour, start of the observation period (`[00|15|30|45]`) `*`
  - `yy` is last two digits of the year

`*`: For example, `[A-X]` and `MM` combined are used to indicate: `A00` for `00:00:00 to 00:14:59`, `B15` for `01:15:00 to 01:29:59`, and so on.

Please use the following Digital Object Identifier https://doi.org/10.21420/RXKE-AZ44 when using GNSS RINEX Data Products.

#### <a name="gnssraw"></a>Raw data in proprietary format
GNSS raw data in proprietary format are available as hourly files, at 30 second sampling rate.

prefix | content
-- | --
`gnss/raw/` | 1 hour long, 30 second sampled binary files

Data are organized by date, and objects' prefixes are formed as:

  `gnss/raw/yyyy/doy/[SITE][YYYY][mm][dd][HH][MM]a.ext`, where:
  - `yyyy` is year (four digits)
  - `doy` is day of year (three digits)
  - `SITE` is the GNSS station 4 character code, upper case
  - `mm` is month (two digits)
  - `dd` is day of month (two digits)
  - `HH` is hour (usually 00)
  - `MM` is minute of the hour (usually 00)
  - `a` is an internal convention used to indicate 30s sampling rate of the data
  - `ext` is the file extension, and indicate the proprietary format and GNSS receiver manufacturer. For most recent data (2019 onward) the extension is `T02`, older dataset will have different extension based on GNSS receiver manufacturer.

This dataset contains the same GNSS data available in [RINEX](#gnssrinex) format. The exception is for a subset of stations for which, from January 2019 onward, additional GNSS constellations that are not available in the current RINEX format can be derived by converting the proprietary raw format.

Please use the following Digital Object Identifier https://doi.org/10.21420/TMHV-0T46 when using GNSS Raw Data Products.

#### <a name="gnssevent"></a>High rate GNSS data for significant geohazard events
High rate (1 second and 0.1 second sampling rate) retrieved for major geologic events, starting from 2013. Please refer to the [GeoNet website](https://www.geonet.org.nz/data/supplementary/gnss_high_rate_data_access) for additional details, disclaimer and a list of events.

Data are available under the prefix `gnss/event.highrate` and organized as follow:

prefix | content
-- | --
`gnss/event.highrate/1hz/rinex/` | 1 sec sampled data, RINEX
`gnss/event.highrate/1hz/raw/` | 1 sec sampled data, proprietary binary
`gnss/event.highrate/10hz/rinex/` | 0.1 sec sampled data, RINEX
`gnss/event.highrate/10hz/raw/` | 0.1 sec sampled data, proprietary binary

Same naming convention used in [RINEX](#gnssrinex) and [raw](#gnssraw) is used at subsequent levels.
  `gnss/event.highrate/[1hz|10hz]/[raw|rinex]/yyyy/doy/[rawfilename|rinexfilename]`

Please use the following Digital Object Identifier https://doi.org/10.21420/NQYC-EG34 when using GNSS High Rate Event Products.

#### <a name="gnssmeta"></a>GNSS station metadata
Sensor and station metadata of GNSS stations.
The following formats are available:

prefix | content
-- | --
`gnss/sitelogs/logs/` | individual station sitelogs, International GNSS Service text format
`gnss/sitelogs/xml/` | individual station sitelogs, XML (Sopac2004) format
`gnss/sitelogs/station.info.geonet` | metadata of all GeoNet GNSS stations, in GAMIT/GlobK station metadata information text format

Individual station sitelogs naming are formed as:

  `[site]_[yyyy][mm][dd].[log|xml]` where:
  - `site` is the GNSS station 4 character code, lower case
  - `[yyyy][mm][dd]` is the year month day when the last equipment change was introduced

Following IGS standards, previous sitelogs are also available, but the most recent one always contain all metadata changes.


#### <a name="gnsstie"></a>Local tie-in survey
Local tie-in survey are conducted when GNSS antenna is changed to have an additional control of the offset introduced in the daily ground deformation time series obtained by processing raw GNSS data.

prexix | content
-- | --
`gnss/site_ties/` | data from tie-in survey conducted on a site

Data are organized in "folders":
  `[site]_[yyyy][mm][dd]/` where:
  - `site` is the GNSS station 4 character code (lowercase) where local tie was conducted
  - `[yyyy][mm][dd]` is the year month day when the antenna was changed

Each folder contains a README file that provide details of the antenna change, raw and rinex data measured on the tie-in temporary station.
Temporary tie-in data are named using the first 3 characters of the continuous site, followed by "1".

### <a name="seismoprod"></a>Seismic data products
Dataset derived by the processing and analysis of raw data recorded by the GeoNet seismic sensors networks.

Data are provided in various formats depending on the application and include:

- [Strong Motion data products](#seismoprod-strong)

Additional information around these datasets can be found on the [GeoNet website](https://www.geonet.org.nz/).

All Seismic derived data products are available under the bucket and prefix `s3://geonet-open-data/seismic-products/`.

#### <a name="seismoprod-strong"></a>Strong Motion data products
Data products derived from the GeoNet strong motion network for earthquakes with magnitude 4.0 and above.

Additional information around these datasets can be found on the GeoNet [Strong Motion tool page](https://strongmotion.geonet.org.nz) and [Strong Motion data products page](https://www.geonet.org.nz/data/types/strong_motion).

Strong Motion data products include current and legacy time series, acceleration, spectra response and summary files, and provided in compressed csv, geocsv and pdf formats.

prexix | content
-- | --
`seismic-products/strong-motion/geocsv` | current strong motion data products (from 1998)
`seismic-products/strong-motion/volume-products` | legacy strong motion data products (1966-2021)

Current strong motion data products are organized by type, year and earthquake event identifier and formed as:

`seismic-products/strong-motion/geocsv/[TYPE]/id_prefix=[yyyy]/[eventID].[TYPE].geocsv.csv.zip`, where:
  - `TYPE` is the data product type [filtered-ts|response-spectra|summary-latest|summary-version|unfiltered-ts]
  - `eventID` is the earthquake identifier as defined in the GeoNet earthquake catalogue
  - `yyyy` is the year (4 digits), `0000` for pre-2012 products

For further details on legacy datasets (`volume-products`) please refer to the GeoNet [volume products format description webpage](https://www.geonet.org.nz/data/supplementary/strong_motion_file_formats).

Please use the following Digital Object Identifier https://doi.org/10.21420/X0MD-MV58 when using Strong Motion Data Products.

### <a name="waveform"></a>Digital waveform data
Raw waveform data recorded by the GeoNet sensor networks.

Data are provided in various formats depending on the application and include:

- [miniseed waveform data](#wave-miniseed)
- [Strong Motion waveform data](#wave-strong)

Additional information around these datasets can be found on the [GeoNet website](https://www.geonet.org.nz/).

All waveform raw datasets are available under the bucket and prefix `s3://geonet-open-data/waveforms/`.


#### <a name="wave-miniseed"></a>Miniseed waveform data
Continuous waveform data recorded by the GeoNet sensor network (seismic, acoustic, tsunami monitoring gauges). Data are provided in miniSEED format.

Sync of miniseed data from the GeoNet archive to the open data bucket is still ongoing.

Additional information around this dataset can be found on the [GeoNet seismic waveform data page](https://www.geonet.org.nz/data/types/seismic_waveforms).

All miniseed data are available under the bucket and prefix `s3://geonet-open-data/waveforms/miniseed/`.

prexix | content
-- | --
`waveforms/miniseed/` | 24 hours long miniSEED data at different sampling rates

Data are organized by date, and objects' prefixes are formed as:

`waveforms/miniseed/[yyyy]/[yyyy].[doy]/[SITE].[NC]/[yyyy].[doy].[SITE].[NC]-[CHA].[LC].D` where:
  - `yyyy` is year (four digits)
  - `doy` is day of year (three digits)
  - `SITE` is the 3 or 4 characters site code, upper case
  - `NC` is the 2 characters network code, upper case
  - `LC` is the 2 characters location code, upper case
  - `CHA` is the 3 characters channel code, upper case

For additional details on miniSEED data format please refer to the [SEED FDSN reference manual](https://www.fdsn.org/publications/).


#### <a name="wave-strong"></a>Strong Motion waveform data
Triggered waveform data recorded by the GeoNet strong motion network. Data are provided in binary format.

Additional information can be found on the GeoNet [Strong Motion Data Products page](https://www.geonet.org.nz/data/types/strong_motion).

All strong motion triggered waveform data are available under the bucket and prefix `s3://geonet-open-data/waveforms/strong-motion/`

prexix | content
-- | --
`waveforms/strong-motion/` | triggered event data

Data are organized by equipment type and date and objects' prefixes are formed as:

`waveforms/strong-motion/[type]/[yyyy]/[yyyy].[doy]/[SITE]/[yyyy].[doy].[hhmm].[ss].[SITE].[SN].[ext]`, where:
  - `type` is the instrument type `[altus|building|cusp]`
  - `yyyy` is year (four digits)
  - `doy` is day of year (three digits)
  - `hhmm` is the hour and minute (four digits)
  - `ss` is the second (two digits, generally `00`)
  - `SITE` is the 3 or 4 characters site code, upper case
  - `SN` is the instrument serial number
  - `ext` is the file extension and format `[evt|csd|xml|csv.gz]`



### <a name="tseries"></a>Time Series data

Time series data derived from the GeoNet sensor network.

Data are provided in commonly used text open file format and include:

- [Tilde time series data](#tilde)

Additional information around this dataset can be found on the [GeoNet website](https://www.geonet.org.nz/).

All time series data are available under the bucket and prefix `s3://geonet-open-data/time-series/`.

#### <a name="tilde"></a>Tilde Time Series data
Time series data derived from GeoNet sensor network, repackaged and formatted via the GeoNet Tilde application.

Details on Tilde data name format can be found on the [GeoNet Tilde API website page](https://tilde.geonet.org.nz/).
Details on available datasets can be found on the [GeoNet Tilde Data Discovery website page](https://tilde.geonet.org.nz/ui/data-exploration).

This dataset is the same one that can be obtained from the Tilde API _data_ endpoint. For large data requests and bulk downloads, users are recommended to download data from this AWS Open Data bucket.

Data are provided in gzip compressed csv (Comma Separated Values) format.

All time series data are available under the bucket and prefix `s3://geonet-open-data/time-series/tilde/`.

prefix | content
-- | --
`time-series/tilde/` | Tilde time series data

The Tilde application was recently released in 2021, so the format of this dataset might change in the future. To allow our users to migrate their downstream procedures, object prefixes will include versioning. 

For this dataset, object prefixes are following an _hive style_ partitioning.

Data are organized by version, domain, station, time series name, sensor code, time series parameters (method and aspect) and time.

Objects' prefixes are formed as:
```
time-series/tilde/[v]/domain=[domainkey]/                         \
 station=[stationkey]/name=[namekey]/sensorcode=[sensorcodekey]/  \
 method=[methodkey]/aspect=[aspectkey]/start=[YYYY-MM-DD]/        \
 [domainkey].[stationkey].[namekey].[sensorcodekey].[methodkey].[aspectkey].[unit].[errorunit].[YYYY-MM-DD]T00:00:00Z.csv.gz
```

where:
 - `v` is the tilde time series archive version number (currently v3)
 - `domainkey` is the domain name, used to describe the type of sensor recording the time series
 - `stationkey` is the station identifier
 - `namekey` is the time series name, used to describe the type of measurement
 - `sensorcodekey` is the sensor code, used when there are multiple sensors at the same station
 - `methodkey` is the collection method or sampling rate
 - `aspectkey` is the time series aspect, used to describe different features of the time series derived with the same method
 - `YYYY-MM-DD` is first value for the windowed time series (year, month, day)
 - `unit` is the unit used for time series values
 - `errorunit` is the unit used for time series errors


Below some examples of possible key values.

key | values
-- | --
`v` | v3
`domainkey` | `[coastal/dart/envirosensor]`
`stationkey` | 3 to 5 alphanumeric characters
`namekey` | `[water-height/water-heigh-detided/soil-moisture/...]`; currently up to 28 different name keys
`sensorcodekey` | 2 or 3 digits
`methodkey` | `[15m/15s/avg/max/min/raw/snapshot/tot]` currently
`aspectkey` | `[10-cm/x-axis/at-source/east-vent/...]` or `nil`; currently up to 28 different aspect keys
`YYYY-MM-DD` | 4 digits year, 2 digits month, 2 digits day of month
`unit` | `[deg/degC/hPa/kPa/m/mm/mps/mV/percent]`
`errorunit` | `[deg/degC/hPa/kPa/m/mm/mps/mV/percent]`

The values listed above are combined depending on the name of the time series.
For example, the `water-height` and `soil-moisture` time series, will only have these combinations available:

name | domain | method | aspect | unit
-----|--------|--------|--------|-----
water-height | coastal/dart | 15m/15s/raw | nil | m
soil-moisture | envirosensor | snapshot | 10-cm/20-cm/30-cm/40-cm/50-cm/60-cm/70-cm/80-cm | percent

We are increasing the number of derived time series distributed via Tilde, so the list below will grow in time.

We recommend to refer to the [Tilde Data Discovery page](https://tilde.geonet.org.nz/ui/data-exploration) for an up-to-date and quick overview of available datasets and possible prefix combinations.
