# MAST30034 Project 2, 'Generic Real Estate Consulting Project', README.md
## Group 58
- Name2: Borui Zou, Ruiyi Hao, Yinuo Sun, Yizhu Zhu, Zixuan Lin 
- Student IDs: 1173911, 1133452, 1045919, 1174257, 1135311

**Research Goal:** This research aims to predict 2025 rental prices in Victoria based on current (2022) data published from Domain rental website together with some other open data sources. This project chooses the 'Simply Liner Regression(LR)' as the baseline model and 'Generalized Linear Regression(GLM)' as an extension of 'LR', and compares these statistical models with machine learning and neural network models, including 'XGB', 'GradientBoosting', 'RandomForest', 'Adaboost', 'Artificial Neural Networks(ANN)'. Finally, we provide solutions based on our predicted rental prices to the 3 main questions:

1. What are the most important internal and external features in predicting rental prices? 
2. What are the top 10 suburbs with the highest predicted growth rate?
3. What are the most liveable and affordable suburbs according to your chosen metrics?


**Timeline:** The timeline for the research is from now to 3 years later, 2022-2025. All data are collected for year 2022, rental predictions are based on predicted data for 2025. However, data for some features might not exists for 2022, so some features without current data are predicted according to the historical data.

To run the pipeline, please visit the `notebooks`, `scripts` as well as `models` directories and run the files in order:
1. `domain_scrape.py/scripts`, `external_scrape.py/scripts`: For raw internal and external data downloading from websites and data saving into `data/raw`.
2. `distance.py/scripts`, `non_inco_distance.py/scripts`: For distance to Melbourne CBM data downloading by openrouteservice and data saving into `data/curated`. (Is very time consuming, costing over 10 hrs. Therefore, we do not recommend to run the files because the data has already saved in `Pre-processing.ipynb/notebooks`, the distance lists for data with income [distance_list] and without income [non_inco_distance_list] can also be found in data folder, outside the raw and curated directories)
3. `Pre-processing.ipynb/notebooks`: For data reading, data cleaning, converting features from 'SA2' to 'Postcode(suburb)', and data aggregation.
4. `Preliminary Analysis.ipynb/notebooks`: For general analysis including checking distribution of attributes, correlation between attributes as well as outliers detection and removal.
5. `Split_train_valid.ipynb.notebooks`: For spliting tarin, valid, predict dataset, data saving in to `data/curated`.
6. `Visualisation.ipynb/notebooks`,`Visualisation2.ipynb/notebooks`: For geospatial visualisation.
7. `Baseline_model.ipynb/models`: For modeling 'LR'.
8. `glm.ipynb/models`: For modeling 'GLM'.
9. `ML_model.ipynb/models`: For modeling machine learning models.
