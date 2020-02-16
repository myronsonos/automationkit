from sqlalchemy import BigInteger, Column, DateTime, VarChar
from sqlalchemy.types import JSON

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils.types.uuid as UUIDType


AutomationBase = declarative_base()


class AutomationRun(AutomationBase):
    __tablename__ = 'automation_run'

    id = Column('run_id', BigInteger, primary_key=True)
    title =  Column('run_title', VarChar(1024), nullable=False)
    instance = Column('run_instance', UUIDType, nullabe=False)
    branch =  Column('run_branch', VarChar(1024), nullable=True)
    build =  Column('run_build', VarChar(1024), nullable=True)
    flavor =  Column('run_flavor', VarChar(1024), nullable=True)
    start = Column('run_start', DateTime, nullable=False)
    stop = Column('run_stop', DateTime, nullable=True)
    detail = Column('run_detail', JSON, nullable=True)

    lscape_id = Column('lscape_id', BigInteger, ForeignKey("landscape.lscape_id"))
    lsscan_id = Column('lsscan_id', BigInteger, ForeignKey("landscape_scan.lsscan_id"))

class Landscape(AutomationBase):
    __tablename__ = 'landscape'

    id = Column('lsdesc_id', BigInteger, primary_key=True)
    name =  Column('lsdesc_name', VarChar(1024), nullable=False)
    detail = Column('lsdesc_detail', JSON, nullable=False)

class LandscapeScan(AutomationBase):
    __tablename__ = 'landscape_scan'

    id = Column('lsscan_id', BigInteger, primary_key=True)
    name =  Column('lsscan_name', VarChar(1024), nullable=False)
    detail = Column('lsscan_detail', JSON, nullable=False)

    lscape_id = Column('lscape_id', BigInteger, ForeignKey("landscape.lscape_id"))

class Task(AutomationBase):
    __tablename__ = 'task'

    id = Column('task_id', BigInteger, primary_key=True)
    name =  Column('task_name', VarChar(1024), nullable=False)
    exname = Column('task_exname', VarChar(1024), nullable=True)
    parameters = Column('task_parameters', Text, nullable=True)
    instance = Column('task_instance', UUIDType, nullable=False)
    parent = Column('task_parent', UUIDType, nullable=True)
    rtype = Column('task_rtype', String(50), nullable=False)
    result = Column('task_result', String(50), nullable=False)
    start = Column('task_start', DateTime, nullable=False)
    stop = Column('task_stop', DateTime, nullable=True)
    detail = Column('task_detail', JSON, nullable=True)

    run_id = Column('run_id', BigInteger, ForeignKey("automation_run.run_id"))

class TaskContainer(AutomationBase):
    __tablename__ = 'task_container'

    id = Column('tcont_id', BigInteger, primary_key=True)
    name =  Column('tcont_id', VarChar(1024), nullable=False)
    instance = Column('tcont_instance', UUIDType, nullable=False)
    parent = Column('tcont_parent', UUIDType, nullable=True)
    rtype = Column('tcont_rtype', String(50), nullable=False)

    run_id = Column('run_id', BigInteger, ForeignKey("automation_run.run_id"))
