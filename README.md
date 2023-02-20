# json_learn
 This repo is for JSON learning.
# 学习笔记
## 注意事项
1. JSON.parse(txt[, reviver])将JSON格式的***字符串***转换为JavaScript对象，并为对象的每个成员调用函数reviver()
2. JSON不能存储Date对象和函数，需要将其转换为字符串存储，之后再转换回Date（使用`new Date(字符串)`）和函数（使用`eval(~)`）
3. 
```json
'{
    "Model_name":"xxx",
    "Total_MACs":"number",
    "Total_Memory":"number",
    ······,
    "layers":[
        {
            "Layer_Name":"xxx",
            "Layer_MACs":"number",
            "CPercent":"number",
            "Layer_Memory":"number",
            ······,
            "InShape":"1x3x224x224",
            "OutShape":"1x3x224x224"
        },

        {
            "Layer_Name":"xxx",
            "Layer_MACs":"number",
            "CPercent":"number",
            "Layer_Memory":"number",
            ······,
            "InShape":"1x3x224x224",
            "OutShape":"1x3x224x224"
        },

        ······,

        {
            "Layer_Name":"xxx",
            "Layer_MACs":"number",
            "CPercent":"number",
            "Layer_Memory":"number",
            ······,
            "InShape":"1x3x224x224",
            "OutShape":"1x3x224x224"
        }
    ]


}'
```

```json
// json for onnx_tool
'{
    "prefix":[
        [
            "",
            "",
            ""
        ],
        [
            "",
            "",
            ""
        ]

    ],
    "Model_name":"xxx",
    "Total_MACs":"number",
    "Total_Memory":"number",
    ······,
    "layers":[
        [
            "Layer_Name1",
            "Layer_MACs",
            "CPercent",
            "Layer_Memory",
            ······,
            "InShape",
            "OutShape"
        ],

        [
            "Layer_Name2",
            "Layer_MACs",
            "CPercent",
            "Layer_Memory",
            ······,
            "InShape",
            "OutShape"
        ],

        ······,

        [
            "Layer_NameX",
            "Layer_MACs",
            "CPercent",
            "Layer_Memory",
            ······,
            "InShape",
            "OutShape"
        ]
    ]

}'
```

```json
// json for opt
[
    {
        "opt_prefix":"xxx or None",
        "opt_postfix":"xxx or None"
    },

    {
        "op_name":"XXX",
        "KARM":"true or false",
        "KOpecnCL":"true or false",
        ······,
        "KUnK":"true or false"
    },
    
    {
        "op_name":"XXX",
        "KARM":"true or false",
        "KOpecnCL":"true or false",
        ······,
        "KUnK":"true or false"
    },

    ······,

    {
        "op_name":"XXX",
        "KARM":"true or false",
        "KOpecnCL":"true or false",
        ······,
        "KUnK":"true or false"
    }


]
```