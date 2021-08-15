import pandas as pd
import plotly
import plotly.express as px
import os
import re



# function importing data from json and recording it to pandas dataframe, adding column with trial name 
def extractData(file_list, folder):
    dfs = [] # an empty list to store the data frames
    for file in file_list:
        data = pd.read_json(folder + file,  orient = 'split') # read data frame from json file
        filename = os.path.basename(folder+file)
        trial = int(re.findall(r'\d+', filename)[0])
        data['trial'] = trial
        dfs.append(data) # append the data frame to the list
    


    temp = pd.concat(dfs, ignore_index=True) # concatenate all the data frames in the list.
    name = re.findall('^.{0,3}', filename)[0]
    temp.columns = ['patient', str('min_' + name), str('max_' + name), 'trial']
    return temp



if __name__ == ('__main__'):
    folder = r'C:\Users\ksesh\Documents\Python\Study 1 iMBE\imbestudy1\Data\\'
    LF = ['21', '24', '32', '63', '66', '78',
        '102', '119', '126', '133', '8', '69', '85', '89',
        '100', '112', '115', '117', '136']
    data_version = extractData(['version_trial1_limits_all_patients.json', 'version_trial2_limits_all_patients.json', 'version_trial3_limits_all_patients.json', 'version_trial4_limits_all_patients.json'], folder)
    data_inclination = extractData(['inclination_trial1_limits_all_patients.json', 'inclination_trial2_limits_all_patients.json', 'inclination_trial3_limits_all_patients.json', 'inclination_trial4_limits_all_patients.json'], folder)
    data = pd.merge(data_version, data_inclination, on = ['patient', 'trial'])
    data.loc[data.patient.isin(LF), 'function'] = 'LF'
    data.loc[data.patient.isin(LF) == False, 'function'] = 'HF'
    df2 = {'patient': 86, 'trial': 4, 'function': 'HF', 'min_ver': -3.11, 'min_inc': 40.41, 'max_inc' : 45.32}
    data = data.append(df2, ignore_index=True)
    fig = px.scatter(data, x='min_ver', y='min_inc', color = 'function', size_max=35, animation_frame='trial', animation_group='patient',
                    hover_name='patient', labels=dict(min_ver="First Angle [<sup>o</sup>]", min_inc="Second Angle [<sup>o</sup>]"))
    fig.update_traces(marker=dict(size=18,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
    fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000

    plotly.offline.plot(fig, 'AnimatedPlots.html')