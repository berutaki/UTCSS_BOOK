---
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"id": "qUalg6b6e-c4"}

# 2023瀧川ゼミ計算社会科学ハンズオンセミナー1

+++ {"id": "fkguF1s669Jd"}

## Pythonの基本の基本
- このパートではPythonの基本の基本を勉強します。
- まずPythonでの数値と演算について説明します。

+++ {"id": "J8xtT5Ny69Jg"}

### 数値と演算
- Pythonの演算子を表にまとめました。累乗```**```、整数の割り算```//```の記法には注意。

|  演算子  | 演算  |
| ---- | ---- |
| **  |  累乗  |
|  * | 掛け算  |
|  / | 割り算  |
|//|整数の割り算|
|%|剰余（割り算のあまり）|
|+|足し算|
|-|引き算|


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 232
  status: ok
  timestamp: 1682732582514
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: dIOZtt_Q69Je
outputId: 259e8978-5d79-44e1-a8d8-e22b5d7d87ec
---
10 // 3
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 243
  status: ok
  timestamp: 1682732600589
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: gFDAUN-E69Jf
outputId: c17f745a-dd16-4456-e277-f2c64c88eb4c
---
10 % 3
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: N0fc6JAV69Jf
outputId: 41cbd96d-d876-4b76-db09-5125b3dea972
---
2 / 5
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: AAemKBVO69Jf
outputId: 67f8a8fb-1f85-4c49-f357-afec5fda8f09
---
5 / 2
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: iOwEJCUQra1p
outputId: e72e2769-82ee-4439-eb3d-a44a5d4df5b0
---
5 % 2
```

- 演算の順番には気をつけましょう。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: 5YKxZTu2ruac
outputId: 3f838a46-2100-4837-bfea-7d404593d0e8
---
 5 ** 2 + 4 * 3 + (-2) * 3#演算の順番に注意
```

+++ {"id": "VcmLH5hjrlyz"}

#### コメント
- 剰余計算%はプログラミングでは頻出。
- 演算の順番に注意。
- #を使うとコメントを書けます。

+++ {"id": "03xzfx5W69Jg"}

### 数値の型
- Pythonのオブジェクトにはすべて型（type）があります。
- ここでは大きく分けて数値型というtypeを扱っています。
- 数値型のなかでもさらに下記のようないくつかのtypeが分かれます。
- int 整数型
- float 浮動小数点型
- 文字列strと混同しないこと
- intやfloatで型変換できる

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 335
  status: ok
  timestamp: 1682732673768
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Isrbv9Ca8e8N
outputId: be3f21ae-2da4-4b44-85cb-a96dc9e59ca5
---
type(5)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 252
  status: ok
  timestamp: 1682732685301
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: kpx7Tq0WsYK1
outputId: 0fe760eb-9a28-44fc-e23a-5fde2eef681d
---
type(5.0)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 316
  status: ok
  timestamp: 1682732698179
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: nd8owGyjsc_C
outputId: b725b4f3-e401-4929-ddc3-5ecac07838d6
---
1/3
```

```{code-cell} ipython3
- ""で囲むと文字列になります。
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 271
  status: ok
  timestamp: 1682732717621
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: SSIW4DXCr4AY
outputId: 2ecd3803-d9b4-4605-8944-7d85420d5095
---
"3"
```

- 異なる型同士の```+```演算はできません。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 170
executionInfo:
  elapsed: 425
  status: error
  timestamp: 1682732734135
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Cf7cJjbQsguH
outputId: d0dfd5ba-a6ac-41d9-dc40-7f4a26edbb2a
---
9 + "3"
```

- floatをintに変換します。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 289
  status: ok
  timestamp: 1682732785900
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Fi7Y_lTwgLo0
outputId: 5eb58dac-81d7-4425-e5f5-0c8c57513003
---
int(5.0)
```

intをfloatに変換します。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 252
  status: ok
  timestamp: 1682732794582
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: WbekbXJDgPJN
outputId: e10bd855-ed6b-42d8-c7c9-c0c24060957e
---
float(5)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682732809902
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: EfoXCInmgSa8
outputId: f1cc7443-7902-40da-e616-d9b3c690d33c
---
int('5') + 10
```

+++ {"id": "cTELQGV069Jh"}

### 変数
- 変数とは、値を入れておく箱のようなものです。
- 代入の演算子は、```=```を使います。
  - 数学の等号とは異なるので注意。比較演算子（後述）では"=="を使う。
- 同じ変数に別の値を代入すると、変数の中身が更新されます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 232
  status: ok
  timestamp: 1682732941543
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: hYTyIxGU69Ji
outputId: 7dbbebd0-a8d5-4a2e-cb5f-1f052e63205c
---
a = 5
b = 2
a/b
```

- ```a```に```4```を代入すると、計算の結果が変わります。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 393
  status: ok
  timestamp: 1682732953308
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: UgRDHAGO69Ji
outputId: c50bdc16-47c9-4afe-a839-0e795bea95d0
---
a = 4
a/b
```

+++ {"id": "0GDLTLCQaRSn"}

### 累積代入文
- プログラミングでは、ある変数の値にさらに別の値を加えたりすることがあります。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 283
  status: ok
  timestamp: 1682732981593
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: U5TO2UcBaBix
outputId: 98083f24-8d36-40e8-ab13-26c87216ae3f
---
a = 3
a = a - 3
a
```

- 以下のような書き方を出来ます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 412
  status: ok
  timestamp: 1682733013487
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: h3fY90Q_aLMB
outputId: 287d0e76-e94a-4132-bf8d-6a64ca8c263f
---
a = 3
a += 3
a
```

+++ {"id": "x2OaB-O0a6xT"}

### 関数

- 関数は引数（インプット）を与えると返り値（アウトプット）を返すはたらきをします。
  - （数学の関数と違って）どちらか、ないし両方なくてもよい。
- Pythonではdefを使って関数を定義できます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 135
executionInfo:
  elapsed: 6
  status: error
  timestamp: 1682733158208
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 7WC7eQoBcDq4
outputId: 862290a1-736f-46d9-b376-42fedcaea89b
---
def myfunc(a, b):
  c = a**2 + b
  return c
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 246
  status: ok
  timestamp: 1682733084103
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: -fKIUhV0cO7e
outputId: abe37d97-f4c6-4d89-e27a-a8b3a8449053
---
myfunc(4,2)
```

+++ {"id": "_Qzr_p9m69J6"}

### 変数のスコープ
- 変数にはそれが機能する空間（名前空間）が決まっています。
- 関数の中で定義した変数はその関数の中でしか定義どおりにはふるまいません。

+++

- 例えば、以下のように関数の外で```b = 10```として...

```{code-cell} ipython3
:id: FHI-l87q69J7

b = 10
def myfunc2(arg):
    b = 10*arg
    print(b)
```

-　関数の中では```b=100```となっているが…

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 270
  status: ok
  timestamp: 1682733270633
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: i5h4_8uU69J7
outputId: b2937b76-50dc-457a-ef2b-ef0a0c7557d6
---
myfunc2(b)
```

- 外では```10```のままである。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 321
  status: ok
  timestamp: 1682733298318
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: os73ZDZz69J7
outputId: aa47d506-3944-4ea9-ba5c-9c1f8d3f54de
---
b
```

+++ {"id": "JWObKv2ldnC2"}

#### グローバル変数とローカル変数
- どこでも（グローバルに）通用する変数を作りたい場合は```global```を用いる。
- グローバル変数はどの空間でも同じようにふるまいます。
- これに対して、関数の中で定義された変数をローカル変数といいます。

```{code-cell} ipython3
:id: -UcP8N4meBhH


def myfunc3(arg):
    global c
    c = b + arg
    print(c)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682734365790
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: QQqnNUB0eP3h
outputId: 9fdd1977-a3f9-4049-bcbe-e9e5bff841d9
---
c
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682734248683
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: jMTZkdcNu05f
outputId: 75371031-7741-4c52-c622-320e7ad24285
---
c
```

+++ {"id": "lqJoKeQs69Jt"}

### ブール型
- ブール型という型のオブジェクトを紹介します。
- これはTrueかFalseの二値をとるデータ型です。

```{code-cell} ipython3
:id: rG-ONT9469Jt

b = True
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682733556492
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: _9r3XmmtvFTs
outputId: 9c72f22b-1d4a-4f01-be39-6227f7a028ff
---
b
```

  - notで否定すると```False```となります。```not```は論理演算子（後述）の一種です。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 243
  status: ok
  timestamp: 1682733566379
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ZwCErLAA69Jt
outputId: ab2a99b3-e7b4-47a5-9549-ab7fffacfb5b
---
not b
```

+++ {"id": "YkUslvpm69Ju"}

### if文とブール型
- プログラミングには制御文といって、プログラミングのフローを制御する文があります。
- if文はある条件のときに、〜せよ、といったタイプの制御文です。
- if文の条件はブール型を返す文で書きます。つまり、ある条件がTrueなら以下を実行せよ、という命令となります。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 279
  status: ok
  timestamp: 1682733606215
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: tLdXfbdu69Ju
outputId: 59795ccd-bb6e-43d2-ed0d-43377a379eca
---
if b:
    print('実行')
```

```{code-cell} ipython3
:id: NKdOWmv469Ju

if not b:
    print('実行')
```

+++ {"id": "ikJlTq4H69Jv"}

### 比較演算子、論理演算子
- if文の条件などを作るときに、比較したり、否定の条件を使うことが多いです。
- このような演算は、比較演算子と論理演算子で行われ、演算の結果ブール型が生み出されます。


- 論理演算子

| 演算子| 意味 |
|:-----------:|:------------:|
|a and b| aかつb|
|a or b| aあるいはb|
|not a|aでない |

- 比較演算子

| 演算子| 意味 |
|:-----------:|:------------:|
|a == b|	bがaに等しい|
|a != b|	bがaに等しくない|
|	a > b|	bよりaが大きい|
|	a >= b|	bよりaが大きいか等しい|
|	a < b	|bよりaが小さい|
|	a <= b|	bよりaが小さいか等しい|


+++

- 以下で例をみていきます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 298
  status: ok
  timestamp: 1682733664363
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Gqc1lBHJ69Jv
outputId: 31aeaace-8df7-469e-93d8-f53d4f122002
---
a = True
b = True
not (a or b)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 274
  status: ok
  timestamp: 1682733721933
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: QHBfwCVVyj5Q
outputId: b429e1d3-18aa-4b0f-e14c-2f80a454183e
---
a = 3; b = 5
a == 3
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 252
  status: ok
  timestamp: 1682733731617
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: FFyEMUbdywCy
outputId: e81aef67-4129-4189-ef3b-7d5a4dcfd59d
---
b != 5
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 311
  status: ok
  timestamp: 1682733740826
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: KL9glDI8yy2o
outputId: 26d6345a-f3bb-44f7-b23e-c09984b91157
---
a > b
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 284
  status: ok
  timestamp: 1682733747781
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: mJmiA3Xmy03V
outputId: bae2aed8-8795-4a3e-c5bd-b14d5d150f84
---
a + 2 >= b
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 286
  status: ok
  timestamp: 1682733757242
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: dMy0Ngk1y6Zh
outputId: 4af78f37-4691-4ba3-d3ee-8132573fa075
---
a + 2 >= b and b != 5
```

