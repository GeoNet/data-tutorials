"""
copy miniseed files from AWS Open Data bucket to a local host
"""

import boto3
import os
from botocore import UNSIGNED
from botocore.config import Config
from pathlib import Path


s3 = boto3.client('s3', config=Config(signature_version=UNSIGNED))
bucket = 'geonet-open-data'
prefix = 'waveforms/miniseed/2023/2023.010/WEL.NZ/'
homedir = os.environ['HOME']
localfolder = homedir+'/tmp-aws/'


# Prepare list of miniseed file keys
keys = []
paginator = s3.get_paginator('list_objects_v2')
page_iterator = paginator.paginate(Bucket=bucket, Prefix=prefix)
for page in page_iterator:
    for object in page['Contents']:
        if object['Size'] > 0:
            keys.append(object['Key'])
for key in keys:
    print("downloading", key)
    localfile = Path(localfolder+key)
    localfile.parent.mkdir(exist_ok=True, parents=True)
    with open(localfile, 'wb') as data:
        s3.download_fileobj(bucket,key,data)
