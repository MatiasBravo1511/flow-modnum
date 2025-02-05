import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import matplotlib.dates as mdates
import os
import shutil

def plot_niveles(obs_dir, sim_dir, scale):
    # Current working directory
    cwd = os.getcwd()
    
    # Directories for plots
    plot_dir = os.path.join(cwd, 'graphs')
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    if os.path.exists(plot_dir):
        shutil.rmtree(plot_dir)
        os.makedirs(plot_dir)
        
    # Lectura de dataframes
    df_sim = pd.read_csv(simulados_dir, sep=r'\s+', header=None)
    df_sim.columns=['pozo', 'fecha', 'hora', 'nivel']
    df_sim['pozo'] = df_sim.pozo.str.upper()
    df_sim['fecha'] = pd.to_datetime(df_sim.fecha, format='%d/%m/%Y')

    df_obs = pd.read_csv(observados_dir, sep=r'\s+', header=None)
    df_obs.columns=['pozo', 'fecha', 'hora', 'nivel']
    df_obs['pozo'] = df_obs.pozo.str.upper()
    df_obs['fecha'] = pd.to_datetime(df_obs.fecha, format='%d/%m/%Y')
    
    for pozo in df_obs.pozo.unique():
        # Grafico de niveles
        fig, axs = plt.subplots(1, figsize=(7,5))

        # Se plotean observados y simulados SMP
        axs.scatter(df_obs.loc[df_obs.pozo == pozo]['fecha'], df_obs.loc[df_obs.pozo == pozo]['nivel'], label='Nivel Observado', color='black')
        axs.plot(df_sim.loc[df_sim.pozo == pozo]['fecha'], df_sim.loc[df_sim.pozo == pozo]['nivel'], label='Nivel simulado')

        # Formato de ejes
        axs.set_ylabel('Nivel (msnm)')
        axs.legend()
        axs.set_title(pozo)
        axs.xaxis.set_major_locator(mdates.YearLocator(1)) 
        axs.xaxis.set_tick_params(rotation=45)
        axs.yaxis.set_major_formatter(ScalarFormatter(useOffset=False))

        # Escala vertical
        means = (df_obs.loc[df_obs.pozo == pozo]['nivel'].mean()+df_sim.loc[df_sim.pozo == pozo]['nivel'].mean())/2
        maxs = max(df_obs.loc[df_obs.pozo == pozo]['nivel'].max(), df_sim.loc[df_sim.pozo == pozo]['nivel'].max())
        mins = min(df_obs.loc[df_obs.pozo == pozo]['nivel'].min(), df_sim.loc[df_sim.pozo == pozo]['nivel'].min())
        maxs = means+maxs-mins
        mins = means-maxs+mins
        maxs = max(maxs, means+scale)
        mins = min(mins, means-scale)
        axs.set_ylim(mins, maxs)

        # Se guarda grafico
        plt.savefig(os.path.join(plot_dir, pozo+'.png'), dpi=300)
        plt.close()
        fig.clear()