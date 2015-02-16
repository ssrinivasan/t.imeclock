'''
Utility function for database related information
'''
from database import engine
from sqlalchemy import MetaData,Table

def populate_tasks_table():
    '''
    Add default tasks to task table.
    '''
    tasks_dict = {1:'modelling',2:'design',3:'personal_time',4:'breaks',5:'discussion',6:'Client Meeting',7:'Misc'}
    tasks_dict = [{'task_id':task_id,'task_name':task_name} for task_id,task_name in tasks_dict.iteritems()]

    print tasks_dict

    connection = engine.connect()
    metadata = MetaData()
    task_table = Table("tasks", metadata)


    ##Populate the table with default tasks
    connection.execute(task_table.insert(),tasks_dict)



