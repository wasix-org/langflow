from uuid import UUID

from sqlmodel import select
from sqlalchemy.orm import Session

from langflow.services.database.models.file.model import File


async def get_file_by_id(db: Session, file_id: UUID) -> File | None:
    if isinstance(file_id, str):
        file_id = UUID(file_id)
    stmt = select(File).where(File.id == file_id)

    return (db.exec(stmt)).first()
