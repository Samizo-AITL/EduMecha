# Creo テンプレート仕様書：`control_case_template.asm`

## ■ 概要

このテンプレートは、制御回路やセンサモジュールを収納する筐体（ケース）構造を設計・アセンブリ演習するための基本モデルです。  
ベース・カバーの2部品構成で、アセンブリ拘束（Mate, Align, Insert）や寸法連携を学べるように設計されています。  
統合設計教材（AITL-H筐体など）や量産設計PoCにも展開可能です。

---

## ■ モデル仕様

| 項目              | 内容 |
|-------------------|------|
| モデル名          | `control_case_template.asm` |
| モデル種別        | Assembly（アセンブリ） |
| 単位系            | mmks（mm, kg, sec, N） |
| 構成部品          | `case_base.prt`, `case_cover.prt` |
| 外形寸法（初期）  | 100 mm × 60 mm × 30 mm |
| ケース厚み        | 2 mm（カバー） / 3 mm（ベース） |
| ネジ穴            | φ3.2 mm × 4（角部固定想定） |
| 拘束方式          | Mate / Align / Insert を使用 |
| パラメータ共有    | `case_height`, `cover_thickness`, `hole_spacing` |
| 注釈              | “このテンプレートは筐体構造の統合設計に使用されます”（Noteにて） |

---

## ■ 作成手順（Creo）

### 🔹 `case_base.prt`（ベース部品）

1. 新規作成 → Top面に 100×60 mm のスケッチを作成
2. 押し出し高さ：27 mm（`case_height`）
3. 外壁厚み：3 mm（全体押し出し → Shell処理も可）
4. 底部 or 側面に φ3.2 mm の穴 ×4（角部想定）
5. パラメータ命名：`base_length`, `base_width`, `case_height`

---

### 🔹 `case_cover.prt`（カバー部品）

1. 新規作成 → 同サイズスケッチ（100×60 mm）
2. 押し出し厚み：2 mm（`cover_thickness`）
3. 嵌合用の段差 or 凸部を設計（ベースとの一致）
4. 拘束のための基準面に Note を追加

---

### 🔹 `control_case_template.asm`（アセンブリ構成）

1. `case_base.prt` を Default で挿入（基準）
2. `case_cover.prt` を Mate（上下面）、Align（側面）で拘束
3. 必要に応じて Insert（ネジ穴 ↔ 仮想ネジ）
4. 寸法共有（高さ、ネジ位置）または Copy Geometry 使用

---

## ■ 使用例

- `05_mechatronic_integration/`：センサ＋制御系統合PoCの筐体モデル
- `02_assembly_design/`：Mate / Align / Insert の基本演習モデル
- `08_production_process/`：製図・加工・組立・評価までの教材展開

---

## ■ 派生展開候補

- `control_case_exercise1.asm`：高さ・構成部品変更の演習モデル
- `control_case_with_board.asm`：内部に制御基板を組み込んだ構成
- `control_case_drawing.drw`：図面生成練習用アセンブリ

---

## ■ 著作・利用条件

© EduMecha Project / 三溝真一（統合設計者）  
このテンプレートは教育・研究目的において自由に使用・改変・再配布できます。
