import psycopg2


def get_teacher(work_name):
    conn = psycopg2.connect(host='ctas.shmtu.edu.cn',
                            port='15432',
                            dbname='testdb',
                            user='smuport',
                            password='smuport',
                            options='-c search_path=study',
                            connect_timeout=20,
                            application_name="supervisor",
                            keepalives=1,
                            keepalives_idle=60,
                            keepalives_interval=5,
                            keepalives_count=5)

    cur = conn.cursor()
    # sql = "select * from study.teacher where work_num = '" + work_num + "'"
    sql3 = "select * from study.teacher where work_name = '" + work_name + "'"
    # sql2 = "select * from teacher where work_num='{}'".format(work_num)
    cur.execute(sql3)
    data = cur.fetchone()
    print(data)
    return data


def get_max_stud():
    conn = psycopg2.connect(host='ctas.shmtu.edu.cn',
                            port='15432',
                            dbname='testdb',
                            user='smuport',
                            password='smuport',
                            options='-c search_path=study',
                            connect_timeout=20,
                            application_name="supervisor",
                            keepalives=1,
                            keepalives_idle=60,
                            keepalives_interval=5,
                            keepalives_count=5)

    cur = conn.cursor()
    # sql = "select * from study.teacher where work_num = '" + work_num + "'"
    # sql2 = "select * from teacher where work_num='{}'".format(work_num)
    # sql3 = "select * from study.teacher where sex = '男'"
    sql4 = "select sum(max_stud) from study.teacher where sex = '男'"
    cur.execute(sql4)
    data = cur.fetchone()[0]
    # maxstudlist = []
    # for i in data:
    #     maxstudlist.append(i[3])
    # print(maxstudlist)
    # print(sum(maxstudlist))
    print(data)

    return data


get_max_stud()



