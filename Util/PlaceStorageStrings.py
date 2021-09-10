basic_join_file = "all_data_join_file.xlsx"
work_join_file = "all_data_work_file.xlsx"

report_001 = "company_colet_day.xlsx"
report_002 = "01_filter_report_RED_flag.xlsx"
report_003 = "02_filter_report_BLUE_flag.xlsx"
report_004 = "03_filter_report_YELLOW_flag.xlsx"
report_005 = "04_filter_report_TODAY_TASKS.xlsx"
report_006 = "filter_report_file_6.xlsx"  # NO USED YET!

input_folder = ".//Demand_Files//"
output_folder = ".//WorkExcelOutPutFiles//"

output_columns = ['SRMS', 'COLET_DAY', 'EMAIL_ACT', 'OPEN_TASK_DAY', 'TASK_NUM', 'COMPANY', 'LOCAL_UF', 'SYS_STATUS',
                 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY', 'CHECK_STATUS', 'OPEN_TASK_MONTH']

filter_words = "SCHEDULED FOR"

red_phrases_list = ['NO UPDATING YET FROM THE BRANCH TEAM, WE ASKED TO SCHEDULE THE SERVICE.',
                    'AWAITING DELIVERY, ASK TO SCHEDULE THE SERVICE.',
                    'THE CUSTOMER HAVE NOT YET RESPONDED TO CONTACT ATTEMPTS.',
                    'THE BRANCH TEAM REPORT WE ARE WAITING THE CUSTOMER SERVICE WINDOW.',
                    'WE ARE WAITING THE CUSTOMER SERVICE WINDOW.',
                    'WE ARE NOT YET SUCCESSFUL IN CONTACTING THE CUSTOMER.',
                    'WE ARE NOT YET SUCCESSFUL IN CONTACTING THE CUSTOMER AND WAITING FOR ETA OF THE PARTS.']