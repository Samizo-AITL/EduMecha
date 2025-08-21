---
layout: default
title: "Exercises"
description: "演習課題：BOMと設計実務の習得 / Exercises: BOM & Design Practice"
---

---

# 🧪 演習課題 | Exercises

---

## 📘 初級 (Basic)

| No | 課題 (Japanese) | Task (English) |
|----|-----------------|----------------|
| 1 | **図面から部品コードを割り当てる**<br>図面番号と仕様を確認し、適切な **6桁コード + 枝番** を付与する。<br>材料コードの場合は SDS を参照して分類を確認する。 | **Assign part code from drawing**<br>Check drawing number/specs and assign correct **6-digit code + suffix**.<br>If material code, confirm classification using SDS. |
| 2 | **属性情報の登録**<br>部品コードごとに以下を入力：環境データ（RoHS/REACH, SDS）、コスト情報（単価・加工費）、輸出関連（該非判定・HSコード） | **Register attributes**<br>For each part code, register: Environmental data (RoHS/REACH, SDS), cost (unit, processing), export info (classification, HS code). |

---

## 📗 中級 (Intermediate)

| No | 課題 (Japanese) | Task (English) |
|----|-----------------|----------------|
| 3 | **BOM作成と積み上げ**<br>部品表を Excel/CSV で作成し、親子関係を定義。<br>サブAssy（基板・筐体など）をまとめて **製品BOM** に統合する。 | **Create and roll up BOM**<br>Create BOM in Excel/CSV, define parent-child relations.<br>Integrate sub-assemblies (PCB, chassis) into full **product BOM**. |
| 4 | **原価集計**<br>各部品の単価を積み上げ、サブAssy → 製品全体の原価を算出。<br>加工費や共通費も加味して最終コストを評価する。 | **Cost roll-up**<br>Sum unit costs from parts → sub-assembly → full product.<br>Include processing and overhead costs for final evaluation. |

---

## 📕 上級 (Advanced)

| No | 課題 (Japanese) | Task (English) |
|----|-----------------|----------------|
| 5 | **輸出可否判定**<br>部品ごとの該非判定と HSコードを積み上げ、製品全体の輸出可否を判断。<br>デュアルユース時は **用途説明書** を作成。 | **Export feasibility check**<br>Aggregate classification and HS codes to judge export eligibility.<br>For dual-use items, prepare **End-use Statement**. |
| 6 | **消防法対応の確認**<br>材料コード（6番）の SDS を参照し、危険物の類・項・指定数量を判定。<br>保管条件を BOM に追記。 | **Fire law compliance**<br>Check SDS for materials (code 6) to classify hazards (category, item, quantity).<br>Add storage conditions to BOM. |
| 7 | **設計変更シナリオ演習**<br>ケースA: メッキ厚変更（枝番更新）<br>ケースB: 金型変更（枝番ルールで区別）<br>ケースC: 機能変更（6桁コード新規発行）<br>各変更で BOM と属性を更新し、積み上げ結果を確認。 | **Design change scenarios**<br>Case A: Plating thickness change (suffix update)<br>Case B: Mold change (suffix distinction)<br>Case C: Functional change (new 6-digit code)<br>Update BOM and attributes, then check roll-up results. |

---

## 🎯 学習成果 | Learning Outcomes

| 日本語 (Japanese) | English |
|-------------------|---------|
| 部品コード付与と属性管理の実務スキル習得 | Acquire skills in part coding & attribute management |
| 積み上げ管理（環境・コスト・輸出）の流れを理解 | Understand roll-up flow (environment, cost, export) |
| 法規制対応（輸出管理・消防法）の重要性を体感 | Experience importance of legal compliance (export/fire law) |
| 設計変更時の判断基準を体系的に学ぶ | Learn systematic decision-making for design changes |

👉 これらの演習を通じて、**設計情報を「単なる図面」から「製品ライフサイクル管理データ」へ昇華させる力** を身につける。  
👉 Through these exercises, you will gain the ability to transform design data from **mere drawings** into **product lifecycle management assets**.  

---

[🔝 08_production_process/06_bom_generation に戻る ](./)

