# Task 4
import pandas as pd
import os
from scipy import stats
import numpy as np
from bokeh.io import output_file, save
from bokeh.plotting import figure
from bokeh.models import LinearAxis, Range1d, ColumnDataSource
from bokeh.models.annotations import Label
from bokeh.models.tools import HoverTool
from bokeh.layouts import gridplot

# Bug notice: Some of the data recieved, had the leading '0' truncated off the front.
# For example '09180000' --> '9180000'
# If there are any errors with reading in the raw data, please check the site numbers.
site_list = ['09180000',  # DOLORES RIVER NEAR CISCO, UT,
             '09209400',  # GREEN RIVER NEAR LA BARGE, WY,
             '09260000',  # LITTLE SNAKE RIVER NEAR LILY, CO
             '09302000',  # DUCHESNE RIVER NEAR RANDLETT, UT,
             '09306500',  # WHITE RIVER NEAR WATSON, UTAH
             '09379500',  # SAN JUAN RIVER NEAR BLUFF, UT
             ]

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

# Read in Data
try:
    df = pd.read_csv('growing_season_et_and_flow.csv')
except:
    print("ERROR WHEN READING IN DATA")
    exit(1)


# Monthly scatter plot
output_file('growing_season_.html')
list_of_monthly_figs = []

for i in range(1):

    df_station = df[df["station_id"] == int(site_list[i])]
    print(df_station)

    p_month = figure(width=450, height=450)
    p_month.xgrid.grid_line_color = None
    p_month.ygrid.grid_line_color = None
    p_month.circle(x='discharge_mean_cfs', y='EToF_MEAN',
                   source=ColumnDataSource(df),
                   color='black', fill_color="#add8e6",
                   size=8)

    '''
    p_month.title.text = month_dict[i + 1] + ' - ' + site_name + ', ' + site
    p_month.yaxis.axis_label = 'EToF_MEAN, Monthly (mm/month)'
    p_month.xaxis.axis_label = cfs_var + ', Monthly (cfs)'

    # Calculate the least-square regression line
    regression_line = np.polyfit(df_monthly[cfs_var], df_monthly['EToF_MEAN'], 1, full=True)
    slope = regression_line[0][0]
    intercept = regression_line[0][1]
    y_predicted = [slope * i + intercept for i in df_monthly[cfs_var]]
    p_month.line(df_monthly[cfs_var], y_predicted, color='black')

    # Calculations to be used in the stats label on every scatter plot
    pearson_r, pearson_p = stats.pearsonr(df_monthly['EToF_MEAN'], df_monthly[cfs_var])
    kendall_r, kendall_p = stats.kendalltau(df_monthly['EToF_MEAN'], df_monthly[cfs_var])

    # The stats label to be added.
    label_text = 'Slope: ' + str(round(slope, 4)) + '\n' + \
                 'Intercept: ' + str(round(intercept, 4)) + '\n' + \
                 'Pearson r: ' + str(round(pearson_r, 4)) + '\n' + \
                 'Pearson P-Value: ' + str(round(pearson_p, 4)) + '\n' + \
                 'Kendall Tau: ' + str(round(kendall_r, 4)) + '\n' + \
                 'Kendall P-Value: ' + str(round(kendall_p, 4)) + '\n' + \
                 'n: ' + str(len(df_monthly))
    label = Label(x=255, y=20, x_units='screen', y_units='screen',
                  text_font_size='8pt', text=label_text)
    p_month.add_layout(label)

    hover3 = HoverTool()
    hover3.tooltips = [
        ('Year', '@year'),
        ('EToF_MEAN', '@EToF_MEAN'),
        (cfs_var, '@' + cfs_var)
    ]
    p_month.add_tools(hover3)

    list_of_monthly_figs.append(p_month)

save(gridplot([[list_of_monthly_figs[0], list_of_monthly_figs[1], list_of_monthly_figs[2], list_of_monthly_figs[3]],
               [list_of_monthly_figs[4], list_of_monthly_figs[5], list_of_monthly_figs[6], list_of_monthly_figs[7]],
               [list_of_monthly_figs[8], list_of_monthly_figs[9], list_of_monthly_figs[10],
                list_of_monthly_figs[11]]]))'''