from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from cv_data.db_base_model import TableBaseModel
from sqlalchemy import create_engine
from po_tools.win_config import json_config, read_json, json_sql_path

conn = json_config["grid"]["conn"]
da_engine = create_engine(conn, echo=False)
da_sql_texts = {}
for item in read_json(json_sql_path)["sqls"]:
    da_sql_texts[item["id"]] = " ".join(item["sql"])


def deprecated_time() -> datetime:
    return datetime.now() - timedelta(days=10)


class CvDatabaseAccess:
    @staticmethod
    def insert(entity: TableBaseModel):
        with Session(da_engine, expire_on_commit=False) as session:
            entity.created = datetime.now()
            session.add(entity)
            session.commit()
    # def update_hook_entity(entity: FrameHookEntity):
    #     with Session(da_engine) as session:
    #         session.add(entity)
    #         entity.updated = datetime.datetime.now()
    #         session.commit()
    #
    # @staticmethod
    # def load_hook_entity(_id) -> FrameHookEntity:
    #     with Session(da_engine) as session:
    #         return session.query(FrameHookEntity).filter_by(id=_id).first()
