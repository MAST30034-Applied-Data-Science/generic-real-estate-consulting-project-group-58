# MAST30034 Project 2, 'Generic Real Estate Consulting Project', README.md
## Group 58
- Name2: Borui Zou, Ruiyi Hao, Yinuo Sun, Yizhu Zhu, Zixuan Lin 
- Student IDs: 1173911, 1133452, 1045919, 1174257, 1135311

**Research Goal:** This research goal is to predict the rental prices in Victoria region published from Domain. The project chooses the 'Simply Liner Regression(LR)' as the baseline model and 'Generalized Linear Regression(GLM)' as an extension of 'LR', and the compares the previous statistical models with machine learning models, including 'XGB', 'GradientBoosting', 'RandomForest', 'Adaboost', 'Artificial Neural Networks(ANA)'.

**Timeline:** The timelines for the research features are from: .

To run the pipeline, please visit the `notebook` directory and run the files in order:
1. 'domain_scrapy.py/scripts', 'external_scrapy.py/scripts': For raw internal and external data downloading from website and data saving into `data/raw`.
2. 'distance.py/scripts', 'non_inco_distance.py/scripts': For distance to Melbourne CBM data downloading by openrouteservice andd data saving into 'data/curated'.
3. 'Pre-processing.ipynb/notebooks`: For data extracting, data cleansing, converting features from 'SA2' to 'Postcode(suburb)', and data aggregation.
4. 'Preliminary Analysis.ipynb/notebooks:': For feature distribution analysis and checking outliers.
5. 'Split_train_valid.ipynb.notebooks': For spliting tarin, valid, predict dataset in to 'data/curated'.
6. 'Visualisation.ipynb/notebooks': For geospatial visualisation.
7. 'Baseline_model.ipynb/models': For modeling 'LR'.
8. 'glm.ipynb/models': For modeling 'GLM'.
9. 'ML_model.ipynb/models': For modeling machine learning models.
