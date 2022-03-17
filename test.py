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
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
## Feladat: minimum az alábbi kód fusson le úgy hogy az img.image egy arrayként jelenjen meg

# %%
from cellanalysis import cellanalysis as ca

# %%
imgZ = ca.ZeissCziImage("data/ZeissConfocalSamples/3_20x.czi")

# %%
imgX = ca.ImageXpressImage("data/imageXpressSamples", "A01", "s10")

# %%
imgX.load_image()

# %%
isinstance(imgX, ca.Image)

# %%
imgX.display_image()

# %%
img.display_image()

# %%

# %%

