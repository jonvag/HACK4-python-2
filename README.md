# Jon Apiscope
### 🏴‍☠️ HACKS 

<br/>

📚 tutoriales de python [tutorial 1](https://docs.python.org/es/3/tutorial/) | [tutorial 2](https://www.w3schools.com/python/)
---

```diff
- NOTA HACER LAS PRÁCTICAS MEDIANTE VISUAL STUDIO CODE  
```

```diff
* 1) Tienes que clonar el repositorio 
  git clone https://github.com/SocialOplesk/test_python_hack_2.git
  
* 2) Instalar los paquetes
  pip install -r requirements.txt

* 3) Para validar los hacks
  pytest test_hack.py -v (ejecuta todos los test)
  pytest test_hack.py::test_hack_1 (ejecuta un test en específico)
  pytest test_hack.py::test_hack_3 -v (ejecuta un test en específico)
```
<br/>

|Hacks | Details | 
|----------|---------|
| H-1      | 3 match |
| H-2      | 3 match |
| H-3      | 5 match | 
| H-4      | 3 match |
| H-5      | 4 match |
| H-6      | 2 match |
| H-7      | 2 match | 
| H-8      | 4 match |
| H-9      | {"Foo":"Fooziman"} |
| H-10      | [{"1":"2"},{"3","4"},{"5":"6"}] | 
<br/> 

## 🏆 H-1
```sh
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
```

## 🏆 H-2
```sh
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
```

## 🏆 H-3
```sh
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
```

## 🏆 H-4
```sh
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
```

## 🏆 H-5
```sh
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
```

## 🏆 H-6 (FOR)
```sh
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
```
<br/>

## 🏆 H-7 (WHILE)
```sh
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [] output => [0] 
```
<br/>

## 🏆 H-8
```sh
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
```
<br/>

## 🏆 H-9 (FOR)
```sh
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
```
<br/>

## 🏆 H-10
```sh
text: [{"a":"b"},{"c":"d"},{"e":"f"}] output => [{"1":"2"},{"3":"4"},{"5":"6"}]
```
<br/>

![Alt text](Screenshot.png)
