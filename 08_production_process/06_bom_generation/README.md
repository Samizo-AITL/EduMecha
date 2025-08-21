---
layout: default
title: "06_bom_generation"
description: "部品表（BOM）の作成と設計情報の構造化 / Bill of Materials (BOM) Generation and Structured Design Data"
author: "Project Design Hub"
date: 2025-08-18
tags: ["BOM", "部品コード", "設計管理", "輸出管理", "環境データ", "コスト管理"]
---

---

# 06_bom_generation

**部品表（BOM）の作成と設計情報の構造化**  
*Bill of Materials (BOM) Generation and Structured Design Data*

---

## 📑 目次 | Table of Contents
1. [📘 概要 | Overview](1_overview.html)
2. [🔢 部品コード体系 | Part Numbering System](2_part_numbering.html)
3. [📎 属性と輸出管理 | Attributes & Export Control](3_attributes.html)
4. [📊 積み上げ管理 | Roll-up Management](4_rollup_management.html)
5. [⚖️ 運用ルール | Rules](5_rules.html)
6. [🧪 演習課題 | Exercises](6_exercises.html)

<h2>📑 目次 | Table of Contents</h2>
<ol>
  <li><a href="1_overview.html">📘 概要 | <em>Overview</em></a></li>
  <li><a href="2_part_numbering.html">🔢 部品コード体系 | <em>Part Numbering System</em></a></li>
  <li><a href="3_attributes.html">📎 属性と輸出管理 | <em>Attributes &amp; Export Control</em></a></li>
  <li><a href="4_rollup_management.html">📊 積み上げ管理 | <em>Roll-up Management</em></a></li>
  <li><a href="5_rules.html">⚖️ 運用ルール | <em>Rules</em></a></li>
  <li><a href="6_exercises.html">🧪 演習課題 | <em>Exercises</em></a></li>
</ol>

---

## 📘 概要 | Overview
部品コード（6桁＋枝番）は **決まったルールに基づいて体系的に管理**されています。  
*Part codes (6 digits + suffix) are systematically managed according to defined rules.*  

コードを見れば大カテゴリ（機械・電子・材料・治具）、条件差（金型・製造地・改版）、さらに安全規制や輸出対応の要否まで追跡できます。  
*The code indicates major categories (mechanical, electronic, materials, jigs), condition differences (mold, production site, revision), and tracks regulatory and export requirements.*  

このセクションでは、設計構成に基づいた**部品表（BOM: Bill of Materials）**を作成し、量産や在庫管理に必要な構成情報を整理します。  
*This section covers creating the Bill of Materials (BOM) based on design structure, organizing essential data for mass production and inventory management.*  

BOMは単なる部品リストではなく、**設計〜調達〜生産〜輸出までをつなぐ共通言語**です。  
*A BOM is not just a list of parts, but a common language connecting design, procurement, production, and export.*  

---

## 🧑‍🏫 学習目標 | Learning Objectives
- 部品コードのルール（6桁＋枝番）を理解する  
  *Understand the rules of part coding (6 digits + suffix).*  
- 組立構造に対応した部品階層と親子関係を整理する  
  *Organize part hierarchy and parent-child relations for assemblies.*  
- 図面・環境・コスト・輸出判定を部品コードに紐づける  
  *Link drawings, environmental, cost, and export control data to part codes.*  
- 積み上げ管理（コスト・環境・輸出可否）の考え方を学ぶ  
  *Learn roll-up management for cost, environmental, and export compliance.*  
- 危険物（材料6番コード）の特別管理を理解する  
  *Understand special management for hazardous materials (category code 6).*  
