from sqlalchemy import (MetaData, create_engine as ce, Table, Column as Col, Integer as Int,
                       Text, String as Str, DateTime as DT, ForeignKey as FK)

DB = ce("postgres://postgres:1234@127.0.0.1:5432/sqlalch")

metadata = MetaData()

product = Table( 'product' , metadata,
    Col('productID', Int(), primary_key=True),
    Col('name', Str(25), nullable=False, unique=True),
    Col('categoryID', Int(), FK('category.categoryID')),
    Col('price', Int(), nullable=False),
    Col('description', Text())
)

category = Table( 'category' , metadata,
    Col('categoryID', Int(), primary_key=True),
    Col('name', Str(25), nullable=False)
)

customer = Table( 'customer' , metadata,
    Col('customerID', Int(), primary_key=True),
    Col('name', Str(20), nullable=False)
)

order = Table( 'order' , metadata,
    Col('orderID', Int(), primary_key=True),
    Col('customerID', Int(), FK('customer.customerID'))
)

order_details = Table( 'order_details' , metadata,
    Col('orderID', Int(), FK('order.orderID'), primary_key=True),
    Col('productID', Int(), FK('product.productID'), primary_key=True),
    Col('amount', Int(), nullable=False)
)

metadata.create_all(DB)

connection = DB.connect()