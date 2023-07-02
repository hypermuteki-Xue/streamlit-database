
import streamlit as st
import connect
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit import session_state as state
import random
# 创建游标
cursor = connect.getCursor()

# 执行查询操作

def showPie():
    cursor.execute("SELECT * FROM xuezy_sche.xuezy_student_info;")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows)
    data=df.iloc[...,4]
    category_counts = data.value_counts()
    explode = [0]*len(category_counts)  # 创建一个全为0的列表
    explode[random.randint(0, len(category_counts) - 1)] = 0.1  # 假设我们想要突出显示第一部分
    fig, ax = plt.subplots()
    ax.pie(category_counts, labels = category_counts.index, autopct='%1.1f%%',explode=explode)
    ax.axis('equal')  # 保证饼图是圆的
    plt.title('Categories Distribution')
    st.pyplot(fig)

def showRank():
    cursor.execute("SELECT * FROM xuezy_sche.xuezy_student_ranking")
    rows = cursor.fetchall()
    df = pd.DataFrame(
         rows,
         columns=['学号','成绩'])
    st.line_chart(df)


def search(name="",number=""):
    if name =="" and number =="":
       st.write("请输入你的姓名和学号")

    elif name =="":
        cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_student_info where student_id={number};")
        rows = cursor.fetchall()
        df = pd.DataFrame(
             rows,
             columns=['学号','姓名','性别','年龄','生源所在地','已修学分总数','课程','成绩'])
        st.table(df)

    elif number =="":
        cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_student_info where student_name='{name}'")
        rows = cursor.fetchall()
        df = pd.DataFrame(
             rows,
             columns=['学号','姓名','性别','年龄','生源所在地','已修学分总数','课程','成绩'])
        
        st.table(df)
    else:
        cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_student_info where student_id={number} and student_name='{name}'")
        rows = cursor.fetchall()
        df = pd.DataFrame(
             rows,
             columns=['学号','姓名','性别','年龄','生源所在地','已修学分总数','课程','成绩'])
        st.table(df)

def sCourse(course=""):
    if course!="":
           cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_courses where xzy_course_name={course}")
           rows = cursor.fetchall()
           df = pd.DataFrame(
             rows,
             columns=['ID','课程名','学期','学时','类别','学分'])
           st.table(df)


def run():
    col1, col2 = st.columns(2)
    with col1:
         name=st.text_input("请输入你的姓名")
         if(name !=""):
             st.write(f"{name}同学你好")

    with col2:
         number=st.text_input("请输入你的学号")
         if(number!=""):
             st.write(f"你的学号是{number}")
    
    if(st.button("查询我的个人信息",key="student")):
       search(name,number)
       with st.chat_message("user"):
            st.write("你的同学分布如下地区👋")
            showPie()
            st.write("班级排名如下")
            showRank()
                 


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

     

           
           



       
    
