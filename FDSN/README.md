# Working with FDSN Waveservers and FDSN Data #

The files in this folder are Jupyter notebooks written in Python. They demonstrate some simple ways to use [GeoNet's FDSN webservices](http://www.geonet.org.nz/data/tools/FDSN) using the Python [ObsPy module](https://github.com/obspy/obspy/wiki).

They apply to all data types available through FDSN:
- seismic
- acoustic-infrasound
- coastal sea level gauge

Other data types are available through other applications.

## Python ##

**All notebooks use Python 3. We do not support Python 2.7.**

## Waveform servers ##

GeoNet operates two FDSN waveform servers
- An archive server that holds verified data that are as complete as possible. If accessing waveform data through the dataselect service, a server can only be used for data at least 7 days old
- A near real-time server that holds unverified data for the last 8 days. This server hold only waveform data, and cannot be used for the event service or the station service. This server is as fast as possible, but may not be complete

Within ObsPy, a `client` is used to access a FDSN webserver.

The archive client is `https://service.geonet.org.nz`. Alternatively it can be referred to by the shortcut name `GEONET`, which will be mapped to the same URL.

The near real-time client is called `https://service-nrt.geonet.org.nz`, it does not have a shortcut name.

## Notebooks ##

| Notebook | Description |
|------|-------------|
| [Clients tutorial](FDSN_clients.ipynb) | Demonstrates different ways to manage multiple clients, the archive and near real-time clients|
| [Specific-event](FDSN_specific-event.ipynb) | Demonstrates how to get waveforms for a specific event using the event ID and utilising information returned from querying event and station services|
| [Dataselect service](FDSN_dataselect.ipynb) | Using the FDSN dataselect service to request waveform data|
| [Event service](FDSN_event.ipynb) | Using the FDSN event service to get event information and parse QuakeML|
| [Station service](FDSN_station.ipynb) | Using the FDSN station service to get station information and parse StationXML|
