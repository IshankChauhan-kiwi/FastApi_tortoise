from fastapi import status, APIRouter, HTTPException, Depends
from passlib.context import CryptContext
from apps.accounts.models import *
from fastapi.security import OAuth2PasswordRequestForm

from utils.token import create_access_token, create_refresh_token

router = APIRouter()
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/item/create/", status_code=status.HTTP_201_CREATED)
async def create_item(item: item_pydantic):
    item = await Item.create(**item.dict())
    return item


@router.get("/items/", status_code=status.HTTP_200_OK)
async def get_items():
    return await item_pydanticOut.from_queryset(Item.all())


@router.get("/item/{item_id}")
async def get_item(item_id: int):
    return await item_pydanticOut.from_queryset_single(Item.get(id=item_id))


@router.put("/item/{item_id}")
async def update_item(item_id: int, item: item_pydanticUp):
    await Item.filter(id=item_id).update(**item.dict())
    return await item_pydanticOut.from_queryset_single(Item.get(id=item_id))


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register(user: user_pydantic):
    hash_pass = password_context.hash(user.password)
    user = user.dict()
    user.pop('password')
    user.update({"password": hash_pass})
    user = await User.create(**user)
    return user


@router.get("/users/", status_code=status.HTTP_200_OK)
async def get_users():
    return await user_pydanticOut.from_queryset(User.all())


@router.get("/user/{user_id}")
async def get_user(user_id: int):
    return await user_pydanticOut.from_queryset_single(User.get(id=user_id))


@router.post('/login', status_code=status.HTTP_200_OK)
async def user_login(request: OAuth2PasswordRequestForm = Depends()):
    user = await User.filter(user_name=request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Email not found')

    if not password_context.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')

    return {'access_token': create_access_token(user.id), 'refresh_token': create_refresh_token(user.id),
            'token_type': 'bearer'}
