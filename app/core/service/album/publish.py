from uuid import uuid4
from asyncio import create_task


class PublishAlbum:

    def __init__(
            self,
            user_dao,
            album_dao,
            file_downloader
    ):
        self.user_dao = user_dao
        self.album_dao = album_dao
        self.file_downloader = file_downloader

    async def __call__(self, dto):
        file_names = [uuid4() for _ in range(dto.tracks)]

        await create_task(self.file_downloader(dto.tracks, file_names))
        await create_task(self.album_dao.save())
