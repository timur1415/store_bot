from fastapi import APIRouter, Request, Response, status
from fastapi.responses import JSONResponse
from telegram import Update
from telegram.ext import Application
from fastapi.responses import FileResponse
from config.logger import logger
from pydantic import BaseModel 
import uuid 
from config.config import CP_PUBLIC_ID

router = APIRouter()

@router.post('/order')
async def create_order(request: Request):
    invoice_id = uuid.uuid4()
    return JSONResponse({'publicId': CP_PUBLIC_ID, 'invoiceId': str(invoice_id)})