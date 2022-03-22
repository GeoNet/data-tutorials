# Data Tutorials

The purpose of this repository is to provide a home for several Data tutorials written to improve the accesibility of the different GeoNet's data sets. This repository provides an easy way to access the tutorials, versioning and allows the users to suggest changes or improvements.

The files in these folders are [Jupyter notebooks](https://jupyter.org/) that will demonstrate some simple ways to retrieve data from different services such as: FDSN, FITS, TILDE, etc. in Python and R programming languages. 

## Summary of Tutorials

| Data type  | Description   |
| ------------- | ------------- |
| [GNSS Data](GNSS_Data) | Demostrative tutorials to retrieve and perform basics task with GNSS Data, mostly with the use of FITS API. The Tutorials are presented in Jupyter notebooks written in Python and R Programming languages.|
| [Seismic Data](Seismic_Data) | Demostrative tutorials showing how to get data through the different FDSN web services (Dataselect, Station and Event). The Tutorials are presented in Jupyter notebooks written in Python and R Programming languages.|
| [Tide Gauge Data](Tide_Gauge_Data) | Demonstrative tutorials to get water level sensor data. The Tutorials are presented in Jupyter notebooks written in Python.|
| [TILDE](TILDE) | Demonstrative tutorials showing how to get DART data through the TILDE API. The Tutorials are presented in Jupyter notebooks written in Python.|
| [Volcano Data](Volcano_Data) | Demostrative tutorials to access Volcano Data with the use of FITS API and FDSN Web services. The Tutorials are presented in Jupyter notebooks written in Python and R Programming languages.|

## How to Run Tutorials
There are 3 files in this GitHub repository to help run these tutorials.
- The [**environment.yml**](environment.yml) file installs everything under dependencies using `conda install -c conda-forge (packagename)`  This is used to install the Python packages.
- [**install.R**](install.R) is R code for installing all R packages used in these tutorials
- [**runtime.txt**](runtime.txt) This file is for binder. Every day there is a snapshot of R taken. This install the snapshot of R taken on the date in this file. 

### 1. Install miniforge.
Install miniforge through this link https://github.com/conda-forge/miniforge for your specific operating system. This can be done on Windows, Mac, and Linux. Once installed, activate the `base` environment by running `conda activate base`, from here is it also best practice to run the following lines: 

`conda config --set channel_priority strict`

`conda config --set auto_activate_base false`

By setting a strict channel priority, this can often speed up conda operations and reduce package incompatibility problems and is often recommended as a default. By setting auto activate base to false, this means that whenever you open a command prompt, conda won't be automatically activated.

**Next we want to clone the git data-tutorials repository**

`git clone https://github.com/GeoNet/data-tutorials.git`

`cd data-tutorials`

**Install the environment file**

`conda env create -f environment.yml`

And then activate this environment 

`conda activate GeoNet`

**Install the following packages if using R**

`conda install -c conda-forge r-base`

`conda install -c conda-forge  r-irkernel`

Run the R script to install all R packages. 

`Rscript install.R`



**Open Jupyter notebook**

`jupyter notebook`

To reopen jupyter notebooks when opening a new command prompt, navigate to your working directory and run,

`conda activate base`

`conda activate GeoNet`

`jupyter notebook`

**Closing notebooks and environments**

Close the web browser and then CTRL-C in terminal, and type 'y' when asked to confirm if you'd like to close the notebook. Then run:

`conda deactivate` To close the 'GeoNet' environment

`conda deactivate` To close the 'base' environment

### 2. In your preferred GUI (Graphical User Interface)
If you wish to run just the code and not the notebooks you can use your own GUI for Python or R

**In your preferred R GUI**

Run the code in the file https://github.com/GeoNet/data-tutorials/blob/master/install.R to install all packages used in all notebooks. Code can then be copied across. Make sure to call packages and run any other code that may be in the beginning of the notebook but is needed for running other code in the notebook. 

**In your preferred Python GUI**

You will need to install all packages under dependencies in the file https://github.com/GeoNet/data-tutorials/blob/master/environment.yml. Some of these packages can't be installed using `pip` and as such may have to be installed from there GitHub.  Code can then be copied across. Make sure to call packages and run any other code that may be in the beginning of the notebook but is needed for running other code in the notebook.  

### 3. In Binder [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/GeoNet/data-tutorials/master)

My Binder is an experimental project still in beta phase that can be used to run notebooks. Any issues with binder can be reported at their project's GitHub  https://github.com/jupyterhub/binderhub 

[My Binder](https://mybinder.org/) is a free online tool to be able to run jupyter notebooks without installing anything on your computer. Binder will launch in your internet browser. 
There are some important things to note when using binder. 

- Binder can take up to 2 minutes to start
- The things you do in binder will **NOT save** for the next time you open binder
- Binder has a **time limit**. If the tab is **inactive** for more than 10 minutes (not running code or have someone scroll on the page) it will time out and you will need to restart it. 

If you want to save a csv or image you have made in binder click on the box next to it (in the file select) and click download. 
You can also do this with the notebook itself.
If you want to run a notebook you have save to your computer in binder you can click upload and upload a saved notebook from your computer.
Each cell of code can be run with `shift + enter` or you can run the entire notebook by selecting `cell`, `Run All` in the toolbar.
The Following link should open the Jupyter Notebook in your browser using Binder:
https://mybinder.org/v2/gh/GeoNet/data-tutorials/master
