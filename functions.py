import numpy as np
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures

"""
Execute heterogeneous treatment on data

Returns: X, X@betas
"""
def heterogeneousTreatment(X, treatments, betas, effect):
    xb = X@betas
    for i in range(X.shape[0]):
        if int(treatments[i]) > 0:
            xb[i] += 1 + effect * X[i][1] * X[i][4] # heterogeneous treatment is 1 + effect*x_2*x_5
    X = np.append(X, treatments, axis=1)
    return X, xb

"""
Data Generating Process
    Configure treatment effect heterogeneity, independent of regression form and sample size

Params:
    effect_type - heterogeneous vs homogeneous
    effect_homogeneous - if effect_type is homogeneous, controls what the treatment coefficient is
    effect_heterogeneous - if effect_type is heterogeneous, controls n where the treatment coefficient is 1 + n * x_2 * x_5
    treatment_probability - probability that an observation is assigned the treatment, default is 0.5
    order - order of interactions between covariates desired, as order is increased, number of covariates and nonlinearity (if specified) is also increased
    linear - flag to control whether the dgp has exponents larger than 1 
    cc - number of continuous covariates to be included (pre-introduction of n order interactions)
    N - sample size
    rho - variance between continuous covariates
Returns: y, X, betas, features
"""
def dgp(effect_type="heterogeneous", effect_homogeneous=3, effect_heterogeneous=2, treatment_probability=0.5, order=3, linear=False, cc=4, N=1000, rho=0.2):
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
    X = np.append(X, np.random.randint(2, size=N).reshape((-1, 1)), axis=1) # add binary [0, 1] covariate

    cat_elements = [1, 2, 3]
    cat_probabilities = [0.2, 0.5, 0.3] # arbitrary

    # add unordered categorical [1, 2, 3] covariate
    X = np.append(X, np.random.choice(cat_elements, size=N, p=cat_probabilities).reshape((-1, 1)), axis=1)

    # add N order interactions if linear is false for X covariates
    # increases number of covariates (to have a high dimensional dataset)
    poly = PolynomialFeatures(order, interaction_only=linear) 
    X = poly.fit_transform(X)
    X = X[:,1:] # drop the constant term
    features = (poly.get_feature_names()[1:])
    features.append("w")

    treat_elements = [0, 1]
    treat_probabilities = [1 - treatment_probability, treatment_probability]

    # randomly assigned treatments with propensity treatment_probability
    treatments = np.random.choice(treat_elements, size=N, p=treat_probabilities).reshape((-1, 1))
    
    # heterogeneous vs. homogeneous treatments
    if effect_type == "homogeneous":
        betas = np.append(np.random.normal(size=X.shape[1]), [effect_homogeneous]).reshape(-1,1)
        X = np.append(X, treatments, axis=1)
        xb = X@betas
    else:
        betas = np.random.normal(size=X.shape[1]).reshape(-1,1)
        X, xb = heterogeneousTreatment(X, treatments, betas, effect_heterogeneous)

    y = xb + error 
    return y, X, betas, features
