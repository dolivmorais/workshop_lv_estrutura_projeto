import pandas as pd
import pytest
from app.pipeline.transforme import concat_data_frames

df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
df2 = pd.DataFrame({"a": [7, 8, 9], "b": [10, 11, 12]})
df_empty = pd.DataFrame()
df_diff_cols = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})  # Colunas diferentes


def test_concatenacao_lista_dataframes():
    """Testa se concat_data_frames retorna um DataFrame válido."""
    data_frame_list = [df1, df2]
    result = concat_data_frames(data_frame_list)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == len(df1) + len(df2)  # Verifica se o tamanho está correto
    pd.testing.assert_frame_equal(result, pd.concat(data_frame_list, ignore_index=True))


def test_concatenacao_com_dataframe_vazio():
    """Verifica se a função lida corretamente com DataFrame vazio."""
    data_frame_list = [df1, df_empty]
    result = concat_data_frames(data_frame_list)
    
    assert isinstance(result, pd.DataFrame)
    assert len(result) == len(df1)  # O resultado deve ter o mesmo número de linhas que df1
    pd.testing.assert_frame_equal(result, df1)  # O resultado deve ser igual a df1


def test_concatenacao_com_colunas_diferentes():
    """Testa comportamento ao concatenar DataFrames com colunas diferentes."""
    data_frame_list = [df1, df_diff_cols]
    result = concat_data_frames(data_frame_list)
    
    assert isinstance(result, pd.DataFrame)
    assert set(result.columns) == {"a", "b", "x", "y"}  # Deve conter todas as colunas
    assert result.isna().sum().sum() > 0  # Deve haver valores NaN devido às colunas diferentes

    

