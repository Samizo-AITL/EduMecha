---
layout: default
title: 設計から量産部品発注までの実務フロー | Design to Mass Production Flow
---

---

# 🏭 設計から量産部品発注までの実務フロー  
*Practical Workflow: From Design to Mass Production Parts Ordering*

> **注記｜Notice**  
> 本資料は、一般的な製造業における実務フローを抽象化した教育用コンテンツであり、特定企業の機密情報を含みません。  
> *This document abstracts a practical workflow commonly used in manufacturing and is intended for educational use. It does not contain any proprietary information of a specific company.*

---

## 📘 概要 | Overview
本資料は、設計段階から量産部品発注に至るまでの社内実務フローを整理したものです。  
*This material organizes the in-house workflow from design to mass-production parts ordering.*

「設計図面検討会」「技術図面検討会」「通知・配布」「BOM連携」「量産部品発注」までを体系的に示します。  
*It systematically covers design/technical drawing reviews, notices and distribution, BOM linkage, and ordering of mass-production parts.*

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

  %% 新規追加ステップ
  H --> H1["環境データ積み上げ判定 (EChemSkip) / Environmental Compliance Check"]
  H --> H2["コスト積み上げ / Cost Roll-up"]

  H1 --> I["構成部品表通知 / BOM Notice"]
  H2 --> I

  I --> J["関係部署配布(BOM) / Distribution (BOM)"]
  J --> K["調達BOM反映 / Procurement BOM Integration"]
  K --> L["量産部品発注 / Mass Production Parts Ordering"]

  %% 属性群
  S1["属性(設計時必須) / Design-time Attributes
  - 図面番号/Rev
  - RoHS/REACH, LCA, SDS
  - コスト(基礎)"] -.-> H

  S2["属性(輸出時追加) / Export-time Attributes
  - 輸出管理(ECCN)
  - 該非判定(Result of Export Control Classification)
  - HSコード
  - 用途説明書(End-use Statement)"] -.-> K

  %% 横から加わる評価・計測情報
  P1["試作評価 / Prototype Evaluation\n(寸法測定・性能検証)"] -.-> B
  P2["量産評価 / Mass Production Evaluation\n(工程能力 Cp/Cpk, 品質検証)"] -.-> E
  P3["計測器情報 / Measurement Instruments\n(三次元測定機, マイクロメータ, 真円度計 等)"] -.-> E
```

---

## 📂 プロセス説明 | Process Description

- **設計図面検討会 → 設計図面**  
  設計意図・仕様をレビューし、正式な設計図面を確定。  
  *Review design intent/specs and finalize the design drawing.*

- **設計通知 → 技術図面検討会**  
  設計図面を通知した上で、加工図面や組立図面に展開。  
  *Issue a design notice, then develop machining and assembly drawings.*

- **技術通知 → 関係部署配布**  
  加工・組立・品質保証・SCM部門に技術情報を共有。  
  *Distribute technical information to manufacturing, assembly, QA, and SCM.*

- **構成部品表接続 → 環境判定・コスト積上 → 構成部品表通知 → 部署配布**  
  BOMに反映し、適合性とコストを確認後、関係部署へ通知・配布。  
  *Link BOM, verify environmental compliance and cost roll-up, then notify and distribute to stakeholders.*

- **調達BOM反映 → 量産部品発注**  
  調達部門が量産用のBOMを基に、部品をサプライヤへ発注。  
  *Procurement updates the purchasing BOM and places orders for mass-production parts.*

- **（輸出が必要な場合）輸出関連属性の付与**  
  ECCN・該非判定・HSコード・用途説明書を付与。  
  *If export is required, add ECCN, export classification result, HS code, and end-use statement.*

---

## 👤 著作・ライセンス | Author & License
- ✍️ 著作 / Author: **三溝真一（Samizo-AITL）**  
  *Author: Shinichi Samizo (Samizo-AITL)*  
- 📜 ライセンス / License: **MIT（教育目的での使用・改変を歓迎）**  
  *MIT License (free use and modification for educational purposes).*
