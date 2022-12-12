# Accessing the Tilde API using Bash 

The purpose of this tutorial is to illustrate how to access Tilde using Bash within a command line terminal. Within this file we will use the DART Network to illustrate the different examples, but any domain currently existing within Tilde can be used. In this tutorial we interrogate Tilde API using curl and jq libraries. `curl` is a tool to transfer data via HTTPs and `jq` is a JSON format interpreter.  

A good way to start would be running the following lines which set up a few base parameters. These specify the source location for tilde (`ip`) and also specify the current version (`v`).

```
#! /bin/bash 
ip=https://tilde.geonet.org.nz 
v=v3 
```
To access the API documentation the following line can be run:
`curl ${ip}/v3/api-docs/`  

## Accessing the Data Summary Endpoint

A few examples on how to access the Data Summary Endpoint. This can also be found using python in the following notebook for [DART Data Summary](DART/TILDE_endpoint01-dataSummary_DART.ipynb).

To visualise the Data Summary details separated by the entry. This will return a quick overview of data domains and how many data are available for each domain. jq can be used to manipulate, reorganise and extract information from a JSON file. For example, [to print a list of the stations]:
`curl ${ip}/${v}/dataSummary/ | jq -r .` 

In this example, jq is extracting all JSON fields that have info on available stations and then only providing the values contained in _station_:
`curl --silent "${ip}/${v}/dataSummary/dart" | jq -r '.domain[] | .stations[] | .station'` 

To visualise all metadata available via Tilde for a specific site, you can use the available API endpoint and then reformat the output with jq. This example is for NZE but to substitute for different sites or domains, change the domain name and the "station=NZE" section.  
`curl "${ip}/${v}/dataSummary/dart?station=NZE" | jq -r .` 
 

## Accessing the Data Endpoint 

To download dart water-height data sampled at 15m from NZE, in csv format, with unknown sensor codes (as these are dependent on the voyage number), and save them in a local file named dart.csv:
`curl -o dart.csv -H "Accept:text/csv" "${ip}/${v}/data/dart/NZE/water-height/-/15m/nil/latest/1d"`

The following examples will need to have the {ip} and {v} parameters specified. 
To downloading the latest day (known sensor code) of water-height data for NZE of 15m data and saving as a csv file:  
`curl -o dart1.csv -H "Accept:text/csv" "${ip}/${v}/data/dart/NZE/water-height/41/15m/nil/latest/1d"` 

Printing the latest 15m data (in the last 6 hours) for NZE:
`curl "${ip}/${v}/data/dart/NZE/water-height/41/15m/nil/latest/6h" |  jq -r .` 

Printing the data with a specific time period for NZE: 
`curl "${ip}/${v}/data/dart/NZE/water-height/40/15m/nil/2021-02-10/2021-02-11" |  jq -r .` 

Printing the number of 15s records for a specific time period for NZE:
`curl "${ip}/${v}/data/dart/NZE/water-height/40/15s/nil/2021-02-10/2021-02-11" |  jq -r '.[] | .data[] | "\(.ts)\t\(.value)"' | wc -l` 

Printing all of the records for a specific time period for NZE: 
`curl "${ip}/${v}/data/dart/NZE/water-height/-/-/-/2021-02-10/2021-02-11" | jq -r '.[] | .data[] | "\(.ts)\t\(.val)"'`
