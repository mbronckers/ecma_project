# Abstract

## Context

Many economists are interested in estimating treatment effects for populations. They do this by estimating Average Treatment Effect (ATE), which is the average outcome of the treatment group in a selected population less the average outcome of the control group in the same population. Naturally however, these treatment effects often vary by individual, and these variations may have to do with underlying individual characteristics that we may or may not be able measure. This variation in response based on individual characteristics is referred to as Heterogenous Treatment Effects. Understanding and being able to estimate heterogenous treatment effects is especially important for policy makers - knowing how groups of people, given particular characteristics, will respond to a policy would help further inform major policy decisions.

In this paper, we want to re-examine the Green and Kern's [2012] proposal of using Bayesian Additive Regression Trees (BART) to estimate heterogenous treatment effects among survey responders, to demonstrate the performative and interpretive benefits of BART. Specifically, we want to directly compare their results by applying Wager and Athey's [2017] more recently proposed method of Causal Forests to estimate the same problem. This will allow us to explicitly outline benefits and drawbacks of these two machine learning methods that have been touted as premier ways to reveal treatment effect heterogeneity, in how they offer strong predictive power while maintaining inferential ability, to better determine future use cases and tradeoffs.

## Problem

Because the cost of survey experiments and experimental data collection has decreased significantly as technology has improved and crowdsourcing (labor) marketplaces such as Amazon's Mechanical Turk have become widely adopted. This has led to a great increase in experimental data collection across many domains (especially outside of academia). At the same time, this increase unaccompanied with proper education on experimental structure and data analysis practices has led to a diminishing concern for statistical rigor. Green and Kern mention that this is particularly evident in the assessment of **treatment effect heterogeneity** as researchers search for interactions between randomly-assigned treatments and the many survey background features in an ad-hoc and unstructured manner. 

The estimation of traditional investigation of treatment effect heterogeneity largely depends on researcher discretion on model specification, and often leads to uncertainties and biased results. An example of this is when researchers choose how to divide their data into subgroups to estimate conditional average treatment effects (CATEs). CATEs are the average treatment effects among subgroups defined by baseline covariates. When researchers perform many subgroup analyses but do not adjust their standard errors, the results are downwardly biased standard errors leading to unfounded statistical significance.

As such, Green and Kern [2012] suggest the usage of Bayesian Additive Regression Trees (BARTs, see Chipman 2010) as a method for analyzing treatment effect heterogeneity in survey experiments. An important advantage is that BARTs offers the automatic detection and modeling of non-linear relationships and interactions, which prevents researchers from introducing discretion into the data analysis. Moreover, Green and Kern report an insensitivity to tuning parameters, making it an approachable tool for survey experimenters to model systematic treatment effect heterogeneity in a robust manner.

## Literature Review

We primarily draw approaches and intuition from three works.

(1) Modeling Heterogenous Treatment Effects in Survey Experiments with Bayesian Additive Regression Trees (Green and Kern [2012])
As aforementioned, we want to extend the work done by Green and Kern in analyzing heterogeneity in treatment effects of survey data that was intended to measure the stigma of the word "welfare" when asking individuals about public spending. We intend to directly compare their results with the results that we obtain from applying Wager and Athey's [2017] Causal Forests method. Their justification for BART's suitability for uncovering heterogeneity in treatment effect is also important in establishing our criteria of comparison - they discuss that BART flourishes in eliminating researcher discretion in choosing their data subgroup formation, detecting and modeling high dimension non-linear relationships and interactions, and minimizing parameter tuning (thereby increasing robustness) so that it works "out of the box".   

(2) Estimation and Inference of Heterogenous Treatment Effects using Random Forests (Wager and Athey [2017])
Causal Forests are an extension of Random Forests and Wager and Athey [2017] make a concerted effort for their extension to have "tractable asymptotic theory", and be useful, unlike most machine learning approaches, for causal inference. They directly criticize BART in being difficult to use for statistical inference, claiming that there is no asymptotic normality theory around the posterior of BART that guarantees "concentration around the true conditional mean function". This is the underlying motivation for our research - we want to focus in on this criticism by direct comparison of BART and Causal Forests using criteria (1) and (2) describe, and offer both quantitative comparison in performance, computational cost, and generated confidence intervals, but also qualitative comparison in statistical inference ability, necessary strength of model assumptions and ease of use.

(3) Machine Learning Methods Economists Should Know About (Athey and Imbens [2019])
This paper serves as a very recent reference point of the current approaches machine learning offers in regards to treatment effect heterogeneity. By summarizing the challenges of estimating treatment effect heterogeneity into three questions main questions, Athey and Imbens [2019] have given us a clearer idea of what to prioritize as criteria when comparing the results of Causal Forest with BART. Furthermore, its mention of Causal Forests pointed us in the direction of even focusing on this extension - BART and Causal Forests are are both tree based approaches that have been studied and described as relatively strong candidates for treatment effect heterogeneity (compared to other approaches), which lead us to believe that such a direct comparison would not only be possible, but important.

## Focus (as an Extension of Green and Kern)

We want to provide a comprehensive comparison of BART and Causal Forests to analyze treatment effect heterogeneity. Though BARTs naturally offer its advantages, they also have their drawbacks. Being a Bayesian MCMC, they are naturally computationally expensive relative to non-bayesian methods and not guaranteed to converge, making them slower and less practical. Furthermore, they appear to lack tractable asymptotic theory that would allow for more rigorous statistical analysis. As such, we want to compare BARTs against Causal Forests, which Wager and Athey [2017] have specifically shown to have asymptotic normality, thus being more suited towards causal inference.

We adopt the empirical data from Green and Kern [2012] for our comparisons. We use the well-known survey experiment about public support for government spending on welfare to the poor from the GSS to model systematic treatment effect heterogeneity based on the wording of the survey question and its interaction with racial and education perceptions.

## Why these methods?

BART is a probabilistic statistical method that combines ensemble learning with nonparametric regression. The probabilistic framework provides prediction uncertainty quantification. The uncertainty quantification in estimates is useful in statistical inference as well as critical decision making.

## Evaluation considerations

We will assess the methods on the following:
- Accuracy/performance
- Model assumptions (the more it makes the weaker the general use case)
- Parameter tuning complexity/ease-of-use
- Computational learning/training cost
- Robustness

## Robustness

Required:
- Evaluate results under different hyper parameter configurations (such as different values of lambda in LASSO)

Optional:
- Monte Carlo simulation with DGP based on empirical dataset
