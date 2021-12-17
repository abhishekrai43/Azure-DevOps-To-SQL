import sqlite3
#import pandas as pd
conn = sqlite3.connect('Azure_Board.db')
c = conn.cursor()
# Get Work Item Relations of for Work Item 181
data = c.execute('''SELECT System_WorkItemType, rel_id, name FROM WI_Relations WHERE workItemId=181''')
# Get Relations
li1 = data.fetchall()
for item in li1:
    sqlcom = c.execute(f"SELECT * FROM {item[0]} WHERE workItemID={item[1]}")
    # Get Related Item Details
    print(item[2], sqlcom.fetchall())


