import pandas as pd
import numpy as np

df = pd.read_csv('data/final.csv', sep=';', encoding='utf-8')

print(df.columns)

temp_df = pd.read_csv('data/avg_temp_cities.csv', sep=';', encoding='utf-8')
df = df.join(temp_df.set_index('NUTS Region'), on='NUTS Region')

to_be_dropped = [
    "CO", "NO", "SO2", "PM10",
    "Euro per inhabitant in percentage of the EU27 (from 2020) average",
    "Million euro",
    "Million purchasing power standards (PPS, EU27 from 2020)",
    "Million units of national currency",
    "Purchasing power standard (PPS, EU27 from 2020), per inhabitant in percentage of the EU27 (from 2020) average",

]
df = df.drop(to_be_dropped, axis=1)

df = df.dropna()

for DISEASE in [
                    'All causes of death (A00-Y89) excluding S00-T98',
                    'Asthma and status asthmaticus',
                    'Chronic lower respiratory diseases' ,
                    'Cerebrovascular diseases',
                    'Diabetes mellitus',
                    'Malignant melanoma of skin' ,
                    'Malignant neoplasm of breast',
                    'Malignant neoplasm of colon, rectosigmoid junction, rectum, anus and anal canal',
                    'Malignant neoplasm of trachea, bronchus and lung',
                    'Mental and behavioural disorders (F00-F99)',
                    'Other ischaemic heart diseases',
                    'Other mental and behavioural disorders (remainder of F00-F99)'
                ]:
    


    y = df[DISEASE]
    to_be_dropped_diseases = [
        'NUTS Region',
        'Acute myocardial infarction including subsequent myocardial infarction',
        'All causes of death (A00-Y89) excluding S00-T98',
        'Asthma and status asthmaticus',
        'Chronic lower respiratory diseases' ,
        'Cerebrovascular diseases',
        'Diabetes mellitus',
        'Malignant melanoma of skin' ,
        'Malignant neoplasm of breast',
        'Malignant neoplasm of colon, rectosigmoid junction, rectum, anus and anal canal',
        'Malignant neoplasm of trachea, bronchus and lung',
        'Mental and behavioural disorders (F00-F99)',
        'Other ischaemic heart diseases',
        'Other mental and behavioural disorders (remainder of F00-F99)',
    ]
    x = df.drop(to_be_dropped_diseases, axis=1)

    from sklearn.model_selection import train_test_split

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=10)

    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler().fit(x_train)

    x_train_scaled = scaler.transform(x_train)
    x_test_scaled = scaler.transform(x_test)


    SCALE = False

    if SCALE:
        x_train = pd.DataFrame(x_train_scaled, index=x_train.index, columns=x_train.columns)
        x_test = pd.DataFrame(x_test_scaled, index=x_test.index, columns=x_test.columns)
    else:
        x_train = pd.DataFrame(x_train, index=x_train.index, columns=x_train.columns)
        x_test = pd.DataFrame(x_test, index=x_test.index, columns=x_test.columns)

    df_train = y_train.to_frame().join(x_train)
    df_test = y_test.to_frame().join(x_test)

    # print number of rows and columns in the dataset
    print("Training dataset has {} rows and {} columns.".format(*df_train.shape))

    import matplotlib.pyplot as plt
    import numpy as np
    from collections import OrderedDict


    from sklearn.ensemble import RandomForestRegressor
    from sklearn.model_selection import GridSearchCV
    from sklearn.metrics import mean_squared_error
    from sklearn.metrics import r2_score
    from sklearn.inspection import permutation_importance

    y_train = np.ravel(y_train)
    y_test = np.ravel(y_test)


    params = {
        "n_estimators": 100,
        "max_depth": 3,
        "warm_start":True,
        "oob_score":True,
        "random_state": 42,
    }

    reg = RandomForestRegressor(**params)

    reg.fit(x_train, y_train)

    y_train_pred = reg.predict(x_train)
    y_test_pred = reg.predict(x_test)

    R2_train = r2_score(y_train, y_train_pred)
    R2_test = r2_score(y_test, y_test_pred)
    print(f"R2: {R2_test}, Disease: {DISEASE}")