"""
.. module:: orm
    :platform: Darwin, Linux, Unix, Windows
    :synopsis: Contains the ORM associated with the akit database storage

.. moduleauthor:: Myron Walker <myron.walker@gmail.com>
"""

__author__ = "Myron Walker"
__copyright__ = "Copyright 2020, Myron W Walker"
__credits__ = []
__version__ = "1.0.0"
__maintainer__ = "Myron Walker"
__email__ = "myron.walker@gmail.com"
__status__ = "Development" # Prototype, Development or Production
__license__ = "MIT"

import enum
import json

from sqlalchemy import BigInteger, Column, DateTime, Enum, Float, Integer, String, Text, VARCHAR, ForeignKey
from sqlalchemy import inspect
from sqlalchemy.types import JSON

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy_utils.types.uuid import UUIDType


class SerializableMode:

    def to_dict(self, query_instance=None):
        dval = {}

        model = type(self)
        mapper = inspect(model)
        for col in mapper.attrs:
            col_key = col.key
            dval[col_key] = str(getattr(self, col_key))

        return dval


    def to_json(self, query_instance=None, indent=4):
        model_dict = self.to_dict(query_instance=query_instance)
        json_str = json.dumps(model_dict, indent=indent)
        return json_str

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

import enum
class WorkQueueJobType(enum.Enum):
    Local = 1
    Global = 2

class WorkQueue(AutomationPod, SerializableMode):
    __tablename__ = 'work_queue'

    id = Column('wkq_id', BigInteger, primary_key=True, autoincrement=True)

    jtype = Column('wkq_jtype', Enum(WorkQueueJobType), nullable=False)
    title =  Column('wkq_title', String(1024), nullable=False)
    description = Column('wkq_description', Text, nullable=False)
    branch =  Column('wkq_branch', String(1024), nullable=True)
    build =  Column('wkq_build', String(1024), nullable=True)
    flavor =  Column('wkq_flavor', String(1024), nullable=True)
    added = Column('wkq_added', DateTime, nullable=False)
    start = Column('wkq_start', DateTime, nullable=True)
    stop = Column('wkq_stop', DateTime, nullable=True)
    progress = Column('wkq_progress', Float, default=0.0)
    status = Column('wkq_status', String(50), nullable=False)
    packet = Column('wkq_packet', JSON, nullable=True)

    result_id = Column('result_id', String(64), nullable=False)
    user_id = Column('user_id', BigInteger, nullable=False)
