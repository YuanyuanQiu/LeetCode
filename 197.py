import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # 1. 构造连接键
    weather['expected_prev_date'] = weather['recordDate'] - pd.Timedelta(days=1)
    
    # 2. 执行 Self-Join (Merge)
    # left: 今天的数据 (使用 expected_prev_date 去寻找昨天)
    # right: 昨天的数据 (使用 recordDate 等待被寻找)
    merged = pd.merge(
        weather, 
        weather, 
        left_on='expected_prev_date', 
        right_on='recordDate', 
        suffixes=('', '_prev') # 加上后缀区分列名
    )
    
    # 3. 筛选温度升高的行
    # temperature: 今天的温度
    # temperature_prev: 昨天的温度
    result = merged[merged['temperature'] > merged['temperature_prev']]
    
    # 5. 返回结果
    return result[['id']]