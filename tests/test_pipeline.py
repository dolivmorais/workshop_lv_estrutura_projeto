import pandas as pd
from app.pipeline.transforme import concat_data_frames

df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df2 = pd.DataFrame({"a": [1, 2, 2], "b": [4, 5, 6]})

#  rodar o comendo no terminal: pytest -v 

def test_concatenacao_lista_dataframes():
    """
    criar função para testar concat_data_frames
    """
    data_frame_list = [df1, df2]
    result = concat_data_frames(data_frame_list)
    assert isinstance(result, pd.DataFrame)


