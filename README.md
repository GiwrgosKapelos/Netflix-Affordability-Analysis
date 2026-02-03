# Is Netflix Actually "Cheap"? 🌍🎬

An Analysis of Global Pricing vs. Purchasing Power

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-ff69b4?style=flat&logo=pandas)
![Data-Analysis](https://img.shields.io/badge/Analysis-Data%20Science-green)

## 💡 The Concept
We often see news about Netflix price hikes or "cheap" subscriptions in different countries. But is a $3 monthly fee truly cheap for someone living in Pakistan compared to a $15 fee for someone in Switzerland?

This project explores the Affordability Gap. By cross-referencing global Netflix pricing with World Bank economic data (GDP per capita), I calculated an **Affordability Index** to show the real economic weight of a digital subscription on households worldwide.

## 📊 Key Insights
* **The Nominal Price Trap:**
 Lower prices in developing nations don't equate to affordability.
* **Systemic Inequality:** In some regions, like Burundi, a standard subscription can consume up to 43.7% of the average annual income.
* **Digital Divide:** While the service is the same globally, the financial barrier to entry varies by over 600x between the most and least affordable markets.

## 🖼️ Visualizations
![Most Affordable Countries Netflix Annual Cost as Percsent of GDP per Capita (2024)](https://github.com/user-attachments/assets/d92ecf75-c263-4da8-a42b-455df21307c6)
> **Figure 1**: This visualization highlights the "Affordability Gap." While nominal prices might be lower in developing nations, the cost relative to average income (GDP per capita) reveals a significant economic burden in those regions.
> 
## 🛠️ Project Structure
I've organized the work into logical steps to make it easy to follow: 

* 📂 `/scripts:` Python scripts using pandas for data cleaning and merging (GDP, Population, and Pricing datasets).
* 📂 `/data:` Contains both the raw World Bank CSVs and the final cleaned datasets used for visualization.
* 📂 `/docs:` The final report (PDF) and the presentation (PPTX) that summarize the findings.

## 🚀 How to Use
1. **Clone the repo:** ```git clone https://github.com/your-username/repository-name.git```
2. **Install dependencies:** ```pip install pandas```
3. Run the cleaning scripts in the scripts/ folder to see how the data was transformed.

## 🎓 Academic Context
This project was developed as part of the MSc in Computer Science at the University of Peloponnese for the "Data Visualization" course.
