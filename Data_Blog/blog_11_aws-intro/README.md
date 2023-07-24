# Introduction to GeoNet AWS Open Data bucket

Examples below use the AWS Command Line Interface. Refer to the official AWS documentation for additional funcionalities and instructions.

## List content
List all data domain available on the _geonet-open-data_ bucket
```
aws s3 ls --no-sign-request s3://geonet-open-data/
```

List all data available for the WEL station for the day 2023-100
```
aws s3 ls --no-sign-request s3://geonet-open-data/waveforms/miniseed/2023/2023.100/WEL.NZ/
```


## Download content

Copy one daily miniseed file to your local folder
```
aws s3 cp --no-sign-request s3://geonet-open-data/waveforms/miniseed/2023/2023.100/WEL.NZ/2023.100.WEL.10-HHE.NZ.D .
```

Copy all miniseed files available for a day to your local folder
```
aws s3 cp --no-sign-request --recursive s3://geonet-open-data/waveforms/miniseed/2023/2023.100/WEL.NZ/ .
```

## Sync content

Sync the bucket content for a specific prefix to your local copy and use wildcards to select what you want to download
```
aws s3 sync --no-sign-request s3://geonet-open-data/waveforms/miniseed/2023/2023.100/ . --exclude "*" --include "*WEL.NZ/*-HH?.NZ.D"
```


## add a download function to your python code

A little script you can use in your code is available [here](copy_miniseed.py).

