# Creo テンプレート仕様書：`base_plate_template.prt`

## ■ 概要

このテンプレートは、Creoによるパラメトリック設計の入門教材として使用される平面プレートのモデルです。  
寸法・データム・穴あけなどがあらかじめ定義されており、演習や派生設計のベースとして使用可能です。

---

## ■ モデル仕様

| 項目         | 内容 |
|--------------|------|
| モデル名     | `base_plate_template.prt` |
| モデル種別   | Part（単体パーツ） |
| 単位系       | mmks（mm, kg, sec, N） |
| 外形寸法     | 100 mm × 60 mm（length × width） |
| 厚み         | 10 mm（パラメータ名：`plate_thickness`） |
| 中心穴       | φ20 mm（パラメータ名：`hole_diameter`） |
| データム     | Top / Front / Right（中心で交差） |
| 注釈         | “このテンプレートは平面ベース設計の出発点です”（Noteにて） |

---

## ■ 作成手順（Creo）

1. **新規パート作成**  
   - ファイル名：`base_plate_template`  
   - 単位系：`mmks`（ミリ）  
   - データム：Top / Front / Right を原点で交差

2. **Top平面でスケッチ作成**  
   - 原点を中心に、100 mm × 60 mm の長方形を描く  
   - 寸法に名前を設定：`length = 100`, `width = 60`

3. **押し出し**  
   - 厚み：10 mm（パラメータ名：`plate_thickness`）  
   - 方向：片側上方押し出し

4. **中心穴の作成**  
   - 上面を選びスケッチ  
   - 原点に φ20 mm の円を配置  
   - 押し出しカット → 貫通（Through All）  
   - 寸法名：`hole_diameter = 20`

5. **パラメータ設定**  
   - モデルツリー内で寸法に名前を付ける  
     - `plate_thickness`, `hole_diameter`, `length`, `width`

6. **注釈の追加（任意）**  
   - 上面に Note を追加  
   - 内容：`このテンプレートは平面ベース設計の出発点です`

---

## ■ 使用例

- `01_parametric_basics/` にて押し出し＋穴あけの操作演習
- `03_drawing_skills/` にて図面生成の基本例として活用
- `05_mechatronic_integration/` の筐体ベースの構成に派生利用

---

## ■ 今後の展開候補

- `base_plate_with_fillet.prt`（フィレット追加演習）
- `base_plate_drawing.drw`（製図用テンプレート）
- 派生テンプレ：ねじ穴付き / スリット入り / リブ付きバージョン

---

© EduMecha Project / 三溝真一（統合設計者）  
教育・研究目的に限り、改変・再配布を自由に行ってください。
