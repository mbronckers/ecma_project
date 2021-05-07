# Abstract

## Context

The cost of survey experiments and experimental data collection has decreased significantly as technology has improved and crowdsourcing (labor) marketplaces such as Amazon's Mechanical Turk have become widely adopted. This has led to a great increase in experimental data collection across many domains (especially outside of academia).

## Problem

At the same time, this increase unaccompanied with proper education on experimental structure and data analysis practices has led to a diminishing concern for statistical rigor. Green & Kern mention that this is particularly evident in the assessment of **treatment effect heterogeneity** as researchers search for interactions between randomly-assigned treatments and the many survey background features in an ad-hoc and unstructured manner. 

The estimation of traditional investigation of treatment effect heterogeneity largely depends on  researcher discretion on model specification, and often leads to uncertainties and biased results. An example of this is when researchers choose how to divide their data into subgroups to estimate conditional average treatment effects (CATEs). CATEs are the average treatment effects among subgroups defined by baseline covariates. When researchers perform many subgroup analyses but do not adjust their standard errors, the results are downwardly biased standard errors leading to unfounded statistical significance.

As such, Green & Kern suggest the usage of Bayesian Additive Regression Trees (BARTs, see Chipman 2010) as a method for analyzing treatment effect heterogeneity in survey experiments. An important advantage is that BARTs offers the automatic detection and modeling of non-linear relationships and interactions, which prevents researchers from introducing discretion into the data analysis. Moreover, Green & Kern report an insensitivity to tuning parameters, making it an approachable tool for survey experimenters to model systematic treatment effect heterogeneity in a robust manner.

## Extension

Given the recent advances in ML, we want to provide a comprehensive comparison of methods to analyze treatment effect heterogeneity. Though BARTs naturally offer its advantages, they also have their drawbacks. Being a Bayesian MCMC, they are naturally computationally expensive relative to non-bayesian methods and not guaranteed to converge, making them slower and less practical. As such, we want to compare BARTs against a set of alternative methods to assess its place in the repertoire of survey experimenters.

Our proposed set of methods to analyze and compare are:
- Bayesian Additive Regression Trees ("BART")
- Random Forest ("RF")
- Bayesian Neural Network ("BNN")
- Feedforward/Deep Neural Network ("NN/DNN")
- Gradient Boosting ("GBT")

We adopt the empirical data from Green & Kern for our comparisons. We use the well-known survey experiment about public support for government spending on welfare to the poor from the GSS to model systematic treatment effect heterogeneity based on the wording of the survey question and its interaction with racial and education perceptions.

## Why these methods?

BART is a probabilistic statistical method that combines ensemble learning with nonparametric regression. The probabilistic framework provides prediction uncertainty quantification. The uncertainty quantification in estimates is useful in statistical inference as well as critical decision making.

Neural networks methods:

- **Feed-forward Neural Networks**: 

- **Bayesian Neural Networks**: one limitation of common machine learning methods is the lack of uncertainty quantification for point estimates, e.g. standard errors and confidence intervals. Regular point estimate neural networks do not offer any insight into uncertainty measures and merely report their prediction output. Bayesian Neural Networks (BNNs) solve this problem. BNNs are stochastic neural networks trained using a Bayesian method. It optimizes a posterior inference distribution with a prior distribution over its network weights. 

Ensemble methods:

- **Gradient Boosting Trees**: like BART, GBT is a boosting technique to build an ensemble of trees. GBTs are a good method to compare with BART due to the iterative nature of both methods to fit on residuals of fellow weak estimators. The main difference is that BART uses a prior distribution to weigh its trees in the ensemble whereas GBT uses a selected learning rate parameter to sum the individual trees sequentially. BART employ Bayesian backfitting for the iterative step whereas GBT uses gradient descent. An evaluation will analyze the trade-off of parameter tuning and gradient descent versus prior distribution specification and non-parametric inference that Green & Kent claim is desirable.

- **Random Forests**: in contrast to BART and GBT, RFs is a bagging approach to the regression tree algorithm. Where BART and GBT will have estimated regression functions with discontinuous jumps, RFs will have a smooth regression function as it averages over the bootstrapped trees

## Evaluation considerations

We will assess the methods on the following:
- Accuracy/performance
- Model assumptions (the more it makes the weaker the general use case)
- Parameter tuning complexity/ease-of-use
- Computational learning/training cost
- Robustness

## Robustness

Required:
- Evaluate results under different hyperparameter configurations (such as different values of lambda in LASSO)

Optional:
- Monte carlo simulation with DGP based on empirical datast
