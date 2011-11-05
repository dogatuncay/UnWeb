import os
import xlrd

path="/home/doga/Desktop/migrate"
dirList=os.listdir(path)
rnum=2
row=3

for fname in dirList:
	if fname.split(".")[1] == "xls":
		xls_file = "/home/doga/Desktop/migrate/"+fname
		xls_workbook = xlrd.open_workbook(xls_file)
		xls_sheet = xls_workbook.sheet_by_index(0)

		raw_data = [['']*xls_sheet.ncols for _ in range(xls_sheet.nrows)]
		raw_str = ''
		feild_delim = ','
		text_delim = '"'

		for rnum in range(xls_sheet.nrows):
	    		for cnum in range(xls_sheet.ncols):
	        		raw_data[rnum][cnum] = str(xls_sheet.cell(rnum,cnum).value)

		for rnum in range(len(raw_data)):
	    		for cnum in range(len(raw_data[rnum])):
	       			if (cnum == len(raw_data[rnum]) - 1):
	            			feild_delim = '\n'
	        		else:
	            			feild_delim = ','
	        		raw_str += text_delim + raw_data[rnum][cnum] + text_delim + 	feild_delim
		final_csv_name_splitdot= fname.split(".")[0]
		final_csv_name=final_csv_name_splitdot+".csv"
		final_csv = open(final_csv_name, 'w')
		final_csv.write(raw_str)
		final_csv.close()

	
