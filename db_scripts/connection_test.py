import oracledb

username = "webstore"
password = "6GuVk8ADDDawRX2P"
connection_str = "(description= (retry_count=20)(retry_delay=3)(address=(protocol=tcps)(port=1521)(host=adb.eu-stockholm-1.oraclecloud.com))(connect_data=(service_name=g9b34ba6c531a5c_c718201anrytzymj_high.adb.oraclecloud.com))(security=(ssl_server_dn_match=yes)))"

connection = oracledb.connect(user=username, password=password, dsn=connection_str)