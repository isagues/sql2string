import re

with open("in.java", "r") as reader:

    query = ""

    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        result = re.search('".*"', line)
        query += result.group(0)[1:-1]
        query += "\n"
        line = reader.readline()

    sql = open("out.sql", "w")
    sql.write(query)
