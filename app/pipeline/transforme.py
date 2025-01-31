import pandas as pd
from typing import List

"""
escrever um função que recebe um lista de dataframes e retorna um dataframe com os dados transformados
"""
def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list)
