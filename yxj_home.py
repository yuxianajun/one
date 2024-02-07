import streamlit as st
import pandas as pd
from PIL import Image


page=st.sidebar.radio('啥都有工作室',['我是谁','我的兴趣推荐','我的图片编辑','我的智慧词典', '我的留言区', '网站推荐', '蛋仔推荐+联系方式'])

def img_change(img, rc,gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            #获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

def page1():
    st.write('我是一个中职生,会一点编程,力推免费,无广告好用的软件和网站,爱玩蛋仔,和平,以及我们学校的一些事')
    st.write('青岛交通职业学校的文艺汇演:链接:https://pan.baidu.com/s/1l22A2DvZjBM_oAn0Pacxkg?pwd=istd 提取码:istd')
    st.write('只要平凡')
    with open('只要平凡.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)
    
def page2():
    st.write(':black[欢迎大家来到我的网站]')
    st.write('作者尽量保证网站不断更')
    st.write('欢迎各位喜欢蛋仔的朋友加入')

    st.write('春三月')
    with open('春三月.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)
    st.write('赤伶')
    with open('赤伶.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)
    st.write('你从未离去')
    with open('你从未离去.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)
    st.write('古代文学常识口诀歌')
    with open('古代文学常识口诀歌.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)

    
    st.write(':red[蛋仔视频推荐.不是本人]')
    st.write(':black[http://xhslink.com/upLtPA]')
    st.write(':black[http://xhslink.com/quTtPA]')
   

def page3():
    st.write('只要平凡')
    with open('只要平凡.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3,format='audio/mp3', start_time=0)
    #图片处理
    st.write(":sunglasses:图片处理小程序:sunglasses")
    st.write('图片编辑仅限png, jpeg, jpg')
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        #获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open((uploaded_file))
        st.image(img)
        st.image(img_change(img, 0, 2, 1))
        tab1,tab2,tab3,tab4=st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))
            #values = st.slider(
            #    'Select a range of values',
            #       img, 1, 0, 2 )
            #st.write('Values:', values)

def page4():
    '''我的智慧词典'''
    st.write('智慧同典')
    #从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt','r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    #将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    #将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
   # 从本地文件中将单词的查询次数读取出来并存储在列表中
    with open('check_out_times.txt','r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    #将列表转为字典
        for i in range(len(times_list)):
            times_list[i] =times_list[i].split('#')
        times_dict ={}
        for i in times_list:
            times_dict[int(i[0])] = int(i[1])
    #创建输入框
    word=st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n]+= 1
        else:
            times_dict[n]= 1
        with open('words_space.txt','r', encoding='utf-8') as f:
            words_list = f.read().split('\n')

        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                # 恭喜你触发彩蛋，这是一行python代码
            print('hello world')''')

def page5():
    '''我的留言区'''
    st.write('我的留言区')
    #从文件中加载内容。并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是......', ['阿短', '编程猫'])
    new_message= st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt','w',encoding='utf-8')as f:
            message =''
            for i in messages_list:
                message+=i[0] + '#' +i[1] + '#' +i[2] + '\n'
            message = message[:-1]
            f.write(message)


def page6():
    #'''网站推荐'''
    st.write('宗旨是一切皆免费,平台个互通')
    st.write('https://tool.liumingye.cn/music/?page=searchPage#/')
    st.write('已知支持Windows,安卓')
    


def page7():
    st.write('视频来源')
    st.write('http://xiaohongshu.com')
    st.write('都来下载啊')
    st.write('https://party.163.com/')
    st.write('和大家一块讨论吧:26271714')
    st.write('如需源码请联系')
    st.image('联系方式.jpg', caption='联系方式')
    st.write('青岛交通职业学校的文艺汇演:链接:https://pan.baidu.com/s/1l22A2DvZjBM_oAn0Pacxkg?pwd=istd 提取码:istd')
    #实验
   # video_file = open('video1.mp4', 'rb')
    #video_bytes = video_file.read()
    
    #st.video(video_bytes)


if (page == '我是谁'):
    page1()
elif (page == '我的兴趣推荐'):
    page2()
elif (page == '我的图片编辑') :
    page3()
elif (page == '我的智慧词典') :
    page4()
elif (page == '我的留言区') :
    page5()
elif (page == '网站推荐') :
    page6()
elif (page == '蛋仔推荐+联系方式') :
    page7()
else :
    pass

#备注
    #st.image("1.jpg")
    #st.write(":red[文字]")
    #st.image("1.png")
    