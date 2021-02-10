import camelot

file = r'C:\Users\GBP\Desktop\PDF Bancos\Daycoval.pdf'
 
tables = camelot.read_pdf(file, pages = "all", encoding="utf-8")

# tables[0].df

# tables[0].parsing_report
tables.export("camelot_tables.csv", f = "csv")
tables.export("camelot_tables.csv", f = "csv", compress = True)
tables.export("camelot_tables.xlsx", f = "excel")
print(tables)
