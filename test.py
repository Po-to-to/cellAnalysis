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
imgx_kk = ca.Image("data/imageXpressSamples/20211119 HTSF1 barrKO_A01_s10_w1_thumb79C9E460-DEAF-4B24-A224-8B7CB288B114.tif")

# %%
imgx_kk.load_image()

# %%
imgx_kk.display_image

# %%
isinstance(imgX, ca.Image)

# %%
imgX.display_image()

# %%
img.display_image()

# %%
imgX.image_path

# %%
imgZ.load_image()


# %%
imgZ.image_path


# %%
imgZ.display_image


# %%

        
        

# %%
