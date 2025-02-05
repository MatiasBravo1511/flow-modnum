import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.dates as mdates
import os
import shutil

def plot_hydrograms(obs_dir, sim_dir, scale, format_date='%d/%m/%Y', lang='EN'):
    """
    Function to plot water level hydrograms. 
    obs_dir: Directory to observation data
    sim_dir: Directory to simulated data
    scale: Vertical scale (+- from mean values)
    format_date: Date format to build DataFrames. Default is '%d/%m/%Y'
    lang: Language. Can choose between EN and SP. Default is EN
    """
    # Current working directory
    cwd = os.getcwd()
    
    # Directories for plots
    plot_dir = os.path.join(cwd, 'graphs')
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    if os.path.exists(plot_dir):
        shutil.rmtree(plot_dir)
        os.makedirs(plot_dir)
        
    # Dataframes are loaded
    df_sim = pd.read_csv(sim_dir, sep=r'\s+', header=None)
    df_sim.columns=['well', 'date', 'time', 'water_level']
    df_sim['well'] = df_sim.well.str.upper()
    df_sim['date'] = pd.to_datetime(df_sim.date, format=format_date)

    df_obs = pd.read_csv(obs_dir, sep=r'\s+', header=None)
    df_obs.columns=['well', 'date', 'time', 'water_level']
    df_obs['well'] = df_obs.well.str.upper()
    df_obs['date'] = pd.to_datetime(df_obs.date, format=format_date)
    
    for well in df_obs.well.unique():
        # Hydrograms
        fig, axs = plt.subplots(1, figsize=(7,5))

        # Plot simulated and observed data
        if lang == 'EN':
            axs.scatter(df_obs.loc[df_obs.well == well]['date'], df_obs.loc[df_obs.well == well]['water_level'], label='Observed', color='black')
            axs.plot(df_sim.loc[df_sim.well == well]['date'], df_sim.loc[df_sim.well == well]['water_level'], label='Simulated')
            
            # Axis format
            axs.set_ylabel('Water Level (msnm)')
            axs.legend()
            axs.set_title(well)
            axs.xaxis.set_major_locator(mdates.YearLocator(1)) 
            axs.xaxis.set_tick_params(rotation=45)
            axs.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))
        elif lang=='SP':
            axs.scatter(df_obs.loc[df_obs.well == well]['date'], df_obs.loc[df_obs.well == well]['water_level'], label='Observado', color='black')
            axs.plot(df_sim.loc[df_sim.well == well]['date'], df_sim.loc[df_sim.well == well]['water_level'], label='Simulado')
            
            # Axis format
            axs.set_ylabel('Nivel (msnm)')
            axs.legend()
            axs.set_title(well)
            axs.xaxis.set_major_locator(mdates.YearLocator(1)) 
            axs.xaxis.set_tick_params(rotation=45)
            axs.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))

        # Vertical scale
        means = (df_obs.loc[df_obs.well == well]['water_level'].mean()+df_sim.loc[df_sim.well == well]['water_level'].mean())/2
        maxs = max(df_obs.loc[df_obs.well == well]['water_level'].max(), df_sim.loc[df_sim.well == well]['water_level'].max())
        mins = min(df_obs.loc[df_obs.well == well]['water_level'].min(), df_sim.loc[df_sim.well == well]['water_level'].min())
        maxs = means+maxs-mins
        mins = means-maxs+mins
        maxs = max(maxs, means+scale)
        mins = min(mins, means-scale)
        axs.set_ylim(mins, maxs)

        # Save plot
        plt.savefig(os.path.join(plot_dir, well+'.png'), dpi=300)
        plt.close()
        fig.clear()