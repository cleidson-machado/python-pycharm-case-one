import pandas as pd
from Util import PlaceStorageStrings as Path
import numpy as np

red_phrases_list = ['NO UPDATING YET FROM THE BRANCH TEAM, WE ASKED TO SCHEDULE THE SERVICE.',
                    'AWAITING DELIVERY, ASK TO SCHEDULE THE SERVICE.',
                    'THE CUSTOMER HAVE NOT YET RESPONDED TO CONTACT ATTEMPTS.',
                    'THE BRANCH TEAM REPORT WE ARE WAITING THE CUSTOMER SERVICE WINDOW.',
                    'WE ARE WAITING THE CUSTOMER SERVICE WINDOW.',
                    'WE ARE NOT YET SUCCESSFUL IN CONTACTING THE CUSTOMER.',
                    'WE ARE NOT YET SUCCESSFUL IN CONTACTING THE CUSTOMER AND WAITING FOR ETA OF THE PARTS.']


def filter_task_red_phrases():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    filter_view_warning = "FILTER RED PHRASES"
    # FILTER START
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    tab_data.loc[tab_data['CHECK_STATUS'].isin(red_phrases_list)].to_excel(Path.output_folder + Path.report_002,
                                                                           index=False)
    print("STATUS FILTER: ", filter_view_warning, " ... OK!")


def filter_task_no_red_phrases():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    filter_view_warning = "FILTER NO RED PHRASES"
    # FILTER START
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    tab_data.loc[~tab_data['CHECK_STATUS'].isin(red_phrases_list)].to_excel(Path.output_folder + Path.report_005,
                                                                            index=False)
    print("STATUS FILTER: ", filter_view_warning, " ... OK!")


def filter_task_scheduled_phrases():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    filter_view_warning = "FILTER SCHEDULED FOR..."
    filter_words = "SCHEDULED FOR"
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

    # HERE ADD TAG COLOR BLUE...
    for row in tab_data.iterrows():
        tab_data.loc[tab_data["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "BLUE"

    tab_data.loc[tab_data['CHECK_STATUS'].str.contains(filter_words)].to_excel(Path.output_folder + Path.report_006,
                                                                               index=False)
    print("STATUS FILTER: ", filter_view_warning, " ... OK!")


def filter_task_color_red():
    tab_data = pd.read_excel(Path.output_folder + Path.report_002)
    filter_view_warning = "FILTER RED COLOR FLAG NAME"

    # FILTER START
    # the_email_filter = tab_data_email_act[~tab_data_email_act["EMAIL_ACT"].isin(['RED'])]

    # HERE ADD TAG COLOR RED...
    for row in tab_data.iterrows():
        tab_data.loc[tab_data["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "RED"

    tab_data.to_excel(Path.output_folder + Path.report_003, index=False)
    print("STATUS FILTER: ", filter_view_warning, " ... OK!")


def filter_task_date_period():
    tab_data = pd.read_excel(Path.output_folder + Path.report_003)
    date_period = pd.Series(pd.date_range("2021-09-01", freq="D", periods=7), dtype=np.dtype("O"))  # ITS WORK GOOD!
    tab_data.loc[tab_data['COLET_DAY'].isin(date_period)].to_excel(Path.output_folder + Path.report_004, index=False)
    return print("FILTER DATE OK...")
