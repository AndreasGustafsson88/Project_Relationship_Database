import sqlalchemy as sa
from sqlalchemy.orm import relationship
from Data.db import Base


class SparePartStore(Base):
    __tablename__ = 'spare_part_stores'
    store_id = sa.Column(sa.Integer, sa.ForeignKey('stores.store_id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True)
    spare_part_id = sa.Column(sa.Integer, sa.ForeignKey('spare_parts.spare_part_id', ondelete='CASCADE',  onupdate='CASCADE'), primary_key=True)
    stock = sa.Column(sa.Integer, nullable=False)
    stock_location = sa.Column(sa.String(45), nullable=False)
    spare_part = relationship('SparePart', back_populates="stores")
    store = relationship('Store', back_populates="spare_parts")


    def __repr__(self):
        return f'SparePartStore(spare_part_id={self.store_id},' \
               f'Spare part id={self.spare_part_id}, ' \
               f'Stock={self.stock}, ' \
               f'Stock location={self.stock_location}, ' \
               f'spare_part={self.spare_part} ' \
               f'store={self.store} ' \
