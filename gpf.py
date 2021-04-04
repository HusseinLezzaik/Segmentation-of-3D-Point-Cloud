#!/usr/bin/env python
# Ground plane fitting (GPF) algorithm from 3D lidar scan shot in the street.
# This code extracts the ground assuming it is a single plane.
# It is based on the work described in "Fast Segmentation of 3D Point Clouds: A Paradigm on LiDAR Data for Autonomous Vehicle Applications", D. Zermas, I. Izzat and N. Papanikolopoulos, 2017.
# The algorithm is well-explained in the reference, PDF is given in this archive.
# 
# A finer extension could be done by cutting the point clouds into independant portions among car direction.

# I/O from pypcd
from pypcd import pypcd # use local pypcd custom version (OK with python 3, no support for lzf compression)

import numpy as np

import pptk # open prompt terminal from Anaconda and type: pip install pptk    # !! Ubuntu users, pptk has a bug with libz.so.1, see how to do a new symlink in https://github.com/heremaps/pptk/issues/3

#%%
def naive_ground_extractor(ptc, n_lpr):
    # First, try to make a basic and naive ground extractor, as a reference to compare with GPF
    # simplest ground extractor: takes points with lowest Z
    # returns ids of ground
    # ptc: array of points
    # n_lpr: number of lowest Z points to keep for ground
    
    # TODO
    
    return ground_ids


#%%
# GPF: from paper "Fast Segmentation of 3D Point Clouds: A Paradigm on LiDAR Data for Autonomous Vehicle Applications"
def gpf_extractinitialseeds(ptc, n_lpr, thresh_seeds = 0.5):
    # GPF, extract initial seeds
    # returns ids of seeds
    # ptc: array of points
    # n_lpr: number of lowest Z points to keep for initialization
    # thresh_seeds: threshold distance to keep seeds from initial ground plane issued from lowest Z points (in meters)
    
    # TODO
    
    return seeds_ids

#%%
def gpf_estimateplane(ptc, plane_ids):
    # GPF, plane estimation from points ids and ptc
    # computes covariance matrix of plane points distribution, then SVD to get normal vector of the plane
    # returns ground plane equation defined by its normal (a,b,c) and d
    # ptc: array of points
    # plane_ids: ids of plane points
    
    # TODO
    
    return normal, d

#%%
def gpf_refinement(ptc, seeds_ids, thresh_dist=0.2, n_iter=5):
    # GPF, main loop to refine ground plane estimation
    # returns ids of ground
    # ptc: array of points
    # seeds_ids: ids of seeds points
    # thresh_dist: distance threshold to keep points from ground plane (in meters)
    # n_iter: number of iterations
    
    # TODO
    
    return ground_ids



#%%
def main(pcd_file):
    # read the pointcloud
    pc = pypcd.PointCloud.from_path(pcd_file)
    # pc.pc_data has the data as a structured array
    # pc.fields, pc.count, etc have the metadata

    #print(pc.pc_data)
    #print(pc.pc_data.shape)
    print(pc.fields)

    # ptc point cloud as an array with x, y, z, class (0: non-ground, 1: ground) / class is used to plot points with distinct colors
    ptc = np.stack((pc.pc_data['x'],pc.pc_data['y'],pc.pc_data['z'],np.zeros((pc.pc_data.shape[0]))), axis=1)
    print(ptc.shape)

    # test naive ground extractor
    #ground_ids = naive_ground_extractor(ptc, 10000)

    # GPF method
    # get initial seeds
    #seeds_ids = gpf_extractinitialseeds(ptc, 20000, 0.2)
    # test ground only from initial seeds
    #ground_ids = seeds_ids
    # complete method, continue with ground detection refinement
    #ground_ids = gpf_refinement(ptc, seeds_ids, 0.2, 5)

    # update ground class info in ptc
    #ptc[ground_ids[:],3] = 1 # 1 for ground points
    #print(ptc)

    # show with colors
    v = pptk.viewer(ptc[:,:3], ptc[:,3])
    v.set(point_size=0.01)
    v.color_map([[1., 1., 1.], [1., 0., 0.]])

#%%
if __name__ == "__main__":
    pcd_file = './pointclouds/1504941056.807104000.pcd'
    main(pcd_file)

