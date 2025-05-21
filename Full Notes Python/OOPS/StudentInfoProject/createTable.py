import oracledb as orc
try:
    con=orc.connect("system/yash@localhost/orcl")
    cur=con.cursor()
    cur.execute("create table student(stno number(3) primary key,sname varchar2(10) not null,smarks number(5,2) not null,collegename varchar2(15) not null)")
    print("table created verify")
except orc.DatabaseError as db:
    print("problem in oracle:",db)