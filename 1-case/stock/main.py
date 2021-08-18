import akshare as ak
import pandas as pd

# 获取股票数据
stock_zh_a_spot_df = ak.stock_zh_a_spot()
print(stock_zh_a_spot_df)

# 保存到excel
#stock_zh_a_spot_df.to_excel("data.xlsx")
