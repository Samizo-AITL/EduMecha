# 06_bom_generation

**部品表（BOM）の作成と設計情報の構造化**  
**Bill of Materials (BOM) Generation and Structured Design Data**

---

## 📘 概要 | Overview

このセクションでは、設計構成に基づいた**部品表（BOM: Bill of Materials）**を作成し、量産や在庫管理に必要な構成情報を整理します。  
部品番号、材質、加工方法、数量、単価などを体系的にまとめ、**構成管理（Configuration Management）**の基礎を学びます。

In this section, learners develop a structured Bill of Materials (BOM) from their design data.  
This includes part numbers, materials, quantities, manufacturing methods, and costs, forming the foundation for configuration and production management.

---

## 🧑‍🏫 学習目標 | Learning Objectives

- 組立構造に対応した部品階層と親子関係を理解する  
- 各部品に対し必要な属性（番号、材質、数量など）を整理する  
- ExcelやCSVで編集可能なBOMテンプレートを活用する  
- 図面・モデルとの対応を明確にしたBOMを作成する  
- コスト意識や部品管理の視点を持って構成を検討する  

---

## 📂 サブディレクトリ構成 | Subdirectories

```text
06_bom_generation/
├── bom_templates/          # Excelテンプレート・記入例
├── sample_boms/            # サンプルBOMデータ（CSV, XLSX）
├── attribute_definitions/  # 項目定義（材質、工程、区分など）
└── bom_checklist/          # 作成時の確認事項・よくあるミス
```

---

## 📝 添付ファイル一覧 | Planned Files (後で作図予定)

| ファイル名 | 内容 | 備考 |
|------------|------|------|
| `bom_template.xlsx` | 教育用BOMテンプレート | Excel形式 |
| `sample_bom_box.csv` | 簡易アセンブリ（箱構造）のBOM | 実装例 |
| `bom_attribute_definitions.md` | 項目説明と注意点まとめ | 教材内文書 |
| `bom_checklist.md` | BOM作成時の確認リスト | 〃 |

---

## 🔗 関連セクション | Related Sections

- [`02_drawing_creation/`](../02_drawing_creation/)  
  → 図面上の部品番号や材料情報を反映
- [`05_production_drawing/`](../05_production_drawing/)  
  → 製図から得られる部品属性をBOMに変換
- [`08_mp_guideline/`](../08_mp_guideline/)  
  → BOMを基に量産体制の構成管理を設計

---

## 💬 コメント・共有 | Feedback

BOMの現場での活用例、属性定義の工夫、ミスの防止方法などがあれば [Discussions](https://github.com/Samizo-AITL/EduMecha/discussions) にてぜひご共有ください。

We welcome your BOM practices, templates, and lessons learned from real projects!
