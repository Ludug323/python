import MySQLdb

# 連線資料庫
conn = MySQLdb.connect(host='loge7'
                       ,user='root'
                       ,passwd='loge717764'
                       ,db='test')
# 獲得一個遊標
cur = conn.cursor()
# 執行SQL語句  (返回值是查詢表中的行數，影響的行數)
reCount = cur.execute('select * from Userinfo')
# 獲取資料庫的資訊
data = cur.fetchall()
# 關閉資料庫
conn.close()

print ("The rows of this table is %d",(reCount))
print  (data)