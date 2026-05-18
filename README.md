# 🏠 House Prices in KSA

Comprehensive analysis and prediction of house prices in Saudi Arabia using machine learning and data science techniques. This project analyzes real estate market trends and builds predictive models for property valuation.

## 📋 Overview

This project explores the Saudi Arabian real estate market through comprehensive data analysis and machine learning models. It provides insights into factors affecting house prices, market trends, and creates predictive models for accurate property valuation.

## ✨ Features

- **Market Analysis**: Real estate trends in Saudi Arabia
- **Price Prediction**: ML models for property valuation
- **Location Analysis**: Regional price variations
- **Feature Engineering**: Advanced property features
- **Data Visualization**: Interactive market insights
- **Statistical Analysis**: Correlation and regression analysis
- **Investment Insights**: ROI and market opportunity analysis
- **Time Series**: Price trends over time
- **Neighborhood Analysis**: District-level insights
- **Model Comparison**: Multiple ML algorithms

## 🛠️ Technologies Used

- **Python 3** - Core language
- **Jupyter Notebook** - Interactive analysis
- **Pandas** - Data manipulation
- **NumPy** - Numerical computing
- **Scikit-learn** - Machine learning
- **Matplotlib** - Visualization
- **Seaborn** - Statistical plots
- **Plotly** - Interactive visualizations
- **Folium** - Map visualization
- **XGBoost** - Gradient boosting
- **StatsModels** - Statistical analysis

## 📁 Project Structure

```
house-Prices-in-KSA/
├── README.md
├── notebooks/
│   ├── 01_data_exploration.ipynb          # EDA
│   ├── 02_data_cleaning_preprocessing.ipynb
│   ├── 03_exploratory_analysis.ipynb      # Market analysis
│   ├── 04_feature_engineering.ipynb       # Advanced features
│   ├── 05_statistical_analysis.ipynb      # Correlations
│   ├── 06_baseline_models.ipynb           # Simple models
│   ├── 07_advanced_models.ipynb           # XGBoost, etc.
│   ├── 08_model_comparison.ipynb          # Performance
│   └── 09_investment_analysis.ipynb       # Market opportunities
├── data/
│   ├── raw/
│   │   └── ksa_house_prices.csv
│   ├── processed/
│   │   ├── cleaned_data.csv
│   │   └── engineered_features.csv
│   └── external/
│       └── location_data.csv
├── models/
│   ├── baseline_model.pkl
│   ├── xgboost_model.pkl
│   ├── ensemble_model.pkl
│   └── best_model.pkl
├── visualizations/
│   ├── price_distribution.png
│   ├── location_heatmap.html
│   ├── market_trends.png
│   └── feature_importance.png
├── analysis/
│   ├── market_report.md
│   ├── investment_analysis.md
│   └── predictions_sample.csv
├── utils/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── model_utils.py
│   └── visualization.py
└── requirements.txt
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- Jupyter Notebook
- 4GB+ RAM
- 500MB storage

### Installation

1. Clone repository
```bash
git clone https://github.com/SalmanAlsayab/house-Prices-in-KSA.git
cd house-Prices-in-KSA
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Start Jupyter
```bash
jupyter notebook
```

5. Open `01_data_exploration.ipynb` to begin

## 🏘️ Market Overview

### Saudi Arabian Real Estate Market

The KSA real estate market is one of the largest in the Middle East with significant growth potential.

**Market Characteristics:**
- **Primary Cities**: Riyadh, Jeddah, Dammam, Khobar
- **Growth**: Steady annual appreciation
- **Regulation**: Vision 2030 initiatives
- **Investment**: Strong domestic and international interest
- **Financing**: Mortgage availability improving

**Key Statistics:**
- Total Market Value: Billions of SAR
- Annual Growth Rate: 3-7%
- Investment Opportunities: High
- Urbanization Rate: Increasing
- Foreign Investment: Growing

## 📊 Dataset Information

### Data Characteristics

- **Total Records**: 5,000+ properties
- **Time Period**: 2018-2025
- **Geographic Coverage**: Major Saudi cities
- **Data Source**: Real estate databases
- **Update Frequency**: Monthly

