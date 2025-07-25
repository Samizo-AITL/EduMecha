# Creo テンプレート仕様書：`sensor_mount_template.prt`

## ■ 概要

このテンプレートは、MEMS / PZTセンサなどを固定・実装するためのマウントベース設計に使用されます。  
取り付け穴、パラメトリック寸法、リファレンス平面が事前定義されており、センサ統合PoCや筐体内実装モデルの土台として活用できます。

---

## ■ モデル仕様

| 項目              | 内容 |
|-------------------|------|
| モデル名          | `sensor_mount_template.prt` |
| モデル種別        | Part（単体パーツ） |
| 単位系            | mmks（mm, kg, sec, N） |
| 外形形状          | 円形 φ60 mm または 矩形 80×40 mm（選択可） |
| 厚み              | 8 mm（パラメータ名：`thickness`） |
| 取付穴            | φ3.0 mm × 3個（等配または対称配置） |
| リファレンス平面 | 上面 / 下面 / 中心軸 に拘束用面あり |
| 凹み（オプション）| φ20 mm・深さ 0.1 mm の円形凹み（`recess_depth`） |
| 注釈              | “このテンプレートはセンサ固定用の中間部品です”（Note にて） |

---

## ■ 作成手順（Creo）

1. **新規パート作成**  
   - 名前：`sensor_mount_template`  
   - 単位系：`mmks`  
   - データム：Top / Front / Right（原点交差）

2. **外形スケッチ**  
   - Top 平面に φ60 mm の円（または 80×40 mm の長方形）  
   - パラメータ名：`diameter = 60` または `length = 80`, `width = 40`

3. **押し出し（厚み）**  
   - 片側方向に 8 mm（パラメータ名：`thickness`）

4. **取付穴の作成**  
   - 上面に φ3.0 mm の円を3つ配置  
   - 円形の場合：等配 120°（中心から 3点）  
   - 矩形の場合：左右対称位置に穴配置  
   - 押し出しカット：貫通

5. **凹みの作成（オプション）**  
   - φ20 mm × 0.1 mm の凹みを中央に追加  
   - パラメータ名：`recess_depth = 0.1`

6. **パラメータ命名**  
   - `thickness`, `hole_diameter`, `recess_depth`, `diameter`（or `length` / `width`）

7. **注釈の追加（任意）**  
   - 上面に Note を追加  
   - 内容：`このテンプレートはセンサ固定用の中間部品です`

---

## ■ 使用例

- `05_mechatronic_integration/`：MEMSセンサやPZTユニットのベースモデル
- `02_assembly_design/`：拘束練習モデルとの連動（Mate / Align）
- `03_drawing_skills/`：簡易製図演習

---

## ■ 派生展開候補

- `sensor_mount_with_pins.prt`：ピン付きマウント版
- `sensor_mount_param_demo.asm`：アセンブリ構成例
- `sensor_mount_drawing.drw`：図面生成演習版

---

## ■ 著作・利用条件

© EduMecha Project / 三溝真一（統合設計者）  
本テンプレートは、教育・研究目的において自由に使用・改変・再配布可能です。