+++ {"id": "LuMlExh62HAE"}

## 問題１

+++ {"id": "NY6d5jxj2MZg"}

### 例題
- 変数xとyが与えられています。xが偶数で、yが奇数の場合に真(True)を返す論理式を作成してください。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 4
  status: ok
  timestamp: 1682733854110
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: gmnS-xpy2cX1
outputId: 31f6b815-a2a3-4e41-c939-05f0f25c75ca
---
x = 8
y = 14

(x % 2 == 0) and (y % 2 == 1)
```

+++ {"id": "ecgn_rvZ2qoZ"}

### 問題1-1
- 与えられた整数xが、3の倍数でもあり、かつ4で割り切れるかどうかを判定する論理式を作成してください。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 228
  status: ok
  timestamp: 1682734579085
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: M3mHojKly3u3
outputId: 4bb98161-0345-4980-d013-2f07a4587c86
---
x = 16
(x % 3 == 0) and (x % 4 == 0)
```

+++ {"id": "jaQqUsao27_H"}

### 問題1-2
- 与えられた2つの整数mとnが、どちらも5で割り切れる場合にTrueを返し、そうでない場合はFalseを返す論理式を作成してください。


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682734625869
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: XGwMk571zA9s
outputId: 0be1bfdf-19b4-4e74-b99a-790344294bc8
---
m = 10
n = 15
(m % 5 == 0) and (n % 5 == 0)
```

+++ {"id": "nPyuQEhF2_Mf"}

### 問題1-3
- 与えられた整数pが、10未満かつ偶数であるか、または20以上かつ奇数である場合に真(True)を返す論理式を作成してください。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 237
  status: ok
  timestamp: 1682734986426
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 8V_8PqihzM3J
outputId: 2b7bb963-a443-4bc4-ec70-31d408cecf52
---

p < 10 and p % 2 == 0 and p % 2 == 1 and p >= 20 
```

+++ {"id": "vzunfVhy6_X7"}

## 制御文
- プログラミングでは、しばしば命令の流れを条件分岐したり繰り返したりして制御する必要がある。
- 条件分岐はif、ループはforを用いる。whileは条件付きのループである。

+++ {"id": "sWaS_-TF69Jx"}

### if文とブロックの書き方。
- if文で条件分岐をする。
- if の後に条件を書き、:で改行し、ブロック部分を書く。
- elseはif以下の条件を満たさないときに実行される。
- 3つ以上条件があるときはelifを使う。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 234
  status: ok
  timestamp: 1682735163143
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: J6Z3X1s969Jy
outputId: a93c790b-5620-49f8-920a-15aa56555ee2
---
# 6がtにあれば、"in"なければ"out"を出力する。
t=[1,2,3,4,5]
if 3 not in t: 
    print ("in")
else:
    print ("out")
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 228
  status: ok
  timestamp: 1682735133448
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: yEynAG8ih1HM
outputId: 93cea98b-06f5-411b-b745-d3b9182ee19d
---
# xが2で割り切れれば'A',3で割り切れれば'B'、どちらでもなければ'C'を返す。
def myfunc(x):
  if x % 2 == 0: 
    print("A")
  elif x % 3 == 0:
    print("B")
  else:
    print("C")
myfunc(7)
```

+++ {"id": "NDfgcLyifOQh"}

#### コメント
- []はリスト型（後述）
- x in y はxがyに含まれればTrue、そうでなければFalseを返す。

+++ {"id": "q4_XonLv69Jy"}

### if文による簡単なプログラム
- 例えば、簡単なクイズを出して、正解／不正解を返すプログラムを作ることができる。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 5084
  status: ok
  timestamp: 1682735228876
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: howAEzdl69Jy
outputId: aed8b6f5-b5ce-464f-f845-3c651650fce8
---
var = input('マックスの誕生年はいつでしょう？')
var = int(var)
if var == 1864:
    print('正解です！')
else:
    print('不正解です。。')
```

+++ {"id": "OmIdi6Oefuu_"}

#### コメント
- input()関数で入力フォームに記入した文字列をプログラムに組み込むことが可能。

+++ {"id": "ZWKGko0H69Jz"}

### for文
- 同じ処理を繰り返し行いたい（ループさせたい）とき、for文を使う。
- for i in XでXの要素を一つずつi回ループする。
- range()は連続する数値からなるデータを返す。
- リストなどの要素をループさせることも可能。
- 単にループだけさせたいときは、_ in range()と書くことも可能

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 252
  status: ok
  timestamp: 1682735271227
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: IlZhnJtr69Jz
outputId: b5e64fb4-5a66-414c-d7fd-dce3237ba435
---
for i in range(1,6):
  print (i)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 266
  status: ok
  timestamp: 1682735313917
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ylqK3NEE69J0
outputId: ae9f8065-b6f7-4985-99e4-152691341db8
---
t=['a','b','c','d','e']
for i in t:
    print (i)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 428
  status: ok
  timestamp: 1682735333427
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Xw9AUr0AhaRQ
outputId: 28c256d2-c1fc-4d14-9a8e-d34fd84d8ed6
---
for _ in range(10):
  print('Hello')
```

+++ {"id": "E-1R2snI69J1"}

### continue とbreak
- プログラムを実行中に、ループを途中で抜けたり、終わらせたりする。
- continueは以後の処理をとばして次の処理へいく。
- breakはループ自体を終了する。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 387
  status: ok
  timestamp: 1682735361750
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: LbPbADk669J1
outputId: 51cec6d8-b54a-4ff4-b98b-e95062560660
---
for item in t:
    if item=='c':
        continue
    print (item)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 420
  status: ok
  timestamp: 1682735424651
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: lSs2VMyJ69J2
outputId: a806e863-a2ad-4f75-b6b3-0fa4e6dc642d
---
for item in t:
    if item!='c':
        print (item)
    else:
        break
```

+++ {"id": "M6Ckn2js69J3"}

### while文
- while文は条件を満たす限り、ブロックの実行を繰り返す。
- while Trueで無限ループを作ることができる。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 260
  status: ok
  timestamp: 1682735499754
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 0Ny1hRQw69J3
outputId: 0cee433c-dbb5-424e-e226-20317142d256
---
t = 1
while t != 6:
    print (t)
    t += 1
    #t = t +1
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 254
  status: ok
  timestamp: 1682735591012
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: AVbXk8pykx-n
outputId: 50394cd6-cd72-4bc8-8140-92ad33cff5d1
---
t = 1
while True:
    print (t)
    t += 1
    if t == 6:
      break
```

+++ {"id": "ZTe8gJVglJFQ"}

#### コメント
- 無限ループは、ある処理をループして条件を満たしたときに終わらせる。プログラミングでは頻出。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682736205982
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Vi1ajEts48Bd
outputId: d6c6984b-4250-47c7-98dd-13951a564789
---
a = 2
b = 4
c = a + b
print(c)
```

+++ {"id": "OdWOdE7FkAe-"}

## 問題2 

+++ {"id": "C2ifVWsokIc_"}


### 問題2-1

- 1から10までの整数のリストから、偶数だけを表示してください。

```{code-cell} ipython3
:id: Rv8sNOkl3Mxq

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
t = range(1,11)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682736266687
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: _1IIaL_n5Sj8
outputId: 4b3f33c9-a643-4692-86e6-94f2da2a01e6
---
for i in t:
  if i % 2 == 0:
    print(i)
```

+++ {"id": "VLLYoqZJkSuP"}

### 問題2-2
- 与えられたリスト[1, 3, 9, 16, 20, 25, 28, 30]の要素に対して、次の条件に従って処理を行ってください。

  - 偶数の場合は2で割る。
  - 奇数の場合は2倍する。

```{code-cell} ipython3
:id: sHNhHr2A3W-i

t = [1, 3, 9, 16, 20, 25, 28, 30]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 283
  status: ok
  timestamp: 1682736335667
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bYBdmVnc5d0i
outputId: 792a95a3-e8d2-4044-cfa9-107c51108e31
---
for i in t:
  if i % 2 == 0:
    print(i//2)
  else:
    print(i*2)
```

+++ {"id": "ImlwXqwpkkAG"}


 ### 問題2-3
- 与えられた整数nに対して、1からnまでのすべての奇数の合計を計算してください（continueを使うこと）。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682736469850
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: CYZbgS2T5xXR
outputId: 3a346c57-8147-4692-f30f-bc2602f6f90b
---
sum = 0
n = 300

for i in range(1, n + 1):
  if i % 2 == 0:
    continue
  sum += i

print(sum)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 4
  status: ok
  timestamp: 1682736563688
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: fFRKN7l_6hCQ
outputId: 52259d5d-c355-4874-a6de-a3d463823cce
---
for i in range(10):
  print(i)
```

+++ {"id": "xYs79-G6jtHe"}

## ユークリッドの互除法
- ここで、プログラミングらしい課題としてユークリッドの互除法というアルゴリズムの実装にトライしてみましょう。
-  ユークリッドの互除法とは、2つの整数、aとbの最大公約数を求めるアルゴリズムです。例えば、2485と1162の最大公約数を求めたい場合

$2485 \div1162 = 2 余り 161$ 

$1162 \div 161 = 7 余り 35$ 

$161 \div 35 = 4 余り 21$ 

$35 \div 21 = 1 余り 14$

$21 \div 14 = 1 余り 7$

$14 \div 7 = 2 余り 0$

割る数と余りを次回の割られる数と割る数にして、次々と計算し、最後に割り切れたら終わりで、最後の割る数が最大公約数です。


+++ {"id": "lUk-CpGVqCGG"}

##問題3
### 例題
- ユークリッドの互除法をPythonで実装しましょう。ヒントwhileを用います。余りがゼロでないならば、〜を実行せよ、という形式をとります。また、余りを計算するには%演算子を使います。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: yx2Hp2ndjtHf
outputId: 71b0fb3b-ef50-4ec6-81ca-9ba6fc17d7c6
---
#答え
a = 2485
b = 1162
while b !=0:
    r = a % b#入れ替え用のrを用意する 
    a = b
    b = r
    print(a,b)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 302
  status: ok
  timestamp: 1682736817622
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: cBqoMvTIlUfp
outputId: 421d6f29-d6df-4a2c-dd58-3f5af6e584fd
---
#別解
a = 2485
b = 1162
while b !=0:
    a, b = b, a % b#この書き方で複数の変数に代入できて、入れ替え用を用意する必要もない。 
    print(a,b)
```

