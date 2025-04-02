from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.wilson_models import WilsonModel
from schemas.wilson_schema import WilsonSchema
from core.deps import get_session

router = APIRouter()
 
# Post
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=WilsonSchema)
async def post_wilson(wilson: WilsonSchema, db: AsyncSession = Depends(get_session)):
    novo_wilson = WilsonModel(nome=wilson.nome, 
                              especialidade= wilson.especialidade, 
                              foto = wilson.foto, 
                              poder = wilson.poder)
    db.add(novo_wilson)
    
    await db.commit()
    
    return novo_wilson

@router.get("/", response_model=List[WilsonSchema])
async def get_wilsons(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(WilsonModel)
        result = await session.execute(query)
        wilsons: List[WilsonModel] = result.scalars().all()
        
    return wilsons


@router.get("/{wilson_id}", response_model=WilsonSchema)
async def get_wilson(wilson_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(WilsonModel).filter(WilsonModel.id == wilson_id)
        result = await session.execute(query)
        wilson = result.scalar_one_or_none()
        
        if wilson:
            return wilson
        else:
            raise HTTPException(detail="Wilson não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        

@router.put("/{wilson_id}", response_model=WilsonSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_wilson(wilson_id: int, wilson: WilsonSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(WilsonModel).filter(WilsonModel.id == wilson_id)
        result = await session.execute(query)
        wilson_up = result.scalar_one_or_none()
        
    if wilson_up:
        wilson_up.nome = wilson.nome
        wilson_up.especialidade = wilson.especialidade
        wilson_up.foto = wilson.foto
        wilson_up.poder = wilson.poder
        
        await session.commit()
        return wilson_up
    
    else:
            raise HTTPException(detail="Wilson não encontrado", status_code=status.HTTP_404_NOT_FOUND)
        
@router.delete("/{wilson_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_wilson(wilson_id: int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(WilsonModel).filter(WilsonModel.id == wilson_id)
        result = await session.execute(query)
        wilson_del = result.scalar_one_or_none()
        
        if wilson_del:
            await session.delete(wilson_del)
            await session.commit()
            return Response(status_code=status.HTPP_204_NO_CONTENT)
        