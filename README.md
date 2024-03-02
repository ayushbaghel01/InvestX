# InvestX
# Stock Prediction Project

This project is an amalgamation of technical analysis, fundamental data exploration, and web scraping techniques aimed at predicting stock prices with enhanced accuracy.

# Technical Indicators
We implemented a variety of technical indicators (Momentum, Volume and Volatility) such as Average Directional Index, Donchian Channel and Volume Price Indicator on real-world stock market data. These indicators provide valuable insights into price trends, momentum, and volatility, aiding in the prediction process.
## Technical Indicator Formulas

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

## Fundamental Data Analysis
In addition to technical indicators, we conducted in-depth analysis on fundamental data including earnings reports,dividends , and company financials. By identifying key metrics that correlate with stock price movements, we gained further understanding of the underlying factors driving market behavior.

## Integration of Technical Indicators
To improve the robustness of our predictions, we integrated the findings from technical analysis with fundamental data exploration. This synergistic approach enabled us to leverage the strengths of both methodologies, resulting in more accurate forecasts.

## Web Scraping with Selenium
Furthermore, we utilized Selenium to scrape additional market data from the Opstra website. This data augmentation strategy provided us with a richer dataset for analysis, allowing for deeper insights and more informed decision-making.

### Requirements
- Python
- Libraries: Pandas, NumPy, Matplotlib, Scikit-learn, Selenium, Tensorflow

### Usage
1. Run scripts for technical indicator calculation.
2. Analyze fundamental data and integrate it with technical indicators.
3. Execute predictive models using integrated data.
4. Configure Selenium webdriver for web scraping and utilize scripts to extract data from Opstra.

### Note
Ensure proper configuration of Selenium webdriver and adhere to web scraping guidelines when extracting data from external sources.
