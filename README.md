# JSON_learn

 This repo is for JSON learning.
# [学习笔记](https://www.runoob.com/json/json-tutorial.html)
## JSON简介
1. JSON: JavaScript Object Notation(JavaScript 对象表示法)，是轻量级的**文本数据交换格式**，JSON 使用 Javascript语法来描述**数据对象**，但是 JSON 仍然独立于语言和平台。JSON 解析器和 JSON 库支持许多不同的编程语言。由于这种相似性，无需解析器，**JavaScript 程序能够使用内建的 eval() 函数**，**用 JSON 数据**来生成原生的 JavaScript 对象。

2. JSON 使用 JavaScript 语法，但是 JSON 格式仅仅是一个文本。文本可以被任何编程语言读取及作为数据格式传递。

3. JSON 是存储和交换文本信息的语法，类似 XML，但比 XML 更小、更快，更易解析：没有结束标签、更短、读写的速度更快、能够使用内建的JavaScript eval() 方法进行解析、使用数组、不使用保留字。XML 需要使用 XML 解析器来解析，JSON 可以使用标准的 JavaScript 函数来解析

4. C、Python、C++、Java、PHP、Go等编程语言都支持 JSON

5. JSON和JS的关系：
   1. JSON 是 **JS 对象的字符串表示法**。它使用文本表示一个 JS 对象的信息，（JSON）本质是一个字符串，JSON对象是一个JS对象，注意声明js对象时键名可以加引号也可以不加引号。
   
      ```javascript
      var obj = {a: 'Hello', b: 'World'}; //这是一个js对象，注意js对象的键名也是可以使用引号包裹的,这里的键名就不用引号包含
      var json = '{"a": "Hello", "b": "World"}'; //这是一个 JSON 字符串，本质是一个字符串
      ```
   
      
   
   2. JSON（格式字符串） 和 **JS 对象**（也可以叫**JSON对象** 或 **JSON 格式的对象**）互转（JSON.parse 和 JSON.stringify）。要实现从JSON字符串转换为JS对象，使用 JSON.parse() 方法：
   ```javascript
   var obj = JSON.parse('{"a": "Hello", "b": "World"}'); 
   // 注意参数是一个字符串'~'
   //结果是 {a: 'Hello', b: 'World'}  一个对象
   ```
   要实现从JS对象转换为JSON字符串，使用 JSON.stringify() 方法：:
   ```javascript
   var json = JSON.stringify({a: 'Hello', b: 'World'}); 
   //结果是 '{"a": "Hello", "b": "World"}'  一个JSON格式的字符串
   ```
   说句不严谨的话：JSON.parse() 就是**字符串转 js 对象**， JSON.stringify()就是 **js 对象转字符串**。
## JSON 语法
JSON 语法是 JavaScript **对象表示语法**的子集：
- 数据在键（key）值（value）对中
- 数据由逗号 , 分隔
- 使用斜杆 \ 来转义字符
- 大括号 {} **保存对象**
- 中括号 [] **保存数组**，数组可以包含多个对象
- JSON **值**可以是：
  - 数字（整数或浮点数）
  - 字符串（在双引号中）
  - 逻辑值（true 或 false）
  - 数组（在中括号中）
  - 对象（在大括号中）
  - null
- JSON中有两种结构：对象和数组

1. 对象

   - 对象是一个***无序的键值对集合。***键必须是字符串，值是合法的JSON数据类型即可（见上）

     一个对象以左括号 **{** 开始， 右括号 **}** 结束。key 和 value 中使用冒号` :` 分割。每个 key/value 对使用逗号`,`分割，比如：

     ```javascript
     { "name":"菜鸟教程" , "url":"www.runoob.com" }
     ```

   - 访问对象值：

     ```javascript
     var myObj, x;
     myObj = { "name":"runoob", "alexa":10000, "site":null };
     x = myObj.name; // 或者 myObj["name"]用键名访问
     ```

   - 循环对象：`for (x in myObj){~}`，但是这种访问是无序访问，要实现有序需要借助数组

   - JSON对象支持嵌套定义和实现，因为JSON的值中包含对象这一种类

   - 对象值的修改可以在访问的基础上直接进行

2. 数组

   数组是***值（value）的有序集合***。

   一个数组以左中括号 **[** 开始， 右中括号 **]** 结束，值之间使用逗号 **,** 分隔。JSON 中**数组值**必须是合法的 JSON 数据类型（字符串, 数字, *对象*, 数组, 布尔值或 null）。而在JavaScript 中，数组值可以是以上的 JSON 数据类型，也可以是 JavaScript 的表达式，包括函数，日期，及 *undefined*。

   - 数组元素的访问/修改：支持**索引**访问和修改
   - 支持for-in循环数组，这次是有序的（吧？
   - 可以用delete关键字删除数组元素（其实只是用undefined占位，并没有真的删除存储空间，只是将数组变成了稀疏数组，想要彻底删除可以使用splice()方法——它删除或者增加数组中的元素）

