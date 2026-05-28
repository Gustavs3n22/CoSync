from db import SessionLocal, IThubStudyGroup

def get_groups():
    db: Session = SessionLocal()
    full_table = db.query(IThubStudyGroup.group_name)
    groups_table = full_table.distinct()
    return groups_table