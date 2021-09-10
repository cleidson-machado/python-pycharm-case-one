import pandas as pd
from Util import PlaceStorageStrings as Path


def company_colet_day_report_maker():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    print("--------------------------------------------------------- REPORT THREE ----")
    # a_local = ['SP']
    a_local = ['SP', 'MG']
    tab_data.loc[tab_data['LOCAL_UF'].isin(a_local)].to_excel(Path.output_folder + Path.report_002, index=False)
    # tab_data.sort_values(["COMPANY", "COLET_DAY"], ascending=True)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    # tab_data[tab_data['CHECK_STATUS'] == 'NO UPDATING YET FROM THE BRANCH TEAM, WE ASKED TO SCHEDULE THE SERVICE.']
    # tab_data.to_excel(Path.output_folder + Path.report_002, index=False)
    # return print(tab_data['LOCAL_UF'] == 'SP')
    return print(tab_data.loc[tab_data['LOCAL_UF'].isin(a_local)])
