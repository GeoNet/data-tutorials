# Data Tutorials

The purpose of this repository is to provide a home for several data tutorials written to improve the accesibility of the different GeoNet data sets. This repository is an easy way to access the tutorials, provides versioning and allows users to suggest changes or improvements.

The tutorials in this repository are mostly [Jupyter notebook](https://jupyter.org/) files. They demonstrate some simple ways to retrieve and work with data from different GeoNet services such as: FDSN, Tilde, etc. Most are written in the Python programming language. Older versions of some notebooks were written in the R programming language. We are no longer supporting these, but the notebooks are still available, although we make no guarantee about their current usability. To access these old R notebooks, please use this [github commit](https://github.com/GeoNet/data-tutorials/tree/5609561894b924211da975d1794eb00b5fcff99d).

**All notebooks use Python 3. We do not support Python 2.7.**

Tutorials are reviewed every 3 - 6 months, or sooner if circumstances require. During review, we confirm that notebooks still run, and make any necessary adjustments so that they remain a valuable, working resource for GeoNet's data users.

Tutorials are mostly organised by data access method, but in some cases we may also provide tutorials for a specific data type.

Within the folder for each data access method is a file README.md. This file contains most of the general material about data accessed by that method. This frees up individual notebooks to concentrate on data access and use, and reduces the maintenance required for each notebook. When you are using a particular notebook, it is therefore important that you refer to the README.md file in the same folder as the notebook.

This repository also hosts scripts and codes used for some GeoNet's data blogs. More information is available at the bottom of this README.

## Summary of Tutorials

### By data access method

| Data access method | Description   |
| ------------- | ------------- |
| [AWS Open Data](./AWS_Open_Data) | A file README.md describing GeoNet's data available through AWS Open Data |
| [Data repository](./Data_Repo) | Demonstrates how to access data through GeoNet's GitHub data repository. These tutorials are applicable to **dart**, **historic volcanic activity**, **moment tensor**, **soil gas**, and **volcanic alert level** data sets. |
| [FDSN](./FDSN) | Demonstrates how to access data through GeoNet's different FDSN web services (Dataselect, Station and Event). These tutorials are applicable to **seismic**, **acoustic-infrasound**, and **tsunami gauge (full sample rate)** data sets. |
| [Tilde](./Tilde) | Shows how to retrieve data from GeoNet's [Tilde API](https://tilde.geonet.org.nz/). These tutorials apply to **DART**, **envirosensor**, **tsunami gauge (down-sampled)**, and **GNSS displacement** data. Tutorials cover Tilde's data, stats, and data summary APIs. Further examples using Tilde are available in the volcano tutorials.|

### By data type

| Data type | Description   |
| ------------- | ------------- |
| [Volcano](./Volcano) | Demonstrates how to access data and use **various manually collected volcano data**, **envirosensor data**, **scanDOAS data**, **daily GNSS position data**, **data aggregation**, and **multi-domain (cross-domain) data**, largely using [the Tilde API](https://tilde.geonet.org.nz/). Most volcano data types are covered.|

## How to Run Tutorials
The file [**environment.yml**](./environment.yml) ensures that you have the correct Python environment to run the data tutorials. It allows you to install the correct Python packages, and where appropriate package versions. We use this environment when writing and reviewing notebooks. If you use a different environment, tutorials may work, but we cannot guarantee it. When we review tutorials we also review the environment and periodically may change that to more recent Python and module versions to ensure we are benefitting from recent updates.

### 1. Python environment manager
We use [miniforge](https://github.com/conda-forge/miniforge) to manage our Python environments. Other environment managers such as [Anaconda](https://www.anaconda.com/) are also suitable. Both support Windows, Mac, and Linux. If you do not yet have a python environment manager, we recommend you install one as you need a specific environment for the notebooks to work correctly.

### 2. Get the data-tutorials material
You have three options.
#### a) Clone the git data-tutorials repository
`git clone https://github.com/GeoNet/data-tutorials.git`

You can also use `SSH` but you will need to add a [SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) to your account and terminal environment.
### b) Copy the zip file containing the code
Click on green `<>Code` icon near the top of the page and then `Download ZIP`.
This will create a file `data-tutorials-main.zip` on your computer, which you will need to uncompress to access the notebooks. All common file compression tools will uncompress the ZIP file.
### c) Copy and paste
Navigate to a section of a notebook you are interested in and copy-paste the code you want to use into a notebook on your computer.

### 3. Installing the Python environment and using JupyterLab
For comprehensive instructions, consulte official [conda documentation for managing Python environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

We recommend using [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/index.html) rather than the older Jupyter Notebook.

If you don't have JupyterLab installed, here are [detailed instructions](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html).

Create an environment called `geonet-tutorial` from the specifications in the file `environment.yml`.

`conda env create -f environment.yml`

Activate this environment and make it available to JupyterLab.

```
conda activate geonet-tutorial
python -m ipykernel install --user --name=geonet-tutorial
```

You can install JupyterLab in your `base` conda environment, run it from that environment and access the `geonet-tutorial` environment from within JupyterLab. Alternatively, you can install JupyterLab in the `geonet-tutorial` environment.

To open JupyterLab from the Linux or MacOS command line type `jupyter lab`. From Windows, open the command prompt from the Start menu and type `jupyter lab`.

### 4. Running tutorials as standalone scripts
Tutorials are only available as Jupyter notebooks. If you want to run a notebook as a standalone Python script you can do that. Open the notebook in JupyterLab and export it as an [Executable Script](https://jupyterlab.readthedocs.io/en/stable/user/export.html).
                                                      
## Data Blogs

Data blogs are news stories focussed on GeoNet data and how to use
and understand it. They were first published in June 2022 and are accessible through the [GeoNet News web page](https://www.geonet.org.nz/news). While data blogs are not tutorials, the material sometimes contains
code excerpts and examples that our data users will find helpful, such as Jupyter notebooks and shell scripts. The material in the repository is that used by the blog's authors to prepare the blog at the time it was written. In contrast to data tutorials, with blogs we make no effort to review and keep up to date Jupyter notebooks, shell scripts, or any other code-like material. Also, we do not provide the environment and software versions that we used in preparing blog material. In many cases, the Python environment in [environment.yml](./environment.yml) may work if you want to run a Jupyter notebook used to generate material for a blog. If you are having difficulties, please ask us.

Code from data blogs are stored in the folder [Data_Blog](./Data_Blog). Within this is a
sequentially numbered folder including a shortened version of the blog's subject. For example, the folder *blog_01_val* contains blog number 01, and the subject was Volcanic Alert Level (VAL) data. Not all blogs have code so not all folders are in the repository.

If you want an up to date list of published blogs, go to the [News section on our web page](https://www.geonet.org.nz/news), filter for Data Blog and then hit the Search button.
