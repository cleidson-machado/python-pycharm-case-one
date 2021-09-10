import pandas as pd
from Util import PlaceStorageStrings as Path


# MIGRATE!!
def company_colet_day_report_maker():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    print("--------------------------------------------------------- REPORT ONE ----")
    tab_data.sort_values(["COMPANY", "COLET_DAY"], ascending=True)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    tab_data.to_excel(Path.output_folder + Path.report_001, index=False)
    return print(tab_data['LOCAL_UF'].value_counts())
