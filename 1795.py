import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # 1. Melt: Wide -> Long
    df = products.melt(
        id_vars=['product_id'], 
        var_name='store', 
        value_name='price'
    )
    
    # 2. Drop NULLs (题目要求)
    return df.dropna(subset=['price'])