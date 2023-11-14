from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass
from sqlalchemy.orm import Mapped, mapped_column


class DeclarativeModel(MappedAsDataclass, DeclarativeBase):
    pass


class TableBaseModel(MappedAsDataclass, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True,
                                    autoincrement=True,
                                    default=None)
    created: Mapped[datetime] = mapped_column(default=datetime.now())
    # created_str: str = dataclasses.field(default=None)
    #
    # def sync_str(self):
    #     self.created_str = str(self.created)
