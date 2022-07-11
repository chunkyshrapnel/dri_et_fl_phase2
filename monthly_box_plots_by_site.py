# Task 1
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Bug notice: Some of the data recieved, had the leading '0' truncated off the front.
# For example '09180000' --> '9180000'
# If there are any errors with reading in the raw data, please check the site numbers.
'''site_list = ['09180000',        # DOLORES RIVER NEAR CISCO, UT,
             '09209400',        # GREEN RIVER NEAR LA BARGE, WY,
             '09260000',        # LITTLE SNAKE RIVER NEAR LILY, CO
             '09302000',        # DUCHESNE RIVER NEAR RANDLETT, UT,
             '09306500',        # WHITE RIVER NEAR WATSON, UTAH
             '09379500',        # SAN JUAN RIVER NEAR BLUFF, UT
             ]'''

site_list = ['09180000']

# Dictionary used to transfer between strings and ints.
month_dict = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'Jun',
    7: 'Jul',
    8: 'Aug',
    9: 'Sept',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}


# Read in the metadata so that the site names can be attached to the graph.
try:
    df_metadata = pd.read_csv('raw_data/metadata.csv')
except:
    print("ERROR WITH READING METADATA")
    exit(1)

for site in site_list:

    site_name = df_metadata.loc[df_metadata['station_id'] == int(site),'site_name'].iloc[0]
    #output_file(site + '_' + ET_var + '_time_series.html')

    # Reads the data in for the given site
    try:
        df_et = pd.read_csv('raw_data/ucrb_riparain_et/'+ site +'_EEMETRIC_monthly_et_etof.csv')
    except:
        print("ERROR WHEN READING DATA FROM SITE: " + site)
        exit(1)

    # Changes the end date column to 'month' through string manipulation
    df_et['END_DATE'] = df_et['END_DATE'].apply(lambda x: int(x[5:7]))
    df_et.rename({'END_DATE': "Month"}, axis=1, inplace=True)

    '''
    # Changes the start date column from type 'string' to 'datetime'
    # This is needed for plotting the x axis
    df_merged['START_DATE'] = df_et['START_DATE'].apply(lambda x: pd.to_datetime(x))'''

    # Here the month column is changed from int to string.
    # Example: 1 --> 'jan'
    df_et['Month'] = df_et['Month'].apply(lambda x: month_dict[x])

    sns.boxplot(y=df_et["ET_MEAN"], x=df_et["Month"]).set(title=site_name + ' - ' + site)
    plt.show()
