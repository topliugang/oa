import xlrd
import sqlite3
import datetime
from obj import Staff
	
xls_file_name = 'database.xlsx'
db_file_name = 'database.db'
sql_script = 'create_table.sql'

def create_table():
	with open(sql_script) as sql_script_file:
		con = sqlite3.connect(db_file_name)
		cur = con.cursor()
		cur.executescript(sql_script_file.read())
		con.commit()
		con.close()

def insert(sql, data = None):
	#with open(sql_script) as sql_script_file:
	con = sqlite3.connect(db_file_name)
	cur = con.cursor()
	if data:
		cur.execute(sql, data)
	else:
		cur.execute(sql)
	con.commit()
	con.close()



def insert_many(sql, data):
	con = sqlite3.connect(db_file_name)
	cur = con.cursor()
	cur.executemany(sql, data)
	con.commit()
	con.close()


def main():
	create_table()
	workbook = xlrd.open_workbook(xls_file_name)
	for sheet in workbook.sheets():
		table_name = sheet.name
		column_names = sheet.row_values(0)
		data = [] #list of list of datas
		for i in range(1, sheet.nrows):
			data.append(sheet.row_values(i))

		column_names_sql = ''
		for index, field in enumerate(column_names):
			column_names_sql += field
			if index+1 < len(column_names):
				column_names_sql += ', '

		wenhaos_sql = '?,'*(len(column_names)-1)+'?'
		#insert into table(name1, name2)values(?, ?)
		sql2 = 'insert into %s(%s) values (%s)'%(table_name, column_names_sql, wenhaos_sql)
		
		insert_many(sql2, data)
		

#export
def get_name_by_number(num):
	con = sqlite3.connect(db_file_name)
	cur = con.cursor()
	cur.execute('select * from staff where littlephone = ?', (num,))
	res = cur.fetchall() 
	if len(res) == 1:
		print res[0]

	con.commit()
	con.close()




		


if __name__ == '__main__':
	main()
	#get_name_by_number('61955')