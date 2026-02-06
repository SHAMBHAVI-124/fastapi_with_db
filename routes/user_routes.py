from fastapi import APIRouter

router=APIRouter()

@router.post("/signup")
def signup():
    return {"message":"user signed up successfully"}

@router.post("/login")
def login():
    return {"message":"user logged in successfully"}