import pymysql

# Criando conexão
connect = pymysql.connect(host='localhost', user='root', password='root', database='inventario')

with connect:
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE stwbrasil(id int not null auto_increment, marca varchar(20), modelo varchar(60), service_tag varchar(60),monitor varchar(20), quant_monitor int unsigned,teclado varchar(20), mouse varchar(20),memoria int unsigned, processador varchar(80), harddisk int unsigned, ssd int unsigned, nome_computador varchar(80), veersao_windows varchar(80), usuario varchar(20), cargo varchar(25), departameento varchar(50), modelo_telefone varchar(20), ramal int unsigned, email varchar(100), ip varchar(15), versao_office varchar(20), antivirus varchar(30), impressora varchar(30), PRIMARY KEY(id))')

