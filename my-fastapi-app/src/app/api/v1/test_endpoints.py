from fastapi import APIRouter

router = APIRouter()

@router.get("/test1")
async def test_endpoint_1():
    return {"message": "This is test endpoint 1"}

@router.get("/test2")
async def test_endpoint_2():
    return {"message": "This is test endpoint 2"}

@router.get("/test3")
async def test_endpoint_3():
    return {"message": "This is test endpoint 3"}

@router.get("/test4")
async def test_endpoint_4():
    return {"message": "This is test endpoint 4"}

@router.get("/test5")
async def test_endpoint_5():
    return {"message": "This is test endpoint 5"}