# Predicitng Beta Event Amplitude from Simulation Parameters
## Background
This repository analyzes a dataset of simulated neural activity underlying EEG/MEG signals. 

The goal of this analysis is to predict the amplitude of a specific waveform known as Beta Events from simulation parameters.

## Repository Structure
The final report describing the results of Beta Event amplitude prediction can be found under `\report`. All source code used to generate figures can be found under `\src`. Figures used in the report are stored under `\figures`. Intermediate results such as hyperparameter tuning for multiple regression models are stored in `.pkl` files as dictionaries in `\results`. The dataset of simulated neural activity can be found under `\data`.

## Simulator
All simulations were performed using the Human Neocortical Neurosolver

https://hnn.brown.edu/

https://github.com/jonescompneurolab/hnn-core
