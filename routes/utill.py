from fastapi import APIRouter, File, UploadFile, HTTPException

from utill.excel import find_different_values

router = APIRouter(prefix="/utill", tags=["utill"])

@router.post('/compare')
async def compareExcels(
  file1: UploadFile = File(...), 
  file2: UploadFile = File(...), 
): 
    try:
        # 비교 함수 호출
        result = await find_different_values(file1, file2)
        
        # JSON 응답 반환
        return {"message": "Different values found successfully", "different_values_data": result.to_dict(orient='records')}

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))