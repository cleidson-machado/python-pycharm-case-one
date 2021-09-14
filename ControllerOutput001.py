import pandas as pd
from datetime import date
from Util import PlaceStorageStrings as Place
import numpy as np
from Util import Cleaner as Clean
from Util import PlaceStorageStrings as Configure


# HERE I AM CREATE A FIRST FILE JOIN FILE TO THIS SYSTEM...
def company_work_join_file_maker():
    tab_data = pd.read_excel(Configure.output_folder + Configure.basic_join_file)

    filter_view_warning = "THE FIRST JOIN DATA TABLE"

    # READING / CLEANING
    tab_data['Opened'] = tab_data['Opened'].apply(Clean.remove_at_sign)
    tab_data['Opened'] = tab_data['Opened'].apply(Clean.remove_letters)
    tab_data['Opened'] = tab_data['Opened'].apply(Clean.remove_some_special_characters)

    # COLUMN Opened DATE TIME FORMATTER
    tab_data['Opened'] = pd.to_datetime(tab_data['Opened'], errors='ignore')  # FIRST CONVERSION
    tab_data['Opened'] = tab_data['Opened'].dt.strftime('%Y-%m-%d')  # REMOVE TIME INFORMATION
    tab_data['Opened'] = pd.to_datetime(tab_data['Opened'], errors='ignore')  # SECOND CONVERSION

    # COLUMN Cust IA DATE TIME FORMATTER
    tab_data['Cust IA'] = pd.to_datetime(tab_data['Cust IA'], errors='ignore')  # JUST CONVERSION

    # RENAME COLUMNS
    tab_data.set_axis(Configure.output_columns, axis='columns', inplace=True)

    # BEGIN COUNT LIVE DAY FOR THE TASKS -------------------------------------------------------------------------------
    colet_day_of_a_task = tab_data["COLET_DAY"]
    open_day_of_a_task = tab_data["OPEN_TASK_DAY"]

    delta_difference = colet_day_of_a_task - open_day_of_a_task

    for row in tab_data.iterrows():
        tab_data["OPEN_TASK_MONTH"] = delta_difference
    # END COUNT LIVE DAY FOR THE TASKS ---------------------------------------------------------------------------------

    # CREATE A FIRST WORKING TABLE
    tab_data.to_excel(Configure.output_folder + Configure.work_join_file, index=False)

    print("STATUS MAKER:  ", filter_view_warning, " ... OK! >>", Place.work_join_file)  # ... THE FIRST JOIN DATA TABLE


# HERE I AM CREATE A FIRST FILE FOR HUMAN ANALYSIS... PERIOD SEVEN DAYS
def company_colet_day_report_maker():
    tab_data = pd.read_excel(Place.output_folder + Place.work_join_file)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

    filter_view_warning = "THE BASIC DATA TABLE"

    # FILTER FOR DATE PERIOD START
    date_period = pd.Series(pd.date_range("2021-09-04", freq="D", periods=7), dtype=np.dtype("O"))  # ITS WORK GOOD!

    # BEGIN COUNT LIVE DAY FOR THE TASKS -------------------------------------------------------------------------------
    colet_day_of_a_task = tab_data["COLET_DAY"]
    open_day_of_a_task = tab_data["OPEN_TASK_DAY"]

    delta_difference = colet_day_of_a_task - open_day_of_a_task

    for row in tab_data.iterrows():
        tab_data["OPEN_TASK_MONTH"] = delta_difference
    # END COUNT LIVE DAY FOR THE TASKS ---------------------------------------------------------------------------------

    tab_data.loc[tab_data['COLET_DAY'].isin(date_period)].to_excel(Place.output_folder + Place.report_001, index=False)

    print("STATUS MAKER:  ", filter_view_warning, " ... OK! >>", Place.report_001)  # ... PERIOD SEVEN DAYS


