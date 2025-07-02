# Copula Estimation Project: S&P 500 and Bond ETF

**Quantitative Risk Management**

This project demonstrates advanced techniques for modeling and analyzing the dependence structure between the S&P 500 (SPY) and a bond ETF (TLT) using **copulas**. It walks through the entire workflow from data collection to risk measure estimation, following best practices from quantitative risk management literature.

## 🚀 Project Goals

- Model and interpret the joint dependence between stock and bond returns  
- Apply copula methods to capture non-linear and tail dependence  
- Simulate joint returns from the estimated copulas  
- Calculate and compare risk measures (VaR, Expected Shortfall) for empirical and simulated returns  
- Provide a modular, reproducible Python implementation for similar future projects


## 💻 Usage

1. Clone this repository:
```bash
git clone https://github.com/mlnbui/Copula-Estimation.git
cd Copula-Estimation
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Follow the notebook cells to:
- download and clean data
- estimate marginals
- fit copulas
- simulate returns
- compute risk metrics