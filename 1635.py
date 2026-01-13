import pandas as pd
import numpy as np

def hopper_company_queries(drivers: pd.DataFrame, rides: pd.DataFrame, accepted_rides: pd.DataFrame) -> pd.DataFrame:
    # 1. Create a DataFrame for all 12 months of 2020
    months = pd.DataFrame({'month': range(1, 13)})
    
    # 2. Calculate Active Drivers
    # Count drivers joined before 2020 (Initial Baseline)
    initial_drivers = drivers[drivers['join_date'] < '2020-01-01'].shape[0]
    
    # Count drivers joining in 2020 by month
    drivers_2020 = drivers[
        (drivers['join_date'] >= '2020-01-01') & 
        (drivers['join_date'] <= '2020-12-31')
    ].copy()
    drivers_2020['month'] = drivers_2020['join_date'].dt.month
    new_drivers = drivers_2020.groupby('month').size().reset_index(name='new_cnt')
    
    # Merge and calculate cumulative sum
    df_res = months.merge(new_drivers, on='month', how='left').fillna(0)
    df_res['active_drivers'] = df_res['new_cnt'].cumsum() + initial_drivers
    
    # 3. Calculate Accepted Rides
    # Filter 2020 rides
    rides_2020 = rides[
        (rides['requested_at'] >= '2020-01-01') & 
        (rides['requested_at'] <= '2020-12-31')
    ].copy()
    
    # Filter for only accepted rides
    accepted_ids = set(accepted_rides['ride_id'])
    rides_2020 = rides_2020[rides_2020['ride_id'].isin(accepted_ids)]
    
    # Group by month
    rides_2020['month'] = rides_2020['requested_at'].dt.month
    monthly_accepted = rides_2020.groupby('month').size().reset_index(name='accepted_rides')
    
    # 4. Final Merge
    df_final = df_res.merge(monthly_accepted, on='month', how='left').fillna(0)
    
    # 5. Formatting
    return df_final[['month', 'active_drivers', 'accepted_rides']].astype(int)