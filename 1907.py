# Option 1
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    # Calculate counts using vectorization
    low = (accounts['income'] < 20000).sum()
    high = (accounts['income'] > 50000).sum()
    # Total rows - low - high = average (since ranges are mutually exclusive)
    average = len(accounts) - low - high
    
    # Construct the result DataFrame manually
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [low, average, high]
    })

# Option 2
import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'category': ['Low Salary', 'Average Salary', 'High Salary'],
        'accounts_count': [
            accounts[accounts.income < 20000].shape[0],
            accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
            accounts[accounts.income > 50000].shape[0],
        ],
    })