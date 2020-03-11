def recency_days3 (last_date,row):
    '''input: the date when the order was done, subtracting from the last date registered in the dataframe
    output: difference in days'''
    return abs((last_date - row['Date']).days)


import cufflinks as cf
from lifelines import KaplanMeierFitter
def survival(data, group_field, time_field, event_field):
    kmf = KaplanMeierFitter()
    results = []

    for i in data[group_field].unique():
        group = data[data[group_field]==i]
        T = group[time_field]
        E = group[event_field]
        kmf.fit(T, E, label=str(i))
        results.append(kmf.survival_function_)

    survival = pd.concat(results, axis=1)
    front_fill = survival.fillna(method='ffill')
    back_fill = survival.fillna(method='bfill')
    smoothed = (front_fill + back_fill) / 2
    return smoothed