+++ {"id": "jl8yrOk-khxD"}

### 問題 3-1
与えられた整数nに対して、nの階乗（n!）を求める関数factorialを定義してください。ただし、0の階乗は1と定義します。

```{code-cell} ipython3
:id: 4u36yL9BkkpT

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

# 例: 5の階乗を計算
result = factorial(5)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 268
  status: ok
  timestamp: 1682736913887
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: r888AX8h749a
outputId: 18423be3-1e42-4bb7-8845-48d2bf4ea7a1
---
result
```

+++ {"id": "CGzcIRLUoG8Z"}

### 問題3-2
与えられた整数nが素数かどうかを判定する関数is_primeを作成してください。


```{code-cell} ipython3
:id: k09Pt5JXoGFG

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = 17
result = is_prime(n)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 237
  status: ok
  timestamp: 1682737034390
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Z-_HHv368SHS
outputId: 1bb87876-5b08-4c05-eba9-aca90d3e77c1
---
is_prime(23095832905823409587)
```

+++ {"id": "C6ZMydQqppAm"}

### 問題3-3
フィボナッチ数列の要素を生成し続けます。要素が1000を超えるような最初のフィボナッチ数を求めてください。
$$F_0 = 0$$
$$F_1 = 1$$
$$F_{n+2} = F_n + F_{n+1} (n ≥ 0)$$

```{code-cell} ipython3
:id: pgCUGQDVptF8

def first_fib_over_n(n):
    a, b = 0, 1
    while True:
        a, b = b, a + b
        if b > n:
            break
    return b

n = 1000
result = first_fib_over_n(n)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 271
  status: ok
  timestamp: 1682737287769
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: VnBoDcPl9UBb
outputId: 9424c783-6f7e-4a4c-98b3-7a9d1d27c97f
---
result
```

+++ {"id": "HrK5n70XuZb7"}

## データ型
- Pythonはオブジェクト指向のプログラミング言語であり、変数、関数をはじめとしたプログラムの部品はすべてオブジェクトである。
- オブジェクトはデータともいわれ、ある型を持っている（すでに数値に型があることは説明した）。
- 以下では、特に重要なデータ型として、文字列、リスト、ディクショナリ、タプルについて解説する。

+++ {"id": "eq4EQv4Q69Ji"}

## 文字列
- 文字列は数値とは異なるデータ型の一つで、文字通り文字を扱う。
- ""ないし''でくくると文字列になる。
- 文字列は、シークエンス型という広義の型に属していて、インデックスで要素を指定して取り出すことができる。

```{code-cell} ipython3
:id: sTlR3tQA69Jj

text = "Hello!"
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682737585783
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 060rq3vH69Jj
outputId: 878d5dfe-bb46-481d-f39c-adf1bb6611cc
---
text
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 256
  status: ok
  timestamp: 1682737621546
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: GvE3_e1769Jj
outputId: c3e1c92e-4828-42fd-f661-bff60900adfc
---
text[3]
```

+++ {"id": "svrIQiDwwBZe"}

## インデックス

- Pythonのインデックスは0から始まる。
- ":"それ以後を続けてとる。
- "-"は後ろから数える。
- <img src="https://raw.githubusercontent.com/berutaki/github.io/main/1-4.png" width="500">

```{code-cell} ipython3
:id: XVzqHLJc69Jj
:outputId: 033ed576-957f-4415-9a2a-a26c7d4440fb

text[0:3]
```

```{code-cell} ipython3
:id: vGwuIyBA69Jk
:outputId: c93d6fdc-ef5b-4976-f4a1-308a897957fb

text[1:]
```

```{code-cell} ipython3
:id: ubuDW0nF69Jk
:outputId: 61c1a9ad-609d-42dd-a8f5-e6fdce6727cb

text[-1]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 170
executionInfo:
  elapsed: 425
  status: error
  timestamp: 1682737766892
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: QuDim2qT69Jk
outputId: c2942f6f-61a5-4b97-e083-1ba86cabd785
---
text[[2,4]]
```

+++ {"id": "axL5ASc769Jl"}

## メソッド
- データ型にはそれぞれに固有の関数のようなものーーメソッドがある。
- メソッドは、それぞれのデータ型をもつオブジェクトに対して何らかの操作をする。
- hoge.XXXX()という形を取る。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 229
  status: ok
  timestamp: 1682737791802
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: oR1O0UUA69Jl
outputId: 1caaf7a5-c38d-47a9-b046-dacda39c75de
---
text.replace('ll','oo')
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 188
executionInfo:
  elapsed: 4
  status: error
  timestamp: 1682737846998
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 8LEt1xKb_YXS
outputId: e4429646-a204-4b28-ede4-38e07a5748c9
---
a = 3943
a.replace(3,4)
```

+++ {"id": "Zph9BGjx69KG"}

### 文字列操作

- '+'で結合できる。
- リストの結合はjoin()を使う。

```{code-cell} ipython3
:id: SQeHMn4X69KG

a = "Hello!"
b = "こんにちは!"
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682737867169
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: -yQ7r0RK69KG
outputId: f9a43e53-27d0-4867-9a22-bd90709ab15a
---
a+b
```

```{code-cell} ipython3
:id: e3SO9FyI69KH

strings = ["Hello!","こんにちは!"]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682737896425
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: nySH3ncn69KH
outputId: 46ac2fd3-4e2d-4294-e0fb-e61c6d932aa2
---
''.join(strings)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 242
  status: ok
  timestamp: 1682737932170
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: xCQ4nbD969KH
outputId: 609edfb4-cbe1-4761-875b-edba69f8e92c
---
','.join(strings)
```

+++ {"id": "j5bQcOsQ69KH"}

#### 置換、replace()メソッド
- 部分文字列を別の部分文字列に置換するには、replace()メソッドを使います。

```{code-cell} ipython3
:id: gyGjBKaQ69KH

a = "私の名前は、マックスです。"
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682737947246
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 96iT1dO869KH
outputId: 580989b2-d6da-4431-f095-c80ede310aed
---
a.replace("マックス","エミール")
```

+++ {"id": "6LJOSLW769KH"}

#### 小文字化、lower()メソッド
- 文字通り小文字化するメソッドです。upper()は大文字化します。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 417
  status: ok
  timestamp: 1682737955626
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: pVSBgmk669KI
outputId: 6fb7e0b2-4820-468d-f9d2-fdb5324d6017
---
a = "Hello!"
a.lower()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 4
  status: ok
  timestamp: 1682737967982
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: LBxa0sGT_53_
outputId: 5c26f8ca-79b9-4160-dec2-c0eab211fc0c
---
a.upper()
```

+++ {"id": "qEoPnbvv69KI"}

 #### 検索、find()メソッド
- find()メソッドはその部分文字列の始まるインデックスを返す。。なければ-1を返す。
- 含まれるかどうかはinを使う方がわかりやすい。

```{code-cell} ipython3
:id: xAvGuXg469KI

a = "私の名前は、マックスです。"
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 4
  status: ok
  timestamp: 1682737982658
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: wm6ecl1569KI
outputId: 567f42e9-5eae-4c72-f781-1f058690304e
---
a.find("マックス")
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 226
  status: ok
  timestamp: 1682738004501
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: hdijPR4E69KI
outputId: 07462404-eca1-4fb6-e6ff-0e016e25426c
---
a.find("ゲオルグ")
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 234
  status: ok
  timestamp: 1682738020882
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bZzYG9F169KI
outputId: b0695062-98b6-4d8a-94dd-13f0c66e6d5f
---
"マックス" in a
```

+++ {"id": "LF5SqP2R69KI"}

#### 分割、split()メソッド
- 文字列を分割したい場合はsplit()メソッドを使います。引数には、分割したい箇所にある文字列、例えば'、'を与えます。ただし、その文字列は失われます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 226
  status: ok
  timestamp: 1682738051844
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 0HQ-BR4869KI
outputId: b45f1e2e-192c-44b3-f069-58d1b5cd20b4
---
a.split('、')
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 242
  status: ok
  timestamp: 1682738060271
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: phkbX7Co69KJ
outputId: a2067bca-67b0-4d49-9a0d-81261059fbec
---
a
```

+++ {"id": "N3faSxk-69KJ"}

#### クリーニング、strip()メソッド

+++ {"id": "DLTKxhBj69KJ"}

- とくにテクストデータを外部から読み込んできた場合など、前後に空白や改行マーク"\n"がついてくることがあります。これを取り除くにはstrip()メソッドを使います。

```{code-cell} ipython3
:id: ggO4-Gv169KJ

b = " マックス・ウェーバー\n"
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682738083940
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: AHY9lXKR69KJ
outputId: ce47b466-7839-4737-8a44-dab57d9e6b32
---
b
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 241
  status: ok
  timestamp: 1682738086450
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 5E_-6cVt69KJ
outputId: f69b2ad5-450f-4aad-d629-f227233a9120
---
b.strip()
```

+++ {"id": "4f0hwoF7H4zt"}

#### startswith(), endwith()メソッド
- ある部分文字列から始まる、あるいは終わるかを調べるには、startswith(), endwith()を使います。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 225
  status: ok
  timestamp: 1682738101588
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 6fNUEiB_IAyr
outputId: 08e5c833-e64b-419f-c48b-edf20cb7dc07
---
'マックス・ウェーバー'.startswith('マックス')
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 241
  status: ok
  timestamp: 1682738104098
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: z8mc5EgqIKh0
outputId: dbbc29d8-4bf3-464e-db85-ec539721951a
---
'マックス・ウェーバー'.endswith('ズ')
```

+++ {"id": "w3gFj5BK69KK"}

