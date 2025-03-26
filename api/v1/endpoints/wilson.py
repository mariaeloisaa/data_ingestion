from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.wilson_models import WilsonModel
from schemas.wilson_scema import WilsonSchema
from core.deps import get_session

router = APIRouter()
