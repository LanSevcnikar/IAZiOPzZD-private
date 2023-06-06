file = 'C:/Users/sevcn/Documents/programming/projects/IAZiOPzZD-private/GermanyPoC/EuroStat/EuroStat.csv'

import pandas as pd

df = pd.read_csv(file, encoding='utf-8', sep=';')
# find all the causes of death
causes = df['ICD-10 2010'].unique()
print (causes)

(0,'All causes of death (A00-Y89) excluding S00-T98'),
(1,'Malignant neoplasm of liver and intrahepatic bile ducts'),
(2,'Malignant neoplasm of pancreas'),
(3,'Malignant neoplasm of larynx'),
(4,'Malignant neoplasm of trachea, bronchus and lung'),
(5,'Malignant melanoma of skin'),
(6,'Malignant neoplasm of kidney, except renal pelvis'),
(7,'Malignant neoplasm of brain and central nervous system'),
(8,'Diseases of the blood and blood-forming organs and certain disorders involving the immune mechanism'),
(9,'Other heart diseases'),
(10,'Influenza (including swine flu)')