#### フォーマット
- 文字列の中に変数の値を埋め込みたい場合、f'hoge{}'のようにする。
- 他に、%演算子を使う方法がある。この場合%s(文字列)のようにデータ型を指定する。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 240
  status: ok
  timestamp: 1682738146213
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ZouH1MhT69KL
outputId: d526f8ef-0e3b-4a4d-b44b-383280a9247d
---
a = 'マックス'
b = 'ウェーバー'
f'私の名前は{a}・{b}です'
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682738172247
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: kvIUs8dnAox2
outputId: 89530eed-5256-4a3a-f495-2417772ac49a
---
'私の名前は{}・{}です'.format(a,b)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 267
  status: ok
  timestamp: 1682738208587
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: -cy3jimE69KL
outputId: 759aff3b-0c61-43ad-8441-7249f21d8bb1
---

'私の名前は%s・%sです'%(a,b)
```

+++ {"id": "72CMp3NY69Jl"}

## リスト
- リストも文字列と同様、シークエンス型で、どんなデータ型でも、異なるデータ型でもいれることができる。
- []でくくって、作る。
- リストのリスト（ネストされたリスト）も可能
  - ネストされたリストからのデータ抽出は[1][1]などとする。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 253
  status: ok
  timestamp: 1682738249461
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: PD_yy6WZ69Jl
outputId: 24185870-d43c-43e2-b0e2-b7cba32e47fb
---
a = [1,2,3,4,5]
a
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 236
  status: ok
  timestamp: 1682738252155
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 1BncWV2p69Jm
outputId: 45d8a4d0-7d33-44d1-ac5c-f9259d506bb6
---
b = ["Apple","Banana"]
b
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 305
  status: ok
  timestamp: 1682738259341
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: umDA7BEy69Jm
outputId: 2edf780f-05f1-47b5-8e35-af4f160ca236
---
c = [1,2,3,4,5,"Apple","Banana"]
c
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 430
  status: ok
  timestamp: 1682738264019
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 5P4dnd-869Jn
outputId: dbc513e9-7560-4c46-9cc6-5bc953f25c67
---
d = [a,b,c]
d
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682738287047
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 98k4Mr8e69Jn
outputId: c6e097b2-4e3a-4267-a59f-31318848acea
---
d[1]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 379
  status: ok
  timestamp: 1682738300455
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: HEcD3nIV69Jn
outputId: 7970ac0d-dc8d-47fc-df98-8433d019a9ce
---
d[1][1]
```

+++ {"id": "Mg-dqRrz69Jo"}

### リストの操作
- +演算でリスト同士を足したり、*で複数にしたりすることもできる。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 244
  status: ok
  timestamp: 1682738328989
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bd_E8rEv69Jo
outputId: 1b39658e-725c-4e16-ce9a-47e9b1ddab52
---
a + b
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 241
  status: ok
  timestamp: 1682738338425
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: NwQLFCkm69Jo
outputId: 39f41d4c-33a9-478a-99a1-eba965dd51c8
---
b * 3
```

+++ {"id": "Sy_L8dnT69Jo"}

####  ミュータブルなリスト（一部、やや難）
- リストの中身は後から変更できる（これをミュータブルという）。
- ミュータブルなデータ型を扱うときは代入の際に注意が必要。
  - 例のようにbにaを代入した後、aの中身を変えるとbの中身も変わってしまう。
- コピーをすることで回避できる。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682738366735
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: -zE6lvMe69Jp
outputId: 27be707b-882d-4c7b-cfc7-29964196b287
---
a
```

```{code-cell} ipython3
:id: NgNftxzN69Jp

a[0] = 2
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 269
  status: ok
  timestamp: 1682738385918
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: lc9daHLN69Jp
outputId: e2de6737-2eba-4776-c9dc-1493b8bad720
---
a
```

```{code-cell} ipython3
:id: h4WKqs6D69Jq

#ミュータブルなリストのふるまい
a = [1, 2, 3, 4, 5]
b = a
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 260
  status: ok
  timestamp: 1682738408023
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: zZz7lGjF69Jq
outputId: 3180e986-da2c-47ff-da11-f54d893fda74
---
b
```

```{code-cell} ipython3
:id: UiOFTBcC69Jq

a[0] = 2#aの中身を変えると。。
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 279
  status: ok
  timestamp: 1682738419559
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: YyxXdtzb69Jq
outputId: b66e2973-3612-41b5-b016-0e3909049b04
---
a
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 404
  status: ok
  timestamp: 1682738426251
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: NYFRSkWV69Jr
outputId: 1d8628b2-8a53-4e52-c522-6476ab8f0ddd
---
b
```

+++ {"id": "hPzI8Zic69Jr"}

- aの本当のコピーを作れば、このことは避けられます。[:]を使う方法とcopy()メソッドを使う方法があります。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 378
  status: ok
  timestamp: 1682738460055
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: RQOlMRo469Jr
outputId: e39e9415-0728-454b-e7bd-5b416957ab83
---
a = [1, 2, 3, 4, 5]
b = a[:]#b = a.copy()
a[0]=2 
b
```

+++ {"id": "H9QzTE2A69J_"}

### リストのメソッドと関数
- リストにも専用のメソッドがある。またリストによく使う関数もある。

+++ {"id": "hzqk4FvH69J_"}

#### len()関数とsum()関数
- len()関数はリストの長さを取得します。
- sum()関数は合計を返します。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 269
  status: ok
  timestamp: 1682738530008
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: fTdGH8mM69J_
outputId: b79d27a5-d94f-4cf3-c622-287fdf5f52a4
---
a = [1, 2, 3, 4, 5]
len(a)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 266
  status: ok
  timestamp: 1682738544203
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bU99o-50CGB1
outputId: 8cdd3ddc-4b80-489b-9338-0afa30c0d2f6
---
len("Hello!")
```

```{code-cell} ipython3
:id: U6nSrI3fCNGw

del(sum)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 278
  status: ok
  timestamp: 1682738587381
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Ipp5dSBAz8b4
outputId: 90b3c895-577b-4524-cf3c-062884e4e072
---
a = [1, 2, 3, 4, 5]
sum(a)
```

+++ {"id": "6BQJ69eh69J_"}

#### del文とremove()メソッド
- リストの中身を削除するにはdel文を使います。インデックスを指定すると、該当要素が削除されます。
- あるいは要素が分かっているときは、remove()メソッドで削除することもできます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 288
  status: ok
  timestamp: 1682738598864
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: GV5p1XaD69KA
outputId: 79284925-52db-494f-bb63-8c0f9277d047
---
del a[2]
a
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 395
  status: ok
  timestamp: 1682738620226
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 6YnJq-lB69KA
outputId: 53c39249-2ae5-4d14-f8fd-7de7d5c0abcf
---
a.remove(5)
a
```

+++ {"id": "-rPqnquH69KA"}

#### index()メソッド
- 要素のインデックスを知りたい場合はindex()を使います。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 242
  status: ok
  timestamp: 1682738633851
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: aBcOh-X069KA
outputId: 70dfb04f-cb13-4ef2-909b-69188854c77e
---
a = [1, 2, 3, 4, 5]
a.index(2)
```

+++ {"id": "S12LTB8A69KB"}

### append()とextend()
- append()は要素を最後方から１つ追加します。
- for文と組み合わせて使うことが多いです。
  - リスト内包表記でよりシンプルに書ける（後述）

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 4
  status: ok
  timestamp: 1682738652182
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: o24jiohY69KB
outputId: 47564faf-04d5-45c2-beaa-7356bcb098f0
---
a.append(6)
a
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 353
  status: ok
  timestamp: 1682738686935
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: qzhUmtykw4Bw
outputId: 50992b63-cacd-4c60-8192-ec45d959f3d6
---
#1-100の整数から3の倍数をリストに格納
a = []
for i in range(1,101):
  if i % 3 == 0:
    a.append(i)
print(a)
```

+++ {"id": "PIpO5A_j69KB"}

- 複数追加したい場合は、extend()を使います(+演算子を使うこともできます)。
- append()を使うと、リストが要素として追加されるので注意。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 237
  status: ok
  timestamp: 1682738707244
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: _4E5-Ebc69KB
outputId: e41f40b1-c8b2-4968-96e0-b67a82580520
---
a + [7,8,9]
```

```{code-cell} ipython3
:id: keIOrlXM69KB

a.extend([7,8,9])
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 253
  status: ok
  timestamp: 1682738718837
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: xb6-XUl-69KB
outputId: 0917cd8a-b3e3-4e70-9277-693fe51825d8
---
a
```

```{code-cell} ipython3
:id: UrZfqygX69KB

a.append([7,8,9])
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 255
  status: ok
  timestamp: 1682738731397
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: mbaBa5Sm69KC
outputId: 6ab580e9-bc1c-4b7d-9113-e71240420492
---
a
```

+++ {"id": "JZdgjAam69KC"}

#### 数える。count()メソッド
- ある要素がリスト内にいくつあるかを調べるにはcount()メソッドを使います。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 282
  status: ok
  timestamp: 1682738744499
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ffQQCR3U69KC
outputId: 6e77e5cb-b041-4cb3-9cd9-6fb79979af83
---
a = [1,1,2,2,2,3]
a.count(2)
```

+++ {"id": "3FV2mfptvPZW"}

### 文字列を要素とするリストの結合、join()メソッド
- " ".join([文字列の要素])とすると、要素が " "を間の区切りとしてつながる。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 255
  status: ok
  timestamp: 1682738756027
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: gu3kBpeJvO_H
outputId: b1621230-196a-48e6-e5e4-88c327c1da4f
---
mylist = ["apple","banana","orange","grape"]
" ".join(mylist)
```

+++ {"id": "gCVkqVfB69KD"}

