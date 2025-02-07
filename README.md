<img src="https://static.wixstatic.com/media/ac0ca5_db4f67801b0149b1ad0ec345e448de8f~mv2_d_3207_1376_s_2.png/v1/fill/w_261,h_111,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Color%20logo%20with%20background.png" alt="flopy3" style="width:50;height:20">

# flow-modnum
Python library with utilities created for Flow Hydro Consulting numerical modeling group.

Introduction
-----------------------------------------------

flow-modnum is a library with utilites created for Flow Hydro Consulting numerical modeling group. The utilites were built to plot results from MODFLOW models, such as water levels, concentrations, properties, among others. flow-modnum supports MODFLOW-USG.


Documentation
-----------------------------------------------


Installation
-----------------------------------------------

flow-modnum requires **Python** 3.12.4+ with:

```
numpy >=1.26.4
matplotlib >=3.8.4
pandas >=2.2.2
folium >= 0.18.0
plotly >= 5.22.0
pyproj >= 3.6.1
tqdm >= 4.66.4
geopandas >= 1.0.1
fiona >= 1.9.6
shapely >= 2.0.5
scipy >= 1.13.1
scikit-image >= 0.23.2
```

    pip install flow-modnum



Getting Started
-----------------------------------------------

### Plotting MODFLOW-USG model results water table results

```python

from flowmodnum import water_levels

# Function to plot hydrograms
water_levels.plot_hydrograms(obs_dir, model_dir, wells_dir, scale, date_ini, format_date='%d/%m/%Y', lang='EN')

# Function to plot fit between observed and simulated values
water_levels.plot_fit(obs_dir, model_dir, wells_dir, date_ini, format_date='%d/%m/%Y', lang='EN')

# Function to get fit statistics between observed and simulated values
water_levels.get_stats(obs_dir, model_dir, wells_dir, date_ini, format_date='%d/%m/%Y', lang='EN')

# Function to generate interactive map with hydrograms
water_levels.mapped_hydrograms(obs_dir, model_dir, EPSG, wells_dir, date_ini, format_date='%d/%m/%Y', lang='EN', grid_dir=None)

# Function to generate contours for given layers and stress periods
water_levels.generate_contours(model_dir, date_ini, layers, sps, EPSG, levels, dry_cells = -999.99)
"""
    Function to generate water level contours (shapefiles) from MODFLOW-USG output file. 
    
    Arguments:
    
    hds_dir: (str) Directory to MODFLOW-USG .hds file.
    gsf_dir: (str) Directory to MODFLOW-USG .gsf file.
    date_ini: (str) Initial date of model. Format dd/mm/YYYY.
    layers: (list) Layers to extract contours of water levels.
    sps: (list) Stress periods to extract contours of water levels.
    EPSG: (int) EPSG code to which all coordinated are referenced.
    levels: (list) Contours levels
    dry_cells: (float) (Optional) Value assigned to dry cells by model.
    
    Outputs: Folder with shapefiles for desired contours.
"""

```



Additional flow-modnum Resources
------------------------------------------------


Questions
------------------------------------------------
Do not open issues for general support questions.  We want to keep GitHub issues for bug reports and feature requests. General support questions are better answered in the [Discussions](https://github.com/modflowpy/flopy/discussions) on the flow-modnum GitHub repository. If using Stack Overflow, questions should be tagged with tag `flow-modnum`.

To save your and our time, **we will systematically close all issues that are requests for general support and redirect people to Stack Overflow or the MODFLOW google group**.


Contributing
------------------------------------------------



How to Cite
-----------------------------------------------



Additional FloPy Related Publications
-----------------------------------------------



MODFLOW Resources
-----------------------------------------------

+ [MODFLOW and Related Programs](https://water.usgs.gov/ogw/modflow/)