from db import SessionLocal, engine, Base, IThubAcademicRecord, IThubDiscipline, IThubStudyGroup, DisciplineMapping, Discipline, AcademicRecord

def get_students_by_group(group_name):
    db = SessionLocal()
    try:
        q = (
            db.query(
                IThubStudyGroup.stud_full_name,
                IThubDiscipline.name_dis,
                IThubAcademicRecord.points,
                Discipline.name,
                AcademicRecord.grade_score
            )
            .join(IThubAcademicRecord, IThubStudyGroup.unique_identifier == IThubAcademicRecord.student)
            .join(IThubDiscipline, IThubAcademicRecord.id_dis == IThubDiscipline.id_dis)
            .join(DisciplineMapping, IThubDiscipline.id_dis == DisciplineMapping.ithub_dis_id)
            .join(Discipline, DisciplineMapping.vvsu_dis_id == Discipline.id_dis)
            .join(AcademicRecord, AcademicRecord.id_dis == Discipline.id_dis)
            .filter(IThubStudyGroup.group_name == group_name)
        )
        rows = q.distinct().all()
        marks = [
            {"stud_full_name": r[0], "name_dis": r[1], "points": r[2], "name": r[3], "grade_score": r[4]}
            for r in rows
        ]
        return marks
    finally:
        db.close()

def get_unique_subjects(group_name):
    db = SessionLocal()
    try:
        q = (db.query(
            IThubDiscipline.name_dis
            ).join(IThubAcademicRecord, IThubAcademicRecord.id_dis == IThubDiscipline.id_dis)
            .join(IThubStudyGroup, IThubStudyGroup.unique_identifier == IThubAcademicRecord.student)
            .filter(IThubStudyGroup.group_name == group_name)
            )
        rows_unique = q.distinct().all()
        return rows_unique
    finally:
        db.close()