# HERE I AM CREATE THE EXCEL FILTER FILE FOR RED FLAG ONLY... PERIOD ALL FILES ON SOURCE FOLDER
def filter_task_red_phrases():
    tab_data = pd.read_excel(Place.output_folder + Place.work_join_file)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

    filter_view_warning = "PHRASES AND ADD FLAGS TO RED"

    # HERE ADD TAG COLOR RED...
    for row in tab_data.iterrows():
        tab_data.loc[tab_data["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "RED"

    # BEGIN COUNT LIVE DAY FOR THE TASKS -------------------------------------------------------------------------------
    colet_day_of_a_task = tab_data["COLET_DAY"]
    open_day_of_a_task = tab_data["OPEN_TASK_DAY"]

    delta_difference = colet_day_of_a_task - open_day_of_a_task

    for row in tab_data.iterrows():
        tab_data["OPEN_TASK_MONTH"] = delta_difference
    # END COUNT LIVE DAY FOR THE TASKS ---------------------------------------------------------------------------------

    # FILTER RED PHRASES START
    tab_data.loc[tab_data['CHECK_STATUS'].isin(Place.red_phrases_list)].to_excel(Place.output_folder + Place.report_002,
                                                                                 index=False)
    print("STATUS FILTER: ", filter_view_warning, " ... OK! >>", Place.report_002)


# HERE I AM CREATE THE EXCEL FILTER FILE FOR BLUE FLAG ONLY... PERIOD ALL FILES ON SOURCE FOLDER
def filter_task_scheduled_phrases():
    tab_data = pd.read_excel(Place.output_folder + Place.work_join_file)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

    filter_view_warning = "SCHEDULED FOR..."

    # HERE ADD TAG COLOR BLUE...
    for row in tab_data.iterrows():
        tab_data.loc[tab_data["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "BLUE"

    # BEGIN COUNT LIVE DAY FOR THE TASKS -------------------------------------------------------------------------------
    colet_day_of_a_task = tab_data["COLET_DAY"]
    open_day_of_a_task = tab_data["OPEN_TASK_DAY"]

    delta_difference = colet_day_of_a_task - open_day_of_a_task

    for row in tab_data.iterrows():
        tab_data["OPEN_TASK_MONTH"] = delta_difference
    # END COUNT LIVE DAY FOR THE TASKS ---------------------------------------------------------------------------------

    # FILTER BLUE PHRASES START
    tab_data.loc[tab_data['CHECK_STATUS'].str.contains(Place.filter_words)].to_excel(
        Place.output_folder + Place.report_003,
        index=False)
    print("STATUS FILTER: ", filter_view_warning, " ... OK! >>", Place.report_003)


# HERE I AM CREATE THE EXCEL FILTER FILE FOR YELLOW FLAG ONLY... PERIOD ALL FILES ON SOURCE FOLDER
def filter_task_no_red_phrases():
    tab_data = pd.read_excel(Place.output_folder + Place.work_join_file)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

    filter_view_warning = "NO RED OR BLUE PHRASES"

    # HERE ADD TAG COLOR BLUE...
    for row in tab_data.iterrows():
        tab_data.loc[tab_data["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "YELLOW"

    # FILTER YELLOW PHRASES START PHASE 01 -- ALL NO RED PHRASES
    no_red = tab_data.loc[~tab_data['CHECK_STATUS'].isin(Place.red_phrases_list)]

    # BEGIN COUNT LIVE DAY FOR THE TASKS -------------------------------------------------------------------------------
    colet_day_of_a_task = tab_data["COLET_DAY"]
    open_day_of_a_task = tab_data["OPEN_TASK_DAY"]

    delta_difference = colet_day_of_a_task - open_day_of_a_task

    for row in tab_data.iterrows():
        tab_data["OPEN_TASK_MONTH"] = delta_difference
    # END COUNT LIVE DAY FOR THE TASKS ---------------------------------------------------------------------------------

    # FILTER YELLOW PHRASES START PHASE 02 -- ALL NO SCHEDULED PHRASES
    no_red.loc[~no_red['CHECK_STATUS'].str.contains(Place.filter_words)].to_excel(
        Place.output_folder + Place.report_004,
        index=False)
    print("STATUS FILTER: ", filter_view_warning, " ... OK! >>", Place.report_004)


# HERE I AM CREATE THE EXCEL FILTER FILE FOR TODAY TASKS... PERIOD TODAY TASKS
def filter_count_today_phrases_status():
    tab_data = pd.read_excel(Place.output_folder + Place.work_join_file)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

    filter_view_warning = "COUNT TODAY PHRASES"
    today = date.today()

    # BEGIN COUNT LIVE DAY FOR THE TASKS -------------------------------------------------------------------------------
    colet_day_of_a_task = tab_data["COLET_DAY"]
    open_day_of_a_task = tab_data["OPEN_TASK_DAY"]

    delta_difference = colet_day_of_a_task - open_day_of_a_task

    for row in tab_data.iterrows():
        tab_data["OPEN_TASK_MONTH"] = delta_difference
    # END COUNT LIVE DAY FOR THE TASKS ---------------------------------------------------------------------------------

    # FILTER FOR DATE PERIOD START
    date_period = pd.Series(pd.date_range(today, freq="D", periods=1), dtype=np.dtype("O"))  # ITS WORK GOOD!
    tab_data.loc[tab_data['COLET_DAY'].isin(date_period)].to_excel(Place.output_folder + Place.report_005, index=False)

    # READ AGAIN TO COUNT
    today_tasks = pd.read_excel(Place.output_folder + Place.report_005)

    print("STATUS FILTER: ", filter_view_warning, " ... OK! >>", Place.report_005)
    print(
        "--------------------------------------------------------------------------- CHECK_STATUS COUNT TODAY -------")
    print(today_tasks['CHECK_STATUS'].value_counts())


# HERE I AM JUST DISPLAY ON CMD PROMPT VIEW SOME USEFUL INFORMATION... ALL PERIOD
def count_all_day_phrases_status():
    tab_data = pd.read_excel(Place.output_folder + Place.work_join_file)  # ...ALL PERIOD

    print(
        "--------------------------------------------------------------------------- LOCAL_UF COUNT ALL DAYS --------")
    print(tab_data['LOCAL_UF'].value_counts())
    print(
        "--------------------------------------------------------------------------- CHECK_STATUS COUNT ALL DAYS ----")
    print(tab_data['CHECK_STATUS'].value_counts())


# HERE I AM ADD A DAY COUNT TO A COLUMN ON OUTPUT EXCEL FILE..
def count_live_day_task():
    tab_data = pd.read_excel(Place.output_folder + Place.work_join_file)
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

    colet_day_of_a_task = tab_data["COLET_DAY"]
    open_day_of_a_task = tab_data["OPEN_TASK_DAY"]

    delta_difference = colet_day_of_a_task - open_day_of_a_task

    for row in tab_data.iterrows():
        tab_data["OPEN_TASK_MONTH"] = delta_difference

    tab_data.to_excel(Place.output_folder + Place.report_006, index=False)
