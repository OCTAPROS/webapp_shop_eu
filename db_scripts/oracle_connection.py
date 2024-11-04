import oracledb
import cx_Oracle


username = "webstore"
password = "pass1"
dsn = "localhost/XEPDB1"
# connection_string = "(description= (retry_count=5)(retry_delay=1)(address=(protocol=tcps)(port=1522)(host=adb.eu-stockholm-1.oraclecloud.com))(connect_data=(service_name=g9b34ba6c531a5c_iwlkc7wmcmofzi7a_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"


cnn = oracledb.connect(user=username, password=password, dsn=dsn)

# cnn = cx_Oracle.connect(
#     user=username,
#     password=password,
#     dsn=connection_string
# )

# print(cnn)

# ORACLE_USERNAME=system
# ORACLE_PASSWORD=password1
# ORACLE_CHARACTERSET=AL32UTF8
# ORACLE_PDB=XEPDB1


cur = cnn.cursor()
cur.execute("""SELECT * FROM KLIENT""")
col = cur.fetchall()
cur.close()
cnn.close()

for r in col:
    print(r)