import pymysql
import click
@click.command()
@click.option("-u",help="username")
@click.option("-p",help="password")
def fun(u,p):
  name=u
  passwd=p
  try:
    # 打开数据库连接
    db = pymysql.connect("localhost","root","","member" )
    # 创建一个游标对象 cursor
    cursor = db.cursor()
    # 执行 SQL 查询
    cursor.execute("SELECT id,name,passwd,face_url,face_id FROM member.users where name='%s'" % (name))
    # 获取单条数据.
    data = cursor.fetchone()
    if(data[2]==passwd):
        print('login success')
    else:
        print('passwd error')
  except Exception as e:
    raise e
  finally:
    db.close()  #关闭连接
if __name__=="__main__":
  fun()
