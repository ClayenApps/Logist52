from fastapi import APIRouter, Depends

from app.repository.offer import OfferRepository
from app.schemas.filters import OfferFilter
from app.schemas.supply import OfferOutDTO

router = APIRouter(prefix="/offers")

_offer_repository = OfferRepository()


@router.get('', response_model=list[OfferOutDTO])
async def get_all_offers(filter_data: OfferFilter = Depends(OfferFilter)):
    return await _offer_repository.get_all(filter_data)

