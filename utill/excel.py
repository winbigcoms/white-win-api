def compare_selected_rows_columns(df1, df2, start_row, end_row, columns_to_compare):
    # 선택한 행과 열만 추출
    df1_subset = df1.iloc[start_row:end_row, :][columns_to_compare]
    df2_subset = df2.iloc[start_row:end_row, :][columns_to_compare]

    # 두 데이터프레임 비교
    diff_df = df1_subset.compare(df2_subset)

    # 차이가 있는 경우 JSON 형태로 반환
    if not diff_df.empty:
        return diff_df.to_json(orient='split')
    else:
        return {"message": "선택한 행과 열에서의 두 시트는 동일합니다."}
    
