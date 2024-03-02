# InvestX
# Stock Prediction Project

This project is an amalgamation of technical analysis, fundamental data exploration, and web scraping techniques aimed at predicting stock prices with enhanced accuracy.

# Technical Indicators
We implemented a variety of technical indicators (Momentum, Volume and Volatility) such as Average Directional Index, Donchian Channel and Volume Price Indicator on real-world stock market data. These indicators provide valuable insights into price trends, momentum, and volatility, aiding in the prediction process.

# Black-Scholes Option Pricing Model

The Black-Scholes model is a mathematical model used to calculate the theoretical price of European-style options. It is widely used by options traders and investors to determine the fair value of options contracts.

## Key Components

### 1. Underlying Asset Price (S)
The current market price of the underlying asset, such as a stock or index.

### 2. Strike Price (K)
The predetermined price at which the option holder has the right to buy (call option) or sell (put option) the underlying asset.

### 3. Time to Expiration (T)
The time remaining until the expiration date of the option contract, usually measured in years.

### 4. Risk-free Interest Rate (r)
The risk-free interest rate, typically the yield on government bonds, which represents the opportunity cost of holding money over the option's time horizon.

### 5. Volatility (σ)
The standard deviation of the returns of the underlying asset, representing the degree of price fluctuation or uncertainty.

## Formula

The Black-Scholes formula for calculating the theoretical price (P) of a European call option is:

\[ C = S_0 N(d_1) - K e^{-rT} N(d_2) \]

Where:
- \( C \) = Call option price
- \( S_0 \) = Current stock price
- \( N(d_1) \) and \( N(d_2) \) = Cumulative distribution functions of the standard normal distribution
- \( K \) = Strike price
- \( r \) = Risk-free interest rate
- \( T \) = Time to expiration
- \( d_1 \) and \( d_2 \) = Parameters calculated as follows:

d1 = (ln(K / S0) + (r + (σ^2) / 2) * T) / (σ * sqrt(T))

d2 = d1 - σ * sqrt(T)
## Usage
To use the Black-Scholes model, input the values of the underlying asset price, strike price, time to expiration, risk-free interest rate, and volatility into the formula. The result will provide an estimate of the fair value of the option contract.
# Technical Indicator Formulas

This README provides formulas for three popular technical indicators: Donchian Channel, Average Directional Index (ADX), and Volume Price Indicator (VPI).

### Donchian Channel
The Donchian Channel consists of three lines:
- **Upper Channel Line (UCL):** Highest high for the last N periods.
- **Lower Channel Line (LCL):** Lowest low for the last N periods.
- **Middle Channel Line (MCL):** Midpoint between the UCL and LCL.

#### Formulas:
- **UCL:** Highest High (HH) of the last N periods.
- **LCL:** Lowest Low (LL) of the last N periods.
- **MCL:** (UCL + LCL) / 2

### Average Directional Index (ADX)
ADX is used to quantify the strength of a trend. It is calculated based on the smoothed moving averages of price movements.

#### Formulas:
1. **True Range (TR):** Maximum of (High - Low), (High - Previous Close), or (Previous Close - Low).
2. **+DI (Plus Directional Indicator):** Smoothed average of positive price movements over N periods.
3. **-DI (Minus Directional Indicator):** Smoothed average of negative price movements over N periods.
4. **Average True Range (ATR):** Smoothed average of TR over N periods.
5. **DX (Directional Movement Index):** (|+DI - -DI|) / (+DI + -DI)
6. **ADX:** Smoothed average of DX over N periods.

### Volume Price Indicator (VPI)
VPI combines price and volume to show how much volume is associated with a price movement.

#### Formulas:
- **VPI:** [(Close - Open) / Open] * Volume

These formulas can be implemented in various programming languages to calculate the respective technical indicators for stock market analysis and prediction.

# Fundamental Data Analysis
In addition to technical indicators, we conducted in-depth analysis on fundamental data including earnings reports,dividends , and company financials. By identifying key metrics that correlate with stock price movements, we gained further understanding of the underlying factors driving market behavior.

# Integration of Technical Indicators
To improve the robustness of our predictions, we integrated the findings from technical analysis with fundamental data exploration. This synergistic approach enabled us to leverage the strengths of both methodologies, resulting in more accurate forecasts.

# Web Scraping with Selenium
Furthermore, we utilized Selenium to scrape additional market data from the Opstra website. This data augmentation strategy provided us with a richer dataset for analysis, allowing for deeper insights and more informed decision-making.

## Requirements
- Python
- Libraries: Pandas, NumPy, Matplotlib, Scikit-learn, Selenium, Tensorflow

## Usage
1. Run scripts for technical indicator calculation.
2. Analyze fundamental data and integrate it with technical indicators.
3. Execute predictive models using integrated data.
4. Configure Selenium webdriver for web scraping and utilize scripts to extract data from Opstra.

## Note
Ensure proper configuration of Selenium webdriver and adhere to web scraping guidelines when extracting data from external sources.
