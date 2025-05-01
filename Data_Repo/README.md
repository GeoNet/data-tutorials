# Working with Data in the GeoNet Data Repository

The files in this folder are [Jupyter notebooks](https://jupyter.org/) written in the [Python programming language](https://www.python.org/). They demonstrate some simple ways to access and use data in the [GeoNet data repository](https://github.com/GeoNet/data/data-repo). For a wider discussion about the data repository, see a [data blog](https://www.geonet.org.nz/news/4qmVUyQIzpp2f00JuyKQ1Q) on the subject.

## Python ##

**All notebooks use Python 3. We do not support Python 2.7.**

## Notebooks ##

| File | Description |
|------|-------------|
| [Dart-triggers](./data_repo_dart-triggers.ipynb) | Demonstrates how to retrive the triggers file, select a trigger event, and graph it with the associated waveform data from [Tilde](https://tilde.geonet.org.nz/). |
| [Historic volcanic activity](./data-repo_historic-volcanic-activity.ipynb) | Demonstrates how to retrieve and graph historic volcanic activity data. Additional examples are available in a [notebook](https://github.com/GeoNet/data-tutorials/tree/main/Data_Blog/blog_05_visualize_eruption_catalogue) used in a related [data blog](https://www.geonet.org.nz/news/2DMtHEzmma5EqfMWmMvhjy). |
| [Moment tensors](./data-repo_moment-tensors.ipynb) | Demonstrates how to retrieve the moment tensor file, to plot a solution on a map, and to compare moment tensor magnitude, Mw, with magnitudes from the same event available through the [GeoNet FDSN webservice](https://www.geonet.org.nz/data/access/FDSN). |
| [Soil gas](./data_repo_soil-gas.ipynb) | Demonstrates how to retrieve a file from one soil gas survey, and plot the data on a photo basemap.|
| [Volcanic alert levels](./data_repo_volcanic-alert-levels.ipynb) | Demonstrates how to retrive a volcanic alert level file, and graph the UTC and NZST/NZDT versions. Additional examples are available in a [notebook](https://github.com/GeoNet/data-tutorials/tree/main/Data_Blog/blog_01_val) used in a related [data blog](https://www.geonet.org.nz/news/3fN5Mbo0RFkS8Bm0CmYcSl).|
