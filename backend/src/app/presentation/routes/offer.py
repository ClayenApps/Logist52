from pathlib import PurePath
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi.responses import FileResponse

from app.repository.offer import OfferRepository
from app.schemas.filters import OfferFilter
from app.schemas.supply import OfferOutDTO
from app.services.import_data import export_offer_xlsx, import_offer_csv

router = APIRouter(prefix="/offers")

_offer_repository = OfferRepository()


@router.get('', response_model=list[OfferOutDTO])
async def get_all_offers(filter_data: OfferFilter = Depends(OfferFilter)):
    return await _offer_repository.get_all(filter_data)

@router.post("/import")
async def import_from_csv(data: UploadFile = File()):
    content = await data.read()
    return await import_offer_csv(content, PurePath(data.filename).suffix) # type: ignore

@router.get("/export")
async def export_to_xlsx(file_name: str = "report.xlsx"):
    return FileResponse(await export_offer_xlsx(file_name))
