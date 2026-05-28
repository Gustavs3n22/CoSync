from db import SessionLocal, engine, Base, IThubAcademicRecord, IThubDiscipline, IThubStudyGroup, DisciplineMapping, Discipline, AcademicRecord

def get_students_by_group(group_name):
    db: Session = SessionLocal()
    full_table = (
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
        .filter(IThubStudyGroup.group_name == group_name))
    marks_table = full_table.distinct()
    return marks_table