## Mysql利用覆盖索引来优化limit语句 
# limit 2, 1 前面表跳过，后面表读取
https://blog.csdn.net/lxw1844912514/article/details/100029337
select * from tbl_works limit 1, 10  // 32.8ms     
select * from tbl_works limit 10, 10 // 34.2ms 
select * from tbl_works limit 100, 10 // 35.4ms 
select * from tbl_works limit 1000, 10 // 39.6ms 
select * from tbl_works limit 10000, 10 // 5660ms 
select * from tbl_works limit 100000, 10 // 61.4 秒 
select * from tbl_works limit 1000000, 10 // 273 秒 
> 以上可以看出 LIMIT分页查询的时间与偏移量值成正比
> 优化方法，覆盖索引

覆盖索引（Cover Index）覆盖索引覆盖所有需要查询的字段
如果索引包含所有满足查询需要的数据的索引成为覆盖索引(Covering Index)，也就是平时所说的不需要回表操作。

MySQL使用覆盖索引来优化limit语句
使用MySQL官方提供的测试数据库sakila来进行测试：
USE sakila;
explain select * from rental limit 10000,5;
explain select * from rental where rental_id >= (select rental_id from rental limit 10000,1) limit 5;
explain select * from rental a join (select rental_id from rental limit 10000,5) b USING(rental_id);

### MYSQL 八大优化方案
## https://blog.csdn.net/liuyanqiangpk/article/details/79827239
1、选取最适用的字段属性
数据库中的表越小，在它上面执行的查询也就会越快。
另外一个提高效率的方法是在可能的情况下，应该尽量把字段设置为NOT NULL
数值型数据被处理起来的速度要比文本类型快得多

2、使用连接（JOIN）来代替子查询(Sub-Queries) 
原因: 连接（JOIN）..之所以更有效率一些，是因为MySQL不需要在内存中创建临时表来完成这个逻辑上的需要两个步骤的查询工作。

3、使用联合(UNION)来代替手动创建的临时表 > UNION 注意的是所有select语句中的字段数目要想同

4、事务
BEGIN;
  INSERT   INTO   salesinfo   SET   customerid=14;
  UPDATE   inventory   SET   quantity =11   WHERE   item='book';
COMMIT;
事务保持数据库中数据的一致性和完整性。
如: 第一个表中成功更新后，数据库突然出现意外状况，造成第二个表中的操作没有完成，这样，就会造成数据的不完整，甚至会破坏数据库中的数据
事务的另一个重要作用是当多个用户同时使用相同的数据源时，它可以利用锁定数据库的方法来为用户提供一种安全的访问方式，这样可以保证用户的操作不被其它的用户所干扰。

5、锁定表
LOCK TABLE inventory WRITE SELECT quantity  FROM   inventory   WHERE Item='book';
UPDATE   inventory   SET   Quantity=11   WHERE  Item='book';UNLOCKTABLES
包含有WRITE关键字的LOCKTABLE语句可以保证在UNLOCKTABLES命令被执行之前，不会有其它的访问来对inventory进行插入、更新或者删除的操作。

6、使用外键
锁定表的方法可以维护数据的完整性，但是它却不能保证数据的关联性。这个时候我们就可以使用外键。

7、使用索引
索引是提高数据库性能的常用方法，它可以令数据库服务器以比没有索引快得多的速度检索特定的行，尤其是在查询语句当中包含有MAX(),MIN()和ORDERBY这些命令的时候，性能提高更为明显。
一般说来，索引应建立在那些将用于JOIN,WHERE判断和ORDERBY排序的字段上。尽量不要对数据库中某个含有大量重复的值的字段建立索引。对于一个ENUM类型的字段来说，出现大量重复值是很有可能的情况

8、优化的查询语句
a、 首先，最好是在相同类型的字段间进行比较的操作
b、 其次，在建有索引的字段上尽量不要使用函数进行操作
ｃ、第三，在搜索字符型字段时，我们有时会使用LIKE关键字和通配符，这种做法虽然简单，但却也是以牺牲系统性能为代价的

### 知乎: https://zhuanlan.zhihu.com/p/157452426
# 如何优化你的MySQL查询语句
1.如果内容能被转化为数字类型，尽量使用数字类型而不是字符类型

