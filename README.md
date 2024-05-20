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
@software{edes_2024_11224470,
  author       = {Edes, Aras},
  title        = {{hurst-estimators: A Python library for Hurst 
                   exponent estimation}},
  month        = may,
  year         = 2024,
  publisher    = {Zenodo},
  version      = {v0.0.3-alpha},
  doi          = {10.5281/zenodo.11224470},
  url          = {https://doi.org/10.5281/zenodo.11224470}
}
```