#### ソート
- リストを要素でソートするには、２つの方法があります。
- まずsort()メソッドを使う方法。この場合、リストの中身自体が変更されます。
- 関数sorted()を使う方法では、リストの中身は変更されず、返り値としてソートされたリストが返されます。
- 降順にしたい場合にはreverse=Trueとします。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 290
  status: ok
  timestamp: 1682738792078
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: C3Sym6I_69KD
outputId: e316902e-a1c6-47ee-8485-80e6988bde64
---
a = [5,3,1,2,4]
a.sort()
print(a)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 229
  status: ok
  timestamp: 1682738823560
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: k5oDX0Rg69KD
outputId: 710fce64-dd24-4475-dce1-b71115e9130f
---
a = [5,3,1,2,4]
sorted(a)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 226
  status: ok
  timestamp: 1682738831460
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: LCz3RqCf69KE
outputId: 3a7868ae-0ddd-4009-d08c-eda51a27eba8
---
a#aの中身は変わらない
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 266
  status: ok
  timestamp: 1682738844475
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 2ZullLK969KE
outputId: b30ee20a-f5f8-4f45-c19f-451df47c9d36
---
b = sorted(a)#ソート結果を別の変数に代入
print(b)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 274
  status: ok
  timestamp: 1682738848284
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bAa1ZR5w69KE
outputId: 004df878-e63a-48d4-c99f-e6df938fa197
---
print(a)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682738873209
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: EfzjEmXp69KE
outputId: 99047457-722f-4a4d-e624-0960a8a5857a
---
sorted(a, reverse=True)
```

+++ {"id": "WR8a0n3Wt5Lo"}

## 問題4

+++ {"id": "qbwqN853uLYq"}

#### 問題 4-1
与えられた文字列textからすべての空白を削除してください。


```
text = "This is a sample text."
```



```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 286
  status: ok
  timestamp: 1682742949033
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: sY1mXAeyS0o9
outputId: fe55bb48-f4a5-4189-894f-955ba320f289
---
text = "This is a sample text."
text.replace(" ","")
```

+++ {"id": "pS5BkmsbuMao"}

####問題4-2
与えられた文字列textを空白で分割し、単語のリストを作成してください。


```
text = "This is a sample text."
```



```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 266
  status: ok
  timestamp: 1682742992565
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: IxabUH2pTBWv
outputId: 13122abf-47ca-44a0-aef5-e7b318550361
---
words = text.split(" ")
print(words)
```

+++ {"id": "PhIQrpXGurHN"}

####問題4-3


与えられた文字列textをカンマで分割し、それぞれの要素を大文字に変換して、新しいリストを作成してください。



```
text = "apple,banana,orange,grape"
```


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 244
  status: ok
  timestamp: 1682743111025
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 7bYEUPH1TNZ4
outputId: 7eaa47d7-b1af-4c3a-d110-adfcad2fba41
---
text = "apple,banana,orange,grape"
words = text.split(",")
upper_words = []
for word in words:
  upper_words.append(word.upper())
print(upper_words)
```

+++ {"id": "8MN1AsTe2uAY"}

問題4-4
- 次のリスト、["Spencer", "is", "dead."]を操作して、一つの文字列"Spencer is dead. "にせよ。

- 次の文字列、"Spencer is dead. But who killed him and how? This is the problem."、の'.'と'?'を削除したあと、小文字の単語を要素としたリストに変換せよ。
  - →のようにする['spencer', 'is', 'dead', 'but', 'who', 'killed', 'him', 'and', 'how', 'this', 'is', 'the', 'problem']



```
mylist = ["Spencer", "is", "dead."]
TP = "Spencer is dead. But who killed him and how? This is the problem."
```


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 256
  status: ok
  timestamp: 1682743140896
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: NX8swN69Tm24
outputId: 76b2fe9b-4e56-458a-9ba4-9c9b8baaebd6
---
mylist = ["Spencer", "is", "dead."]
TP = "Spencer is dead. But who killed him and how? This is the problem."
" ".join(mylist)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682743233689
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: uJuz3nJ1TrG5
outputId: 2887ae98-6122-4fbe-b3c2-beb75fd002e8
---
TP.lower().replace(".","").replace("?", "").split(" ")
```

+++ {"id": "nWoLUhv469Jr"}

## ディクショナリ
- ディクショナリは、keyとvalueからなり、マップ型と呼ばれる型に属する。
- {}でくくって、作成する。{key:value}と書く。
- シーケンス型ではないのでインデックスは使えない。代わりにkeyを指定して要素を取り出します。要素は基本的にどのような型でもOK。
- ディクショナリもしばしばネストされる。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 258
  status: ok
  timestamp: 1682743297829
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: tduqWNqa69Js
---
d={'A':'Apple','B':'Banana'}
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 6
  status: ok
  timestamp: 1682743298715
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: dm7lrLkF69Js
outputId: e7579af9-5060-4b79-a1d8-d92a40fe914f
---
d['A']
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 282
  status: ok
  timestamp: 1682743311198
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 92jw4w2j69Js
---
nested_d = {'nest':d}
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 254
  status: ok
  timestamp: 1682743333545
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: t3JFqxgT69Js
outputId: 6269b743-863a-4720-f2fa-d4394b2a62e7
---
nested_d['nest']
```

+++ {"id": "wBCDxqN069KL"}

### ディクショナリ操作

+++ {"id": "4dyUzqLf69KM"}

#### ディクショナリに新しい項目を加える
- 空の辞書に新しい項目を加えるには、新しくkeyを指定してvalueを代入すればよい。
- もちろん既存の辞書に新しい項目を加えることもできる。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 244
  status: ok
  timestamp: 1682743363206
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: hJO4eaOsUfOL
---
d = {}
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 1
  status: ok
  timestamp: 1682743364580
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bHRHaPNj69KM
---
d['ゲオルグ'] = 1858
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 396
  status: ok
  timestamp: 1682743366388
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: L1FCMyxV69KM
outputId: d52a99d0-d3d5-49a9-88c9-df47e79bfe58
---
d
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 313
  status: ok
  timestamp: 1682743369552
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: yWhPrbTF69KM
---
d = {'マックス':1864,'エミール':1858}
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 248
  status: ok
  timestamp: 1682743372520
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 4pCT1JA-69KM
---
d['ゲオルグ'] = 1858
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 249
  status: ok
  timestamp: 1682743374496
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: WXyxX6gl69KN
outputId: 66f65a65-34b6-4a52-81bc-9cb333508eee
---
d
```

+++ {"id": "427bbX5f69KN"}

#### ２つの辞書の統合：update()メソッド
- 2つの辞書を統合するにはupdate()メソッドを使います。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 4
  status: ok
  timestamp: 1682743389697
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 86blxD0h69KN
---
e = {'タルコット':1902,'ロバート':1910}
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 328
  status: ok
  timestamp: 1682743392909
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: KgR3cIa769KN
outputId: 192a8d43-f281-4d0b-9651-b191e6e8ed75
---
e
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 239
  status: ok
  timestamp: 1682743404818
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: WekxRIJM69KN
---
d.update(e)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: joj7qd4u69KN
outputId: 0d1d6bc1-4fd6-433a-b6b7-f8efd0956f2a
---
d
```

+++ {"id": "J31_AoSV69KN"}

#### key, value, itemの取得
- それぞれ、keys(), values(), items()とすると取得できる。
- items()はkeyとvalueのタプルを要素とするリスト形式のオブジェクトを返す。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 235
  status: ok
  timestamp: 1682743420333
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: TNGHq2cM69KO
outputId: 830a3e1e-ce9d-4758-b638-e10d8fd45637
---
d.keys()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 355
  status: ok
  timestamp: 1682743432065
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: GQpfy0_o69KO
outputId: 839597c8-4f64-44e0-e62f-25a29709f651
---
'ガブリエル' in d.keys()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 245
  status: ok
  timestamp: 1682743436948
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: xoDexBYD69KO
outputId: 1f306f51-48bf-4753-9912-9b0ecaa31731
---
d.values()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 247
  status: ok
  timestamp: 1682743443151
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: uXiNzjzm69KO
outputId: 1f46db1e-a7fe-47ff-95a4-93107b867960
---
d.items()
```

+++ {"id": "TkY5mcvY69KO"}

#### get()メソッドによるvalueの取得
- ディクショナリのvalueはkeyを指定して取れるが、keyが存在しない場合はエラーが出る。
- get()メソッドを使うとkeyが存在すれば、valueを返し、存在しなければ何も返さない（Noneを返す)。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 295
  status: ok
  timestamp: 1682743458743
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ZdEWOjCM69KO
outputId: 8276815e-127d-485c-951c-57ffd8d7e460
---
d['マックス']
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 172
executionInfo:
  elapsed: 269
  status: error
  timestamp: 1682743462651
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 6d0eGUXa69KP
outputId: 36fa36f1-4f8b-4d16-a10a-51088587af9e
---
d['ガブリエル']
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 243
  status: ok
  timestamp: 1682743478375
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: h6oGJyXU69KP
outputId: 0f7f5ed5-9ae2-432c-e412-ea5a5b081546
---
if d.get('マックス'):
    print(d['マックス'])
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 250
  status: ok
  timestamp: 1682743490839
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: qSQioC2Q69KP
outputId: 126a1c2b-7684-4717-b9ec-d0e17ebedd4d
---
if d.get('ガブリエル'):
    print(d['ガブリエル'])
else:
    print('そのkeyは存在しません')
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682743505474
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: hYAAjE_PVCqI
---
d.get('ガブリエル')
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 172
executionInfo:
  elapsed: 248
  status: error
  timestamp: 1682743519794
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 1ijd-8LMVFRM
outputId: 73c10ce8-a792-4e12-a1cf-6c83c1c19c28
---
d['ガブリエル']
```

+++ {"id": "jPwTN7Mf8e74"}

##### コメント
- ifの条件節はNoneだとFalse、それ以外はTrueを返す

+++ {"id": "H-mWbFFb69KP"}

#### ディクショナリのループ
- ディクショナリの中身をループするときには、d.items()を使う。
- key, valueのペアをループする。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 242
  status: ok
  timestamp: 1682743544400
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: OebLDdUx69KP
outputId: 6043b4d4-69f7-4630-e525-1129b2c410c2
---
d.items()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682743579190
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: lQIDqItm69KP
outputId: d433bff2-e33d-4688-af06-77337337e5ea
---
for key, value in d.items():
    print(f'{key}:{value}')
```

+++ {"id": "ZufRo41F80un"}

##### コメント
- for文のinの前の項目は複数でもよい。

+++ {"id": "tzdEZlaO69KP"}

#### ディクショナリのソート
- ディクショナリをvalueでソートしたい場合は一工夫必要です。sorted()を使えますが、ソートのkey（ディクショナリのkeyではない）として、lambda関数というやり方を使い、ディクショナリのvalueをソートのkeyとすると指定します。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 261
  status: ok
  timestamp: 1682743658442
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: N3o3ff4V69KQ
outputId: 7a1c5586-2714-4109-b345-080e0b03965e
---
sorted(d.items(), key = lambda x : x[1])
```

+++ {"id": "DANvGeT2yvax"}

## 問題5

+++ {"id": "gDK3J-NIyxju"}

####問題5-1
空の辞書gradesを作成し、次のキーと値のペアを追加してください。

'math': 85
'science': 90
'english': 88

```{code-cell} ipython3
---
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682743942361
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: LFXPuJ36WiID
---
grades = {}
grades['math'] = 85
grades['science'] = 90
grades['english'] = 88
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 326
  status: ok
  timestamp: 1682743947057
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: D1AsOs3nWuQX
outputId: 49d05cc9-b2e9-4cea-e70c-52fa253a2ed3
---
grades
```

+++ {"id": "2pZw038Oy70S"}

