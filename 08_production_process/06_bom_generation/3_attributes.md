---
title: "Attributes and Export Control"
description: "部品コードに紐づける属性と輸出関連管理のポイント | Attributes linked to part numbers and export control essentials"
author: "Project Design Hub"
date: 2025-08-18
tags: ["BOM", "部品コード", "環境データ", "コスト管理", "輸出管理", "SDS", "消防法"]
---

# 📎 部品コードと紐づける属性 | Attributes Linked to Part Numbers

## 📋 基本属性一覧 | Basic Attributes

| **区分 / Category** | **内容例 / Examples** |
|---------------------|-----------------------|
| **図面 / Drawing** | CAD, 図面番号, Rev / CAD data, drawing number, revision |
| **環境データ / Environmental Data** | RoHS/REACH, LCA, SDS |
| **コスト / Cost** | 単価, 加工費, 原価 / Unit price, processing cost, base cost |
| **該非判定 / Export Control Classification** | 輸出管理: 該当/非該当, ECCN / Export control judgment, ECCN |
| **HSコード / HS Code** | 輸出入分類番号 / Harmonized System Code |
| **用途説明書 / End-use Statement** | デュアルユース時必要 / Required for dual-use items |
| **消防法情報 / Fire Law Data** | 類・項, 指定数量, 保管条件 / Category, quantity, storage conditions |

---

## 🔎 特記事項（6番コード: 材料）  
**Special Notes (Digit 6: Materials)**

- 材料コード（6番）は **必ず SDS（安全データシート）を参照**  
  *Digit 6 (Materials) always requires reference to SDS.*  

- SDSから登録すべき項目 / Attributes to register from SDS:  
  - 危険物判定（引火性、腐食性、粉じん爆発性）  
    *Hazard classification: flammability, corrosivity, dust explosion risk*  
  - 消防法「類・項・指定数量」  
    *Fire Law: category, item, specified quantity*  
  - 保管条件（容器、温度、換気など）  
    *Storage conditions: container type, temperature, ventilation*  

👉 **SDS更新時は BOM を必ず見直す | BOM must be updated whenever SDS is revised.**

---

# 🌍 輸出関連属性 | Export-Related Attributes

輸出に伴い必須となる属性 | **Mandatory for export procedures**:

| **区分 / Category** | **内容 / Details** |
|----------------------|--------------------|
| **該非判定 / Export Classification** | 外為法に基づき「該当／非該当」を判定。ECCNを付与。<br>Judgment under Foreign Exchange Law; ECCN if applicable. |
| **HSコード / HS Code** | 税関手続き用の品目分類番号。国際共通だが細分類は国ごとに異なる。<br>Customs classification code; globally standardized, country-specific subcategories. |
| **用途説明書 / End-use Statement** | デュアルユースや規制品の場合に必須。最終ユーザー・使用目的を明記。<br>Required for dual-use or controlled items; describes end-user and purpose. |

---

## 🚢 該非判定を行う理由 | Why Export Classification is Necessary

1. **法律遵守 / Legal Compliance**  
   - 外為法に基づき軍事転用可能品は規制対象  
   - Violations lead to fines, imprisonment, or export bans  

2. **国際安全保障 / International Security**  
   - 大量破壊兵器やミサイル転用を防止  
   - Prevent proliferation and misuse  

3. **業務円滑化 / Smooth Customs Clearance**  
   - 適切な判定と書類で通関を迅速化  
   - Faster export procedures  

4. **企業リスク管理 / Corporate Risk Management**  
   - 不正利用によるブランド毀損防止  
   - Protect brand and credibility  

---

## ⚠️ 該非判定が必要となる典型品目 | Typical Items Requiring Classification

### 🖥 高度な半導体 / Advanced Semiconductors
- 高性能プロセッサ（GPU, FPGA, AIチップ）  
- High-performance processors (GPU, FPGA, AI chips)  
- 高速AD/DAコンバータ、暗号処理LSI  
- High-speed AD/DA converters, encryption LSIs  
- 先端メモリ（HBM, MRAM, ReRAM）  
- Advanced memories (HBM, MRAM, ReRAM)  

### 🧪 特殊材料 / Special Materials
- 高性能炭素繊維（航空機・ミサイル用）  
  High-performance carbon fibers (aerospace, missiles)  
- 高純度フッ化水素・エッチングガス  
  High-purity HF and etching gases  
- 超耐熱合金、特殊金属  
  Superalloys and special metals  

### 📡 その他 / Others
- 暗号ソフトウェア・通信機器 / Cryptographic software & telecom equipment  
- 高精度センサー（赤外線、レーザー測距、ジャイロ）  
  High-precision sensors (IR, LIDAR, gyroscopes)  

👉 **デュアルユース品は「該非判定書＋用途説明書」が必須**  
*Dual-use items always require both Export Classification documents and End-use Statements.*  
