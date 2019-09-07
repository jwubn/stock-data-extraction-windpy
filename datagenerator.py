# from WindPy import w
import pandas as pd
import numpy as np

# w.start()


mkt = pd.read_csv('mkt.csv')
mkt = mkt.iloc[-4:-1,1:]
# print(mkt)
pb = pd.read_csv('pb_raw.csv').T
roe = pd.read_csv('roe_raw.csv').T
ag = pd.read_csv('assetsgrowth_raw.csv').T
rf = pd.read_csv('rf_week.csv', header = None)

# header process
header = pb.iloc[0,:]
pb.drop(pb.index[0], inplace = True)
roe.drop(roe.index[0], inplace = True)
ag.drop(ag.index[0], inplace = True)
pb.columns, roe.columns, ag.columns = [header]*3

# 2016-2018
mkt = mkt.T
mkt.columns = ['2016','2017','2018']
pb = pb.iloc[-4:-1,:].T
roe = roe.iloc[-4:-1,:].T
ag = ag.iloc[-4:-1,:].T
print(ag)
mkt.to_csv('mktinfo.csv')
pb.to_csv('pbinfo.csv')
roe.to_csv('roeinfo.csv')
ag.to_csv('aginfo.csv')
# rf
rf = rf/100

stock_list = list(header)

start_date = list(np.arange(20160101, 20190101, 10000))
start_date = [str(i) for i in start_date]
end_date = list(np.arange(20170131, 20190131, 10000))
end_date.append(20181101)
end_date = [str(i) for i in end_date]

# top/bottom market value portfolios
mkt = mkt.T
p_mkt_top = pd.DataFrame()
p_mkt_bottom = pd.DataFrame()
mv_num = 100
for i in range(0,mkt.shape[1]):
    mkt_temp = mkt.iloc[:,i]
    mkt_temp = mkt_temp[~ (mkt_temp == 0.0)]
    mkt_temp = mkt_temp.sort_values(ascending = False)
    p_mkt_top[i] = mkt_temp.head(mv_num).index
    p_mkt_bottom[i] = mkt_temp.tail(mv_num).index

# top/bottom pb porfolios
pb = pb.T
p_pb_top = pd.DataFrame()
p_pb_bottom = pd.DataFrame()
pb_num = 100
for i in range(0,pb.shape[1]):
    pb_temp = pb.iloc[:,i]
    pb_temp = pb_temp[~ (pb_temp == 0.0)]
    pb_temp = pb_temp.sort_values(ascending = False)
    p_pb_top[i] = pb_temp.head(pb_num).index
    p_pb_bottom[i] = pb_temp.tail(pb_num).index

# top/bottom roe porfolios
roe = roe.T
p_roe_top = pd.DataFrame()
p_roe_bottom = pd.DataFrame()
roe_num = 100
for i in range(0,roe.shape[1]):
    roe_temp = roe.iloc[:,i]
    roe_temp = roe_temp[~(roe_temp == 0.0)]
    roe_temp = roe_temp.sort_values(ascending = False)
    p_roe_top[i] = roe_temp.head(roe_num).index
    p_roe_bottom[i] = roe_temp.tail(roe_num).index

# top/bottom asset growth porfolios
ag = ag.T
p_ag_top = pd.DataFrame()
p_ag_bottom = pd.DataFrame()
ag_num = 100
for i in range(0,ag.shape[1]):
    ag_temp = ag.iloc[:,i]
    ag_temp = ag_temp[~(ag_temp == 0.0)]
    ag_temp = ag_temp[~(ag_temp == '#DIV/0!')]
    ag_temp = pd.Series(ag_temp, dtype = 'float')
    ag_temp = ag_temp.sort_values(ascending = False)
    p_ag_top[i] = ag_temp.head(ag_num).index
    p_ag_bottom[i] = ag_temp.tail(ag_num).index

# p_mkt_top.columns = ['2016','2017','2018']
    #p_mkt_bottom.columns, p_pb_top.columns, p_pb_bottom.columns = ['2016','2017','2018'] * 4
