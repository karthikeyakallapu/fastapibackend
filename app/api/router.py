from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.schema.user import UserCreate, UserBase
from app.models.user import User


router = APIRouter()

@router.post("/user/create", response_model=UserBase ,status_code=201)
async def create_user(user:UserCreate , db: AsyncSession = Depends(get_db)):
    new_user = User(email= user.email, password= user.password,  username= user.username )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user


