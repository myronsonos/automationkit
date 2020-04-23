from sqlalchemy import BigInteger, Column, DateTime, String, Text, VARCHAR, ForeignKey
from sqlalchemy.types import JSON

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils.types.uuid import UUIDType


AutomationBase = declarative_base()


class AutomationJob(AutomationBase):
    __tablename__ = 'automation_job'

    id = Column('job_id', BigInteger, primary_key=True)
    title =  Column('job_title', VARCHAR(1024), nullable=False)
    description = Column('job_description', Text, nullable=False)
    instance = Column('job_instance', UUIDType, nullable=False)
    branch =  Column('job_branch', VARCHAR(1024), nullable=True)
    build =  Column('job_build', VARCHAR(1024), nullable=True)
    flavor =  Column('job_flavor', VARCHAR(1024), nullable=True)
    start = Column('job_start', DateTime, nullable=False)
    stop = Column('job_stop', DateTime, nullable=True)
    detail = Column('job_detail', JSON, nullable=True)

    lscape_id = Column('lscape_id', BigInteger, ForeignKey("landscape.lscape_id"), nullable=True)
    lsscan_id = Column('lsscan_id', BigInteger, ForeignKey("landscape_scan.lsscan_id"), nullable=True)

class Landscape(AutomationBase):
    __tablename__ = 'landscape'

    id = Column('lsdesc_id', BigInteger, primary_key=True)
    name =  Column('lsdesc_name', VARCHAR(1024), nullable=False)
    detail = Column('lsdesc_detail', JSON, nullable=False)

class LandscapeScan(AutomationBase):
    __tablename__ = 'landscape_scan'

    id = Column('lsscan_id', BigInteger, primary_key=True)
    name =  Column('lsscan_name', VARCHAR(1024), nullable=False)
    detail = Column('lsscan_detail', JSON, nullable=False)

    lscape_id = Column('lscape_id', BigInteger, ForeignKey("landscape.lscape_id"))

class Task(AutomationBase):
    __tablename__ = 'task'

    id = Column('task_id', BigInteger, primary_key=True)
    name =  Column('task_name', VARCHAR(1024), nullable=False)
    extname = Column('task_extname', VARCHAR(1024), nullable=True)
    parameters = Column('task_parameters', Text, nullable=True)
    instance = Column('task_instance', UUIDType, nullable=False)
    parent = Column('task_parent', UUIDType, nullable=True)
    rtype = Column('task_rtype', String(50), nullable=False)
    result = Column('task_result', String(50), nullable=False)
    start = Column('task_start', DateTime, nullable=False)
    stop = Column('task_stop', DateTime, nullable=True)
    detail = Column('task_detail', JSON, nullable=True)

    run_id = Column('job_id', BigInteger, ForeignKey("automation_job.job_id"))

class TaskContainer(AutomationBase):
    __tablename__ = 'task_container'

    id = Column('tcont_id', BigInteger, primary_key=True)
    name =  Column('tcont_name', VARCHAR(1024), nullable=False)
    instance = Column('tcont_instance', UUIDType, nullable=False)
    parent = Column('tcont_parent', UUIDType, nullable=True)
    rtype = Column('tcont_rtype', String(50), nullable=False)

    run_id = Column('job_id', BigInteger, ForeignKey("automation_job.job_id"))


AutomationPod = declarative_base()

class WorkQueue(AutomationPod):
    __tablename__ = 'work_queue'

    id = Column('wkq_id', BigInteger, primary_key=True)

    title =  Column('wkq_title', VARCHAR(1024), nullable=False)
    description = Column('wkq_description', Text, nullable=False)
    branch =  Column('wkq_branch', VARCHAR(1024), nullable=True)
    build =  Column('wkq_build', VARCHAR(1024), nullable=True)
    flavor =  Column('wkq_flavor', VARCHAR(1024), nullable=True)
    added = Column('wkq_added', DateTime, nullable=False)
    started = Column('wkq_started', DateTime, nullable=True)
    status = Column('wkq_status', String(50), nullable=False)
    detail = Column('wkq_detail', JSON, nullable=True)

    user_id = Column('user_id', BigInteger, nullable=False)
