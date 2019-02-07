# Seismic Data
## Accessing Seismic Data in R ## 
R notebooks that will demonstrate some simple ways to use the GeoNet FDSN webservices in R.

|File                  | Description  | Output|
|--------------------- | ------|---------------------------------------|
|[Overview](R/Seismic_data_overview_using_FDSN_in_R.ipynb) | In this tutorial we will look at the work flow from knowing the data of the Seismic Event we wish to look at to getting data on this Seismic Event. | |
|[Event](R/Event_Data_using_FDSN_in_R.ipynb) |In this tutorial we find all the seismic events that happend in set time| <img src="R/event.png"> |
|[Station](R/Station_Data_using_FDSN_in_R.ipynb) |In this notebook we will look at the station active in a set time frame in a set area.| <img src="R/station.png"> |
|[Waveform Data](R/Get_waveform_data_using_FDSN_in_R.ipynb)|In this tutorial we will get the wavefrom data from one station.|<img src="R/waveform.png">|



## Accessing Seismic Data in Python ## 
Python notebooks will demonstrate some simple ways to use the GeoNet FDSN webservices in Python and with the Python module, ObsPy. Please note these examples use Python 3, so the syntax may differ slightly to Python 2.7. We recommend you use Python 3 as it has some important bug fixes.

| File | Description | Output |
|------|-------------|--------|
| [clients](Python/GeoNet_FDSN_demo_clients.ipynb) | Demostrates different ways to manage multiple clients,  the archive and near real-time clients. | 1 Trace(s) in Stream: NZ.WEL.10.HHZ 2018-11-18T01:20:32.853131Z - 2018-11-21T01:20:35.453131Z 100.0 Hz, 25920261 samples
| [general](Python/GeoNet_FDSN_demo_general.ipynb) | Demostrates how to get waveforms for a specific event using the event ID and utilising information returned from querying event and station services.  |<img src="Python/waveform.png">
| [dataselect](Python/GeoNet_FDSN_demo_dataselect.ipynb) | Examples of using the dataselect to request waveform data.  |<img src="Python/day_plot.png">
| [event](Python/GeoNet_FDSN_demo_event.ipynb) | Examples of using the event service to get event information and parse QuakeML. |<img src ="Python/event.png">
| [station](Python/GeoNet_FDSN_demo_station.ipynb) | Examples of using the station service to get station information and parse StationXML. | <img src="Python/station.png">
