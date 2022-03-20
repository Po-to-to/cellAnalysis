# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
from cellanalysis import cellanalysis as ca

# %%
imgZ = ca.ZeissCziImage("data/ZeissConfocalSamples/3_20x.czi")

# %%
imgX = ca.ImageXpressImage("data/imageXpressSamples", "A01", "s10")

# %%
imgX.load_image()

# %%
imgZ.load_image()

# %%
isinstance(imgX, ca.Image)

# %%
imgZ.display_image()

# %%
imgX.display_image()

# %%
#from skimage.io import imread, imshow #https://forum.image.sc/t/display-multi-channel-images-with-scikit-image/51009
#imgY = ca.ImageXpressImage("data/imageXpressSamples", "A01", "s10")
#imgY.load_image()

#cdict = {'red':   [(0.0,  0.0, 0.0),
#                  (0.5,  1.0, 1.0),
#                  (1.0,  1.0, 1.0)],

#         'green': [(0.0,  0.0, 0.0),
#                   (0.25, 0.0, 0.0),
#                   (0.75, 1.0, 1.0),
#                   (1.0,  1.0, 1.0)],

#         'blue':  [(0.0,  0.0, 0.0),
#                   (0.5,  0.0, 0.0),
#                   (1.0,  1.0, 1.0)]}

#from matplotlib.colors import LinearSegmentedColormap
#cmap = LinearSegmentedColormap('testCmap', segmentdata=cdict,)

#imshow(imgY.image/imgY.image.max(), cmap=cmap)

# %%
