from pipeline.extract import estract_from_excel
from pipeline.transforme import concat_data_frames
from pipeline.load import load_excel
import os

if __name__ == "__main__":
    data_frame_list = estract_from_excel("data/input")
    dataframe = concat_data_frames(data_frame_list)
    load_excel(dataframe, "data/output", "output.xlsx")