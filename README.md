# Level Set Methods
This repo was created for the following peer-reviewed manuscript:

**Wu, Q.**, Lane, C.R., Wang, L., Vanderhoof, M.K., & Christensen, J.R. (2018). Delineating nested depressions in digital elevation models for hydrological analysis using level set methods. *Journal of the American Water Resources Association* (under review) 

## How to use the level set algorithm

This tutorial assumes that you have used conda before. Please follow the [conda user guide](https://conda.io/docs/user-guide/install/index.html) to install conda if necessary.

### Step 1: Creating a conda environment
Please create an environment from the provided [environment.yml](environment.yml) file using the following command:

`conda env create -f environment.yml`

The command above will create a conda environment named `levelset`. If you want to remove the levelset conda environment, use the following command:

`conda remove --name levelset --all`

## Step 2: Setting Python interpreter
Clone this repo and create a PyCharm project using the repo folder. Set the Python interpreter to your conda env path (e.g., `~/anaconda3/envs/levelset/bin/python`)

## Step 3: Setting algorithm parameters
Open the Python script [level_set/slicing.py](level_set/slicing.py) and change the following parameters if needed.

    # set input files
    in_dem = "../data/CLSA_LiDAR.tif"
    in_sink = "../data/CLSA_Sink.tif"
    
    # parameters for level set method
    min_size = 2000         # minimum number of pixels as a depression
    min_depth = 0.3         # minimum depression depth
    interval = 0.2          # slicing interval, top-down approach
    
    # set output directory
    out_dir = "../result"
 
## Step 4: Executing the algorithm
Run the Python script [level_set/slicing.py](level_set/slicing.py). By default, results will be saved under the `result` folder under the project root directory.  
    
## Examples
The images below show working examples of the level set method for delineating nested depressions in the Cottonwood Lake Study Area (CLSA), North Dakota.
More test datasets (e.g., the Pipestem watershed in the Prairie Pothole Region of North Dakota) can be downloaded from <http://gishub.org/2018-JAWRA-Data>

![CLSA DEM](/figures/CLSA_DEM.png)

![CLSA Result](/figures/CLSA_Result.png)

![CLSA Aerials](/figures/CLSA_Aerials.png)