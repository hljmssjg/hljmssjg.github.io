---
layout: post
title: "java学习笔记257-271 Map，Collections，斗地主"
date: 2021-11-07 15:50:53
blurb: "根据B站学习的Java学习笔记，从第257集到第271集"
og_image: /assets/img/content/post-example/Banner.jpg
toc: true  
---
## 前言
b站java课程学习笔记整理。

b站视频: [黑马程序员全套Java教程_Java基础入门视频教程，零基础小白自学Java必备教程]( https://www.bilibili.com/video/BV18J411W7cE?p=9)

## 257. Map集合概述和特点

`Map`集合概述:
`Interface Map<K,V> `     其中 K: 键的类型； V：值的类型。

将键映射到值的对象；不能包含重复的键；每个键可以映射到最多一个值。

创建`Map`对象使用多态的形式。

```java
package Map集合对象;

import java.util.HashMap;
import java.util.Map;

public class MapDemo {


    //添加

    public static void main(String[] args) {
        Map<String,String> map = new HashMap<String,String>();
        map.put("2016160061","孙健耕");
        map.put("jisu0012","Jiangeng Sun");
        map.put("2016160061","孙健森"); //当键重复的时候，值会替代。

        System.out.println(map);
    }


}

```

## 258. Map集合的基本功能

|方法名|说明|
|:---:|:---:|
|`V put(K key, V value)`|添加元素|
|`V remove(Object key)`|根据键删除键值对元素|
|`void clear()`|移除所有的键值对元素|
|`boolean containsKey(Object key)`|判断集合是否包含指定的键|
|`boolean containsValue(Object value)`|判断集合是否包含指定的值|
|`boolean isEmpty()`|判断集合是否为空|
|`int size()`|集合的长度，也就是集合中键值对的个数|

```java

package Map集合对象;

import java.util.HashMap;
import java.util.Map;

public class MapDemo {


    //添加

    public static void main(String[] args) {
        Map<String,String> map = new HashMap<String,String>();
        map.put("2016160061","孙健耕");
        map.put("jisu0012","Jiangeng Sun");
        map.put("2016160060","孙健森"); //当键重复的时候，值会替代。

        System.out.println(map.remove("jisu0012")+"，删除后的map为"+map);
        System.out.println(map.remove("jisu")+"，删除后的map为"+map);

        map.clear();
        System.out.println(map);

        map.put("2016160061","孙健耕");
        map.put("jisu0012","Jiangeng Sun");
        System.out.println(map.containsKey("jisu0012"));
        System.out.println(map.containsKey("2016160000"));

        System.out.println(map.containsValue("孙健耕"));
        System.out.println(map.containsValue("孙健森"));

        System.out.println(map.isEmpty());
        System.out.println(map.size());
        map.clear();
        System.out.println(map.isEmpty());
    }


}

```

## 259. Map集合的获取功能

|方法名|说明|
|:---:|:---:|
|`V get(Object key)`|根据键获取值|
|`Set<K> keySet()`|获取所有键的集合|
|`Collection<V> values()`|获取所有值的集合|
|`Set <Map.Entry<K,V>> entrySet()`|获取所有键值对对象的集合|

```java
package Map集合对象;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapDemo2 {
    public static void main(String[] args) {
        Map<String,String> map = new HashMap<String,String>();
        map.put("2016160061","孙健耕");
        map.put("jisu0012","Jiangeng Sun");

        System.out.println(map.get("2016160061"));
        System.out.println(map.get("dasda"));

        Set<String> keyset = map.keySet();

        for(String i: keyset){
            System.out.println(i);
        }

        Collection<String> mapvalue = map.values();
        for (String i: mapvalue){
            System.out.println(i);
        }
    }
}

```

## 260. Map集合的遍历（方式1）
遍历`key`。

```java
package Map集合对象;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapDemo2 {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();
        map.put("2016160061", "孙健耕");
        map.put("jisu0012", "Jiangeng Sun");


        Set<String> keyset = map.keySet();

        for (String key : keyset) {
            String value = map.get(key);
            System.out.println(key + "," + value);
        }


    }
}

```
## 261. Map集合的遍历（方式2）
通过`map`集合中所有键值对对象的集合。

`Set<Map.Entry<K,V>> entrySet()`: 获取所有键值对对象的集合。

```java
package Map集合对象;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class MapDemo2 {
    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();
        map.put("2016160061", "孙健耕");
        map.put("jisu0012", "Jiangeng Sun");


        Set<String> keyset = map.keySet();

        for (String key : keyset) {
            String value = map.get(key);
            System.out.println(key + "," + value);
        }

        System.out.println("----------------------------------");

        Set<Map.Entry<String,String>> entrySet= map.entrySet();
        for(Map.Entry<String,String> es: entrySet){
            String key = es.getKey();
            String value = es.getValue();
            System.out.println(key+","+value);
        }


    }
}

```

## 262. HashMap存储学生对象并遍历

```java
package hashmap存储学生对象;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class HashMapDemo {
    public static void main(String[] args) {
        Student s1 = new Student("孙健耕", 24);
        Student s2 = new Student("李安然", 23);
        Student s3 = new Student("李维瀚", 22);
        Student s4 = new Student("施霁桐", 21);

        Map<String, Student> studentMap = new HashMap<String, Student>();
        studentMap.put("2016160061", s1);
        studentMap.put("2016160062", s2);
        studentMap.put("2016160063", s3);
        studentMap.put("2016160064", s4);


        Set<String> s = studentMap.keySet();
        for (String num : s) {
            Student person = studentMap.get(num);
            System.out.println(num + "," + person);
        }
        System.out.println("---------------------------");

        Set<Map.Entry<String, Student>> entrySet = studentMap.entrySet();
        for (Map.Entry<String, Student> ME : entrySet) {
            String key = ME.getKey();
            Student student = ME.getValue();
            System.out.println(key + "," + student);
        }


    }
}

```
## 263. 键是Student，值是String

需求:创建一个`HashMap`集合，键是学生对象(`Student`)，值是居住地(`String`)。存储多个键值对元素，并遍历。要求保证键的唯一性。

```java
package hashmap存储学生对象键是学生;

public class Student {
    private String name;
    private int age;

    public Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public Student() {
    }

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

    @Override
    public String toString() {
        return "Student{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Student student = (Student) o;

        if (age != student.age) return false;
        return name != null ? name.equals(student.name) : student.name == null;
    }

    @Override
    public int hashCode() {
        int result = name != null ? name.hashCode() : 0;
        result = 31 * result + age;
        return result;
    }
}

```
```java
package hashmap存储学生对象键是学生;


import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class HashMapDemo {
    public static void main(String[] args) {
        Student s1 = new Student("孙健耕", 24);
        Student s2 = new Student("李安然", 23);
        Student s3 = new Student("李维瀚", 22);
        Student s4 = new Student("施霁桐", 21);

        String address1 = "Mingshui";
        String address2 = "Fengjing";
        String address3 = "Fengjing";
        String address4 = "Yujing";

        Map<Student,String> studentAddressMap = new HashMap<Student,String>();
        studentAddressMap.put(s1,address1);
        studentAddressMap.put(s2,address2);
        studentAddressMap.put(s3,address3);
        studentAddressMap.put(s4,address4);

        Student s5 = new Student("李维瀚", 22);
        String address5 = "Ningbo";
        studentAddressMap.put(s5,address5);


        Set<Student> studentSet =  studentAddressMap.keySet();

        for(Student s : studentSet){
            System.out.println(s + "," + studentAddressMap.get(s));
        }






    }
}

```


## 264. Arraylist嵌套HashMap
需求: 创建一个`ArrayList`集合，存储三个元素，每一个元素都是`HashMap`，每一个`HashMap`的键和值都是`String`，并遍历。

```java
package ArrayList存储Hashmap元素;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

public class AHDemo {
    public static void main(String[] args) {
        ArrayList<HashMap<String, String>> al = new ArrayList<>();

        HashMap<String, String> map1 = new HashMap<String, String>();
        map1.put("Map1中的一号", "孙健耕");
        map1.put("Map1中的二号", "李维瀚");
        map1.put("Map1中的三号", "李安然");
        map1.put("Map1中的四号", "施霁桐");

        HashMap<String, String> map2 = new HashMap<String, String>();
        map2.put("Map2中的一号", "孙健耕");
        map2.put("Map2中的二号", "薛雨霏");
        map2.put("Map2中的三号", "高璎榕");
        map2.put("Map2中的四号", "张林");

        HashMap<String, String> map3 = new HashMap<String, String>();
        map3.put("Map3中的一号", "孙健耕");
        map3.put("Map3中的二号", "陈天翔");
        map3.put("Map3中的三号", "陈展鸿");
        map3.put("Map3中的四号", "刘腾俊");

        HashMap<String, String> map4 = new HashMap<String, String>();
        map4.put("Map4中的一号", "孙健耕");
        map4.put("Map4中的二号", "文新源");
        map4.put("Map4中的三号", "黄祯");
        map4.put("Map4中的四号", "魏彬钰");

        al.add(map1);
        al.add(map2);
        al.add(map3);
        al.add(map4);


        for (HashMap<String, String> map : al) {
            Set<String> keyset = map.keySet();
            for (String key : keyset) {
                System.out.println(key + "," + map.get(key));

            }
        }


    }


}


```

注意:`HashMap`是`Map`的主要实现类，可以通过哈希值自定义去除重复元素。

## 265.HashMap嵌套Arraylist

需求:创建一个`HashMap`集合，存储三个键值对元素，每一个键值对元素的键是`String`，值是`ArrayList`，每一个`ArrayList`的元素是`String`，并遍历。

```java
package HashMap嵌套ArrayList;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

public class HashMapInArrayList {
    public static void main(String[] args) {
        ArrayList<String> al1 = new ArrayList<>();
        ArrayList<String> al2 = new ArrayList<>();
        ArrayList<String> al3 = new ArrayList<>();

        al1.add("al1.1");
        al1.add("al1.2");
        al1.add("al1.3");

        al2.add("al2.1");
        al2.add("al2.2");
        al2.add("al2.3");

        al3.add("al3.1");
        al3.add("al3.2");
        al3.add("al3.3");

        HashMap<String, ArrayList<String>> hm = new HashMap<>();

        hm.put("第一个数组", al1);
        hm.put("第二个数组", al2);
        hm.put("第三个数组", al3);

        Set<String> hmKeySet = hm.keySet();

        for (String num : hmKeySet) {
            for(String index : hm.get(num) ){
                System.out.println(num + index);
            }
        }
    }
}

```

## 266. 统计字符串中每个字符出现的次数

举例：键盘录入"aababcabcdabcde"， 输出"a(5)b(4)c(3)d(2)e(1)"。

```java
package 统计字符个数;

import java.util.HashMap;
import java.util.Scanner;
import java.util.Set;

public class Statistics {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        HashMap<String,Integer> hm = new HashMap<>();

        String[] strArr = input.split("");
        for (String s : strArr) {
            if(!hm.containsKey(s)){
                hm.put(s,1);
            }else{
                int newNum = hm.get(s)+1;
                hm.put(s,newNum);

            }
        }
        Set<String> strings = hm.keySet();
        for(String s : strings){
            System.out.print(s+"("+hm.get(s)+")");
        }


    }
}


```

个人觉得用`containsKey`来判断更好一点。最后不用调用`remove`方法去除旧的键值对，因为`HashMap`继承了`Map`，键不能重复，如果有重复的会自动更新。

## 267. Collections概述和使用

此类全部都由静态方法构成，为针对集合操作的工具类。注意和`Collection`区分（`Collection`是用来构造单列结合的）。

常用方法：

|方法|解释|
|:---:|:---:|
|`sort(List<T> list)`|将指定的列表按升序排序|
|`reverse(List<?> list)`|反转指定列表中的元素顺序|
|`shuffle(List<?> list)`|将指定的列表按随即顺序排序。常用来模拟洗牌。|

注意：之前学的那个`sort`，`reverse`是`Arrays`包下，针对数组的方法！这个是针对列表的，注意区分。

```java
package CollectionsDemo;

import java.util.ArrayList;
import java.util.Collections;

public class CollectionsDemo {
    public static void main(String[] args) {
        ArrayList<Integer> al = new ArrayList<>();

        al.add(10);
        al.add(20);
        al.add(30);
        al.add(40);
        al.add(50);
        System.out.println(al);

        Collections.reverse(al);
        System.out.println(al);

        Collections.sort(al);
        System.out.println(al);

        Collections.shuffle(al);
        System.out.println(al);
    }
}

```

## 268. ArrayList存储学生对象并排序

需求: 按照年龄大小排序，年龄相同时，按照姓名的字母顺序排序。 注意之前的排序案例中是用`TreeSet`做的！

和`TreeSet`类似，还是得用比较器或者继承`Comparable`这个类。

```java
package ArrayList存储学生对象并排序;

import java.text.Collator;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

public class test {
    public static void main(String[] args) {
        Student s1 = new Student("孙健耕", 24);
        Student s2 = new Student("李安然", 23);
        Student s3 = new Student("李维瀚", 22);
        Student s4 = new Student("施霁桐", 21);


        ArrayList<Student> al = new ArrayList<>();
        al.add(s1);
        al.add(s2);
        al.add(s3);
        al.add(s4);

        Collections.sort(al, new Comparator<Student>() {
            @Override
            public int compare(Student o1, Student o2) {
                int num = s1.getAge()-s2.getAge();
                int num2 = num==0? s1.getName().compareTo(s2.getName()):num;
                return num2;
            }
        });


        for (Student s:al){
            System.out.println(s);
        }
    }
}

```

## 269. 模拟斗地主

需求：通过程序实现斗地主过程中的洗牌，发牌和看牌。

思路:
1. 创建一个牌盒，也就是定义一个集合对象，用`ArrayList`集合实现。
2. 往牌盒里面装牌。
3. 洗牌，也就是把牌打散，用`shuffle()`实现。
4. 发牌，也就是遍历集合，给三个玩家发牌，
5. 看牌，也就是三个玩家分别遍历自己的牌。

```java
package 模拟斗地主;

import java.util.ArrayList;
import java.util.Collections;

public class DouDiZhu {
    public static void main(String[] args) {
        ArrayList<String> CardsBox = new ArrayList<>();
        String[] colors = {"♣", "♦", "♠", "♥"};
        String[] marks = {"2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"};
        String[] Jokers = {"小王", "大王"};

        for (String color : colors) {
            for (String mark : marks) {
                CardsBox.add(color + mark);
            }
        }
        CardsBox.add(Jokers[0]);
        CardsBox.add(Jokers[1]);

        Collections.shuffle(CardsBox);

        ArrayList<String> player1 = new ArrayList<>();
        ArrayList<String> player2 = new ArrayList<>();
        ArrayList<String> player3 = new ArrayList<>();
        ArrayList<String> HiddenCards = new ArrayList<>();
        for (int i = 0; i < 18; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 17) {
                    HiddenCards.add(CardsBox.get(i * 3 + j));
                    continue;
                }
                switch (j) {
                    case 0 -> player1.add(CardsBox.get(i * 3 + j));
                    case 1 -> player2.add(CardsBox.get(i * 3 + j));
                    case 2 -> player3.add(CardsBox.get(i * 3 + j));
                }


            }
        }

        System.out.println("选手一的牌为-------------------");
        for (String card : player1) {
            System.out.print(card + ",");
        }
        System.out.println();
        System.out.println("选手二的牌为-------------------");
        for (String card : player2) {
            System.out.print(card + ",");
        }
        System.out.println();
        System.out.println("选手三的牌为-------------------");
        for (String card : player3) {
            System.out.print(card + ",");
        }
        System.out.println();
        System.out.println("底牌为-------------------");
        for (String card : HiddenCards) {
            System.out.print(card + ",");
        }
    }
}

```
分析:这么搞没有排序，而且没有面向对象编程。

## 270. 模拟斗地主升级版思路

尝试对牌排序。

思路: 
1. 创建`HashMap`, 键是编号, 值是牌。
2. 创建`ArrayList`, 存储编号。
3. 创建花色数组和点数数组。
4. 从0开始往`HashSet`里存储编号，并存储相应的牌。同时往`ArrayList`里面存储编号。
5. 洗牌（洗的是编号），用`Collections`的`shuffle()`方法实现。
6. 发牌（发的也是编号，为了保证编号是排序的，创建`TreeSet`集合接收）。
7. 定义方法看牌（遍历`TreeSet`集合，获取编号，到`HashMap`集合找对应的牌）
![模拟斗地主升级版思路](https://cdn.jsdelivr.net/gh/hljmssjg/PicGo/img/模拟斗地主升级版.JPG)
## 271. 模拟斗地主升级版代码

```java
package 模拟斗地主升级版;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.TreeSet;

public class NewDouDiZhu {
    public static void main(String[] args) {
        // 定义HashMap 牌盒
        HashMap<Integer, String> CardsBox = new HashMap<>();
        // 定义花色序号牌值大小王的集合
        ArrayList<Integer> index = new ArrayList<>();

        String[] colors = {"♥", "♣", "♠", "♦"};
        String[] values = {"3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"};
        String[] Jokers = {"大王", "小王"};

        // 添加值
        int num = 0;
        for (String value : values) {
            for (String color : colors) {
                CardsBox.put(num, color + value);
                index.add(num);
                num++;
            }
        }

        for (String joker : Jokers) {
            CardsBox.put(num, joker);
            index.add(num);
            num++;
        }

        Collections.shuffle(index);

        TreeSet<Integer> player1 = new TreeSet<>();
        TreeSet<Integer> player2 = new TreeSet<>();
        TreeSet<Integer> player3 = new TreeSet<>();
        TreeSet<Integer> hiddenCards = new TreeSet<>();

        for (int i = 0; i < 18; i++) {
            for (int j = 0; j < 3; j++) {
                if (i == 17) {
                    hiddenCards.add(index.get(i * 3 + j));
                    continue;
                }
                switch (j) {
                    case 0 -> player1.add(index.get(i * 3 + j));
                    case 1 -> player2.add(index.get(i * 3 + j));
                    case 2 -> player3.add(index.get(i * 3 + j));
                }


            }
        }

        checkCards("玩家1", player1, CardsBox);
        checkCards("玩家2", player2, CardsBox);
        checkCards("玩家3", player3, CardsBox);
        checkCards("底牌", hiddenCards, CardsBox);

    }

    public static void checkCards(String name, TreeSet<Integer> eachSet, HashMap<Integer, String> CardsBox) {
        System.out.println(name + "的牌为：");
        for (Integer cardIndex : eachSet) {
            System.out.print(CardsBox.get(cardIndex) + " ");
        }
        System.out.println();
    }
}

```

思考: 

为啥`treemap`能自动对这个牌进行排序呢? 在这里，`treeset`存储的是牌的编号，而编号是`Integer`，不是自定义的类，所以不需要用比较器。

同时在对牌编号的时候，使用了数值作为外层嵌套（这点很重要！），花色作为里层嵌套。同时在定义数值的数组时要按正确顺序定义。这些都是决定因素。