#p_ag_top.columns, p_ag_bottom.columns, p_roe_top.columns, p_roe_bottom.columns = ['2016','2017','2018'] * 4
# p_mkt_top.to_csv('mkttop.csv')
# p_mkt_bottom.columns = ['2016','2017','2018']
# p_mkt_bottom.to_csv('mktbottom.csv')
# p_pb_top.columns = ['2016','2017','2018']
# p_pb_top.to_csv('pbtop.csv')
# p_pb_bottom.columns = ['2016','2017','2018']
# p_pb_bottom.to_csv('pbbottom.csv')
# p_ag_top.columns = ['2016','2017','2018']
# p_ag_top.to_csv('agtop.csv')
# p_ag_bottom.columns = ['2016','2017','2018']
# p_ag_bottom.to_csv('agbottom.csv')
# p_roe_top.columns = ['2016','2017','2018']
# p_roe_top.to_csv('roetop.csv')
# p_roe_bottom.columns = ['2016','2017','2018']
# p_roe_bottom.to_csv('roebottom.csv')
# Rm
# data_rm = w.wsd('SPX.GI', "close", start_date[0], end_date[-1], Period = 'W')
# df_rm = pd.DataFrame(data_rm.Data).T
# rm = df_rm.pct_change()
# rm = rm.iloc[1:,:]
# fillnan = rm.iloc[-1,:]
# rm = pd.concat([rm, fillnan], axis = 0)
# rm.reset_index(inplace = True, drop = True)
# rf.reset_index(inplace = True, drop = True)

# rm_rf = rm - rf
# rm_rf = rm_rf.iloc[:-1,0]
# # Extract data from Wind and process data
# def ExtractData(datalist, startdate, enddate):
#     raw_data = w.wsd(list(datalist), 'close', startdate, enddate, Period = 'W')
#     df_data = pd.DataFrame(raw_data.Data).T
#     df = df_data.pct_change()
#     df = df.iloc[1:]
#     return df
#
# rm, smb, hml, rmw, cma = [pd.Series() ] * 5
# for i in range(0,len(start_date)):
#     rm_temp =  ExtractData('SPX.GI', start_date[i], end_date[i])
#     df_smb_b_temp = ExtractData(p_mkt_top.iloc[:,i], start_date[i], end_date[i])
#     df_smb_s_temp = ExtractData(p_mkt_bottom.iloc[:,i], start_date[i], end_date[i])
#     df_hml_l_temp = ExtractData(p_pb_top.iloc[:,i], start_date[i], end_date[i])
#     df_hml_h_temp = ExtractData(p_pb_bottom.iloc[:, i], start_date[i], end_date[i])
#     df_rmw_r_temp = ExtractData(p_roe_top.iloc[:, i], start_date[i], end_date[i])
#     df_rmw_w_temp = ExtractData(p_roe_bottom.iloc[:, i], start_date[i], end_date[i])
#     df_cma_c_temp = ExtractData(p_ag_bottom.iloc[:, i], start_date[i], end_date[i])
#     df_cma_a_temp = ExtractData(p_ag_top.iloc[:, i], start_date[i], end_date[i])
#     smb_temp = df_smb_s_temp.mean(1) - df_smb_b_temp.mean(1)
#     hml_temp = df_hml_h_temp.mean(1) - df_hml_l_temp.mean(1)
#     rmw_temp = df_rmw_r_temp.mean(1) - df_rmw_w_temp.mean(1)
#     cma_temp = df_cma_c_temp.mean(1) - df_cma_a_temp.mean(1)
#     rm = pd.concat([rm,rm_temp], axis = 0)
#     smb = pd.concat([smb, smb_temp], axis = 0)
#     hml = pd.concat([hml, hml_temp], axis = 0)
#     rmw = pd.concat([rmw, rmw_temp], axis = 0)
#     cma = pd.concat([cma, cma_temp], axis = 0)
#
# rm.reset_index(inplace = True, drop = True)
# smb.reset_index(inplace = True, drop = True)
# hml.reset_index(inplace = True, drop = True)
# rmw.reset_index(inplace = True, drop = True)
# cma.reset_index(inplace = True, drop = True)
# # all_data = pd.DataFrame({'Rm': df_rm, 'SMB': smb, 'HML': hml, 'RMW': rmw, 'CMA': cma})
# rm_rf = rm - rf
# all_data = pd.concat([rm_rf,smb,hml,rmw,cma], axis = 1)
# all_data.columns = ['Rm_Rf','SMB','HML','RMW','CMA']
# print(all_data)
# all_data.to_csv('alldata.csv')



