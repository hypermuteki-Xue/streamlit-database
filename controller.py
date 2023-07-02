import streamlit as st
import connect
import pandas as pd
cursor = connect.getCursor()

# 执行查询操作
def insert():
    col1, col2 ,col3,col4,col5,col6= st.columns(6)
    with col1:
        value1=st.text_input("ID")
    with col2:
        value2=st.text_input("名称")
    with col3:
        value3=st.text_input("性别或开课学期")
    with col4:
        value4=st.text_input("年龄或学时")
    with col5:
        value5=st.text_input("生源、职称类别")
    with col6:
        value6=st.text_input("学分或电话")

    option = st.selectbox(
    '你想插入哪个表',
    ('学生', '教师', '课程','教师-课程','成绩表'))

    if option=='学生':
       if(st.button("插入该数据",key="insert1")):
          if not value1 or not value2 or not value3 or not value4 or not value5 or not value6:
             st.write("不能为空")
          else:
             cursor.execute(f"INSERT INTO xuezy_sche.Xuezy_students VALUES ({value1}, '{value2}', '{value3}', {value4}, '{value5}', {value6});")
    elif option=='教师':
        if(st.button("插入该数据",key="insert2")):
          if not value1 or not value2 or not value3 or not value4 or not value5 or not value6:
             st.write("不能为空")
          else:
             cursor.execute(f"INSERT INTO  xuezy_sche.Xuezy_teachers VALUES ({value1}, '{value2}', '{value3}', {value4}, '{value5}', '{value6}');")
    elif option=='课程':
        if(st.button("插入该数据",key="insert3")):
          if not value1 or not value2 or not value3 or not value4 or not value5 or not value6:
             st.write("不能为空")
          else:
             cursor.execute(f"INSERT INTO xuezy_sche.Xuezy_courses VALUES ({value1}, '{value2}', '{value3}', {value4}, '{value5}', {value6});")
    elif option=='教师-课程':
        if(st.button("插入该数据",key="insert4")):
          if not value1 or not value2 or not value3:
             st.write("不能为空")
          else:
             cursor.execute(f"INSERT INTO xuezy_sche.Xuezy_teacher_course VALUES ({value1}, {value2}, '{value3}');")
    elif option=='成绩表':
        if(st.button("插入该数据",key="insert5")):
          if not value1 or not value2 or not value3 or not value4 :
             st.write("不能为空")
          else:
             cursor.execute(f"INSERT INTO xuezy_sche.Xuezy_grades VALUES ({value1}, '{value2}', {value3}, {value4});")
            
     
    




