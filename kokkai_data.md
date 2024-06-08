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

+++ {"id": "8BbhAfksWiI1"}

## 国会会議録のAPIからデータ取得する。
https://kokkai.ndl.go.jp/#/

- 第1回国会（昭和22年5月）からの本会議・委員会の会議録を検索し、閲覧できる。
- APIという仕組みを使えば、データを自動的に大量取得できる。
- まずAPIの仕様書を読みましょう。
- APIは、指定されたurlに検索条件を加えることで所望のデータを取得します。

https://kokkai.ndl.go.jp/api.html

- 1. アクセスURLの確認
    - 発言単位：http://kokkai.ndl.go.jp/api/1.0/speech?{検索条件}
    - 会議単位：http://kokkai.ndl.go.jp/api/1.0/meeting?{検索条件}
- 2. 検索条件の確認
- 3. 検索パラメータの確認
  - 	startRecord	開始位置	検索結果の取得開始位置を「1～検索件数」の範囲で指定可能。
  - 	maximumRecords	一回の最大取得件数	一回のリクエストで取得できるレコード数を、会議単位簡易出力
  - ...
- 4. 返戻結果の形式の確認
  - xml or json
  

+++ {"id": "pLaEzC4XWiI8"}

### 準備
- 必要なモジュールをインストールしていきます。各モジュールの説明は使う場面で行います。

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 25544
  status: ok
  timestamp: 1682756717784
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 4w8G-Cu7WwiG
outputId: 0636fecb-bed1-4e99-df5d-9ad0467b983f
---
from google.colab import drive
drive.mount('/content/drive')
%cd /content/drive/MyDrive/cssws2023/
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 6043
  status: ok
  timestamp: 1682756771551
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ffmyLa0pWiI9
outputId: 55409e5e-388b-4e7a-f1fc-87d119fd3b25
---
#xmlをdictに変換するモジュール
!pip install xmltodict
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 458
  status: ok
  timestamp: 1682756777209
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: jDU-xZ-NWiI-
---
import requests
import urllib.parse
import xmltodict 
import pprint
import pandas as pd
from collections import defaultdict
```

+++ {"id": "Z_VDVJOfTBCh"}

### APIからのデータ取得
- APIのurlとparamsを変数にまとめておく。
- fetchする関数を定義する。
- 1回の呼び出しで得られる件数が限られているため、'startsRecord'を指定して繰り返し取得する必要がある。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 5
  status: ok
  timestamp: 1682756852576
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: QUIeltQfWiJA
---
url = 'http://kokkai.ndl.go.jp/api/1.0/speech?'
params = {'any':'コロナ',
          'from':'2020-01-01',
          'until':'2023-04-13',
          'startRecord':'1'
}
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 241
  status: ok
  timestamp: 1682756862678
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: LJrHV4IwSa8o
---
def fetch_kokkaikaigiroku(url, params):
    dat = []
    while params['startRecord'] != None:#繰り返し取得する。
        print(f"{params['startRecord']}番からの取得を開始します。")
        response = requests.get(url,params)#requests.get()でデータ取得
        res = xmltodict.parse(response.content)
        dat.extend(res['data']['records']['record'])
        params['startRecord'] = res['data'].get('nextRecordPosition')
    return dat
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 1757022
  status: ok
  timestamp: 1682758627719
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: 1YBhHl1kSa8p
outputId: a384dec5-7d17-4729-d0df-24c1edf218c6
---
dat = fetch_kokkaikaigiroku(url, params)
```

+++ {"id": "9afXfz1iWiJY"}

#### ディクショナリを整形してデータフレームに変換
- さらに、必要な項目だけを抜き出し、ディクショナリに整形しデータフレームに変換する
- defaultdict(list)はkey呼び出ししたときにキーがなければlistを作成する。
- GoogleDriveにマウントしてあれば、cssws2023の下にdataというディレクトリを作成し、そこにcsvファイルを保存する。

```{code-cell} ipython3
---
executionInfo:
  elapsed: 297
  status: ok
  timestamp: 1682758647646
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: WDfA5lM-WiJZ
---
def to_DataFrame(dat):
    dat_dict = defaultdict(list)
    for item in dat:
        row = item['recordData']['speechRecord']#この階層に発言の実体がある。
        for key, value in row.items():
            dat_dict[key].append(value)
    df = pd.DataFrame(dat_dict)
    return df
    
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 740
  status: ok
  timestamp: 1682758652486
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: Z2K5JnAIWiJd
---
df = to_DataFrame(dat)
```

```{code-cell} ipython3
---
executionInfo:
  elapsed: 4072
  status: ok
  timestamp: 1682758673516
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: ZhPeb5lpWiJd
---
import os 
if not os.path.exists('data'):
    os.makedirs('data')
df.to_csv('data/kokkai_corona.csv', index = False)
```

+++ {"id": "2HnKCq4YhKQw"}

### APIからのデータ取得コードの補足説明
- #requests.get()でAPIのアクセスurlとパラメータを指定するとデータが取得できる。
- resonsen.contentにxml形式でテキストが格納される。
- xmltodict.parse()によってxmlをパースしてディクショナリに変換する。
- 発言内容は'data'>'records'>'record'という上から3階層目にある。
- 'data'>'nextRecordPosition'に次のスタート番号が記録されている。存在しない場合があるのでget()を使って取得。

```{code-cell} ipython3
:id: LE6a_PbJhWUs

response = requests.get(url,params)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 607
  status: ok
  timestamp: 1682193381514
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: uEZUsYB3iZod
outputId: 3baa6208-541b-43de-f265-f7b70375d076
---
response.content
```

```{code-cell} ipython3
:id: Qy40TCr7ifP_

res = xmltodict.parse(response.content)
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 617
  status: ok
  timestamp: 1682193422370
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: FRscO7aMioNJ
outputId: ea408952-e4a2-4861-ff52-d768d32c9bd7
---
res
```

```{code-cell} ipython3
---
colab:
  base_uri: https://localhost:8080/
executionInfo:
  elapsed: 537
  status: ok
  timestamp: 1682193531434
  user:
    displayName: "\u7027\u5DDD\u88D5\u8CB4"
    userId: 05752887510241032794
  user_tz: -540
id: fDnX0L82jDYR
outputId: 225b5f5d-0370-4f91-bbc5-5ba2ed602968
---
res['data']['records']['record']
```

+++ {"id": "ECk8fzpRk_-n"}

### 課題
- 自分の興味のあるテーマで検索し、データを取得してください。
- ただし、あまりにデータが多くなると取得に時間がかかるので、最大2万件程度を目安にしてください。
