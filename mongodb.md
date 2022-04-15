### 

db                  显示当前数据库
show dbs            显示所有数据库
use <dbname>        选择数据库
show collections    显示表，显示集合
show tables         显示表，显示集合

show users          显示用户


db.createUser({"user":"fox", "roles":["root"], "pwd":"fox"})    创建用户
db.auth("fox", "fox")       验证用户权限

db.<collections>.find().pretty() 显示表数据

启动mongodb时可以进行配置， 可以写到conf文件中 mongo -f .conf 启动


load('book.js')     支持脚本

### 文档增删改查

----------

#### 增加文档
##### 1. insertOne 支持writeConcern
db.collection.insertOne(
    <document>,
    {
        writeConcern: <document>
    }
)
    writeConcern: 0-不关心是否成功， 1-n:指点节点数， majority:大多数

    db.emp.insert({name: "zhangsan", age: "25"})

##### 2. insertMany
    db.emp.insertMany([{name: "zhangsan", age: "25"}, {name: "lisi", age: "16"}])

---------

#### 查询文档

db.collection.find(query, projection)   # query:查询条件, projection:投影

    db.emp.find({name: 'zhangsan'})
    db.emp.findOne({name: 'zhangsan', age:"25"}, {age: 1})  # 投影只显示age

##### 数值查询
    age = 1         {age: 1}
    age != 1        {age: {$ne: 1}}
    age > 1         {age: {$gt: 1}}
    age >= 1        {age: {$gte: 1}}
    age < 1         {age: {$lt: 1}}
    age <= 1        {age: {$lte: 1}}

    and             {a:1, b:1}或 {$and:[{a:1}, {b:1}]}
    or              {$or:[{a: 1}, {b: 1}]}
    a is null       {a: {$exists: false}}
    a in (1, 2, 3)  {a: {$in: [1, 2, 3]}}

##### 分页查询
    find().skip(i1).limit(i2)

##### 正则匹配
    find({type: {$regex: "so"}})
    find({type: /so/})

##### 排序
    find().sort(-1)

--------

#### 更新文档
db.collection.update(query, update, options)
options:
    upsert: 可选，默认false 不存在记录，是否插入
    multi:  可选，默认false 是否全部更新，还是只更新第一条文档
    writeConcern

##### 更新操作符
    $set
    $unset
    $rename
    $push
    $pushAll
    $pull
    $