def update():

    id = st.text_input("输入你想修改数据的id值")
    option = st.selectbox('你想修改哪个表',('学生', '教师', '课程'))


    if option=='学生':
           update_value= st.multiselect('请输入你想修改的属性',['学号', '姓名','性别' ,'年龄', '生源','已修学分'])#属性
           value_dict={'学号':'xzy_id','姓名':'xzy_name','性别':'xzy_gender','年龄':'xzy_age','生源':'xzy_origin','已修学分总数':'xzy_credit_total'}
           set_list = [value_dict.get(key) for key in update_value]
    
           value_list=[]#值
           col1, col2 ,col3,col4,col5,col6= st.columns(6)
           with col1:
               value1=st.text_input("ID",key="ID")
           with col2:
                value2=st.text_input("名称",key="ID1")
           with col3:
              value3=st.text_input("性别或开课学期",key="ID2")
           with col4:
              value4=st.text_input("年龄或学时",key="ID3")
           with col5:
              value5=st.text_input("生源、职称类别",key="ID4")
           with col6:
              value6=st.text_input("学分或电话",key="ID5")
            
           if(st.button("修改",key="update")):
                if value1!="":
                     value_list.append(value1)
                if value2!="":
                     value_list.append(value2)
                if value3!="":
                         value_list.append(value3)
                if value4!="":
                      value_list.append(value4)
                if value5!="":
                     value_list.append(value5)
                if value6!="":
                     value_list.append(value6)
                set_clause = ', '.join([f"{k} = %s" for k in set_list])
                sql = f"UPDATE xuezy_sche.xuezy_students SET {set_clause} WHERE xzy_id = {id}"
                cursor.execute(sql, value_list)
            
 

    elif option=='教师':
           update_value= st.multiselect('请输入你想修改的属性',['教师编号', '姓名', '性别', '年龄','职称','联系电话'])#属性
           value_dict={'教师编号':'xzy_tid','姓名':'xzy_name','性别':'xzy_gender','年龄':'xzy_age','职称':'xzy_title','联系电话':'xzy_number'}
           set_list = [value_dict.get(key) for key in update_value]
    
           value_list=[]#值
           col1, col2 ,col3,col4,col5,col6= st.columns(6)
           with col1:
               value1=st.text_input("ID",key="ID")
           with col2:
                value2=st.text_input("名称",key="ID1")
           with col3:
              value3=st.text_input("性别或开课学期",key="ID2")
           with col4:
              value4=st.text_input("年龄或学时",key="ID3")
           with col5:
              value5=st.text_input("生源、职称类别",key="ID4")
           with col6:
              value6=st.text_input("学分或电话",key="ID5")
            
           if(st.button("修改",key="update1")):
                if value1!="":
                     value_list.append(value1)
                if value2!="":
                     value_list.append(value2)
                if value3!="":
                         value_list.append(value3)
                if value4!="":
                      value_list.append(value4)
                if value5!="":
                     value_list.append(value5)
                if value6!="":
                     value_list.append(value6)
                set_clause = ', '.join([f"{k} = %s" for k in set_list])
                sql = f"UPDATE xuezy_sche.xuezy_teachers SET {set_clause} WHERE xzy_tid = {id}"
                cursor.execute(sql, value_list)
    else:
           update_value= st.multiselect('请输入你想修改的属性',['课程编号', '课程名称', '开课学期', '学时','类别','学分'])#属性
           value_dict={'课程编号':'xzy_course_id','课程名称':'xzy_course_name','开课学期':'xzy_term','学时':'xzy_hours','类别':'xzy_exam_or_test','学分':'xzy_credit'}
           set_list = [value_dict.get(key) for key in update_value]
    
           value_list=[]#值
           col1, col2 ,col3,col4,col5,col6= st.columns(6)
           with col1:
               value1=st.text_input("ID",key="ID")
           with col2:
                value2=st.text_input("名称",key="ID1")
           with col3:
              value3=st.text_input("性别或开课学期",key="ID2")
           with col4:
              value4=st.text_input("年龄或学时",key="ID3")
           with col5:
              value5=st.text_input("生源、职称类别",key="ID4")
           with col6:
              value6=st.text_input("学分或电话",key="ID5")
            
           if(st.button("修改",key="update")):
                if value1!="":
                     value_list.append(value1)
                if value2!="":
                     value_list.append(value2)
                if value3!="":
                         value_list.append(value3)
                if value4!="":
                      value_list.append(value4)
                if value5!="":
                     value_list.append(value5)
                if value6!="":
                     value_list.append(value6)
                set_clause = ', '.join([f"{k} = %s" for k in set_list])
                sql = f"UPDATE xuezy_sche.xuezy_courses SET {set_clause} WHERE xzy_course_id = {id}"
                cursor.execute(sql, value_list)




def delete():
    option = st.selectbox('你想删除哪个表中的数据',('学生', '教师', '课程'))
    if option=='学生':
           update_value= st.multiselect('请输入你想根据哪个属性删除',['学号', '姓名','性别' ,'年龄', '生源','已修学分'])#属性
           value_dict={'学号':'xzy_id','姓名':'xzy_name','性别':'xzy_gender','年龄':'xzy_age','生源':'xzy_origin','已修学分总数':'xzy_credit_total'}
           set_list = [value_dict.get(key) for key in update_value]
    
           value_list=[]#值
           col1, col2 ,col3,col4,col5,col6= st.columns(6)
           with col1:
               value1=st.text_input("ID",key="ID")
           with col2:
                value2=st.text_input("名称",key="ID1")
           with col3:
              value3=st.text_input("性别或开课学期",key="ID2")
           with col4:
              value4=st.text_input("年龄或学时",key="ID3")
           with col5:
              value5=st.text_input("生源、职称类别",key="ID4")
           with col6:
              value6=st.text_input("学分或电话",key="ID5")
            
           if(st.button("删除",key="delete")):
                if value1!="":
                     value_list.append(value1)
                if value2!="":
                     value_list.append(value2)
                if value3!="":
                         value_list.append(value3)
                if value4!="":
                      value_list.append(value4)
                if value5!="":
                     value_list.append(value5)
                if value6!="":
                     value_list.append(value6)
                set_clause = ' and '.join([f"{k} = %s" for k in set_list])
                sql = f"delete from xuezy_sche.xuezy_students WHERE {set_clause}"
                cursor.execute(sql, value_list)
            
 

    elif option=='教师':
           update_value= st.multiselect('请输入你想修改的属性',['教师编号', '姓名', '性别', '年龄','职称','联系电话'])#属性
           value_dict={'教师编号':'xzy_tid','姓名':'xzy_name','性别':'xzy_gender','年龄':'xzy_age','职称':'xzy_title','联系电话':'xzy_number'}
           set_list = [value_dict.get(key) for key in update_value]
    
           value_list=[]#值
           col1, col2 ,col3,col4,col5,col6= st.columns(6)
           with col1:
               value1=st.text_input("ID",key="ID")
           with col2:
                value2=st.text_input("名称",key="ID1")
           with col3:
              value3=st.text_input("性别或开课学期",key="ID2")
           with col4:
              value4=st.text_input("年龄或学时",key="ID3")
           with col5:
              value5=st.text_input("生源、职称类别",key="ID4")
           with col6:
              value6=st.text_input("学分或电话",key="ID5")
            
           if(st.button("修改",key="update1")):
                if value1!="":
                     value_list.append(value1)
                if value2!="":
                     value_list.append(value2)
                if value3!="":
                         value_list.append(value3)
                if value4!="":
                      value_list.append(value4)
                if value5!="":
                     value_list.append(value5)
                if value6!="":
                     value_list.append(value6)
                set_clause = ' and '.join([f"{k} = %s" for k in set_list])
                sql = f"delete from xuezy_sche.xuezy_teachers WHERE {set_clause}"
                cursor.execute(sql, value_list)
    else:
           update_value= st.multiselect('请输入你想修改的属性',['课程编号', '课程名称', '开课学期', '学时','类别','学分'])#属性
           value_dict={'课程编号':'xzy_course_id','课程名称':'xzy_course_name','开课学期':'xzy_term','学时':'xzy_hours','类别':'xzy_exam_or_test','学分':'xzy_credit'}
           set_list = [value_dict.get(key) for key in update_value]
    
           value_list=[]#值
           col1, col2 ,col3,col4,col5,col6= st.columns(6)
           with col1:
               value1=st.text_input("ID",key="ID")
           with col2:
                value2=st.text_input("名称",key="ID1")
           with col3:
              value3=st.text_input("性别或开课学期",key="ID2")
           with col4:
              value4=st.text_input("年龄或学时",key="ID3")
           with col5:
              value5=st.text_input("生源、职称类别",key="ID4")
           with col6:
              value6=st.text_input("学分或电话",key="ID5")
            
           if(st.button("修改",key="update")):
                if value1!="":
                     value_list.append(value1)
                if value2!="":
                     value_list.append(value2)
                if value3!="":
                         value_list.append(value3)
                if value4!="":
                      value_list.append(value4)
                if value5!="":
                     value_list.append(value5)
                if value6!="":
                     value_list.append(value6)
                set_clause = ' and '.join([f"{k} = %s" for k in set_list])
                sql = f"delete from xuezy_sche.xuezy_courses WHERE {set_clause}"
                cursor.execute(sql, value_list)



