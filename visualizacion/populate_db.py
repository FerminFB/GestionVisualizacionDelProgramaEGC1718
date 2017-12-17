# -*- coding: utf-8 -*-
import sqlite3
import openpyxl


def create_db():
    bd = sqlite3.connect("programa.db")
    cursor = bd.cursor()
    cursor.execute("DROP TABLE IF EXISTS PROGRAMA;")
    cursor.execute('''CREATE TABLE PROGRAMA (ID	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,DIA VARCHAR,FECHA VARCHAR,SESSIONCODE VARCHAR, HORA_INICIO TEXT,HORA_FIN TEXT,TITULO VARCHAR);''')
    cursor.execute("DROP TABLE IF EXISTS CHARLAS;")
    cursor.execute('''CREATE TABLE CHARLAS (SESSIONCODE	VARCHAR NOT NULL PRIMARY KEY UNIQUE,EVENTO VARCHAR,TITULO VARCHAR,PONENTES VARCHAR, RESUMEN VARCHAR ,SESSION_NAME VARCHAR);''')
    print("Tablas creadas correctamente.")
    bd.close()


def get_file(numero):
    if numero == 1:
        return openpyxl.load_workbook('../programme-pre-v8.xlsx')
    elif numero == 2:
        return openpyxl.load_workbook('../programme-main-v9.xlsx')
    else:
        print "No es un numero de archivo valido."


def populate_1(nombre_hoja):
    doc = get_file(1)
    hoja = doc.get_sheet_by_name(nombre_hoja)
    row = {}
    cont = 0
    for fila in hoja.rows:
        data = []
        for columna in fila:
            if columna.value is not None:
                if columna.value.find("-") > -1:
                    hora_ini = columna.value.split('-')[0]
                    hora_fin = columna.value.split('-')[1]
                    data.append(hora_ini)
                    data.append(hora_fin)
                elif columna.value.find("(") > -1:
                    sessioncode = columna.value.replace('(', '').replace(')', '')
                    data.append(sessioncode)
                else:
                    data.append(columna.value)
        row['fila'+str(cont)] = data
        # "-------- final de fila ---------"
        cont = cont + 1

    dia = row.pop('fila0')[0]
    conn = sqlite3.connect("programa.db")
    cursor = conn.cursor()
    for k, v in row.iteritems():
        if len(v) == 3:
            cursor.execute("""INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, TITULO) VALUES (?,?,?,?,?)""",
                           (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[2])))
        else:
            cursor.execute("""INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, SESSIONCODE) VALUES (?,?,?,?,?)""",
                           (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[2])))
            cursor.execute("""INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, SESSIONCODE) VALUES (?,?,?,?,?)""",
                           (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[3])))
            cursor.execute("""INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, SESSIONCODE) VALUES (?,?,?,?,?)""",
                           (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[4])))
    conn.commit()
    print "Datos insertados correctamente de la hoja "+nombre_hoja+"."
    conn.close()


def populate_2(nombre_hoja):
    doc = get_file(2)
    hoja = doc.get_sheet_by_name(nombre_hoja)
    row = {}
    cont = 0
    for fila in hoja.rows:
        data = []
        for columna in fila:
            if columna.value is not None:
                if columna.value.find("-") > -1:
                    hora_ini = columna.value.split('-')[0]
                    hora_fin = columna.value.split('-')[1]
                    data.append(hora_ini)
                    data.append(hora_fin)
                elif columna.value.find("(") > -1:
                    aux = columna.value.split("(")[1]
                    sessioncode = aux.split(")")[0]
                    data.append(sessioncode)
                else:
                    data.append(columna.value)
        row['fila' + str(cont)] = data
        # "-------- final de fila ---------"
        cont = cont + 1

    if nombre_hoja is "Wednesday":
        row.pop('fila13')
    dia = row.pop('fila0')[0]
    conn = sqlite3.connect("programa.db")
    cursor = conn.cursor()
    for k, v in row.iteritems():
        if len(v) == 3:
            if v[2].find('.') != -1:
                cursor.execute("""INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, SESSIONCODE) VALUES (?,?,?,?,?)""",
                           (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[2])))
            else:
                cursor.execute(
                    """INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, TITULO) VALUES (?,?,?,?,?)""",
                    (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[2])))
        else:
            if len(v) == 2:
                cursor.execute(
                    """INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, TITULO) VALUES (?,?,?,?,?)""",
                    (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[0]), str(v[1])))
            else:
                cursor.execute(
                    """INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, SESSIONCODE) VALUES (?,?,?,?,?)""",
                    (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[2])))
                cursor.execute(
                    """INSERT INTO PROGRAMA (DIA, FECHA, HORA_INICIO, HORA_FIN, SESSIONCODE) VALUES (?,?,?,?,?)""",
                    (str(dia).split(", ")[0], str(dia).split(", ")[1], str(v[0]), str(v[1]), str(v[3])))

    conn.commit()
    print "Datos insertados correctamente de la hoja " + nombre_hoja + "."
    conn.close()


def populate_charlas(numero_documento):
    doc = get_file(numero_documento)
    hoja = doc.get_sheet_by_name('Talks')
    row = {}
    cont = 0
    for fila in hoja.rows:
        data = []
        for columna in fila:
            if columna.value is not None:
                data.append(columna.value)
        row['fila' + str(cont)] = data
        # "-------- final de fila ---------"
        cont = cont + 1
    row.pop('fila0')
    conn = sqlite3.connect("programa.db")
    cursor = conn.cursor()
    for k, v in row.iteritems():
        if len(v) != 0:
            if numero_documento == 1:
                if len(v) == 6:
                    cursor.execute("""INSERT INTO CHARLAS (SESSIONCODE, EVENTO, TITULO, PONENTES, RESUMEN) VALUES (?,?,?,?,?)""",
                        (str(v[1]), str(v[0]), str(v[2]).encode('utf-8'), str(v[3]).encode('utf-8'), str(v[4]).encode('utf-8')))
                else:
                    cursor.execute(
                        """INSERT INTO CHARLAS (SESSIONCODE, EVENTO, TITULO, PONENTES) VALUES (?,?,?,?)""",
                        (str(v[1]), str(v[0]), str(v[2]).encode('utf-8'), str(v[3]).encode('utf-8')))

            elif numero_documento == 2:
                if len(v) == 11:
                    cursor.execute(
                        """INSERT INTO CHARLAS (SESSIONCODE, EVENTO, TITULO, PONENTES) VALUES (?,?,?,?)""",
                        (str(v[4]), str(v[3]), str(v[5]).encode('utf-8'), str(v[6]).encode('utf-8')))
                else:
                    cursor.execute(
                        """INSERT INTO CHARLAS (SESSIONCODE, EVENTO, TITULO, PONENTES, SESSION_NAME) VALUES (?,?,?,?,?)""",
                        (str(v[4]), str(v[3]), str(v[6]).encode('utf-8'), str(v[7]).encode('utf-8'), str(v[5]).encode("utf-8")))

    conn.commit()
    print "Datos insertados correctamente de la hoja Talks del documento "+str(numero_documento)+"."
    conn.close()


if __name__ == '__main__':
    create_db()
    populate_1('Monday')
    populate_1('Tuesday')
    populate_2('Wednesday')
    populate_2('Thursday')
    populate_2('Friday')
    populate_charlas(1)
    populate_charlas(2)
