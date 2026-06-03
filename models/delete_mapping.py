from db import SessionLocal, IThubDiscipline, DisciplineMapping

def delete_mapping_by_code(code_dis: str, vvsu_id_dis: int) -> None:
    db = SessionLocal()
    try:
        ithub_row = db.query(IThubDiscipline).filter_by(code_dis=code_dis).first()
        if not ithub_row:
            raise ValueError(f"Нет дисиплины колледжа с кодом {code_dis!r}")

        mapping = (
            db.query(DisciplineMapping)
              .filter_by(ithub_dis_id=ithub_row.id_dis, vvsu_dis_id=vvsu_id_dis)
              .first()
        )
        if not mapping:
            raise ValueError("Соответствие не найдено")

        db.delete(mapping)
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()