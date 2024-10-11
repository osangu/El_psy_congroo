from typing import List

from fastapi import Depends, APIRouter, UploadFile

from app.core.service.album import AlbumService

from ..swagger import SwaggerDetails
from .request import AlbumDistributeRequest

album_router = APIRouter(prefix="/albums")


@album_router.post(
    **SwaggerDetails.publish_album,
)
async def upload_album(
        track_files: List[UploadFile],
        requests: AlbumDistributeRequest,
        user_id: int = Depends(),
        service=Depends(AlbumService.publish)
):
    await service()
