---
layout: post
title: "java学习笔记01-09 java和notepad的安装，hello world案例"
date: 2021-10-26 16:08:13
blurb: "根据B站学习的Java学习笔记，从第1集到第9集"
og_image: /assets/img/content/post-example/Banner.jpg
toc: true  
---
## 前言
b站java课程学习笔记整理。

b站视频: [黑马程序员全套Java教程_Java基础入门视频教程，零基础小白自学Java必备教程]( https://www.bilibili.com/video/BV18J411W7cE?p=9)

## 1. Java语言发展史
没啥用，不记了
## 2. Java语言跨平台原理
Java通过JVM而适应不同的操作系统
## 3. JRE和JDK
### 3.1 JRE
JRE（*Java Runtime Environment*）是Java程序的运行时环境，包含JVM和运行时所需要的核心类库。JRE可以实现跨平台。可以实现Java运行。
### 3.2 JDK（最重要的）
是Java程序开发工具包，包含JRE和开发人员使用工具。（JDK是最牛b的）
## 4. JDK的下载和安装
略
## 5. 常用DOS命令
| 命令 | 作用 |
|:---:|:---:|
| e: | 进入E盘 | 
| dir | 查看当前文件夹 | 
| cd | 进入 | 
| cd ..| 回退 |
| cd \ | 回退到根目录 |
| cls | 清屏 |
| exit | 退出 |
| 写个首字母，按Tab | 命令自动补齐 |
## 6. path环境变量配置
流程: 改<code>JAVA_HOME</code> 改成JDK地址。
![配置成功](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/java环境变量配置.JPG)

## 7. Hello world 案例
代码需要经过“**书写-编译-运行**”三个步骤。
### 7.1 新建文本文档
文本文档命名为<code>HelloWorld.java</code>
### 7.2 写程序
用记事本打开该文档，输入代码<br>
```java
public class HelloWorld {
    public static void main(String[] args){
        System. out. println("HelloWorld);
    }
}
```
### 7.3 编译和运行
#### 7.3.1 编译
<code>javac 文件名.java</code>

#### 7.3.2 运行
<code>java 类名</code>
### 7.4 实战
遇到的坑:`txt`改不了`.java`后缀。

解决办法: 查看-文件拓展名-勾选
结果：
![Hello world!](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/helloworld案例.JPG)

## 8. HelloWorld案例常见问题
| bug | 什么原因 |
|:---:|:---:|
| 非法字符 | 有中文符号 |
| xxx不存在 | xxx拼写错误了 |
## 9. Notepad软件的安装与使用
没啥要记的，就是个简易IDE，比txt好点，编译不了也运行不了。









