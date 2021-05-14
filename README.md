# Django实现我爱看电影网站<br>
## 主要实现功能: 注册，登陆，播放视频，评论视频，xadmin实现后台提供视频管理，权限管理等等<br>

### 首页(搜索，筛选）<br>

![image](https://user-images.githubusercontent.com/56242720/118259099-4f8abb80-b4e3-11eb-851f-9007453e44b8.png)


### 搜索页面<br>
![image](https://user-images.githubusercontent.com/56242720/118259201-734e0180-b4e3-11eb-86d0-b9068b92db9e.png)



### 播放页面<br>
![image](https://user-images.githubusercontent.com/56242720/118259347-9f698280-b4e3-11eb-9e5e-fa7e28b43942.png)




### 个人中心<br>
![image](https://user-images.githubusercontent.com/56242720/118259286-8f51a300-b4e3-11eb-9e31-46170c060651.png)




### 后台<br>
![image](https://user-images.githubusercontent.com/56242720/118259256-852fa480-b4e3-11eb-97a8-bda083091e01.png)





### 环境配置：python2.7  pip install -r requirements.txt<br>

### 创建数据库将movie.sql文件导入<br>

### 进入项目目录执行如下命令：<br>

python manage.py collectstatic(关闭了debug需要收集静态文件)<br>

python manage.py runserver 0.0.0.0：8000<br>

### 打开浏览器输入：http://127.0.0.1:8000<br>

## 说明：<br>
视频文件可以使用七牛云的外链，也可以本地上传，可以在play.html文件中修改(文件这有注释说明）<br>
后台：http://127.0.0.1:8000/admin  用户名：sky  密码：1234mdzz
