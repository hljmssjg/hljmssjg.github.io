---
layout: post
title: "java学习笔记 150-168 继承，权限修饰符，final，static"
date: 2021-10-31 09:29:37
blurb: "根据B站学习的Java学习笔记，从第150集到第168集"
og_image: /assets/img/content/post-example/Banner.jpg
toc: true  
---
## 前言
b站java课程学习笔记整理。

b站视频:[黑马程序员全套Java教程_Java基础入门视频教程，零基础小白自学Java必备教程]( https://www.bilibili.com/video/BV18J411W7cE?p=9)
## 150. 继承

主要目的是避免代码重复，可以把两个类相同的地方归纳到一起。
![避免代码重复](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/继承.JPG)

定义： `public class 子类名 extends 父类名` 

父类也被称为基类和超类。子类也被称为派生类。

```java
package 继承;

public class Fu {
    public void show(){
        System.out.println("Show方法被调用。");
    }
}
```

```java
package 继承;

public class Zi extends Fu {
    public void method(){
        System.out.println("method 方法被调用");
    }
}

```

```java
package 继承;

public class test {
    public static void main(String[] args) {
        Fu f = new Fu();
        f.show();
        Zi z = new Zi();
        z.method();
        z.show();
    }
}

```
子类可以继承得到父类的内容，子类还可以有自己的内容。

## 151. 继承的好处和弊端

好处：

* 提高代码复用性。 
* 提高了代码的维护性。（修改一个类即可。）

弊端:
* 削弱了子类的独立性。

使用继承的原则：
* 如果类A是类B的一种，那么就可以考虑使用继承。例子：苹果和水果。

## 152. 继承中变量的访问特点

* 子类中没有的成员变量，如果父类中有，测试类和子类中依然可以访问这个变量。

* 如果子类中有的成员变量，父类中也有，那么优先使用子类。

* 如果方法内部有一个成员变量，优先使用方法内部的。

总结：子类方法内部>子类成员范围>父类成员范围>报错.
## 153. Super

在子类方法中访问本类的成员变量`age`用`this.age`。在子类方法中访问父类的成员变量`age`用`super.age`。

|关键字| this | super |
|:---:|:---:|:---:|
|访问成员变量|`this.成员变量`（访问本类成员变量）|`super.成员变量`（访问父类成员变量）|
|访问构造方法|`this(...)`访问本类构造方法|`super(...)`访问父类构造方法|
|访问成员方法|`this.成员方法(...)`访问本类成员方法|`super.成员方法(...)`访问父类成员方法|

## 154. 继承中构造方法的访问特点

* 子类中的所有的构造方法默认都会访问父类中的无参构造方法。因为子类初始化前要完成父类的初始化。

* 每一个子类的构造方法的第一条语句默认都是`super()`。所以默认访问父类的无参构造方法。

* 在父类无参构造方法缺失的情况下，可以在子类中使用`super(参数)`，调用父类的带参构造方法。或者在父类中手动给出一个无参构造方法。

## 155. 继承中成员方法的访问特点
通过子类对象调方法，先看子类中有没有，有使用子的，没有访问父类的。再没有就报错了。如果想访问父类的，使用`super`。

## 156. super的内存图
![super内存图](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/super内存图.JPG)
![super内存图](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/super内存图b.JPG)
![super内存图](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/super内存图c.JPG)

## 157. 方法重写

子类中出现了和父类一模一样的方法声明。

### 157.1 应用场景
当子类需要父类的功能，而功能主体子类有自己特有的内容时，可以重写父类的方法。这样即沿袭了父类的功能，又有子类特有的内容。

练习:手机类和新手机类。

`@override` 用来检查写子类方法时候方法声明的正确性。
```java
package 方法重写;

public class Phone {
    public void call(String name) {
        System.out.println("给" + name + "打电话");
    }
}

```

```java
package 方法重写;

public class NewPhone extends Phone{
    @Override
    public void call(String name){
        System.out.println("开启视频功能");
        super.call(name);
    }
}

```

```java
package 方法重写;

public class test {
    public static void main(String[] args) {
        NewPhone np = new NewPhone();
        np.call("Jiangeng");
    }
}

```

方法重写与方法重载：二者都是方法名相同，但方法重载是在一个类里面，一般用于标准类构造方法的制作。方法重写是用于父与子类里。
## 158. 方法重写的注意事项
* 父类中的私有内容（`private`修饰），子类无法重写。

* 子类重写方法时，访问权限**不能比父类低**。

## 159. 继承的注意事项
java中类只能继承**一个**类。 但是可以使用多层继承。（继承嵌套）
## 160. 老师和学生

* 需求:使用继承写出老师类和学生类。

* 老师：姓名，年龄，教学方法。

* 学生：姓名，年龄，学习方法。

* 思路:定义一个`person`类，拥有姓名年龄作为父类。

```java
package 老师与学生.继承版;

public class Person {
    private String name;
    private String age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public Person(){};

    public Person(String name,String age){
        this.age = age;
        this.name = name;
    };



}

```
```java
package 老师与学生.继承版;

public class Teacher extends Person{
    public void teach(){
        System.out.println("上课");
    }
}

```

```java
package 老师与学生.继承版;

public class Student extends Person{
    public Student(String name,String age){
        super(name,age);
    }

    public void study(){
        System.out.println("学习");
    }
}

```

```java
package 老师与学生.继承版;

public class test {
    public static void main(String[] args) {
        Teacher t1 = new Teacher();
        t1.setAge("20");
        t1.setName("Jiangeng");
        System.out.println(t1.getName() + "," + t1.getAge());
        t1.teach();

        Student s1 = new Student("Jiangeng", "21");
        System.out.println(s1.getName() + "," + s1.getAge());
        s1.study();
    }
}

```
## 161. 猫和狗

使用继承实现猫和狗的类及其测试。

* 动物类:姓名年龄，无参带参，getset。
* 猫：无参带参，抓老鼠。
* 狗：无参带参，看大门。

```java
package 猫与狗;

public class Animal {
    private String name;
    private String age;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getAge() {
        return age;
    }

    public void setAge(String age) {
        this.age = age;
    }

    public Animal(){};

    public Animal(String name, String age){
        this.age = age;
        this.name = name;
    };
}

```

```java
package 猫与狗;

public class Cat extends Animal {
    public Cat(){
        super();
    }

    public Cat(String name, String age){
        super(name,age);
    }

    public void catchMouse(){
        System.out.println("猫可以抓老鼠");
    }
}

```

```java
package 猫与狗;

public class Dog extends Animal{
    public Dog() {
        super();
    }

    public Dog(String name, String age) {
        super(name, age);
    }

    public void security(){
        System.out.println("狗可以看门");
    }
}

```

```java
package 猫与狗;

public class test {
    public static void main(String[] args) {
        Cat kitty = new Cat();
        kitty.setAge("21");
        kitty.setName("Kitty Marcus");
        System.out.println(kitty.getAge()+","+kitty.getName());
        kitty.catchMouse();

        Dog lucas = new Dog("Lucas Andersson","20");
        System.out.println(lucas.getAge()+","+lucas.getName());
        lucas.security();

    }
}

```
## 162. package

包其实就是文件夹。不同包下的class文件可以实现同名，方便分类管理。多级包之间用"."分开。

Dos小技巧：` javac -d . "xxxxx.java"`  在当前目录下建包。

## 163. import
![import的作用](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/import的作用.JPG)

`import`就是省略了class文件前的包（文件夹名字）。

## 164. 权限修饰符

|权限修饰符| 同一个类中 | 同一个包中子类无关类 | 不同的包中的子类 | 不同的包中的无关类 |
|:---:|:---:|:---:|:---:|:---:|
| `private`  | * |   |   |   |
| 默认       | * | * |   |   |
| `protected`| * | * | * |   |
| `public`   | * | * | * | * |

## 165. final
`final`可以修饰成员方法，成员变量和类。

* `final`修饰的方法叫最终方法，不可以被重写。但是如果是父类的最终方法被子类继承，还是可以通过子类调用。

* 被`final`修饰的成员变量不可以被赋值了。

* 类如果被`final`修饰，不可以被子类继承了。

* 总结: `final`意思就是不让修改了。是一个恒定的，不可改变的东西。
## 166. final修饰局部变量
`final Student s = new Student();`

这里`final`修饰的是s的地址值，也就是s的地址不可更改。而如果重新赋值 `s.age = 100;` 是可以的。因为这和地址无关。

## 167. static
静态的意思，可以修饰成员方法和成员变量。

如果一个成员变量的值对于所有的对象都是一样的，可以用static修饰。

可以通过类名 例：`Student.university`来修改。
## 168. static的访问特点

非静态的成员方法:

* 可以访问静态、非静态的成员变量和成员方法。

静态的成员方法：

* 可以访问静态成员变量和方法。

所以之前访问`main`方法中的变量时要用`static`修饰，因为`main`方法是`static`修饰的方法。

