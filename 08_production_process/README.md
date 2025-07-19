# 08_production_process

**設計から量産立上げまでの一貫プロセス教材**  
**Integrated Process Training from Design to Mass Production**

---

## 📘 概要 | Overview

本セクションでは、**Creoを用いた設計初期段階から、量産図面作成、BOM（部品表）生成、設計レビュー（DR）を経て、MP（Mass Production：量産）に至るまでの一連の実践プロセス**を学びます。  
設計意図の明確化、試作・計測結果の反映、公差・材料指定、構成管理までを網羅し、実務に近い設計フローを体験できます。

This module provides hands-on training in the complete development cycle—from initial 3D CAD modeling using Creo, to creating production-ready drawings, generating BOMs, conducting design reviews, and preparing for mass production.  
It emphasizes design intent, feedback from prototyping, proper tolerance/material specification, and configuration management for practical application.

---

## 🔁 設計プロセスフロー | Design-to-MP Workflow

```mermaid
flowchart LR
  A[Creo設計 / 3D Modeling] --> B[設計図面 / Initial Drawing]
  B --> C[試作 / Prototyping]
  C --> D[計測 / Evaluation]
  D --> E[量産図面 / Production Drawing]
  E --> F[BOM作成 / BOM Generation]
  F --> G[DR（設計レビュー） / Design Review]
  G --> H[MP（量産） / Mass Production]
```

---

## 📂 ディレクトリ構成 | Directory Structure
```
08_production_process/
├── 01_creo_modeling/         # 初期モデリング例（パラメトリック設計）
├── 02_drawing_creation/      # 設計図面（設計意図入り）
├── 03_prototyping/           # 試作とモデル出力（STL等）
├── 04_measurement_report/    # 計測結果と改善点レポート
├── 05_production_drawing/    # 量産用製図（材料・公差含む）
├── 06_bom_generation/        # BOMテンプレートと記入例
├── 07_design_review/         # DR資料（チェックリスト・議事録）
└── 08_mp_guideline/          # 量産移行ガイドライン（工程/構成管理）
```

---

## 🧑‍🏫 学習目標 | Learning Objectives

- Creoによるパラメトリック設計と図面出力  
- 試作→評価→設計反映のフィードバックループ構築  
- 材料・公差・検査基準を含む量産図面作成  
- Excel形式の部品表（BOM）の構築と構成管理  
- チェックリストに基づく設計レビューの実施  
- SCM・QA部門との連携を想定したMP準備  

---

## 📄 使用テンプレート | Provided Templates

| ファイル名 | 内容 / Description |
|------------|--------------------|
| `bom_template.xlsx` | 部品表テンプレート（品番・材質・数量・版数） |
| `dr_checklist.md` | DR用チェックリスト（レビューポイント付き） |
| `measurement_sheet.xlsx` | 寸法測定と評価記録シート |
| `mp_guideline.md` | 量産化に向けた設計移行ガイドライン |

---

## 🔗 関連セクション | Related Sections

- [`03_drawing_skills/`](../03_drawing_skills/)  
  基本的な製図スキルと連携  
- [`07_measurement_tools/`](../07_measurement_tools/)  
  寸法評価と計測器の使用法  
- [`05_mechatronic_integration/`](../05_mechatronic_integration/)  
  制御対象と設計統合したPoC演習  

---

## 📝 備考 | Notes

- このプロセス教材は、EduMecha全体の集大成として設計されています。  
- チーム設計演習やPoC検証における「現実的な設計フロー」を想定しています。  
- SCM／QA部門との設計インタフェース教材としても活用可能です。  

---

## 📬 ご意見・貢献 | Feedback & Contribution

改善提案・教材拡張・サンプル事例の共有などを歓迎します。  
Pull Request または Discussions にてご連絡ください。  

We welcome your suggestions, enhancements, and case studies.  
Feel free to submit a PR or join the [Discussions](https://github.com/Samizo-AITL/EduMecha/discussions).

---

