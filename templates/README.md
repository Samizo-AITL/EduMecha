# 🧰 EduMecha Creo テンプレート集

このフォルダには、Creo による設計学習用テンプレートモデル（`.prt` / `.asm`）を収録しています。

- ✅ データム・拘束・パラメータを定義済み
- ✅ 各テンプレートには設計意図と使用方法が記された仕様書付き
- ✅ AITL教材との連動や PoC 実装にも展開可能

---

## 📌 利用目的

- データム・寸法拘束・パラメータを事前定義した「設計の出発点」を提供  
- 初学者がすぐに操作・編集に集中できるようにする  
- 教材間で一貫性あるモデル展開を実現  
- 統合設計（AITL-H 等）への PoC 連携を効率化  

---

## 📂 テンプレート一覧

| ファイル名                       | 種別 | 内容概要                             | 連携教材 | 仕様書 |
|----------------------------------|------|--------------------------------------|-----------|--------|
| [`base_plate_template.prt`](./base_plate_template.prt) | Part | 平面ベース＋中心穴付き                 | [`01_parametric_basics/`](../01_parametric_basics/) | [`📄`](./template_base_plate_spec.md) |
| [`sensor_mount_template.prt`](./sensor_mount_template.prt) | Part | センサ固定用の穴付き円形板             | [`05_mechatronic_integration/`](../05_mechatronic_integration/) | [`📄`](./template_sensor_mount_spec.md) |
| [`control_case_template.asm`](./control_case_template.asm) | Asm  | ベース筐体＋カバー構成モデル           | [`05_mechatronic_integration/`](../05_mechatronic_integration/) | [`📄`](./template_control_case_spec.md) |

---

## 🛠️ 使用方法

1. 本テンプレートを **複製（別名保存）** して使用します。
2. パラメータ（寸法変数）には明示的な名前が設定されています（例：`plate_thickness`、`hole_diameter` など）。
3. 教材ごとの演習では、本テンプレートを基にした派生モデルを作成します。

---

## 🧩 命名規則（推奨）

| 種類             | 接尾語       | 命名例                               |
|------------------|--------------|----------------------------------------|
| テンプレートモデル | `_template`  | `sensor_mount_template.prt`           |
| 演習派生モデル     | `_exerciseX` | `sensor_mount_exercise1.prt`          |
| 統合・PoCモデル   | `_PoC`       | `casing_sensor_mount_PoC.asm`         |

---

## 🔄 今後の拡張予定

- ジグ・冶具・測定用ブロックのテンプレート追加  
- 製図教材（[`06_drafting_fundamentals/`](../06_drafting_fundamentals/)）との連携（断面・公差定義モデル）  
- Creo API / マクロと連携したテンプレート展開機能

---

## 📮 お問い合わせ・貢献

テンプレートの改善提案・追加希望・修正依頼などは、EduMecha リポジトリの  
[📬 Issue ページ](https://github.com/your-org/EduMecha/issues) にてお知らせください。

---

© EduMecha Project / 三溝真一（統合設計者）  
本テンプレートは教育・研究目的において自由に使用・改変いただけます。
