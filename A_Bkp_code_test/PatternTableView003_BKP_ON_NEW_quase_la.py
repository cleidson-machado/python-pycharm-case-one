import pandas as pd
from Util import PlaceStorageStrings as Path


def company_colet_day_report_maker():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    # EMAIL_ACT
    print("--------------------------------------------------------- REPORT THREE ----")
    phrases = ['NO UPDATING YET FROM THE BRANCH TEAM, WE ASKED TO SCHEDULE THE SERVICE.']
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    tab_data.loc[tab_data['CHECK_STATUS'].isin(phrases)].to_excel(Path.output_folder + Path.report_002, index=False)
    return print(tab_data['CHECK_STATUS'].value_counts())
