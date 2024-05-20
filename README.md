# Hurst Estimators

Hurst Estimators is a Python library for estimating the Hurst exponent of time series data using various methods. This library includes implementations of several popular Hurst exponent estimation methods, as well as utilities for generating synthetic data and analyzing results.

## Installation

You can install the library using `pip`:

```sh
pip install hurst-estimators
```

or clone from the github repo:
```sh
git clone https://github.com/edesaras/hurst-estimators.git
```



## Importing the library

```python
import hurst_estimators as he
```

## Available Methods

### Time Domain Estimators 
* Central Estimator
* Detrended Fluctuation Estimator
* General Hurst Exponent Estimator
* Higuchi Estimator
* Rescaled Range Estimator

### Frequency Domain Estimators
* Periodogram Estimator

### Wavelet Estimators
* Average Wavelet Coefficient Estimator
* Variance Versus Level Wavelet Estimator

### Simulators
* Fractional Gaussian Noise (Circulant Embedding Method)

## Quick Example

## Contributing

## Citation

```bibtex
@software{hurst_estimators,
  author = {Aras Edes},
  title = {hurst-estimators: A Python library for Hurst exponent estimation},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/edesaras/hurst-estimators}},
}
```
