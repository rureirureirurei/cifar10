import os
import sys
import pickle
import numpy as np
import pandas as pd
import scipy.stats as sstats
import multiprocessing as mp
from sklearn import datasets
from tqdm.auto import tqdm
from matplotlib import animation, pyplot, rc
import matplotlib.pyplot as plt
import httpimport
from os.path import join
import os.path
from PIL import Image


from sklearn.cluster import KMeans, MiniBatchKMeans
import numpy as np

from sklearn.feature_extraction import image
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.linear_model import LogisticRegression

class FeaturesExtractor():
    
    def __init__(self, PATCH_SIZE, PATCH_NUM, STRIDE, K):
        self.PATCH_SIZE = PATCH_SIZE
        self.PATCH_NUM = PATCH_NUM
        self.STRIDE = STRIDE
        self.K = K
        self.centroids = []
        
	# return number of elements corresponding to each centroid
    def fit(self, X):
        print("Started fitting extractor:")
        P_zca = self.extract_patches(X)
        kmeans = MiniBatchKMeans(n_clusters=self.K, random_state=0, verbose=False, max_iter=200, batch_size=10000, n_init=10)
        kmeans.fit(P_zca)
        self.centroids = kmeans.cluster_centers_
        labels = kmeans.labels_
        counts = np.bincount(labels, minlength=kmeans.n_clusters)
        return counts
    
    def contrast(self, image):
        return (image-image.min())/(image.max() - image.min())

    def normalize_patch(self, patch, eps=10):
        return (patch - patch.mean())/np.sqrt(patch.var() + eps)

    def whiten(self, X):
        X_norm = (X - X.mean(axis=0))/X.std(axis=0)
        cov = np.cov(X_norm, rowvar=False) 
        U,S,V = np.linalg.svd(cov)

        X_zca = U.dot(np.diag(1.0/np.sqrt(S + 0.1))).dot(U.T).dot(X_norm.T).T
        return X_zca

    def extract_patches(self, data):
        patches = []
        reshaped = data.reshape(-1,32,32,3)
        n = int(self.PATCH_NUM / (32-self.PATCH_SIZE+1) ** 2 + 1)
        for i in tqdm(range(n)):
            for r in range(32-self.PATCH_SIZE+1):
                for c in range(32-self.PATCH_SIZE+1):
                    patch = reshaped[i][c:(c+self.PATCH_SIZE),r:(r+self.PATCH_SIZE)].flatten()
                    patch_norm = self.normalize_patch(patch, eps=10)
                    patches.append(patch_norm)

        P = np.vstack(patches)
        return self.whiten(P)
    
    def dist(self, x,y):
        return np.sqrt((x - y).dot(x-y))

    
    def normalize(self, data):
        return (data - data.mean(axis=0))/data.std(axis=0)  

    def create_patch_features__vectorized(self, X):    
        X_mapped_list_per_image = []
        for i in tqdm(range(X.shape[0])):
            patches = image.extract_patches_2d(X[i], (self.PATCH_SIZE, self.PATCH_SIZE))
            strided_patches = patches.reshape( 32-self.PATCH_SIZE+1 , 32-self.PATCH_SIZE+1, self.PATCH_SIZE, self.PATCH_SIZE, 3)[::self.STRIDE,::self.STRIDE,:,:,:]
            strided_patches = strided_patches.reshape(((32-self.PATCH_SIZE)//self.STRIDE+1)**2, self.PATCH_SIZE * self.PATCH_SIZE * 3)
            mapped_features = euclidean_distances(np.asarray([self.normalize_patch(patch, eps=0.01) for patch in strided_patches]), self.centroids)
            X_mapped_list_per_image.append(mapped_features.reshape(((32-self.PATCH_SIZE)//self.STRIDE+1)**2 * self.centroids.shape[0]))
        X_mapped = np.asarray(X_mapped_list_per_image)
        return X_mapped
    
    def extract(self, X):
        print("Started extracting")
        mapped = self.create_patch_features__vectorized(X)
        norm = self.normalize(mapped)
        return norm
     