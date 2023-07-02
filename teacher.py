import streamlit as st
import connect
import pandas as pd
from streamlit import session_state as state


cursor = connect.getCursor()

def search_T():
    col1, col2 = st.columns(2)
    with col1:
         name=st.text_input("请输入你的姓名")
         if(name !=""):
             st.write(f"{name}老师你好")

    with col2:
         number=st.text_input("请输入你的手机号")
         if(number!=""):
             st.write(f"你的手机号是{number}")

    if name =="" and number =="":
       st.write("姓名和手机号不能为空")
    elif name =="":
        cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_teacher_course_view where xzy_teacher_number like '{number}%';")
        rows = cursor.fetchall()
        df = pd.DataFrame(
             rows,
             columns=['ID','姓名','性别','年龄','职称','手机号','课程','任课日期'])
        st.table(df)

    elif number =="":
        cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_teacher_course_view where xzy_teacher_name like'{name}%'")
        rows = cursor.fetchall()
        df = pd.DataFrame(
             rows,
             columns=['ID','姓名','性别','年龄','职称','手机号','课程','任课日期'])
        
        st.table(df)
    else:
        cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_teacher_course_view where  xzy_teacher_number like '{number}%' and xzy_teacher_name like '{name}%'")
        rows = cursor.fetchall()
        df = pd.DataFrame(
             rows,
             columns=['ID','姓名','性别','年龄','职称','手机号','课程','任课日期'])
        st.table(df)
def search_rank():
        cursor.execute("SELECT * FROM xuezy_sche.xuezy_student_ranking")
        rows = cursor.fetchall()
        df = pd.DataFrame(
                rows,
                columns=['学号','成绩'])
        st.table(df)

def term_count():
        cursor.execute("SELECT * FROM xuezy_sche.xuezy_student_yearly_average")
        rows = cursor.fetchall()
        df = pd.DataFrame(
                rows,
                columns=['学号','学年','成绩'])
        st.table(df)

def ave_count():
        cursor.execute("SELECT * FROM xuezy_sche.xuezy_course_average_grade")
        rows = cursor.fetchall()
        df = pd.DataFrame(
                rows,
                columns=['课程编号','平均成绩'])
        st.table(df)


def run():
    course = st.chat_input("请输入你想查询的课程")
    if course:
        st.write(f"你想查询的课程是: {course}")
        if course != '':
           cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_courses where xzy_course_name='{course}'")
           rows = cursor.fetchall()
           df = pd.DataFrame(
                rows,
                columns=['ID','课程名','学期','学时','类别','学分'])
           st.table(df)
    
    tab1, tab2, tab3,tab4 = st.tabs(["查询个人信息", "查询班级成绩排名", "学生成绩按每学年成绩统计","每门课程平均成绩统计"])
    with tab1:
        search_T()
    with tab2:
        search_rank()
    with tab3:
        term_count()
    with tab4:
        ave_count()