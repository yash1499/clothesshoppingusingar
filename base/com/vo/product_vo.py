from base import database
from base.com.vo.category_vo import CategoryVO
from base.com.vo.subcategory_vo import SubCategoryVO


class ProductVO(database.Model):
    __tablename__ = 'orm_product_master'
    product_id = database.Column('product_id', database.Integer, primary_key=True, autoincrement=True)
    product_name=database.Column('product_name', database.String(100))
    product_description = database.Column('product_description', database.String(100))
    product_price = database.Column('product_price', database.Integer)
    product_category_name=database.Column('product_category_name',database.Integer,database.ForeignKey(CategoryVO.category_id))
    product_subcategory_name = database.Column('product_subcategory_name', database.Integer,database.ForeignKey(SubCategoryVO.subcategory_id))

    def as_dict(self):
        return {
            'product_id': self.product_id,
            'product_name': self.product_name,
            'product_description': self.product_description,
            'product_price': self.product_price,
            'category_name':self.product_category_name,
            'subcategory_name':self.product_subcategory_name
        }


database.create_all()