#### 問題5-2
与えられた辞書studentのキーと値をイテレートし、次の形式で出力してください

key: value


```
student = {'name': 'John', 'age': 21, 'major': 'Computer Science'}
```


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 7
  status: ok
  timestamp: 1682744000315
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: LCr13IlZWxNr
outputId: 28eb509a-9671-4b6b-981b-f27d132301f1
---
student = {'name': 'John', 'age': 21, 'major': 'Computer Science'}
for key, value in student.items():
  print(f'{key}:{value}')
```

+++ {"id": "3AAL4zko0D4J"}

#### 問題5-3
与えられた辞書pricesのすべての値の合計を計算してください。



```
prices = {'apple': 1.5, 'banana': 0.5, 'orange': 0.75}
```


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 3
  status: ok
  timestamp: 1682744032537
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Ro300kU9XBP1
outputId: a9fc1953-b916-4fa0-84a9-250e1f76b702
---
prices = {'apple': 1.5, 'banana': 0.5, 'orange': 0.75}
sum(prices.values())
```

+++ {"id": "4OZpO-nG0dLw"}

####問題5-4
5-1で作成したgradeを値でソートしてください。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 272
  status: ok
  timestamp: 1682744093244
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: jt2weHmNXFx2
outputId: 178e5b66-d87d-4d59-cc8c-8534e9410c2f
---
sorted(grades.items(), key = lambda x: x[1])
```

+++ {"id": "fM8ISm3C69Jt"}

##  タプル
- リストに似ていますが、イミュータブルであるという点で異なります。不用意に要素が変更されることがないのでリストよりも安全です。
- ()でくくって作ります。
- リストのように要素に代入しようとするとエラーが発生します。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 263
  status: ok
  timestamp: 1682744115673
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: f8xJ1ZgZ69Jt
---
t=(1,2,3,4,5)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 172
executionInfo:
  elapsed: 255
  status: error
  timestamp: 1682744126481
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: azBWSamQ69Jt
outputId: a88c5c5f-dc04-48a4-bec1-43a49fb4ca65
---
t[0] = 5
```

+++ {"id": "L2wi_6-R69J8"}

## モジュール（ライブラリ）
- Pythonではモジュールと呼ばれるプログラムパッケージが多数存在する。
-  モジュールは以下に分かれる。
  - 1)Pythonにあらかじめ組み込まれているもの
  - 2)Colabに最初から入っているもの
  - 3)その他、別個インストールが必要となるもの
- 3)については、pip install, conda installなどとして別個インストールが必要になる。
- モジュールを読み込むときは"import XX"とする。"import XX as Y"とすると、Yという名前で使うことができる。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682744272286
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Ax7havjB0WBH
outputId: 812c07e9-a999-4348-aff1-0c0a71742f03
---
import random
random.choice([1,2,3,4,5,6])
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 112
executionInfo:
  elapsed: 9
  status: ok
  timestamp: 1682744311095
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: FePCd4Ny1AsC
outputId: d4ed5c21-8bf4-40e5-e12e-77552834f4ba
---
import pandas as pd
pd.DataFrame({"A":[1,2],"B":[3,4]})
```

+++ {"id": "z91RMZNi69KQ"}

## いろいろなプログラミングテクニック

+++ {"id": "5TIl4dJx69KQ"}

#### forloopの進んだ使い方。enumerateとzip
- リストをループしているときにそのインデックスもあわせて取得したい場合があります。
- enumerate()を使ってループすると、インデックスと要素を使ってループすることができます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 275
  status: ok
  timestamp: 1682744379523
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: mlVoGWzM69KQ
outputId: 59975587-9570-4cc5-c538-b5ad314f5f26
---
l = ['エミール', 'ゲオルグ','マックス', 'タルコット', 'ロバート']
for idx, name in enumerate(l):
    print("私（{}）のインデックスは{}番です".format(name,idx))
```

+++ {"id": "UlyCFwS669KQ"}

- zip()を使うとペアごとにループできます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 251
  status: ok
  timestamp: 1682744471617
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Avg9_zs769KQ
outputId: 6ba338cd-58d7-49ea-b380-3b11fd876cf7
---
l = ['エミール', 'ゲオルグ','マックス', 'タルコット', 'ロバート']
m = ['デュルケム','ジンメル','ウェーバー','パーソンズ','マートン']
for first,last in zip(l,m):
    print("私は{}・{}です".format(first,last))
```

+++ {"id": "sITeZo9H69KQ"}

#### リスト内包表記

+++ {"id": "QcUI4IA969KQ"}

- [item for item in list]のような形でリストの内部でfor文を使う方法。
- さらにifで条件付けることができる。
  - ifのみの場合はforの後。
  - if else で条件付けるときはforの前に来る。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 525
  status: ok
  timestamp: 1682744531755
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: AthaHP4B5eQk
outputId: bca4e8f2-53e5-4952-e76a-323b6143f093
---
nums = [2, 4, 5, 6, 8, 10, 12]
new_nums = [num // 2 for num in nums]
print(new_nums)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 253
  status: ok
  timestamp: 1682744562255
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: YiD6SYIM6AnB
outputId: 5f41b01f-4622-4098-bc41-735fc9b7b6d2
---
nums = [2, 4, 5, 6, 8, 10, 12]
new_nums = [num // 2 for num in nums if num > 5]
print(new_nums)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 252
  status: ok
  timestamp: 1682744602591
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: l8yqN9cr5c4K
outputId: dca42c9f-8a81-494e-d625-3c47b96d307e
---
nums = [2, 4, 5, 6, 8, 10, 12]
new_nums = [num // 2 if num > 5 else num for num in nums]
print(new_nums)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 245
  status: ok
  timestamp: 1682744624125
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Ieiw_TIa69KR
outputId: d6c11c19-3fb9-4e18-c11f-aa76982b1ffc
---
d = {'マックス': 1864, 'エミール': 1858, 'ゲオルグ': 1858, 'タルコット': 1902, 'ロバート': 1910}
statement = [f"私（{key}）の誕生年は{value}年です" for key, value  in d.items()]
statement
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 242
  status: ok
  timestamp: 1682744627264
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Ut01gO1A69KR
outputId: 4a2271ff-c669-492f-cf89-91be016905f5
---
[f"私（{key}）の誕生年は{value}年です" for key, value  in d.items() if int(value) >1900]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 401
  status: ok
  timestamp: 1682744637214
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: YU4_dLK06W6W
outputId: bed46629-d810-482d-bd5e-e486cafbde06
---
[f"私（{key}）の誕生年は{value}年です" if int(value) >1900 else "" for key, value  in d.items() ]
```

+++ {"id": "XtlFzlMG7B-Q"}

## 問題6


+++ {"id": "JzVNIGmf8k1M"}

#### 問題6-1
与えられたリストnumsの各要素の値とそのインデックスを掛けた新しいリストを、リスト内包表記とenumerateを用いて作成してください。


```{code-cell} ipython3
---
executionInfo:
  elapsed: 482
  status: ok
  timestamp: 1682744719796
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: BgcTPxamZfJK
---
nums = [1,2,3,4,5]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 386
  status: ok
  timestamp: 1682745050154
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: YFFQaKrVa1uz
outputId: 62fee93b-25fe-40b4-ceeb-1c544c8220e7
---
[num * index for index, num in enumerate(nums)]
```

+++ {"id": "YreQ_G479Fso"}

#### 問題6-2
与えられたリストnamesとagesを使って、"{name} is {age} years old"という形式の文字列のリストを作成してください。zipを用いてください。


```{code-cell} ipython3
---
executionInfo:
  elapsed: 4
  status: ok
  timestamp: 1682744721391
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: wINjTD9dZi8U
---
names = ["Alice", "Bob", "Carol"]
ages = [25, 30, 35]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 515
  status: ok
  timestamp: 1682745091226
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: -irYxgmfa99T
outputId: dbfaf67e-b1ab-4084-8036-09b5404c3dcb
---
[f"{name} is {age} years old" for name, age in zip(names,ages)]
```

+++ {"id": "GpQFXobl9Rfx"}

### 問題6-3
与えられたリストvaluesの各要素について、インデックスが偶数の要素は2倍し、インデックスが奇数の要素は3倍した新しいリストを作成してください。リスト内包表記とenumerateを用いてください。


```{code-cell} ipython3
---
executionInfo:
  elapsed: 278
  status: ok
  timestamp: 1682744749428
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: uBGl-BMXZuI0
---
values = [1,2,3,4,5]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 250
  status: ok
  timestamp: 1682745185634
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: CM5VOcDgbJcl
outputId: 303fd871-9670-4d25-d467-2ee62abb8ec5
---
[value*2 if index % 2 ==0 else value*3 for index, value in enumerate(values)]
```

+++ {"id": "-uY1NxDu69KR"}

## numpyについて
- numpyは数値計算用に開発された非常にポピュラーなモジュールです。数学的処理をする場合に不可欠なだけでなく、後で出てくるpandasなどのデータ処理用のモジュールはこのnumpyの機能を基礎にして組み立てられています。numpyを使うと、通常の方法よりも処理速度を大幅に上げることもできます。ここではそのさわりの部分だけを紹介します。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 258
  status: ok
  timestamp: 1682745243338
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: pO1S8BDQ69KS
---
import numpy as np
```

+++ {"id": "b5WoBFAP69KS"}

###numpy配列
- numpyの基本は配列(array)です。リストに似ていますが、同じ型の要素しか取れないなどいくつかの違いがあります。
- 配列はnp.array([])によって作ることができます。これは数学的にはベクトルに相当します。
- 2次元配列も作ることができます。数学的には行列にあたります。
- ベクトルや行列として演算したいときにはnp.dot()などを用います。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 319
  status: ok
  timestamp: 1682745263301
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: rdSkZTGS69KS
outputId: c8726e43-79a7-4e7a-c89f-51d3b1794df0
---
vec = np.array([1,2,3])
vec
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 301
  status: ok
  timestamp: 1682745278200
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: znDi5KW469KS
outputId: 00155200-a17f-4883-9930-315b71d7d0e5
---
mat = np.array([
              [1,2,3],
              [4,5,6],
              [7,8,9]
                ])
mat
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682745291989
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: EyKxBlVi69KS
outputId: 4033c75f-2d75-4fce-ae66-1e6fb053d395
---
mat2 = np.array([
              [10,20,30],
              [40,50,60],
              [70,80,90]
                ])
mat2
```

```{code-cell} ipython3
:id: VVvARQoM69KS
:outputId: 3b9ccfe4-b9c1-4a92-b3b5-44cb324dcd86

np.dot(mat,mat2)#1*10+2*40+3*70=300,...
```

