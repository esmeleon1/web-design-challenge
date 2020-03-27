import pandas as pd

cities = pd.read_csv('/Users/JLow/Desktop/UCD-DSB/web-design-challenge/WebVisualizations/Resources/cities.csv')

cities.to_html('/Users/JLow/Desktop/UCD-DSB/web-design-challenge/WebVisualizations/raw_data.html',
    classes=['table-bordered', 'table-striped', 'table-md-responsive'],
    index=False,
    justify='left')