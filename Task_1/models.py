from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine

Base = declarative_base()


class Energy(Base):
    __tablename__ = 'Energy'
    position = Column('Позиція', Integer,  primary_key=True)
    kind = Column('Вид', String(16), nullable=False)
    state = Column('Стан', String(16), nullable=False)
    seller = Column('Продавець', String(100), nullable=False)
    sales_schedule = Column('Тип графіку продажу електричної енергії', String(75), nullable=False)
    shopping_area = Column('Торгова зона', String(75), nullable=False)
    electricity_period = Column('Період відпуску/відбору електричної енергії', String(40), nullable=False)
    number_lots = Column('Кількість лотів', String(10), nullable=False)
    lot_mw = Column('Лот, МВт.', String(10), nullable=False)
    lot_mwh = Column('В лоті, МВт.г', String(10), nullable=False)
    total_volume_mwh = Column('Загальний обсяг, МВт.г', String(10), nullable=False)
    starting_price_without_vat = Column('Стартова ціна, грн./МВт.г без ПДВ', String(10), nullable=False)
    cost_without_vat = Column('Вартість, грн. без ПДВ', String(10), nullable=False)
    terms_payment = Column('Умови оплати', String(100), nullable=False)
    additional_conditions = Column('Додаткові умови', String(600), nullable=False)
    type = Column('Тип', String(16), nullable=False)
    rate = Column('Ставка', String(10), nullable=False)
    document = Column('Документи', String(100), nullable=False)

    def __repr__(self):
        return '<Energy exchange model {}>'.format(self.position)


DATABASE_URI = 'sqlite:///./dtrading'
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(bind=engine)
