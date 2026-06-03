from db import SessionLocal, IThubDiscipline, DisciplineMapping

def add_mapping_by_code(code_dis: str, vvsu_id_dis: int) -> DisciplineMapping:
    db = SessionLocal()
    try:
        ithub_row = db.query(IThubDiscipline).filter_by(code_dis=code_dis).first()
        if not ithub_row:
            raise ValueError(f"Нет дисиплины колледжа с кодом {code_dis!r}")
        new_mapping = DisciplineMapping(
            ithub_dis_id=ithub_row.id_dis,
            vvsu_dis_id=vvsu_id_dis
        )
        db.add(new_mapping)
        db.commit()
        db.refresh(new_mapping)
        return new_mapping
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()