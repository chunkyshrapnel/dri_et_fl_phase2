# Task 4
import pandas as pd

site_list = ['09180000',  # DOLORES RIVER NEAR CISCO, UT,
             '09209400',  # GREEN RIVER NEAR LA BARGE, WY,
             '09260000',  # LITTLE SNAKE RIVER NEAR LILY, CO
             '09302000',  # DUCHESNE RIVER NEAR RANDLETT, UT,
             '09306500',  # WHITE RIVER NEAR WATSON, UTAH
             '09379500',  # SAN JUAN RIVER NEAR BLUFF, UT
             ]


# Reads the data in for the dishcarge raw data.
list_of_flow_dfs =[]
for site in site_list:
    try:
        df_flow = pd.read_csv('raw_data/flow/' + site + '_monthly_summary.csv')
    except:
        print("ERROR WHEN READING DATA FROM SITE: " + site)
        exit(1)
    list_of_flow_dfs.append(df_flow)

# Read the data in for the et growing seasons.
try:
    df_et = pd.read_excel('raw_data/ucrb_riparain_et/ucrc_riparian_means.xlsx')
except:
    print("ERROR WHEN READING DATA FROM: ucrc_riparian_means.xlsx")
    exit(1)