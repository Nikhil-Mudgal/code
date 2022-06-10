import os 
import sys 
import io 

import pandas as pd 
import numpy as np 
from sklearn.metrics import mean_squared_error, mean_absolute_error, \
    r2_score
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import mlflow 
import mlflow.sklearn 

import logging


logging.basicConfig(level=logging.WARN)
logger = loggin.getLogger(_name_)


def eval_metric(actual_pred):
    rmse = np.sqrt 