## JSON 文件

- JSON 文件的文件类型是 **.json**
- JSON 文本的 MIME 类型是 **application/json**

## JSON和JS对象的转换

1. JSON.parse()

   语法：

   ```javascript
   JSON.parse(text[, reviver])
   ```

   - text：必需， 一个有效的 JSON **字符串**。
   - reviver: 可选，一个转换结果的函数， 将为 **JS对象的每个成员** 调用此函数。

   示例：

   ```javascript
   var obj = JSON.parse('{ "name":"runoob", "alexa":10000, "site":"www.runoob.com" }');	// 注意字符串前后的引号
   ```

   **注意事项：**

   1. JSON不能存储Date对象和函数，如果想用的话需要将它们转换为字符串存储，之后再从JS对象中取出值然后转换回Date类型：

   ```javascript
   var text = '{ "name":"Runoob", "initDate":"2013-12-14", "site":"www.runoob.com"}';
   var obj = JSON.parse(text);
   obj.initDate = new Date(obj.initDate);
    
   document.getElementById("demo").innerHTML = obj.name + "创建日期: " + obj.initDate;
   ```

   2. 同理，JSON 不允许包含函数，可以将函数作为字符串存储，之后再将字符串转换为函数（用eval()方法，注意参数先加括号：

   ````javascript
   var text = '{ "name":"Runoob", "alexa":"function () {return 10000;}", "site":"www.runoob.com"}';
   var obj = JSON.parse(text);
   obj.alexa = eval("(" + obj.alexa + ")");
    
   document.getElementById("demo").innerHTML = obj.name + " Alexa 排名：" + obj.alexa();
   ````

   3. 我们可以启用 JSON.parse 的第二个参数 reviver，一个转换结果的函数，在JS对象的每个成员上使用此函数（看起来默认对象的成员传递参数是key + value：

   ```javascript
   var text = '{ "name":"Runoob", "initDate":"2013-12-14", "site":"www.runoob.com"}';
   var obj = JSON.parse(text, function (key, value) {
       if (key == "initDate") {
           return new Date(value);
       } else {
           return value;
   }});
    
   document.getElementById("demo").innerHTML = obj.name + "创建日期：" + obj.initDate;
   ```

2. JSON.stringfy()

   语法：

   ```javascript
   JSON.stringify(value[, replacer[, space]])
   ```

   - value：必需， 要转换的 JavaScript 值（通常为对象或数组）。

   - replacer：可选。用于转换结果的函数或数组。

     如果 replacer 为函数，则 JSON.stringify 将调用该函数，并传入每个成员的键和值。使用返回值而不是原始值。如果此函数返回 undefined，则排除成员。根对象的键是一个空字符串：""。

     如果 replacer 是一个数组，则仅转换该数组中具有键值的成员。成员的转换顺序与键在数组中的顺序一样。当 value 参数也为数组时，将忽略 replacer 数组。

   - space：可选，文本添加缩进、空格和换行符，如果 space 是一个数字，则返回值文本在每个级别缩进指定数目的空格，如果 space 大于 10，则文本缩进 10 个空格。space 也可以使用非数字，如：\t。

   JavaScript 对象转换：

   ```javascript
   var obj = { "name":"runoob", "alexa":10000, "site":"www.runoob.com"};
   var myJSON = JSON.stringify(obj);
   document.getElementById("demo").innerHTML = myJSON;
   ```

   JavaScript 数组转换：

   ```javascript
   var arr = [ "Google", "Runoob", "Taobao", "Facebook" ];
   var myJSON = JSON.stringify(arr);
   document.getElementById("demo").innerHTML = myJSON;
   ```

   注意事项：

   1. JSON 不能存储 Date 对象，JSON.stringify() 会将所有日期转换为字符串：

      ```javascript
      var obj = { "name":"Runoob", "initDate":new Date(), "site":"www.runoob.com"};
      var myJSON = JSON.stringify(obj);
      document.getElementById("demo").innerHTML = myJSON;
      ```

   2. JSON 不允许包含函数，JSON.stringify() 会删除 JavaScript 对象的函数，包括 key 和 value:

      ```javascript
      var obj = { "name":"Runoob", "alexa":function () {return 10000;}, "site":"www.runoob.com"};
      var myJSON = JSON.stringify(obj);
       
      document.getElementById("demo").innerHTML = myJSON;
      ```

      我们可以在执行 JSON.stringify() 函数前将函数转换为字符串来避免以上问题的发生：

      ```javascript
      var obj = { "name":"Runoob", "alexa":function () {return 10000;}, "site":"www.runoob.com"};
      obj.alexa = obj.alexa.toString();
      var myJSON = JSON.stringify(obj);
       
      document.getElementById("demo").innerHTML = myJSON;
      ```

