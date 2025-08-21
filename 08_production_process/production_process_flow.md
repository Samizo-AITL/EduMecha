---
layout: default
title: 設計から量産部品発注までの実務フロー | Design to Mass Production Flow
---

# 🏭 設計から量産部品発注までの実務フロー  
**Practical Workflow: From Design to Mass Production Parts Ordering**

---

## 📘 概要 | Overview
本資料は、設計段階から量産部品発注に至るまでの社内実務フローを整理したものです。  
「設計図面検討会」「技術図面検討会」「通知・配布」「BOM連携」「量産部品発注」までを体系的に示します。  

---

## 🔁 実務ワークフロー | Practical Workflow

```mermaid
flowchart TD
  A["設計図面検討会 / Design Drawing Review"] --> B["設計図面 / Design Drawing"]
  B --> C["設計通知 / Design Notice"]
  C --> D["技術図面検討会 / Technical Drawing Review"]
  D --> E["技術図面(加工図面・組図) / Technical Drawings"]
  E --> F["技術通知 / Technical Notice"]
  F --> G["関係部署配布 / Distribution to Departments"]
  G --> H["構成部品表接続 / BOM Linkage"]
  H --> I["構成部品表通知 / BOM Notice"]
  I --> J["関係部署配布(構成部品表) / Distribution (BOM)"]
  J --> K["調達BOM反映 / Procurement BOM Integration"]
  K --> L["量産部品発注 / Mass Production Parts Ordering"]

  %% 横から入る属性群（06_bom_generation/3_attributes.md）
  S["部品コードと紐づける属性 / Attributes linked to Part Numbers
  - 図面(Drawing/番号/Rev)
  - 環境(RoHS/REACH/LCA/SDS)
  - コスト(Cost)
  - 輸出管理(ECCN)
  - HSコード(HS Code)
  - 用途説明(End-use)
  - 消防法(Fire Law)
  - SDS更新時はBOM改訂必須"] -.-> H
```

---

## 📂 プロセス説明 | Process Description

- **設計図面検討会 → 設計図面**  
  設計意図・仕様をレビューし、正式な設計図面を確定。  

- **設計通知 → 技術図面検討会**  
  設計図面を通知した上で、加工図面や組立図面に展開。  

- **技術通知 → 関係部署配布**  
  加工・組立・品質保証・SCM部門に技術情報を共有。  

- **構成部品表接続 → 技術通知更新 → 部署配布**  
  BOMに反映し、関連部門へ再度通知・配布。  

- **調達BOM反映 → 量産部品発注**  
  調達部門が量産用のBOMを基に、部品をサプライヤへ発注。  

---

## 👤 著作・ライセンス | Author & License
- ✍️ 著作 / Author: **三溝真一（Samizo-AITL）**  
- 📜 ライセンス / License: **MIT**（教育目的での使用・改変を歓迎）  