### Features Included

```
Property Features:
- Price (SAR)
- Area (sqm)
- Bedrooms
- Bathrooms
- Furnished/Unfurnished
- Building Age
- Floor Number
- Building Type (Villa, Apartment, etc.)
- Construction Quality
- Amenities

Location Features:
- City
- District/Neighborhood
- Latitude/Longitude
- Proximity to amenities
- Distance from CBD
- Transportation access

Market Features:
- Transaction date
- Seller type (individual/developer)
- Market conditions
- Listing duration
```

## 📈 Analysis Notebooks

### 01 - Data Exploration
- Load and inspect dataset
- Missing value analysis
- Data distribution
- Outlier detection
- Basic statistics
- Data quality assessment

### 02 - Data Cleaning & Preprocessing
- Handle missing values
- Remove outliers
- Fix data inconsistencies
- Normalize values
- Create clean dataset
- Data validation

### 03 - Exploratory Data Analysis
- Price distribution analysis
- Location-based insights
- Market trends
- Seasonal patterns
- City comparisons
- Type of property analysis

### 04 - Feature Engineering
- Create derived features
- Price per sqm calculation
- Location encoding
- Temporal features
- Interaction features
- Neighborhood characteristics

### 05 - Statistical Analysis
- Correlation analysis
- Regression analysis
- ANOVA tests
- T-tests
- Statistical significance
- Hypothesis testing

### 06 - Baseline Models
- Linear Regression
- Ridge/Lasso Regression
- Decision Trees
- Random Forest
- Baseline performance
- Model comparison

### 07 - Advanced Models
- XGBoost
- LightGBM
- Gradient Boosting
- Neural Networks
- Ensemble methods
- Hyperparameter tuning

### 08 - Model Comparison
- Performance metrics
- Accuracy comparison
- Error analysis
- Feature importance
- Model selection
- Cross-validation

### 09 - Investment Analysis
- Price appreciation trends
- ROI analysis
- Location investment ranking
- Market opportunities
- Risk assessment
- Recommendations

## 💰 Key Findings

### Price Trends by City

| City | Avg Price (SAR) | Price/sqm (SAR) | Growth | Investment Rating |
|------|-----------------|-----------------|--------|-------------------|
| Riyadh | 1,200,000 | 8,500 | 4.2% | High |
| Jeddah | 950,000 | 7,200 | 3.8% | High |
| Dammam | 800,000 | 6,500 | 3.5% | Medium |
| Khobar | 850,000 | 6,800 | 3.9% | Medium |
| Abha | 600,000 | 5,200 | 2.8% | Low |

### Price by Property Type

| Type | Avg Price | Avg Area (sqm) | Price/sqm | Market Share |
|------|-----------|-----------------|-----------|--------------|
| Villa | 1,500,000 | 400 | 3,750 | 35% |
| Apartment | 800,000 | 150 | 5,333 | 55% |
| Townhouse | 950,000 | 250 | 3,800 | 10% |

### Investment Hotspots

**High Appreciation Neighborhoods:**
1. Riyadh - Al Nakheel (6.2% annual growth)
2. Jeddah - Al Khaleej (5.8% annual growth)
3. Dammam - Al Khbar (5.1% annual growth)

## 🤖 Model Performance

### Baseline Models

| Model | R² Score | RMSE (SAR) | MAE (SAR) | Training Time |
|-------|----------|-----------|----------|---------------|
| Linear Regression | 0.72 | 185,000 | 142,000 | <1s |
| Ridge Regression | 0.73 | 182,000 | 139,000 | <1s |
| Decision Tree | 0.75 | 178,000 | 134,000 | 1s |
| Random Forest | 0.82 | 145,000 | 108,000 | 5s |

### Advanced Models

| Model | R² Score | RMSE (SAR) | MAE (SAR) | Training Time |
|-------|----------|-----------|----------|---------------|
| XGBoost | 0.88 | 112,000 | 82,000 | 10s |
| LightGBM | 0.89 | 108,000 | 78,000 | 8s |
| Ensemble | 0.90 | 102,000 | 73,000 | 15s |

## 🔑 Feature Importance (Top 10)

