# coding:utf-8
from sqlalchemy import Column
from sqlalchemy import Integer, String, Text, JSON, DATETIME, ForeignKey, PickleType, DateTime, text
from util.dbmanager import db_manager
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # __bind_key__ = 'users_write'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username


class Apps(Base):
    __tablename__ = 'apps'
    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    appid = Column(String(200), primary_key=True, nullable=False, unique=True)
    parent_appid = Column(String(200), nullable=False, default="unknow")
    desc = Column(String(200), nullable=False)
    ip = Column(JSON, nullable=False)
    ns = Column(JSON, nullable=False)
    cli_publickey = Column(Text, nullable=False)
    cli_privatekey = Column(Text, nullable=False)
    srv_publickey = Column(Text, nullable=False)
    srv_privatekey = Column(Text, nullable=False)
    srv = Column(JSON, nullable=False)
    master_contract_address = Column(JSON, nullable=False, default=[])
    wallet = Column(String(200), nullable=False, default="no set")
    callback_url = Column(String(250), nullable=True)
    status = Column(Integer, nullable=False)


class Accounts(Base):
    __tablename__ = "accounts"
    id = Column(Integer, autoincrement=True, primary_key=True)
    address = Column(String(100), primary_key=True)
    balance = Column(String(20))
    create_time = Column(String(20))
    type = Column(String(10))
    # 到账提醒 1为有新到账
    arrival_reminder = Column(Integer, default=0)
    

class TransactionRecord(Base):
    __tablename__ = "transaction_record"
    id = Column(Integer, autoincrement=True, primary_key=True)
    from_address = Column(String(50))
    to_address = Column(String(50))
    value = Column(String(20))
    transaction_time = Column(String(20))
    tx_hash = Column(String(100))
    type = Column(String(10))
    pay_gas = Column(String(50))
    tr_appid = Column(String(100), default="wallet tr")  # 调用方的appid
    

class DeployContracts(Base):
    __tablename__ = "deploy_contracts"
    id = Column(Integer, autoincrement=True, primary_key=True)
    master_contract_name = Column(String(200), primary_key=True)
    deploy_account = Column(String(200))
    deploy_tx_hash = Column(String(100))
    deploy_time = Column(String(20))
    pay_gas = Column(String(20))
    master_contract_address = Column(String(100))
    contract_address = Column(String(100))
    contract_name = Column(String(100))
    master_mark = Column(String(20))
    # service_id = Column(Integer, ForeignKey('deploy_contracts.id'), nullable=True)
    

class Contracts(Base):
    __tablename__ = "contracts"
    contract_id = Column(Integer, autoincrement=True, primary_key=True)
    contract_address = Column(String(100), primary_key=True)
    contract_version = Column(String(20))
    contract_text = Column(Text)
    

class Tokens(Base):
    __tablename__ = "tokens"
    token_id = Column(Integer, autoincrement=True, primary_key=True)
    token_full_name = Column(String(20), primary_key=True)
    token_nick_name = Column(String(10), primary_key=True)


# class Services(Base):
#     __tablename__ = "services"
#     service_id = Column(Integer, autoincrement=True, primary_key=True)
#     service_name = Column(String(20), primary_key=True)
#     service_description = Column(String(1000))
#     contracts = relationship('DeployContracts')
    

class ContractOp(Base):
    # 合约调用表
    __tablename__ = "contract_op_table"
    op_id = Column(Integer, autoincrement=True, primary_key=True)
    contract_name = Column(String(200), primary_key=True)
    contract_address = Column(String(100), primary_key=True)
    op_info = Column(PickleType)
    op_time = Column(String(20))
    tx_hash = Column(String(100))
    order_id = Column(String(100))
    pay_gas = Column(String(50))
    type = Column(Integer, default=0)  # 2为无需支付 1为已支付 0为初始态 -1为失效
    op_appid = Column(String(100))  # 调用方的appid


class RecodeLogs(Base):
    __tablename__ = "recode_logs"
    rl_id = Column(Integer, autoincrement=True, primary_key=True)
    create_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    level_name = Column(String(10))
    message = Column(String(255))
    func_name = Column(String(255))
    stack_info = Column(String(255))

    
def create_tables():
    engine = db_manager.get_engine_master()
    Base.metadata.create_all(engine)


