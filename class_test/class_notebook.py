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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randint(0, 255, size=(100,100)))

data.values

data.shape

data2 = np.array([1, 2, 3, 4, 4])


class Allat:
    
    def __init__(self, nev, faj):
        self.nev = nev
        self.nev = faj
        self.kor = 0
    
    def ugat(self):
        print("Vau")
    
    def oregszik(self):
        self.kor += 1


enkutyam = Allat("Buksi", kutya) #data = pd.DataFrame()
tekutyad = Allat("Fifi", kutya) #data = pd.DataFrame()


class MyDataFrame(pd.DataFrame):
    
    def __init__(self, data, user):
        super().__init__(data)
        
        self.user = user
        self.hello()
    
    def imshow(self):
        plt.imshow(self.values)
        print(self.user)
        self.hello()
        
    def hello(self):
        print("Hello")


mydata = MyDataFrame(np.random.randint(0, 255, size=(100,100)), user = "Dominik")

mydata.user

mydata.hello()

mydata.imshow()


