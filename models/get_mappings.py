from db import SessionLocal, engine, Base, IThubAcademicRecord, IThubDiscipline, IThubStudyGroup, DisciplineMapping, Discipline, AcademicRecord

def get_mappings():
    db: Session = SessionLocal()
    full_table = (
        db.query(
            IThubDiscipline.name_dis,
            IThubDiscipline.code_dis,
            Discipline.name,
            Discipline.id_dis
        )
        .select_from(IThubAcademicRecord)
        .join(IThubStudyGroup, IThubStudyGroup.unique_identifier == IThubAcademicRecord.student)
        .join(IThubDiscipline, IThubAcademicRecord.id_dis == IThubDiscipline.id_dis)
        .join(DisciplineMapping, IThubDiscipline.id_dis == DisciplineMapping.ithub_dis_id)
        .join(Discipline, DisciplineMapping.vvsu_dis_id == Discipline.id_dis)
        .limit(1000)
        )

    mappings = [
    {
    "ithub_name": row[0],
    "code_dis": row[1],
    "vvsu_name": row[2],
    "vvsu_id": row[3],
    }
    for row in full_table]

    return mappings