2.不要用select *,而是要select具体的字段
反例 > select * from employee;
正例 > select id，name from employee;
原因 - 通过选择需要的字段，能够节约资源和减少网络开销

3.预先知道只有一条返回结果，推荐使用limit 1
反例 > select id，name from employee where name='jay';
正例 > select id，name from employee where name='jay' limit 1;
原因 - 通过加上limit 1，当一条相关的记录被查询到时，数据库不会继续扫表，而是返回结果

4.在where条件中避免使用or
以下面的user表为例子，usedId作为索引。

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) NOT NULL,
  `age` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `idx_userId` (`userId`) 
)
如果你想查询用户id为1或者，年龄为18的用户，你可能使用以下sql语句。 
反例 > select * from user where userid = 1 or age = 18;

正例
select * from user where userid=1 
union all 
select * from user where age = 18;
// 或者使用两条独立的sql
select * from user where userid=1;
select * from user where age = 18;
原因 - or的使用可能导致全表扫表，导致没有使用索引

5.优化limit分页
当使用limit去分页的时候，offset的值可能非常大，查询的效率就会下降。 反例

select id，name，age from employee limit 10000，10;
正例

// 方案1
select id，name from employee where id>10000 limit 10;
// 方案2
select id，name from employee order by id  limit 10000，10;
原因 
- 使用方案1，返回的是最后的查询记录，这里跳过了偏移，所以能提高查询效率 
- 使用方案2，使用order by和主键索引，也能提高查询效率

6.优化LIKE语句
模糊查询的时候，如果不是前缀查询，会使索引失效。 反例

select userId，name from user where userId like '%Patrick';
正例

select userId，name from user where userId like 'Patrick%';

7.where语句中避免使用!=或<>
反例

select age,name  from user where age <>18;
正例

select age,name from user where age > 18;
select age,name from user where age < 18;
原因 使用!=或者<>有可能使索引失效

8.需要插入大量数据的时候，使用批量插入
反例

for(User u :list){
 INSERT into user(name,age) values(#name#,#age#)   
}
正例

// 500个插入，将插入语句拼接成一个sql
<foreach collection="list" item="item" index="index" separator=",">
    (#{item.name},#{item.age})
</foreach>
原因 - 批量插入能节省每次插入数据库表的结构调整（例如索引等），从而节省时间

9.注意distinct的使用
distinct一般用来过滤重复的记录。当时查询单个或者少量的字段时，能够提高查询的效率。 但是，当对很多字段使用distinct时，会降低查询的效率。 反例

SELECT DISTINCT * from  user;
正例

select DISTINCT name from user;
原因 - 当对很多字段使用distinct时，CPU需要花费大量的时间进行去重。

10.去掉冗余的索引
反例

KEY `idx_userId` (`userId`)  
KEY `idx_userId_age` (`userId`,`age`)
正例

KEY `idx_userId_age` (`userId`,`age`)
原因 - 冗余的索引需要数据库进行维护，当优化器选择索引时，需要一个个地选择。

11.如果数据量太大，优化delete语句
当删除大量的数据时，因为删除记录需要对表进行加锁。删除大量的数据，需要占用较多的时间，从而会导致其他事务处于等待锁的阶段，从而超时。 反例

// 一次删除1百万条记录
delete from user where id <100000;
// 在一个循环里面删除单条记录
for（User user：list）{   delete from user； }
正例

// 批量删除，每次删除500条记录
delete product where id>=500 and id<1000；

12.不要使用NULL,而是使用默认值，
反例

select * from user where age is not null;
正例

select * from user where age>0; // 将0作为默认值
原因 - MySQL中，NULL会占用空间，并且MySQL对含有NULL的列很难进行查询优化。

13.使用union all替代union
反例

select * from user where userid=1 
union  
select * from user where age = 10
正例

select * from user where userid=1 
union all  
select * from user where age = 10
原因 - 使用union, 在shuMySQL会对查询结果进行去重操作,而去重操作涉及到排序，这可能会影响性能 - 使用union all没有对查询结果进行去重。如果确定查询结果没有重复的记录，可以使用union all而不是union

14.使用explain去分析你的sql语句
explain select * from user where userid = 10086 or age =18;