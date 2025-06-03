---
layout: post
title: "java学习笔记99-133： 标准类的制作，String和StringBuilder"
date: 2021-10-28 18:56:27
blurb: "根据B站学习的Java学习笔记，从第99集到第133集"
og_image: https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/cat.jpg
---
# 前言
b站java课程学习笔记整理。

b站视频: [黑马程序员全套Java教程_Java基础入门视频教程，零基础小白自学Java必备教程]( https://www.bilibili.com/video/BV18J411W7cE?p=9)


#  99. 类和对象

没有对象就`new`一个！

| 对象 | 类 | 属性 | 行为 |
|:---:|:---:|:---:|:---:|
|一个**具体的**东西| 有相同的**属性**和**行为**的**对象**的集合 |对象的特征，每个属性都有特定的值|对象能干什么|
| 我的手机 | 手机类 |手机的价格是229元 | 可以打电话 |

#  100. 类的定义
类是java的基本组成单位。类的组成：属性和行为。
1. 属性:在类中通过**成员变量**来体现（类中方法外的变量）。
2. 行为:在类中通过**成员方法**来体现（和前面的方法相比**去掉`static`**关键字即可）。

定义:
![类的定义](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/类的定义.JPG)
#  101. 对象的使用
对象的使用：
![对象的使用](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/对象的使用.JPG)

#  102. 学生

首先定义一个学生类，然后在学生测试类中定义一个对象（具体的学生），在学生类中完成成员变量和方法的使用。

1. 成员变量：姓名，年龄。
2. 成员方法： 学习，做作业。
```java
package 学生;

public class Student {
    String name;
    int age;

    public void doHomework(){
        System.out.println("他可以做作业");
    }
    public void goToSchool(){
        System.out.println("他上学去");
    }
}
 
```
```java
package 学生;

public class StudentTest {
    public static void main(String[] args) {
        Student x = new Student();
        x.age = 24;
        System.out.println("年龄为" + x.age);
        x.name = "Jiangeng";
        System.out.println("名字为" + x.name);

        x.doHomework();
        x.goToSchool();
    }
}
```
不难解释之前的`Scanner`用法了！
* `import java.util.Scanner; `意思就是导入`java`下`util`下`Scanner`类，因为要用到这个包里的`class`。
* `Scanner sc = new Scanner(System.in);` 创建一个`sc`对象，`sc`对象属于`Scanner`这个类。
* `int input = sc.nextInt(); `调用了`sc`的成员方法。

注意，如果在使用成员变量时不赋值，输出的是默认值。`string`是`null`，数值类是`0`；

#  103. 单个对象的内存图
![单个对象的内存图](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/单个对象的地址.JPG)
总结:` new`的使用使用堆内存储存，对象代表的是堆内存的地址。

![单个对象的方法调用](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/单个对象的method.JPG)
#  104. 多个对象的内存图
![多个对象的内存图1](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/多个对象内存图1.JPG)
![多个对象的内存图2](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/多个对象的输出2.JPG)
#  105. 多个对象指向相同内存图
![多个对象的指向相同](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/多个指向相同.JPG)
和数组那个例子一样。
#  106. 成员变量和局部变量的区别
![成员变量和局部变量](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/成员变量和局部变量.JPG)

比较:


| 区别 | 成员变量 | 局部变量 |
|:---:|:---:|:---:|
| 类中位置不同 | 类中方法外 | 方法内或者方法声明上 |
| 内存中位置不同 | 堆内存 | 栈内存 |
| 生命周期不同 | 随着对象的存在而存在 | 随着方法的存在而存在 |
| 初始化值 | 可以有系统给的默认的 | 没有默认的 |


#  107-108. private
可以修饰成员变量和成员方法。作用是保护成员不被别的类使用，被`private`修饰只能在本类使用。

如果想被别的类使用，可以:
1. 提供`get变量名()`方法，用于获取成员变量的值，用`public`修饰。
2. 提供`set变量名()`方法，用于设置成员变量的值，用`public`修饰。

#  109. this
解决**名字相同**时，局部变量无法赋值给成员变量的问题。 this被哪个方法调用，指定的就是哪个对象。（对象.xxx不就是成员变量的读取么！）

#  110. this内存原理
![this的堆栈内存原理](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/使用This的堆栈.JPG)

核心思想就是`This`是指调用方法的对象。

`This`用法实例：

```java
package 学生;

public class Student {

    private int age;

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }


}

```
```java
package 学生;

public class StudentTest {
    public static void main(String[] args) {
        Student x = new Student();
        x.setAge(23);
        System.out.println("年龄为" + x.getAge());



    }
}

```
# 111. 封装
封装是面向对象的三大对象之一（封装，继承，多态）。 封装原则：使用`private`修饰，然后使用`get`、`set`方法。

封装的好处：提高了代码的安全性和复用性。
# 112. 构造方法
构造方法本质上是对调用这个类创建一个对象进行了条件约束（必须满足什么样的条件才能创建对象）。
![构造方法](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/构造方法.JPG)
# 113. 构造方法的注意事项
当一个类中没有写构造方法，系统会给一个无参的构造方法。如果已经定义了有参构造，系统就不会再提供无参的构造了。
```java
package 学生;

public class Student {

    private int age;

    private String name;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Student(String name, int age) {
        System.out.println("使用带参方法定义");
        this.name = name;
        this.age = age;
    }

    public Student() {
        System.out.println("使用无参方法定义");
    }

    public void getInfo() {
        System.out.println("学生名为" + name);
        System.out.println("学生年龄为" + age);
    }

}

```

```java
package 学生;

public class StudentTest {
    public static void main(String[] args) {
        Student x = new Student();
        x.setAge(23);
        x.setName("Jiangeng");
        x.getInfo();

        Student y = new Student("Jiangeng", 23);
        y.getInfo();


    }
}

```

总结：对象的构造方法本质上也是一种成员方法，书写的格式和书写成员方法的相同，只不过构造方法的方法名要和类名一致。本质上也是一种重载。
在自己写代码时建议手动给出无参方法构建。
# 114. 标准类的制作
![标准类的制作](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/标准类的制作.JPG)
# 115. API
API应用程序编程接口：厂商提供给应用程序编程的接口，把这些类称为api。Java API指的是 Java JDK中提供各种功能的Java类。

之前用的nextInt()就是使用了API。
# 116. API练习-帮助文档
根据帮助文档学习`Scanner`使用。

文档地址：[点这里]( https://docs.oracle.com/en/java/javase/17/)

`sc.nextLine();` 按下`Ctrl Alt V `自动生成对象。

# 117. String
![字符串概述](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/字符串概述.JPG)
# 118. String构造方法
```java
package 字符串构建;

public class StringDemo {
    public static void main(String[] args) {
        // 创建一个空白字符串内容
        String s1 = new String();
        System.out.println("s1:" + s1);

        //根据字符数字内容创建对象
        char[] chs = {'a', 'b', 'c'};
        String s2 = new String(chs);
        System.out.println("s2:" + s2);

        //根据字节数组内容创建对象
        // 97 98 99 是ASCII 码
        byte[] byts = {97, 98, 99};
        String s3 = new String(byts);
        System.out.println("s3:" + s3);

        //直接赋值
        String s4 = "abc";
        System.out.println("s4:" + s4);
    }


}

```
# 119. String对象的特点
![String对象的特点](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/String对象的特点.JPG)

总结：`new`的会新建一个地址值，直接赋值相同字符串的话只会指向之前生成好的地址值。
# 120. 字符串的比较

直接`==`比较的是地址值是否相同。比较内容是否相同用`equals()`

```java
package 字符串的比较;

public class StringCompare {
    public static void main(String[] args) {
        char[] chr = {'a','b','c'};
        String s1 = new String(chr);
        String s2 = new String(chr);

        String s3 = "abc";
        String s4 = "abc";

        // 地址是否相等
        System.out.println(s1==s2);
        System.out.println(s1==s3);
        System.out.println(s3==s4);

        System.out.println();

        // 内容是否相等
        System.out.println(s1.equals(s2));
        System.out.println(s1.equals(s3));
        System.out.println(s3.equals(s4));
    }
}
```

# 121. 用户登录

需求:已知用户名和密码，用程序实现登录。一共三次机会，登陆成功后给出提示。

```java
package 登陆系统;

import java.util.Scanner;

public class LogIn {
    private String account = "zhanghu";
    private String password = "mima";
    Scanner sc = new Scanner(System.in);


    public void login() {
        for (int i = 0; i < 3; i++) {
            System.out.println("请输入账号");
            String account = sc.nextLine();
            System.out.println("请输入密码");
            String password = sc.nextLine();
            if (account.equals(this.account) && password.equals(this.password)) {
                System.out.println("登陆成功！");
                break;
            } else {
                if (i == 2) {
                    System.out.println("登陆失败，你的账号已经被锁定！");
                    break;
                }
                System.out.println("账号密码错误！你还有" + (3 - i - 1) + "次机会！");
            }
        }


    }


}

```
```java
package 登陆系统;

public class LoglInTest {
    public static void main(String[] args) {
        LogIn demo = new LogIn();
        demo.login();
    }
}

```

# 122. 遍历字符串

要求: 程序输入一个字符串，在控制台遍历

学到的命令：`line.charAt()`获取字符串中的某一个字符。

```java
package 遍历字符串;

import java.util.Scanner;

public class bianlistring {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入字符串！");
        String input = sc.nextLine();
        for (int i = 0; i < input.length(); i++){
            System.out.print(input.charAt(i));
        }
    }
}
```

# 123. 案例：统计字符次数
需求：键盘录入一个字符串，统计该字符串中大写字母字符，小写字母字符，数字字符出现的次数。

注意：既然 `==` 直接比较的是ASCII值，那么`<= `也是可以直接比较地址值！

```java
package 统计字符串;

import java.util.Scanner;

public class CalculateChar {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("请输入字符串！");
        String input = sc.nextLine();
        int countCapital = 0;
        int countLetter = 0;
        int countNum = 0;
        int countNone = 0;
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) >= 'A' && input.charAt(i) <= 'Z') {
                countCapital++;
            } else if (input.charAt(i) >= 'a' && input.charAt(i) <= 'z') {
                countLetter++;
            } else if (input.charAt(i) >= '0' && input.charAt(i) <= '9') {
                countNum++;
            } else{
                countNone++;
            }
        }
        System.out.println("大写字母的个数是"+countCapital+",小写字母的个数是"+countLetter+",数字的个数是"+countNum+",无法识别的字符个数是"+countNone);
    }
}

```

# 124. 案例：拼接字符串
需求:定义一个方法，把int数组中的数据按照指定的格式拼接成一个字符串返回。

```java
package 字符串拼接;

public class StringTogether {
    public String joint(int[] arr) {
        String temp = "[";
        for (int i = 0; i < arr.length; i++) {
            temp += arr[i];
            if (i != arr.length - 1) {
                temp += ",";
            } else {
                temp += "]";
            }
        }
        return temp;
    }
}

```

```java
package 字符串拼接;


public class JointTest {

    public static void main(String[] args) {
        int[] inputArr = {1, 2, 3};

        StringTogether test = new StringTogether();
        System.out.println(test.joint(inputArr));
    }
}

```

注意： 字符串直接加数组中的`int` 数值，是可以的。本质上和`sout("字符" + 数字)`可以正常输出是一个道理。数字被自动转换为字符了。
# 125. 案例：字符串反转
键盘录用一个字符串，调用该方法，实现字符串反转。
```java
package 字符串反转;

public class StringConvert {
    public String convert(String line) {
        String temp = "";
        for (int i = line.length()-1; i >= 0 ; i--){
            temp += line.charAt(i);
        }
        return temp;
    }
}
```
```java
package 字符串反转;
import java.util.Scanner;
public class ConvertTest {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        StringConvert test = new StringConvert();
        System.out.println(test.convert(input));
    }
}

```
# 126. 帮助文档查看String方法
`String replace(char oldChar, char newChar)`
用新字符`newChar `替换所有的 旧字符`oldChar` 。

`String replace(CharSequence target, CharSequence replacement)`
用新字符串`replacement`替换所有的 旧字符串`target`。

`String replaceAll(String regex, String replacement)`
用新字符串`replacement `替换所有的 正则模式匹配的串。——（替换的是模糊字串）

`String replaceFirst(String regex, String replacement)`
用新字符串`replacement `替换第一个 正则模式匹配的串。——（替换的是模糊字串）

如果未找到，则返回原来的字符串。

# 127. StringBuilder
![普通的字符串拼接](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/普通的字符串拼接.JPG)

普通的字符串拼接耗时并且浪费堆内存空间。

`StringBuilder`可以解决这个问题。本质上是一个可变的字符串容器。

# 128. StringBuilder的构建方法

主要有两种构建方式：
```java
package StringBuilderDemo;

public class StringBuilderDemo {


    public static void main(String[] args) {
        // 无参构造
        StringBuilder sb = new StringBuilder();
        System.out.println("sb:"+sb);
        System.out.println("length:"+sb.length());

        // 带参构造
        StringBuilder sb2 = new StringBuilder("hello");
        System.out.println("sb2:"+sb2);
        System.out.println("length2:"+sb2.length());
    }
}

```

# 129. StringBuilder的添加和反转

```java
package StringBuilderDemo;

public class StringBuilderAddReverse {
    public static void main(String[] args) {
        StringBuilder sb = new StringBuilder();
        StringBuilder sb2 = sb.append("hello");

        System.out.println("sb:" + sb);
        System.out.println("sb2:" + sb2);
        System.out.println(sb == sb2); //说明sb2和sb是指的一个对象，sb2没有必要存在。

        // 一般用法
        StringBuilder sb3 = new StringBuilder();
        sb3.append("hello ");
        sb3.append("world");
        System.out.println(sb3);

        // 链式编程
        StringBuilder sb4 = new StringBuilder();
        sb4.append("hello ").append("world");
        System.out.println(sb4);

        // 反转
        sb4.reverse();
        System.out.println("reversed sb4 " + sb4);


    }
}

```
# 130. StringBuilder和String相互转换

`StringBuilder`里面有反转和添加方法很好用，所以将`String`转化为`StringBuilder`。

![String和StringBuilder的转换方法](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/StringBuilder转换方法.JPG)

代码：
```java
package StringBuilder的转换;

public class Converse {
    public static void main(String[] args) {
        // StringBuilder 转换为 String
        StringBuilder sb = new StringBuilder();
        sb.append("hello");

        String s = sb.toString();
        System.out.println(s);

        // String 转换为 StringBuilder
        String s1 = "hello";
        StringBuilder sb1 = new StringBuilder(s1); //本质上也是一种StringBuilder的构造方式。
        System.out.println(sb1);




    }
}

```
# 131. 拼接字符串：升级版
案例:使用`StringBuilder`把一个数组中的元素拼接成字符串。

```java
package 字符串的拼接升级版;

public class Joint {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4};
        System.out.println("输出的数组是" + joint(arr));
    }

    public static String joint(int[] arr) {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < arr.length; i++) {
            sb.append(arr[i]);
            if (i != arr.length - 1) {
                sb.append(",");
            }

        }
        sb.append("]");
        String line = sb.toString();
        return line;
    }
}
```
# 132. 反转字符串：升级版

键盘输入字符串，控制台输出反转。

```java
package StringBuilder反转;
import java.util.Scanner;
public class StringBuilderReverse {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        System.out.println("反转后的字符串是:"+reverse(input));
    }

    public static String reverse(String s){
        StringBuilder sb = new StringBuilder(s);
        sb.reverse();
        String backLine = sb.toString();
        return backLine;
        
        // 也可以用一行代码来实现
        // return new StringBuilder(s).reverse().toString();

    }

}

```
# 133. 帮助文档方法查看StringBuilder的用法
看帮助文档。
