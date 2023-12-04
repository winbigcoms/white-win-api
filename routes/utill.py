from fastapi import APIRouter, Body, FastAPI, Form, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import pandas as pd

from utill.excel import compare_selected_rows_columns

router = APIRouter(prefix="/utill/excel", tags=["excel"])

@router.post('/compare')
async def compareExcels(
  file1: UploadFile = File(...), 
  sheet1: str = Form(...),
  file2: UploadFile = File(...), 
  sheet2: str = Form(...),
  start_row: int = Form(1), end_row: int = Form(10), columns_to_compare: list = Form(['열1', '열2', '열3'])
): 
    try:
        # 엑셀 파일에서 데이터 프레임으로 읽기
        df1 = pd.read_excel(file1.file, sheet_name=sheet1)
        df2 = pd.read_excel(file2.file, sheet_name=sheet2)

        # 비교 함수 호출
        result = compare_selected_rows_columns(df1, df2, start_row, end_row, columns_to_compare)

        # JSON 응답 반환
        return JSONResponse(content=result, media_type="application/json")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))