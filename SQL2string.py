

with open("in.sql", "r") as reader:

    string = ""

    line = reader.readline()

    firstLine = True

    while line != '':  # The EOF char is an empty string
        
        if(firstLine):
            firstLine = False
        else:
            string+= '+ '
        
        aux = line.replace('\n', '').strip()
        string += f'"{aux} " \n'

        line = reader.readline()

    sql = open("out.java", "w")
    sql.write(string)
