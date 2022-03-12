# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
## Feladat: minimum az alábbi kód fusson le úgy hogy az img.image egy arrayként jelenjen meg
# -

from cellanalysis import cellanalysis as ca

img = ca.Image("data/imageXpressSamples/20211119 HTSF1 barrKO_A01_s10_w1CC4EC46A-D8FC-4FE8-81F8-B798022EED0D.tif")

img.load_image()

img.image