def select():
    col1, col2 ,col3,col4,col5,col6= st.columns(6)
    with col1:
        value1=st.text_input("ID")
        if value1=='':
            value1='%'
    with col2:
        value2=st.text_input("名称")
        if value2=='':
            value2='%'
    with col3:
        value3=st.text_input("性别或开课学期")
        if value3=='':
            value3='%'
    with col4:
        value4=st.text_input("年龄或学时")
        if value4=='':
            value4='%'
    with col5:
        value5=st.text_input("生源、职称类别")
        if value5=='':
            value5='%'
    with col6:
        value6=st.text_input("学分或电话")
        if value6=='':
            value6='%'
    option = st.selectbox(
    '你想查询哪个表',
    ('学生', '教师', '课程'))
    if option=='学生':
        if(st.button("查询",key='select1')):
           cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_students where xzy_id like '{value1}' and xzy_name like '{value2}' and xzy_gender like '{value3}' and xzy_age like '{value4}' and xzy_origin like '{value5}' and xzy_credit_total like'{value6}';")
           rows = cursor.fetchall()
           df = pd.DataFrame(
                rows,
                columns=['学号','姓名','性别','年龄','生源所在地','已修学分总数'])
           st.table(df)
    elif option=='教师':
        if(st.button("查询",key='select2')):
           cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_teachers where xzy_tid like '{value1}' and xzy_name like '{value2}' and xzy_gender like '{value3}' and xzy_age like '{value4}' and xzy_title like '{value5}' and xzy_number like'{value6}';")
           rows = cursor.fetchall()
           df = pd.DataFrame(
                rows,
                columns=['教师编号','姓名','性别','年龄','职称','联系电话'])
           st.table(df)
    else:
         if(st.button("查询",key='select3')):
           cursor.execute(f"SELECT * FROM xuezy_sche.xuezy_courses where xzy_course_id like '{value1}' and xzy_course_name like '{value2}' and xzy_term like '{value3}' and xzy_hours like '{value4}' and xzy_exam_or_test like '{value5}' and xzy_credit like'{value6}';")
           rows = cursor.fetchall()
           df = pd.DataFrame(
             rows,
             columns=['课程编号','课程名称','开课学期','学时','考试或考查','学分'])
           st.table(df)





    

def run():
    st.balloons()
    choose = st.radio(
    "选择你想进行的操作",
    ('增加数据', '删除数据', '修改数据','查找数据'))
    if choose == '增加数据':
       insert()
    elif choose=='删除数据':
       delete()
    elif choose=='修改数据':
       update()
    else: 
       select()
    
    


