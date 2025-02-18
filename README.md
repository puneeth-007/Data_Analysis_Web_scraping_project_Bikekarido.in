Analysis of Used Bikes on BikeKharido.in
Introduction
BikeKharido.infocuses on the buying and selling of two-wheeler vehicles. Our analysis project aims to identify the most popular used bikes available for sale and develop an application that facilitates finding bikes based on various parameters, such as price range and other features.

Project Tasks
The project consisted of the following tasks:

Data Extraction/Web Scraping

Preprocessing

Data Analysis

Visualization

Streamlit Application

Data Extraction
We utilized a two-layer page structure to extract the data:

Layer 1: List of bikes

Layer 2: Detailed bike information

The data was stored in a dataframe, redundant columns were removed, and formatting was done using Regex.

Preprocessing
Adjusted the pattern of the price column to ensure consistency.

Cleaned numerical columns and assigned appropriate data types.

Managed missing features.

Merged data from multiple layers and removed redundant columns.

Data Analysis
Univariate Analysis
Price: Range from ₹10,000 to ₹8,50,000, with an average price of ₹97,368.76.

Registration Year: Bikes registered from 2007 to 2024, with 2008 missing.

Make: Top manufacturers include Bajaj, Honda, Royal Enfield, TVS, and Hero.

Model: Most popular models are NTORQ 125, Classic 350, Bullet 350, Interceptor 650, and Pulsar 150.

Fuel Type: Predominantly petrol bikes (97.1%), with a small percentage of EVs (2.9%).

Ownership: Mostly first-hand bikes, followed by second-hand, third-hand, and above.

Kilometers Driven: Ranges up to 200,000 km.

Bivariate Analysis
Price vs Make: Higher average prices for brands like Ducati, Kawasaki, and BMW.

Make vs Count: Bajaj has the highest number of bikes available.

Price vs Registration Year: Newer bikes tend to have higher prices.

Multivariate Analysis
Correlation Analysis: Explored relationships between numerical features such as price, registration year, kilometers driven, and engine capacity.

Streamlit Application
A Streamlit application was developed to facilitate data exploration with the following features:

Price range filter

Ownership filter

Brand filter

Year of registration filter

The application allows users to visualize data through scatter plots and sunburst charts, and to download the data as CSV files.

Final Thoughts & Recommendations
For Buyers: Look for first-owner, low-mileage bikes from reputed brands for the best value.

For Sellers: Maintaining bikes well and selling within 3-5 years maximizes resale value.

For BikeKharido.in: Implementing price recommendation tools and improving listing quality can enhance user experience.