+++ {"id": "7FdLO6XH69KT"}

### アダマール積とブロードキャスト
- '*'演算子は要素ごとのかけ算をかえす。これをアダマール積という。
- かけ算する行列同士の次元が異なる場合、ブロードキャストが行われる。簡単にいえば、次元が少ない方のオブジェクトを複数コピーして次元を合わせて演算する。

```{code-cell} ipython3
:id: 9oKWXKrN69KT
:outputId: 992bcb6d-2513-46be-86f8-d7e4ea4e8158

mat*mat2　#アダマール積1*10,...
```

```{code-cell} ipython3
:id: MkKbAs9T69KT
:outputId: d13913b7-209a-4ac3-ef25-eca4a17e9971

vec
```

```{code-cell} ipython3
:id: TjPQGRmx69KT
:outputId: c2e21239-0abb-4910-a289-149c51d8b265

mat
```

```{code-cell} ipython3
:id: orIc_iL-69KU
:outputId: 57562b82-cbd7-406f-9d9a-47a6c801f0b2

mat * vec
```

+++ {"id": "woB4uReu69KU"}

### インデックスによる選択
- インデックスによる選択はリスト等に似ていますが、リストで選択する機能が追加されています。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 261
  status: ok
  timestamp: 1682745584674
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: vPd3conO69KU
outputId: f6e7529f-ede9-4909-e43c-208415606542
---
mat[:2,1]
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 245
  status: ok
  timestamp: 1682745593074
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Ni1N9Wf169KU
outputId: 65910716-2356-4b4e-b244-54181b4bfd83
---
mat[[0,2],:]
```

+++ {"id": "FzaovK_L6S4x"}

#### 零行列、単位行列など
- np.zeros()を使うと、ゼロからなる行列を作ることができる。
- np.eye()は単位行列を作る。
- その他、np.ones()など類似の関数もいくつか用意されている。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 236
  status: ok
  timestamp: 1682745617146
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: JLvKGd3k69KU
outputId: 8cb762d4-08c0-4001-c46c-3fdb83225755
---
np.zeros([3,3])
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 251
  status: ok
  timestamp: 1682745624736
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: yUwuBKeT6oYn
outputId: 07ed5e32-4d06-4cb2-d1f2-03224028a4f8
---
np.eye(3)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 237
  status: ok
  timestamp: 1682745633610
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: RPeT0KUN69KU
outputId: 03580165-600d-4e30-c107-ac42843d4435
---
np.ones([3,3])
```

+++ {"id": "3RSnzbrk69KV"}

### 数学関数とapply
- np.sum()やnp.mean()などの多くの数学関数が用意されている。
- np.apply_along_axis()を使うと行ごとや列ごとに数学関数を適用できる。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: PQFbOcMn69KV
outputId: 9acf9ca1-2b6f-4d23-c73f-962105c642bb
---
mat
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 245
  status: ok
  timestamp: 1682745652970
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 6hoc9iWs69KV
outputId: 75f79e30-4b8e-45c9-890c-a2fdc7ef6c01
---
np.mean(mat)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 256
  status: ok
  timestamp: 1682745654457
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: sZltNcx07EOu
outputId: c62eb53a-7147-42a0-bb52-5360fbef37de
---
np.sum(mat)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 236
  status: ok
  timestamp: 1682745706838
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bWo41wpn69KV
outputId: 0d704f56-fc5f-4f28-9dd5-a8efa89608af
---
np.apply_along_axis(np.sum, 1, mat)#行の足し算
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 248
  status: ok
  timestamp: 1682745708177
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: L1QQqP5869KV
outputId: 8d21b027-92cc-4b4f-a816-69694a8dd59b
---
np.apply_along_axis(np.sum, 0, mat)#列の足し算
```

+++ {"id": "3zXNh6d2BsR_"}

## ディレクトリ構造とLinuxコマンド
- Colabはクラウド上のLinuxコンピュータで、図のようなディレクトリ（Winでいうフォルダに相当）構造を持っている。

<img src="https://raw.githubusercontent.com/berutaki/github.io/main/1-5.png" width="300">

- (Colab)から見て外部ドライブ（各自のグーグルドライブ）を接続するにはマウントをする必要がある。

- マウントの場所を''/content/drive'と指定するとcontentディレクトリの直下にMy diriveが接続される。

<img src="https://raw.githubusercontent.com/berutaki/github.io/main/1-6.png" width="300">


```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 29212
  status: ok
  timestamp: 1682745939099
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: bOJr6f26DhR7
outputId: b23f810c-106b-4136-c0f2-c5daf81f1edd
---
from google.colab import drive
drive.mount('/content/drive')#実行すると許可を求められるが、すべてOKする。
```

+++ {"id": "FLInl94nNkFV"}

### Linuxコマンド
- Colabでは'!'を頭につけることでLinuxのコマンドを入力できる（ただし、サブプロセスで実行されるため意図した動作をできないこともある）。
- '%'はIPythonのマジックコマンドで'!'と同じようなことができる（pipなどは不可）。以下では基本的に'%'を使う（実は何もつけなくても以下のコマンドは動く）。
- 'pwd'は現在のワーキングディレクトリを表示。
- 'cd'はディレクトリの移動。
- 'ls'はディレクトリやファイルのリストの表示
- 'mkdir'はディレクトリの作成
- 'rm -r'はディレクトリの削除

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 646
  status: ok
  timestamp: 1682745998191
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ymeOPskWehkt
outputId: f9bbec58-1af5-4e81-ffcd-67edee4588c6
---
!pwd
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 322
  status: ok
  timestamp: 1682746030202
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: qpbPJhx7NjUH
outputId: a60e9f74-1f30-457d-88e4-9bb5904544e2
---
%pwd
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: ZsPZKRppO8zR
outputId: 40b9ee8d-c018-49a4-9439-824d0b33127c
---
%cd /content/drive/MyDrive/cssws2023
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 258
  status: ok
  timestamp: 1682746085288
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 6ASIK659O_2j
outputId: 5af9e3dc-66d7-4f6b-f96e-8272fc70c561
---
%ls
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 2
  status: ok
  timestamp: 1682746117428
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: rkzX91Xwe_pa
outputId: 6abbbaeb-0437-4003-fe3b-503ee67a562d
---
%cd drive
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 333
  status: ok
  timestamp: 1682746126248
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: F1oDEDfNfCUL
outputId: 9b865f06-8879-4925-b864-a7196d0bb473
---
%ls
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 263
  status: ok
  timestamp: 1682746166147
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: FS3U9205fJZV
outputId: 588d9443-fb0b-4a77-b7a8-48e6198b2ad5
---
%cd MyDrive
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 440
  status: ok
  timestamp: 1682746172298
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: LTJIRlwRfNRq
outputId: f51aafea-b86e-4ac4-d4a6-b1b1f9d67205
---
%ls
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 362
  status: ok
  timestamp: 1682746208912
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: sknmTkZ9fVP6
outputId: 75d1842f-0a68-4881-d30d-5fe770d23256
---
%cd cssws2023
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 388
  status: ok
  timestamp: 1682746215655
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: -vmnir87fYKr
outputId: cedbe285-adff-4f24-8237-1a46a280fd23
---
ls
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 252
  status: ok
  timestamp: 1682746242410
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: FehhgSFNPbiS
---
%mkdir test
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 270
  status: ok
  timestamp: 1682746245948
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 8qTVxokgRYue
outputId: ed70dfea-1109-4b60-ff49-425741399d36
---
%ls
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 243
  status: ok
  timestamp: 1682746260373
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: TMQx1O7YRZ4k
---
%rm -r test
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 257
  status: ok
  timestamp: 1682746266707
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: jzFjKJF_fkZe
outputId: 75b0c294-4ca6-4690-b4d4-58a89c521e25
---
%ls
```

+++ {"id": "2Z9mQDSERjB7"}

#### パスとcd
- /content/drive/MyDrive/cssws2023は絶対パスでディレクトリやファイルの場所を示す住所のこと。
- 相対パスはカレントディレクトリから見た場所を示す。例えば、MyDriveにいるときに絶対パス /content/drive/MyDrive/cssws2023を相対パスで表せば /cssws2023 となる。
- 'cd ..'はカレントディレクトリの一つ前のディレクトリへいく。
- ' cd -'は直前にいたディレクトリに戻る。
- 'cd ~'はhomeに戻る（Colbaでは/root）

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 295
  status: ok
  timestamp: 1682746410186
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: J-0Pj8Bpfw7u
outputId: 6b5bce9e-6f37-44c9-fb40-28e413be3865
---
%cd /content/drive
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 500
  status: ok
  timestamp: 1682746438147
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: YZTcXZVDfzTF
outputId: 53053fe4-6bac-443c-8ec0-665e2676990d
---
%cd MyDrive/cssws2023
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 533
  status: ok
  timestamp: 1682746494778
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: i7XdFfVKgben
outputId: 18505347-4ac0-40db-f674-765676a85049
---
%cd ..
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 531
  status: ok
  timestamp: 1682746511883
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: c0STHKxugfwv
outputId: 9c760660-7c13-4d10-fdac-bd4319f211ea
---
%cd -
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 251
  status: ok
  timestamp: 1682746528928
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: P4_Cy_0Lgi45
outputId: b270ce52-56fe-4807-fb21-a309c816663b
---
%cd ~
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
id: M1smrxPES4yP
outputId: 017f37a1-0a9a-4e0d-c74e-fa4a15aab408
---
%pwd
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: 9UC_S8uVS6OF
outputId: ab93894b-11e4-4176-ada6-354e3c6d1784
---
%cd ..
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: cDGSO-tWRh04
outputId: fdf76f2c-95a6-4615-a0e6-a5526028100b
---
%cd -
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: 6YKRQr2AS9Xu
outputId: 55ce33d4-60a6-4122-f6d5-d5158684a0c5
---
%cd ~
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 267
  status: ok
  timestamp: 1682746554349
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: iIclD3s-Rcnu
outputId: a0b98743-7a4d-45d8-a541-b9762e3ceb0a
---
%cd -
```

+++ {"id": "5uAcXxVYFb4v"}

### osによるディレクトリ、ファイルの操作
- osライブラリでディレクトリやファイルを操作すると便利なことがあります。
- mkdir()でディレクトリを作る。
- os.path.exists('test')で確かめてなければ作る。
- os.listdir()でディレクトリ内のファイルを取得。
- globライブラリを使うと条件を指定してファイルを取得できる。
- os.remove()でファイルを消す。
-  ディレクトリを消すには、shutilライブラリのrmtree()を使う。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 404
  status: ok
  timestamp: 1682746632892
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: gq2V9U06Fl2Z
---
import os
os.mkdir('test')
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 10
  status: ok
  timestamp: 1682746641450
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: a30rQRMHg_3P
outputId: e3eaa3a5-cc93-4ce1-bd36-2a6c0789b183
---
%ls
```

