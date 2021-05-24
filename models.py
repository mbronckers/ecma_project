from econml.dml import CausalForestDML
from econml.grf import CausalForest
from sklearn.linear_model import LassoCV
from econml.inference import BootstrapInference

def estimate_grf(Y_train, Y_test, X_train, X_test, T_train, T_test, criterion='mse'):
    # specify hyperparams of model
    est = CausalForest(criterion=criterion, n_estimators=1000,       
                          min_samples_leaf=1, 
                          max_depth=100, max_samples=0.5,
                          honest=True, inference=True)

    # fit model
    est.fit(X=X_train, T=T_train, y=Y_train)
    
    predict, sigma = est.predict_and_var(X_test)
    
    return est, predict, sigma


def estimate_dml(Y_train, Y_test, X_train, X_test, T_train, T_test, test_size=0.2, criterion='mse'):
    # split data into train and test sets 
    X_train, X_test, Y_train, Y_test, T_train, T_test = train_test_split(X, y, treatments, test_size=test_size)

    # homo => no covariates affecting treatment
    if effect_type == "homogeneous":
#         W_train = X_train[:, :-1]
#         W_test = X_test[:, :-1]
        W_train = None
        W_test = None
    else:
        W_train = X_train[:, [1, 4]] # effect_modifiers
        W_test = X_test[:, [1, 4]]
        
    # specify hyperparams of model
    est = CausalForestDML(criterion='mse', n_estimators=1000,       
                          min_samples_leaf=1, 
                          max_depth=100, max_samples=0.5,
                          discrete_treatment=True, 
                          honest=True, inference=True)

    # fit model
    est.fit(Y_train.ravel(), T_train, X=X_train, W=W_train)
    
     # Estimate the treatment effects on test set
    treatment_effects = est.effect(X_test)

    # Confidence intervals via Bootstrap-of-Little-Bags for forests
    lb, ub = est.effect_interval(X_test, alpha=0.05)

    # Estimate the CATE with the test set (is just mean treatment_effect)
    cate_test = est.const_marginal_ate(X_test)
    
    return est, treatment_effects, lb, ub, cate_test