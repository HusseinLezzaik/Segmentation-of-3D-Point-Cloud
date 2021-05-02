# Segmentation of 3D Point Cloud

## Introduction
Code for implementation of the paper titled :  Fast Segmentation of 3D Point Clouds: A Paradigm on LiDAR Data for Autonomous Vehicle Applications.

## Overview of the Repository
In this repo, you'll find :
* `pointclouds`: point clouds dataset.
* `paper.pdf`: the paper of Fast Segmentation of 3D Point Clouds.
* `gpf.py`: ground plane fitting (GPF) algorithm from 3D lidar scan shot in the street.
* `pypcd`: folder for mapping between PointField types and numpy types, extracting PointCloud object from a dataframe, etc.

## Getting Started
1.  Clone repo: `git clone https://github.com/HusseinLezzaik/Segmentation-of-3D-Point-Cloud.git`
2.  Install dependencies:
    ```
    conda create -n segmentation-point-clouds python=3.7
    conda activate segmentation-point-clouds
    pip install -r requirements.txt
    ```

## Contact
* Hussein Lezzaik : hussein dot lezzaik at gmail dot com


