---
layout: post
title: "java学习笔记187-200 内部类、Math，System，冒泡排序，Arrays"
date: 2021-11-03 09:51:33
blurb: "根据B站学习的Java学习笔记，从第187集到第200集"
og_image: /assets/img/content/post-example/Banner.jpg
---
# 前言
b站java课程学习笔记整理。

b站视频: [黑马程序员全套Java教程_Java基础入门视频教程，零基础小白自学Java必备教程]( https://www.bilibili.com/video/BV18J411W7cE?p=9)

# 187.类名/抽象类名作为形参和返回值

## 187.1 类名作为形参和返回值

* 方法的形参是类名，其实需要的是该类的对象。
* 方法的返回值是类名，其实返回的是该类的对象。

## 187.2 抽象类名作为形参和返回值

* 方法的形参是抽象类名，其实需要的是该抽象类的子类对象。
* 方法的返回值是抽象类名，其实返回的是该抽象类的子类对象。

# 188.接口名作为形参和返回值
* 方法的形参是接口名，其实需要的是该接口的实现类对象。
* 方法的返回值是接口名，其实返回的是该接口的实现类对象。

# 189.内部类
在类A中定义一个类B，那这个类B就称之为内部类。
定义格式：
```java
/*
public class 类名{
    修饰符 class 类名{
    }
}
*/

public class Outer{
    public class Inter{
    }
}
```
内部类的访问特点：

* 内部类可以直接访问外部类的成员，包括私有。
* 外部类要想访问内部类，必须创建对象。

```java
package 内部类;

public class Outer {
    private int num = 10;
    public class Inner{
        // 内部类访问外部类成员
        public void show(){
            System.out.println(num);
        }
    }


    public void method(){
        // 这样不行
        // show();

        Inner i = new Inner();
        i.show();
    }
}

```
# 190.成员内部类

按照内部类在类中的定义的位置不同，可以分为如下的两种形式
* 在类的成员位置：成员内部类
* 在类的局部位置，局部内部类

成员内部类，外界如何创建使用呢？
* 格式:`外部类名.内部类名 对象名= new 外部类对象.内部类对象`
* 例子：`Outer.Inner oi = new Outer().new Inner();`

```java
package 成员内部类;

public class Outer {
    private int num = 10;

    /*    public class Inner{
            public void show(){
                System.out.println(num);
            }
        }*/
    private class Inner {
        public void show() {
            System.out.println(num);
        }
    }

    public void method(){
        Inner i = new Inner();
        i.show();
    }
}

```

```java
package 成员内部类;

public class InnerDemo {
    public static void main(String[] args) {
        // 这样写不行
        // Inner i = new Inner();

        // 当内部类为public，但是不常用
/*        Outer.Inner oi = new Outer().new Inner();
        oi.show();*/

        // 当内部类为private时，需要在外部类编写一个方法，创建对象，调用内部类的方法，然后再测试类调用外部类中的调用方法。
        Outer o = new Outer();
        o.method();
    }
}

```

# 191.局部内部类

局部内部类外界也无法访问，需要外部类创建对象调用。

```java
package 局部内部类;

public class Outer {
    private int num = 10;


    public void method(){
        int num2 = 20;
        class Inner{
            public void show(){
                System.out.println(num);
                System.out.println(num2);
            }
        }

        Inner i = new Inner();
        i.show();
    }
}

```

```java
package 局部内部类;

public class InnerTest {
    public static void main(String[] args) {
        Outer o = new Outer();
        o.method();
    }


}

```

# 192.匿名内部类
匿名内部类是**局部内部类**的特殊形式。

前提: 存在一个类（可以是具体类也可以是抽象类）。

格式：

```java
/*
new 类名或者接口名(){
    重写方法;
}
*/

new Inner(){
    public void show(){
    }
}
```

本质：继承了该类或实现了该接口的一个子类匿名对象。
```java
package 匿名内部类;

public interface Inter {
    void eat();
}

```

```java
package 匿名内部类;

public class Outer {
    private int num = 10;

    public void method(){
        /*new Inter(){
            @Override
            public void eat() {
                System.out.println("重写吃饭方法");
            }
        }.eat();*/


        Inter i = new Inter(){
            @Override
            public void eat() {
                System.out.println("重写吃饭方法");
            }
        };
        i.eat();
    }
}

```

```java
package 匿名内部类;

public class OuterDemo {
    public static void main(String[] args) {
        Outer o = new Outer();
        o.method();
    }
}

```

# 193.匿名内部类在开发中的使用

每次实现一个接口都要重新创建一个新的实现类，然后再`main`方法中用多态的方法创建一个新对象，再实现接口功能。太麻烦了。

这种情况下可以使用匿名内部类。
```java
package 匿名内部类实现;

public class Cat  implements Jumpping{
    @Override
    public void jump() {
        System.out.println("猫可以跳高了");
    }
}

```

```java
package 匿名内部类实现;

public class JumpingOperator {
    public void operate(Jumpping j ){
        j.jump();
    }
}

```

```java
package 匿名内部类实现;

public interface Jumpping {
    void jump();
}

```

```java
package 匿名内部类实现;

public class JumppingDemo {
    public static void main(String[] args) {
        // 之前学过的接口的构造方法
        JumpingOperator jo = new JumpingOperator();
        Jumpping c = new Cat();
        jo.operate(c);

        // 如果有很多个动物，就要创建很多个类，太麻烦了。这时可以使用匿名内部类
        // 匿名内部类本质是继承了该类或实现了该接口的一个子类匿名对象。

        JumpingOperator jo1 = new JumpingOperator();
        jo1.operate(new Jumpping() {
            @Override
            public void jump() {
                System.out.println("狗可以跳高了");
            }
        });

        jo1.operate( new Jumpping() {
            @Override
            public void jump() {
                System.out.println("猪可以跳高了");
            }
        });
        // 匿名内部类的多次调用
        Jumpping n = new Jumpping() {
            @Override
            public void jump() {
                System.out.println("袋鼠可以多次跳高了");
            }
        };
        jo1.operate(n);
        jo1.operate(n);
        jo1.operate(n);



    }
}

```
# 194.MATH
`Math`包含执行基本数字类型的方法。它没有构造方法，但是类的成员都是静态的。因此可以直接通过类名调用。

|`Math`类的常用方法|说明|
|:---:|:---:|
|`public static int abs(int a)`|返回参数的绝对值|
|`public static double ceil(double a)`|返回大于或等于参数的最小整数值，类型为`double`|
|`public static double floor(double a)`|返回小于或等于参数的最小整数值，类型为`double`|
|`public static int round(float a )`|返回四舍五入下的最接近参数的int|
|`public static int max(int a, int b)`|返回两个参数中的较大值|
|`public static int min(int a, int b)`|返回两个参数中的较小值|
|`public static double pow(double a, double b)`|返回a的b次幂的值|
|`public static double random()`|返回值为`double`的正值，范围是[0.0,1.0)|

示例代码:
```java
package Math常用方法;

public class MathTest {
    public static void main(String[] args) {
        System.out.println(Math.abs(-88));
        System.out.println();

        System.out.println(Math.ceil(12.22));
        System.out.println();

        System.out.println(Math.floor(12.22));
        System.out.println();

        System.out.println(Math.round(12.49));
        System.out.println();

        System.out.println(Math.max(2,1));
        System.out.println();

        System.out.println(Math.min(3,4));
        System.out.println();

        System.out.println(Math.pow(2.0,3.0));
        System.out.println();

        System.out.println(Math.random());
    }
}

```
# 195.System
`System`类的成员都是静态的。因此可以直接通过类名调用。

|`System`类的常用方法|说明|
|:---:|:---:|
|`public static void exit (int status)`|中止当前的java虚拟机。非零表示中止异常|
|`public static long currentTimeMillis()`|返回当前时间，以毫秒为单位|

```java
package System常用方法;

public class SystemTest {
    public static void main(String[] args) {
        System.out.println("开始");
        long start = System.currentTimeMillis();


        for (int i = 0; i < 10000; i++) {
            System.out.println(i);
        }


//        System.exit(0);
        System.out.println("结束");
        long end = System.currentTimeMillis();

        System.out.println("共耗时" + (end - start) + "毫秒");
        System.exit(0);
    }
}

```

注意定义为`long`的数据形式。

# 196.Object类的toString()方法

`Object`是类层次结构的根，每个类都可以将`Object`类当作父类。所有的类都间接的或者直接的继承该类。

构造方法`public Object()`

所以说子类的默认构造方法默认访问的是父类的无参构造方法。

toString方法的作用是将内容简明扼要的以字符串表达出来。但是`Object`类中的不太好看。自己写类的时候最好用`Alt+Insert`生成一个重写的`toString`方法。

# 197.Object类的equals()方法
比较两个字符串的内容是否相同。之前用过了。不说了。

注意`equals`在像之前那样比较字符串的时候才正常工作，但是如果用来比较两个对象，比较的是地址值！

如果一定要用`equals`比较两个对象，需要重写方法。用`Alt+Insert `选择默认的Idea模板，生成完把哈希code删掉就行了。

用法就是`s1.equals(s2);`

示例代码：

```java
package equals方法;

public class Student {
    private String name;
    private int age;

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
        this.name = name;
        this.age = age;
    }

    public Student(){}

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Student student = (Student) o;

        if (age != student.age) return false;
        return name != null ? name.equals(student.name) : student.name == null;
    }


}

```

```java
package equals方法;

public class StudentTest {


    public static void main(String[] args) {
        Student s1 = new Student();
        s1.setAge(20);
        s1.setName("Jiangeng Sun");

        Student s2 = new Student();
        s2.setAge(20);
        s2.setName("Jiangeng Sun");

        System.out.println(s1.equals(s2));
    }
}

```

`Object`方法总结：

|方法|说明|
|:---:|:---:|
|`toString()`|返回字符串的表现形式，建议重写，自动生成|
|`equals()`|比较对象是否相等。默认比较地址值。重写可以比较内容，自动生成|


# 198-199. 冒泡排序原理与代码实现

排序：将一组数据按照固定的规则进行排序。

冒泡排序：数据两两比对，大的放后面。如果有n个数据比较，那么就需要比较n-1次。

```java
package 冒泡排序;

public class MaoPao {
    public static void main(String[] args) {
        int[] arr = {13, 15, 61, 16, 41, 1};
        System.out.println("排序前的数组为" + joint(arr));


        for (int j = 0; j < arr.length-1; j++ ){
            int tempValue;
            for (int i = 0; i < arr.length - j - 1; i++) {
                if (arr[i] > arr[i + 1]) {
                    tempValue = arr[i];
                    arr[i] = arr[i + 1];
                    arr[i + 1] = tempValue;
                }
            }

        }


        System.out.println("排序后的数组为"+joint(arr));


    }

    // 用来显示数组的方法
    public static String joint(int[] arr) {
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

# 200. Arrays

有用于操作数组的各种方法。

|方法名|说明|
|:---:|:---:|
|`toString(int[] a )`|返回指定数组的内容的字符串表示形式|
|`sort(int[] a )`|按照数字的顺序排列指定的数组|

```java
package Arrays;

import java.util.Arrays;

public class ArraysMethod {
    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 3, 6};
        System.out.println("排序前"+ Arrays.toString(arr));

        Arrays.sort(arr);

        System.out.println("排序后"+ Arrays.toString(arr));
    }
}

```

需要注意的是，这个是`Arrays.toString`,返回的是数组中的值，和`Object.toString`（返回的是默认的简明扼要的说明）是不一样的！

工具类的设计思想：
* 构造方法用`private`修饰。（这样外面就创建不了对象）
* 成员用`public static`修饰。（为了让用户使用类名来访问成员方法）

