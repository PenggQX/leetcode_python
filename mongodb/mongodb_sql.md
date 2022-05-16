### 命令

#### 0. 帮助文档

-----

help

db.help()

db.collection.help()

db.collection.find().help()

-----
#### 1. 数据库和集合

----
show dbs:   显示数据库

show collections: 显示集合

db: 显示当前数据库

use db: 切换数据库，db可替换

db.c2.insertOne({y: 1})

-----

#### 2. 查询

--------
db.c2.find().pretty()

db.getCollection("c2").find()