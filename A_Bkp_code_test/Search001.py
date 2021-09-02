import pandas as pd
from Util import PlaceStorageStrings as Path

tab_data = pd.read_excel(Path.output_folder + Path.work_join_file)

# HERE JUST SHORT BY TWO COLUMNS
tab_data.sort_values(["COMPANY", "COLET_DAY"], ascending=True)

# tab_data.groupby(['COLET_DAY']

# DROP UNNECESSARY COLUMN TO SEND REPORT TO EMC.. working good!!!
# tab_data.drop(['LOCAL_UF', 'SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)
tab_data.drop(['SYS_STATUS', 'SLA', 'PRIORITY', 'PRODUCT_CODE', 'SYS_SCHEDULE', 'COUNTRY'], axis=1, inplace=True)

# HERE OUTPUT SAVE TO USE IN EXCEL
tab_data.to_excel(Path.output_folder + Path.report_001, index=False)

# print(tab_data.tail(15))
# print(tab_data['COMPANY'].value_counts())
print(tab_data['LOCAL_UF'].value_counts())

# WAY TO FIND 2 -----------------------------------------------------------
# JUST SHORT BY A COLUMN
# tab_data = pd.read_excel(Path.output_folder + Path.work_join_file, index_col='COMPANY')

# tab_data.to_excel(Path.output_folder + Path.report_by_company, index=False)

# print(tab_data.tail(15))
# -------------------------------------------------------------------------

# WAY TO FIND 1 -----------------------------------------------------------
# company_grp = tab_data.groupby(['COMPANY'])
# print(company_grp.get_group('DELL HES/YABORA INDUSTRIA AERONAUTICA'))

# day_count = tab_data['COLET_DAY'].value_counts()

# print(day_count.sort_values(ascending=True))
# https://www.datacamp.com/community/tutorials/pandas-sort-values?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377086&utm_targetid=aud-299261629574:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=9101969&gclid=Cj0KCQjwsZKJBhC0ARIsAJ96n3XbYEycCyYCFA6vQcKhzPQA7EiMKos787fr5h82Rkslk-nWfidvZhgaAnfIEALw_wcB
# -------------------------------------------------------------------------

# company_grp = tab_data.groupby(['COLET_DAY'])

# print(company_grp.get_group('2021-08-24'))

# company_grp = tab_data.groupby(['COMPANY'])

# print(company_grp.get_group('DELL HES/YABORA INDUSTRIA AERONAUTICA'))

# print(tab_data['COMPANY'].value_counts())

# print(tab_data['COMPANY'].tail(15))

# tab_data['SRMS'] = tab_data.index

# tab_data[tab_data['SRMS'].str.contains("Hello|Britain")]

# print(tab_data['SRMS'].head())

# tab_data.query('col.str.contains("foo")', engine='python')

# tab_data['SRMS'] = pd.DataFrame.filter(like='59735576', axis=0, self=True)

# XXX = tab_data[tab_data.SRMS.str.contains('59735576')]

# tab_data['SRMS'] = tab_data.loc[59735576]

# print(tab_data.head())

# count_find = tab_data.groupby('SRMS').count()

# filter_test = (count_find <= 1).any()

# sub_item = tab_data.loc[:, filter_test]

# print(tab_data.groupby('SRMS').count())

# print(count_find)
