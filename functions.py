import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

"""
Execute heterogeneous treatment on data

Returns: X, X@betas
"""
def heterogeneousTreatment(X, betas):
    xb = X@betas
    treatments = np.random.randint(2, size=X.shape[0]).reshape(
        (-1, 1))  # randomly assigned treatments with propensity 0.5
    for i in range(X.shape[0]):
        if int(treatments[i]) > 0:
            # heterogenous treatment is 1 + 2*x_2*x_5
            xb[i] += 1 + 2 * X[i][1] * X[i][4]
    X = np.append(X, treatments, axis=1)
    return X, xb

"""
Data Generating Process
    Configure treatment effect heterogeneity, independent of regression form and sample size

Params:
    treatment - heterogeneous vs homogeneous 
    cc - number of continuous covariates to be included (pre-introduction of third order interactions)
    linear - 

Returns: y, X, betas, features
"""
def dgp(treatment="heterogeneous", linear=False, cc=4, N=1000, rho=0.2):
    error = np.random.normal(size=(N,1))
    
    added_covariates = 2
    if linear: 
        # linear => include 2 more continuous covariates
        # to have approximately same number of covariates between the linear and nonlinear cases
        cov = (np.eye(cc+added_covariates) * (1-rho)) + (np.ones((cc+added_covariates, cc+added_covariates)) * rho)
        
        # generate N continuous covariates of X
        X = np.random.multivariate_normal(np.zeros(cc+added_covariates),
                                         cov, size=N, check_valid='warn', tol=1e-8) 
    else:
        cov = (np.eye(cc) * (1-rho)) + (np.ones((cc, cc)) * rho)
        
        # generate N continuous covariates of X
        X = np.random.multivariate_normal(np.zeros(cc),
         cov, size=N, check_valid='warn', tol=1e-8) 

    # add binary [0, 1] covariate
    X = np.append(X, np.random.randint(2, size=N).reshape((-1, 1)), axis=1)

    elements = [1, 2, 3]
    probabilities = [0.2, 0.5, 0.3] # arbitrary
    
    # add unordered categorical [1, 2, 3] covariate
    X = np.append(X, np.random.choice(elements, N, p=probabilities).reshape((-1, 1)), axis=1) 

    # add third order interactions if linear is false for X covariates
    # increases number of covariates (to have a high dimensional dataset)
    poly = PolynomialFeatures(3, interaction_only=linear) 
    X = poly.fit_transform(X)
    X = X[:,1:] # drop the constant term
    features = (poly.get_feature_names()[1:])
    features.append("w")

    # randomly assigned treatments with propensity 0.5
    treatments = np.random.randint(2, size=N).reshape((-1, 1)) 
    
    # heterogenous vs. homogenous treatments
    if treatment == "homogeneous":
        betas = np.append(np.random.normal(size=X.shape[1]), [3]).reshape(-1,1)
        X = np.append(X, treatments, axis=1)
        xb = X@betas
    else:
        betas = np.random.normal(size=X.shape[1]).reshape(-1,1)
        X, xb = heterogeneousTreatment(X, betas)

    y = xb + error
    return y, X, betas, features
