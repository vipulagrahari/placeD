import sqlite3

conn = sqlite3.connect("database.db")
c = conn.cursor()
# SQL_STATEMENT = """CREATE TABLE jobs(

#         Year TEXT NOT NULL,

#         company_name TEXT NOT NULL,

#         job_prof TEXT,

#         job_desc TEXT,

#         remarks TEXT,

#         venue TEXT,

#         date TEXT NOT NULL,

#         eligibility TEXT,

#         ctc TEXT NOT NULL,

#         college VARCHAR(50) NOT NULL,

#         FOREIGN KEY(college) REFERENCES login(college)

# );
# """
# c.execute(SQL_STATEMENT)
c.execute(
    """INSERT INTO jobs VALUES ('2020',"TCS", "SDE",'Software', 'none', 'online', '2020-07-03',"75+",'3-7 LPA', "SRIT");""")

c.execute("SELECT * FROM jobs")
result = c.fetchall()
for i in result:
	print(i)

# Remember to save + close
conn.commit()
conn.close()