import streamlit as st
import student
import teacher
import controller
class PageManager(object):
    def __init__(self, pages: dict):
        self.pages = pages

    def run(self):
        page = st.sidebar.selectbox("请选择你的身份", list(self.pages.keys()))
        self.pages[page]()

pages = {
    "老师": teacher.run,
    "学生": student.run,
    "管理者": controller.run
}


def main():
    st.title("高校成绩管理系统")
    PageManager(pages).run()

if __name__ == "__main__":
    main()
