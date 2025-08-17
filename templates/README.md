---
layout: default
title:  Creo Macro Collection | Creo マクロ集
---

---

# 🧰 **Creo Macro Collection | Creo マクロ集**

本フォルダには、**Creo Parametric** による設計作業を効率化する **マクロスクリプト** を収録しています。  
This directory provides **macro scripts for Creo Parametric** that streamline design workflows.  

- ✅ **繰り返し操作の自動化**（寸法変更・エクスポート等）  
- ✅ **教材内ワークフローの効率化**  
- ✅ **API / Toolkit 拡張を見据えた実装**  

---

## 📌 **利用目的 | Purpose**

- 教材演習における繰り返し操作を削減  
  *Reduce repetitive tasks in exercises*  
- 図面出力・形式変換などのルーチン処理を自動化  
  *Automate routine tasks such as drawing export & format conversion*  
- 学習者が「設計意図」に集中できる環境を提供  
  *Allow learners to focus on **design intent***  
- 統合設計・PoC（AITL-H 等）との連動効率化  
  *Enable smooth integration with **AITL-H** and PoC workflows*  

---

## 📂 **マクロ一覧 | Macro List**

| ファイル名 / Filename | 内容概要 / Description | 連携教材 / Linked Module | 仕様書 / Spec |
|----------------------|------------------------|--------------------------|---------------|
| [`auto_export_pdf.mac`](./auto_export_pdf.mac) | 図面を一括 PDF 出力<br>Batch export drawings to PDF | [`03_drawing_skills`](../03_drawing_skills/) | [`📄`](./macro_auto_export_pdf_spec.md) |
| [`param_update_batch.mac`](./param_update_batch.mac) | パラメータ一括更新<br>Batch parameter updates | [`01_parametric_basics`](../01_parametric_basics/) | [`📄`](./macro_param_update_spec.md) |
| [`asm_bom_generator.mac`](./asm_bom_generator.mac) | アセンブリから BOM 生成<br>Generate BOM from assemblies | [`08_production_process`](../08_production_process/) | [`📄`](./macro_bom_generator_spec.md) |

---

## 🛠️ **使用方法 | Usage**

1. Creo の **Mapkeys** に登録して実行  
   *Register macros in Creo Mapkeys and execute*  
2. 各マクロには、操作手順・必要入力が仕様書に記載  
   *Each macro includes a spec with workflow and required inputs*  
3. 実習教材では、**手動操作との比較学習**を推奨  
   *Compare with manual operations for learning purposes*  

---

## 🧩 **命名規則 | Naming Rules**

| 種類 / Type | 接尾語 / Suffix | 命名例 / Example |
|-------------|-----------------|------------------|
| 自動化マクロ / Macro Script | `_mac` | `param_update_batch.mac` |
| 仕様書 / Spec | `_spec.md` | `macro_bom_generator_spec.md` |

---

## 🔄 **拡張予定 | Future Extensions**

- Creo **API（Toolkit, J-Link）** を利用した拡張サンプル  
- Excel 連携による寸法リスト読込・BOM 出力  
- [`07_measurement_tools`](../07_measurement_tools/) 等との連携マクロ追加  

---

## 📮 **お問い合わせ・貢献 | Feedback & Contribution**

マクロの改善提案・追加希望・修正依頼は、EduMecha リポジトリの  
[📬 Issue ページ](https://github.com/your-org/EduMecha/issues) までご連絡ください。  

Please submit suggestions, improvements, or bug reports via the  
[📬 Issues page](https://github.com/your-org/EduMecha/issues).  

---

© 2025 EduMecha Project / **三溝真一（統合設計者 | Chief Integrator）**  
本マクロ群は **教育・研究目的に限り**、自由に使用・改変・再配布いただけます。  
This collection is released for **educational and research use only**, with permission to modify and redistribute.  
