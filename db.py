from typing import Any, Generator
from sqlalchemy.orm import Session, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:123123@localhost/DATA"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 1. Учебные планы
class StudyPlan(Base):
    __tablename__ = 'vvsu_study_plans'

    id_pln = Column(Integer, primary_key=True)
    direction = Column(String(255), nullable=False)
    profile = Column(String(255))
    specialty_code = Column(String(50), nullable=False)
    enrollment_year = Column(Integer, nullable=False)

# 2. Учебные группы
class StudyGroup(Base):
    __tablename__ = 'vvsu_study_groups'

    id_group = Column(Integer, primary_key=True)
    group_name = Column(String(50), nullable=False)
    id_pln = Column(Integer, ForeignKey('vvsu_study_plans.id_pln'), nullable=False)

    study_plan = relationship('StudyPlan', backref='groups')


# 3. Студенты
class Student(Base):
    __tablename__ = 'vvsu_students'

    id_stud = Column(Integer, primary_key=True)
    full_name = Column(String(255), nullable=False)
    birth_date = Column(Date)
    unique_identifier = Column(String(100))


# 4. Связка студентов и планов (Зачисление)
class StudentEnrollment(Base):
    __tablename__ = 'vvsu_student_enrollments'

    id_stud = Column(Integer, ForeignKey('vvsu_students.id_stud'), primary_key=True)
    id_group = Column(Integer, ForeignKey('vvsu_study_groups.id_group'), primary_key=True)
    id_pln = Column(Integer, ForeignKey('vvsu_study_plans.id_pln'), nullable=False)
    enrollment_date = Column(Date, default='CURRENT_DATE')
    is_active = Column(Boolean, default=True)

    student = relationship('Student', backref='enrollments')
    study_group = relationship('StudyGroup', backref='enrollments')
    study_plan = relationship('StudyPlan', backref='enrollments')


# 5. Справочник дисциплин (Общий)
class Discipline(Base):
    __tablename__ = 'vvsu_disciplines'

    id_dis = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    __table_args__ = {
        'comment': 'Общий справочник дисциплин'
    }


# 6. Дисциплины учебного плана (Состав плана)
class PlanDiscipline(Base):
    __tablename__ = 'vvsu_plan_disciplines'

    id_pln = Column(Integer, ForeignKey('vvsu_study_plans.id_pln'), primary_key=True)
    id_dis = Column(Integer, ForeignKey('vvsu_disciplines.id_dis'), primary_key=True)
    hours_total = Column(Integer, default=0)
    semester = Column(Integer, nullable=False)

    study_plan = relationship('StudyPlan', backref='plan_disciplines')
    discipline = relationship('Discipline', backref='plan_disciplines')


# 7. Академическая успеваемость (Оценки)
class AcademicRecord(Base):
    __tablename__ = 'vvsu_academic_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_stud = Column(Integer, ForeignKey('vvsu_students.id_stud'), nullable=False)
    id_pln = Column(Integer, ForeignKey('vvsu_study_plans.id_pln'), nullable=False)
    id_dis = Column(Integer, ForeignKey('vvsu_disciplines.id_dis'), nullable=False)
    grade_score = Column(Integer, nullable=False)
    grade = Column(String(10))
    grade_date = Column(Date)

    student = relationship('Student', backref='academic_records')


# 8. Дисциплины IThub
class IThubDiscipline(Base):
    __tablename__ = 'ithub_disciplines'

    id_dis = Column(String(50), primary_key=True)
    code_dis = Column(String(20), nullable=False)
    name_dis = Column(String(200), nullable=False)


# 9. Таблица сопоставления id дисциплин ВВГУ и IThub
class DisciplineMapping(Base):
    __tablename__ = 'disciplines_mapping'

    ithub_dis_id = Column(String(50), ForeignKey('ithub_disciplines.id_dis'), nullable=False, primary_key=True)
    vvsu_dis_id = Column(Integer, ForeignKey('vvsu_disciplines.id_dis'), nullable=False, primary_key=True)


# 10. Справочник групп LXP
class IThubStudyGroup(Base):
    __tablename__ = 'ithub_study_groups'

    unique_identifier = Column(String(100), primary_key=True)
    stud_full_name = Column(String(255))
    group_name = Column(String(255))


# 11. Оценки LXP
class IThubAcademicRecord(Base):
    __tablename__ = 'ithub_academic_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    student = Column(String(100), ForeignKey('ithub_study_groups.unique_identifier'))
    id_dis = Column(String(50), ForeignKey('ithub_disciplines.id_dis'), nullable=False)
    name_dis = Column(String(255), nullable=False)
    code_dis = Column(String(36))
    points = Column(Integer)

Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, Any, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()