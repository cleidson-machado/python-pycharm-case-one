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


def company_colet_day_report_maker():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    # EMAIL_ACT
    print("--------------------------------------------------------- REPORT THREE ----")
    phrases = ['NO UPDATING YET FROM THE BRANCH TEAM, WE ASKED TO SCHEDULE THE SERVICE.']
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    tab_data.loc[tab_data['CHECK_STATUS'].isin(phrases)].to_excel(Path.output_folder + Path.report_002, index=False)
    return print(tab_data['CHECK_STATUS'].value_counts())


def company_filter_report_maker_1():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    # FILTER START
    print("--------------------------------------------------------- REPORT FOUR FILTER ----")
    # phrases = ['NO UPDATING YET FROM THE BRANCH TEAM, WE ASKED TO SCHEDULE THE SERVICE.',
    #            'THE CUSTOMER HAVE NOT YET RESPONDED TO CONTACT ATTEMPTS.']
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    tab_data.loc[tab_data['CHECK_STATUS'].isin(red_phrases_list)].to_excel(Path.output_folder + Path.report_002,
                                                                           index=False)

    # tab_data_email_act = pd.read_excel(Path.output_folder + Path.report_002)
    # the_email_filter = tab_data_email_act[~tab_data_email_act["EMAIL_ACT"].isin(['RED'])]
    #
    # for row in the_email_filter.iterrows():
    #     tab_data_email_act.loc[tab_data_email_act["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "RED"
    #
    # tab_data_email_act.to_excel(Path.output_folder + Path.report_003, index=False)
    return print("FILTER OK...")


def company_filter_color_red():
    tab_data_email_act = pd.read_excel(Path.output_folder + Path.report_002)
    the_email_filter = tab_data_email_act[~tab_data_email_act["EMAIL_ACT"].isin(['RED'])]

    for row in the_email_filter.iterrows():
        tab_data_email_act.loc[tab_data_email_act["EMAIL_ACT"] == 43200131, "EMAIL_ACT"] = "RED"

    tab_data_email_act.to_excel(Path.output_folder + Path.report_003, index=False)


def company_filter_report_maker_2():
    tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)
    # date_period = ['20210906'] # ITS WORK GOOD JUST A ONE DAY!
    # date_period = ['20210902', '20210903', '20210906']  # ITS WORK GOOD!
    date_period = pd.Series(pd.date_range("2021-09-01", freq="D", periods=7), dtype=np.dtype("O"))  # ITS WORK GOOD!
    tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
    tab_data.loc[tab_data['COLET_DAY'].isin(date_period)].to_excel(Path.output_folder + Path.report_002, index=False)
    return print("FILTER DATE OK...")
