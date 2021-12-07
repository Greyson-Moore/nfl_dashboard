#imports
from sqlalchemy import create_engine
import pandas as pd
from flask import jsonify

#class that loads in the database
class LoadHelp():
    def __init__(self):
        pass
    
    def loadHelp(self,table_name):
        #creates connection to the database
        engine = create_engine('postgresql://postgres:Password@34.68.100.219:5432/postgres')

        qb_df = pd.read_sql_query(f'select * from {table_name}',con=engine)
        
        #changes the results from a dataframe into html
        html = qb_df.to_html(index=False)
        
        # f = open("table.html",'w')
        # f.write(html)
        # f.close()

        return(html)

