from fastapi import UploadFile 
import pandas as pd
import subprocess

async def find_different_values(file1:UploadFile, file2:UploadFile ):
    file1_path = f"uploaded_files/{file1.filename}"
    file2_path = f"uploaded_files/{file2.filename}"

    with open(file1_path, "wb") as file_object:
        file_object.write(file1.file.read())

    with open(file2_path, "wb") as file_object:
        file_object.write(file2.file.read())

    # 엑셀 파일 읽기
    df1 = pd.read_excel(file1_path, header=None, engine="openpyxl")
    df2 = pd.read_excel(file2_path, header=None, engine="openpyxl")
    
    # 이름을 기준으로 두 데이터프레임을 병합
    merged_df = pd.merge(df1, df2, left_on=0, right_on=0,suffixes=('_left','_right'))
    
    different_values_df = merged_df[merged_df['1_left'] != merged_df['1_right']]
    subprocess.run(["rm",file1_path])
    subprocess.run(["rm",file2_path])

    return different_values_df