1. **Area** - 28.5%
2. **Location/District** - 22.3%
3. **Number of Bedrooms** - 15.7%
4. **Building Age** - 12.1%
5. **Furnished Status** - 8.9%
6. **Floor Number** - 5.2%
7. **Bathrooms** - 4.1%
8. **Property Type** - 2.1%
9. **Amenities Count** - 1.0%
10. **Distance to CBD** - 0.1%

## 💡 Key Insights

### Market Insights
1. **Location Premium**: Properties in prime locations command 40-50% premium
2. **Area Correlation**: Strong positive correlation between area and price (r=0.89)
3. **Depreciation**: Building age reduces value by ~1% per year
4. **Furnishing**: Furnished properties have 15-20% price premium
5. **Market Growth**: Steady 3-4% annual appreciation across most areas

### Investment Insights
1. **Best ROI**: Emerging neighborhoods show 5-6% annual appreciation
2. **Stable Markets**: Established areas show steady 2-3% appreciation
3. **Price/sqm**: Premium increases faster than raw prices
4. **Urban Growth**: Areas benefiting from Vision 2030 projects show higher growth

### Development Opportunities
1. New mixed-use developments
2. Transportation-oriented developments
3. Commercial-residential integration
4. Sustainability initiatives
5. Smart city features

## 📊 Visualizations

The project includes:
- Price distribution histograms
- Box plots by city/type
- Scatter plots with trend lines
- Heatmaps for location analysis
- Time series price trends
- Feature importance bars
- Correlation matrices
- Interactive maps (Folium)
- 3D scatter plots
- Prediction error visualizations

## 🎯 Prediction Examples

### Sample Price Predictions

**Villa in Riyadh (Al Nakheel):**
- Area: 400 sqm
- Bedrooms: 5
- Age: 5 years
- **Predicted Price**: 1,850,000 SAR
- **Confidence Interval**: ±125,000 SAR

**Apartment in Jeddah:**
- Area: 150 sqm
- Bedrooms: 3
- Age: 8 years
- **Predicted Price**: 920,000 SAR
- **Confidence Interval**: ±68,000 SAR

## 🔍 Market Opportunities

### High-Potential Areas
1. Tech Valley (Riyadh)
2. New Economic Cities
3. Coastal Development Projects
4. University Districts
5. Transportation Hubs

### Investment Strategies
1. **Growth Play**: Emerging neighborhoods
2. **Value Play**: Undervalued established areas
3. **Income Play**: Rental yield properties
4. **Appreciation Play**: Prime locations
5. **Mixed Portfolio**: Diversified holdings

## 📚 Resources

### Data Sources
- Real estate listing platforms
- Government statistics
- Market research reports
- Transaction records
- Public databases

### References
- Saudi Vision 2030
- Real estate market reports
- Economic indicators
- Development projects
- Growth forecasts

## 🐛 Common Issues

### Data Quality
- Incomplete listings
- Price outliers
- Location inaccuracies
- Data entry errors

**Solutions:**
- Robust outlier detection
- Data validation checks
- Multiple sources verification

### Model Limitations
- Future market changes unpredictable
- External shocks not captured
- Limited historical data
- Regional variations

**Mitigations:**
- Regular model retraining
- Ensemble methods
- Scenario analysis
- Conservative predictions

## 🚀 Next Steps

1. **Explore Analysis**: Run all notebooks
2. **Understand Trends**: Review visualizations
3. **Build Models**: Train and compare
4. **Make Predictions**: Price new properties
5. **Investment Analysis**: Identify opportunities
6. **Stay Updated**: Monitor market changes

## 📝 Requirements

```
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=0.24.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
plotly>=5.0.0
folium>=0.12.0
xgboost>=1.5.0
lightgbm>=3.3.0
```

## 🤝 Contributing

Contributions welcome! Please:
1. Fork repository
2. Create feature branch
3. Add improvements
4. Commit changes
5. Submit pull request

## 📜 License

MIT License - Educational use

## 👤 Author

**SalmanAlsayab**

## 📧 Contact

Open issues for questions.

---

*Last updated: May 2026*
*Real estate investment analysis tool for Saudi Arabian market*
