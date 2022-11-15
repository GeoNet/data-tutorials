# Accessing the Tilde API using Bash 

The purpose of this tutorial is to illustrate how to access Tilde using Bash within a command line terminal. Within this file we will use the DART Network to illustrate the different examples, but any domain currently existing within Tilde can be used.   

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

To visualise the Data Summary details separated by the entry:
`curl ${ip}/${v}/dataSummary/ | jq -r .` 

To print a list of the stations:
`curl --silent "${ip}/${v}/dataSummary/dart" | jq -r '.domain[] | .stations[] | .station_name'` 

To visualise for a particular site the different entries. This example is for NZE but to substitute for different sites, change the "station=MZE" section.  
`curl "${ip}/${v}/dataSummary/dart?station=NZE" | jq -r .` 
 

## Accessing the Data Endpoint 

A few examples on how to access the Data Endpoint. For DART, this can also be found using python in the following notebook [DART Data](DART/TILDE_endpoint02-data_DART.ipynb).

Without setting the {ip} and {v} parameters this can also be run like this:
`curl -o dart.csv -H "Accept:text/csv" https://tilde.geonet.org.nz/v3/data/dart/NZE/water-height/-/15m/nil/latest/1d`

The following examples will need to have the {ip} and {v} parameters specified. 
To downloading the latest day of water-height data for NZE of 15m data and saving as a csv file:  
`curl -o dart1.csv -H "Accept:text/csv" "${ip}/${v}/data/dart/NZE/water-height/41/15m/nil/latest/1d"` 

If the sensorcodes are not known (as these are dependent on the voyage numner) it is often easiest to leave sensor codes blank by using “-“: 
`curl -o dart1.csv -H "Accept:text/csv" "${ip}/${v}/data/dart/NZE/water-height/-/15m/nil/latest/1d"` 

Printing the latest 15m data (in the last 6 hours) for NZE:
`curl "${ip}/${v}/data/dart/NZE/water-height/40/15m/nil/latest/6h" |  jq -r .` 

Printing the data with a specific time period for NZE: 
`curl "${ip}/${v}/data/dart/NZE/water-height/40/15m/nil/2021-02-10/2021-02-11" |  jq -r .` 

Printing the number of 15s records for a specific time period for NZE:
`curl "${ip}/${v}/data/dart/NZE/water-height/40/15s/nil/2021-02-10/2021-02-11" |  jq -r '.[] | .data[] | "\(.ts)\t\(.value)"' | wc -l` 

Printing all of the records for a specific time period for NZE: 
`curl "${ip}/${v}/data/dart/NZE/water-height/-/-/-/2021-02-10/2021-02-11" |  jq -r '.[] | .data[] | "\(.ts)\t\(.value)"' | wc -l` 