+++ {"id": "hJMjvKgNFvUD"}

- os.path.exists()とすると、当該ファイルが存在するかどうかを確認できます。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 7
  status: ok
  timestamp: 1682746664648
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 79gxlcnI7YtR
outputId: 7485f71a-4fcd-48db-cea8-464c522a77a8
---
os.path.exists('test')
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 494
  status: ok
  timestamp: 1682746686014
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 8aEQwnJhFruS
---
if not os.path.exists('test2'):
  os.mkdir('test2')
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 281
  status: ok
  timestamp: 1682746701727
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: GCBCDfop8HFE
---
#操作練習用テキストファイル
with open ('text1.txt','w') as f:
  pass
with open ('text2.txt','w') as f:
  pass
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 418
  status: ok
  timestamp: 1682746709449
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: y2b4qge9hQu_
outputId: f8ee15e6-0b08-4712-f00d-f932ae873209
---
ls
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 327
  status: ok
  timestamp: 1682746740377
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: qlGrJPhyF40Y
outputId: 0a7e1688-7c33-498c-d86b-d057f27ac132
---
my_listdir = os.listdir()
print(my_listdir)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 404
  status: ok
  timestamp: 1682746843049
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: k5tRc7vKGQN5
outputId: c35457f9-1de9-4e5d-c2f0-9fc1664c26e2
---
import glob
glob.glob('*.ipynb')
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 299
  status: ok
  timestamp: 1682746864937
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: XkJ09WYd9XWA
---
os.remove('text1.txt')
os.remove('text2.txt')
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 257
  status: ok
  timestamp: 1682746877219
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: y29u5OtdGgyU
---
import shutil
shutil.rmtree('test')
shutil.rmtree('test2')
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 284
  status: ok
  timestamp: 1682746888832
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: cwSV3MWx9cbz
outputId: bb6766f5-aaf0-44d8-fee7-e938bbf587bd
---
os.listdir()
```

+++ {"id": "HMYAHIci69KY"}

## ファイルインプット／アウトプット
- Pythonではいろいろな方法で外部のファイルを読み込んだり、外部にファイルを出力することができる。
  - with open()を使う方法
  - csvモジュールを使う方法
  - pandasを使う方法
  - pickleを使う方法


+++ {"id": "1gXNHl_b-3M6"}

### open()による書き込み
- with open('hoge.hoge','w') as f:とすると、ファイルオブジェクトfを'w'書き込みモードで作り、'hoge.hoge'に書き込む。
- withを使わずにもかけるが、ファイルオブジェクトをクローズする必要がある。
- 'a'で開くと上書きモードとなる。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 266
  status: ok
  timestamp: 1682746967213
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: -Btrqc-d_IGY
---
d = {'マックス': 1864, 'エミール': 1858, 'ゲオルグ': 1858, 'タルコット': 1902, 'ロバート': 1910}
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 258
  status: ok
  timestamp: 1682747056288
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: QFRunYVU_8U8
---
with open('sample.csv','w') as f:
  for key, value in d.items():
    f.write(f"{key},{value}\n")
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 384
  status: ok
  timestamp: 1682747063239
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: N_148DTxim3m
outputId: c2ca7ca6-927d-40d3-fcc9-85ca1428adbe
---
%ls
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 727
  status: ok
  timestamp: 1682747076669
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: KwoXk9uXipZ3
outputId: 6124dba3-0890-4cb9-a983-aae60b1be791
---
%cat sample.csv
```

```{code-cell} ipython3
:id: Q9e5my7SAisA

f = open('sample.csv','w')
for key, value in d.items():
  f.write(f"{key},{value}\n")
f.close()
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
id: NgANqmff_mN6
outputId: 39adb9f0-0582-465f-a91b-9d1d578b5f7b
---
%cat sample.csv
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 346
  status: ok
  timestamp: 1682747156527
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: _2DOjO1kA6OF
---
with open('sample.csv','a') as f:
  key = "ニクラス"
  value =  1927
  f.write(f"{key},{value}\n")
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 261
  status: ok
  timestamp: 1682747159693
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: KLa-UICuBueE
outputId: 03a7a37d-cfd2-4aac-ff50-5f5eca646cb8
---
%cat sample.csv
```

+++ {"id": "aG4GJa6q-hot"}

### open()による読み込み
- open()を使って"r"読み込みモードで開く。
- Windowsでは文字コードが異なるので、encoding = 'utf-8'とする。
- read()メソッドでは、ファイルが一つの文字列として読みこまれる。
- readlines()は改行コード(\n)で区切ったリストを返す。
- readline()はファイルを一行ずつ呼んでいきます。whileの無限ループを使って次々に呼び出していき、最後まで読むと、空の文字列を返すので、if notで条件づけてbreakで無限ループを脱出する。
- 注意。ファイルオブジェクトは１回呼び出すと中身が更新される（例えば、f.read()をすると、fの中身は空になります。）

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 35
executionInfo:
  elapsed: 246
  status: ok
  timestamp: 1682747233761
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: VwntrZrT69KY
outputId: 9138429a-c11a-4da6-e135-e034f6a4e339
---
with open('sample.csv','r',encoding = 'utf-8') as f:
  sample = f.read()
sample
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 256
  status: ok
  timestamp: 1682747272382
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: R5aLESw669KZ
outputId: de88d5f5-98ad-4452-a16b-84f2dc431293
---
with open('sample.csv','r',encoding = 'utf-8') as f:
  sample = f.readlines()
sample
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 318
  status: ok
  timestamp: 1682747317872
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: hsxVANg069Kb
outputId: 698ef684-c60f-4b8b-8c0c-2600674be644
---
with open('sample.csv','r',encoding = 'utf-8') as f:
  while True:#一行ずつ読み込んでいき、空になったらbreak
      line = f.readline()
      print(line)
      if not line:
          break
```

+++ {"id": "Ffa4LfVe69Kc"}

#### csvによる書き込み
- csv.writer()で書き込み用オブジェクトを作成。
- writerow()メソッドを用いて、一行ずつ書き込む。
- wroterows()は二次元リストを一気に書き込む。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 239
  status: ok
  timestamp: 1682747426148
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: WuqvgReh69Kd
---
sample = [['マックス','1864'], ['エミール', '1858'], ['ゲオルグ', '1858']]
import csv
with open('sample.csv','w') as f:
    writer = csv.writer(f)
    for row in sample:
        writer.writerow(row)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 316
  status: ok
  timestamp: 1682747428989
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: VqpxAmRsGph5
outputId: 790952af-6d73-4c44-c359-4594ad67c358
---
%cat sample.csv
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 258
  status: ok
  timestamp: 1682747455981
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: iFZ44vo-JbaH
---
with open('sample.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(sample)
 
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 335
  status: ok
  timestamp: 1682747457475
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 7GlJHPTDJgA8
outputId: 56bd3f32-e476-4b0b-ce64-0ecaf96a754c
---
%cat sample.csv
```

+++ {"id": "78740vmGJnWH"}

### csvによる読み込み
- reader()メソッドでファイルを読み込む。
- for文で一行ずつ取り出す。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 295
  status: ok
  timestamp: 1682747501470
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: yT85zTcU69Kc
outputId: b5735718-9da1-4ee3-8bbf-231edd36f4e4
---
sample = []
with open('sample.csv','r') as f:
    reader = csv.reader(f)
    #print(type(reader))
    for item in reader:
        sample.append(item)
sample
```

+++ {"id": "Rbscprw5Lyjz"}

#### コメント
- csv.reader()で作られたreaderオブジェクトはイテレータと呼ばれるオブジェクトで、for 文で一個ずつ繰り返し呼び出して中身を取り出すことができる。

+++ {"id": "g_aWRBU869Kd"}

#### pandasで読み書きする。
- pandasのread_csv()メソッドを使うことでcsvをデータフレームとして読み込むことができる。
- to_csv()メソッドでデータフレームをcsvとして書き込むことができる。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 413
  status: ok
  timestamp: 1682747565199
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: WKeQn3CW69Kd
---
import pandas as pd
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 283
  status: ok
  timestamp: 1682747571119
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: YZQLHhM769Kd
---
dat = pd.read_csv('sample.csv', header = None)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
  height: 143
executionInfo:
  elapsed: 8
  status: ok
  timestamp: 1682747571952
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: mn_6CsCN69Kd
outputId: 34225f35-4f2a-4aaf-da80-591870dc5f36
---
dat.head()
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 475
  status: ok
  timestamp: 1682747594580
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: PcLKFK5l69Kd
---
dat.to_csv('sample.csv',index = False, header = False)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 298
  status: ok
  timestamp: 1682747595994
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: cyiY58QtMeWX
outputId: e611fb38-7202-4eed-aad8-799778a00b92
---
%cat sample.csv
```

+++ {"id": "ymViIWPiOAIC"}

### pickleで読み書きする
- pickleはPythonオブジェクトのままバイナリ形式で保存し、読み込む。処理がPythonのみで完結している際は推奨。
- 書き込みはpickle.dump()を使う。
- 読み込みはpickle.load()を使う。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 432
  status: ok
  timestamp: 1682747672248
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: QvkyhLiFMf8S
---
sample = [['マックス','1864'], ['エミール', '1858'], ['ゲオルグ', '1858']]

import pickle
with open ('sample.pickle','wb') as f:#バイナリオブジェクトなので'w'ではなく'wb'とする。
  pickle.dump(sample,f)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 262
  status: ok
  timestamp: 1682747678593
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: zEJCWe6Ck9Sl
outputId: 86a6051f-492c-4f83-c2e5-1f83fd9fd67e
---
%ls
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 7
  status: ok
  timestamp: 1682747692099
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ws8kQODBk_P8
outputId: a83b0a9f-2b4a-4b75-a5da-d2d47e0152e5
---
%cat sample.pickle
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 355
  status: ok
  timestamp: 1682747706289
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: mKOjBtkSNIUU
---
with open ('sample.pickle','rb') as f:#バイナリオブジェクトなので'r'ではなく'rb'とする。
  sample = pickle.load(f)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 258
  status: ok
  timestamp: 1682747712065
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: mVK1y3fsNPXh
outputId: cc2cef1c-edb8-412d-ac58-e853e34c0337
---
sample
```
