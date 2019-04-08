









CREATE TABLE employee(
    id TINYINT PRIMARY KEY auto_increment,
    name VARCHAR(25),
    gender boolean,
    age INT,
    department VARCHAR(20),
    salary DOUBLE(7,2)
);


CREATE TABLE ExamResult(
  id INT PRIMARY KEY auto_increment,
  name VARCHAR(20),
  JS DOUBLE,
  Django DOUBLE,
  DBS DOUBLE
);


INSERT INTO ExamResult VALUES (1, "yuan", 98, 98, 98),
                              (2, "elex", 98, 98, 98),
                              (3, "amy", 98, 98, 98),
                              (4, "bob", 98, 98, 98),
                              (5, "qq", 98, 98, 100),
                              (6, "oo", 98, 98, 98);


CREATE TABLE CC(
  id TINYINT PRIMARY KEY auto_increment,
  name VARCHAR(20),
  age INT,
  is_married boolean
);


INSERT INTO CC (name, age, is_married) values ('bingbing', 52, 0),
 ('cc', 22, 0),
  ('dd', 33, 0),
   ('ee', 44, 0),
    ('ss', 55, 0);


create table student(
id int primary key auto_increment,
name varchar (20),
charger_id tinyint
) engine=innodb;

create table student2(
id int primary key auto_increment,
name varchar (20),
charger_id tinyint,
FOREIGN KEY (charger_id) REFERENCES classcharger(id)
) engine=innodb;




insert into S3 (name, charger_id) values ('s1', 2),
('s2', 5),
('s3', 4),
('s4', 3),('s1', 2),
('s5', 2),
('s6', 5);


ALTER TABLE student ADD CONSTRAINT abc
                    FOREIGN KEY (charger_id)
                    REFERENCES classcharger(id);


create table S3(
id int primary key auto_increment,
name varchar (20),
charger_id tinyint,
FOREIGN KEY (charger_id) REFERENCES CC(id) on DELETE CASCADE
) engine=innodb;



create table tableA (id int primary key, name varchar(20));
create table tableB (id int primary key, name varchar(20), tableA_id int);

insert into tableA values(1, 'alvin'), (2, 'xialv'), (3, 'yuan');
insert into tableB values(1, 'aaaaaaa', 1), (2, 'bbbbbb', 2), (3, 'cccccc', 4);





CREATE TABLE employee (
emp_id int auto_increment primary key,
emp_name varchar (50),
age int,
dept_id int
);

insert into employee(emp_name, age, dept_id) values ('A',19,200),
('B',26,201),('C',22,201),('D',19,202),('E',19,200),('F',19,204);


CREATE TABLE department(
dep_id int,
dep_name varchar(100)
);

insert into department values
(200, 'renshibu'),
(201, 'jishubu'),
(202, 'xiaoshoubu'),
(203, 'caizhengbu');


create table emp(
id int,
name varchar (20),
index index_name (name)

);

create table emp3(
id int,
name varchar (30),
resume varchar (50),
fulltext index index_resume (resume)

)


create table t1 (id int, name varchar(20));

-- 存50万个数据
delimiter $$
create procedure autoinsert()
begin
declare i int default 1;
while (i<500000)do
insert into t1 values(i, 'yuan');
set i=i+1;
end while;
END$$
delimiter ;
call autoinsert();

































