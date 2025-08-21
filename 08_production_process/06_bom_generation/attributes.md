---
layout: default
title: "Attributes & Export Control"
description: "属性情報と輸出管理の仕組み / Attributes Management and Export Control"
---

---

# 📎 部品コードと紐づける属性 | Attributes Linked to Part Numbers

---

## 📋 基本属性一覧 | Basic Attributes

| 区分 / Category | 内容例 / Examples |
|-----------------|-------------------|
| 図面 / Drawing | CAD, 図面番号, Rev / CAD data, drawing number, revision |
| 環境データ / Environmental Data | RoHS/REACH, LCA, SDS |
| コスト / Cost | 単価, 加工費, 原価 / Unit price, processing cost, base cost |
| 該非判定 / Export Control | 輸出管理: 該当/非該当, ECCN |
| HSコード / HS Code | 輸出入分類番号 / Harmonized System Code |
| 用途説明書 / End-use Statement | デュアルユース時必要 / Required for dual-use items |
| 消防法情報 / Fire Law Data | 類・項, 指定数量, 保管条件 / Category, quantity, storage conditions |

---

## 🔎 特記事項（6番コード: 材料）| Special Notes (Digit 6: Materials)

| 属性 / Attribute | 登録内容 / Details |
|------------------|----------------------|
| 危険物判定 / Hazard classification | 引火性・腐食性・粉じん爆発性<br>Flammability, corrosivity, dust explosion |
| 消防法 / Fire Law | 類・項・指定数量<br>Category, item, specified quantity |
| 保管条件 / Storage conditions | 容器、温度、換気など<br>Container, temperature, ventilation |

👉 **SDS更新時は BOM を必ず見直す | BOM must be updated whenever SDS is revised.**

---

# 🌍 輸出関連属性 | Export-Related Attributes

| 区分 / Category | 内容 / Details |
|-----------------|----------------|
| 該非判定 / Export Classification | 外為法に基づき「該当／非該当」を判定、ECCNを付与<br>Judgment under Foreign Exchange Law; ECCN if applicable |
| HSコード / HS Code | 税関手続き用の品目分類番号。国際共通だが細分類は国ごとに異なる<br>Customs classification; globally standardized, country-specific subcategories |
| 用途説明書 / End-use Statement | デュアルユースや規制品の場合に必須。最終ユーザー・使用目的を明記<br>Required for dual-use items; end-user and purpose |

---

## 🚢 該非判定の目的 | Why Export Classification is Necessary

| 観点 / Aspect | 内容 / Details |
|---------------|----------------|
| 法律遵守 / Legal Compliance | 軍事転用可能品は規制対象、違反時は罰則<br>Controlled under law, violations lead to fines, bans |
| 国際安全保障 / International Security | 大量破壊兵器・ミサイル転用を防止<br>Prevent WMD and missile proliferation |
| 業務円滑化 / Smooth Customs | 適切な判定と書類で通関を迅速化<br>Faster customs clearance |
| 企業リスク管理 / Corporate Risk | 不正利用によるブランド毀損防止<br>Protect brand and credibility |

---

## ⚠️ 該非判定が必要な典型品目 | Typical Items Requiring Classification

| 区分 / Category | 品目例 / Examples |
|-----------------|------------------|
| 高度な半導体 / Advanced Semiconductors | GPU, FPGA, AIチップ / High-performance processors<br>高速AD/DA, 暗号LSI / High-speed AD/DA, encryption LSI<br>先端メモリ（HBM, MRAM, ReRAM） |
| 特殊材料 / Special Materials | 高性能炭素繊維 / High-performance carbon fiber<br>高純度フッ化水素 / High-purity HF, etching gases<br>超耐熱合金 / Superalloys |
| その他 / Others | 暗号ソフト / Cryptographic software<br>通信機器 / Telecom equipment<br>高精度センサー / IR, LIDAR, gyroscopes |

👉 **デュアルユース品は「該非判定書＋用途説明書」が必須**  
*Dual-use items always require both Export Classification documents and End-use Statements.*

---

[🔝 トップに戻る / Back to top](./)
