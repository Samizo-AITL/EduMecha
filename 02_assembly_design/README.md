---
layout: default
title:  02_assembly_design - アセンブリ設計演習 | Assembly Design Exercises
---

---

# 🧩 **02_assembly_design - アセンブリ設計演習 | Assembly Design Exercises**

---

## 📖 **概要 | Overview**

このセクションでは、複数の部品を組み合わせて1つの機構を構成する  
**「アセンブリ設計」** を学びます。  

Creo Parametric における **拘束条件**（マテ、アライメント、距離、角度など）を活用し、  
パーツ同士の位置関係を明確に定義する技術を習得します。  

In this section, you will learn **assembly design**, where multiple parts are combined into one mechanism.  
You will practice applying **constraints** (mate, align, distance, angle, etc.) in Creo Parametric to define the positional relationships between parts.  

---

## 🎯 **学習目標 | Learning Goals**

- 🛠️ アセンブリモードでの基本操作の理解  
  Understanding basic operations in **Assembly Mode**  
- 🔗 拘束条件（Mate / Coincident / Distance / Angle）の適用方法習得  
  Applying **constraints** (mate, coincident, distance, angle)  
- ⚠️ アセンブリ設計におけるエラー検出（干渉、自由度過多など）の理解  
  Detecting **errors** in assembly design (interference, redundant constraints, etc.)  

---

## 📂 **使用モデル一覧 | Model Files**

| 📄 **ファイル名 / File** | 📘 **説明（日本語） / Description (English)** |
|---------------------------|----------------------------------------------|
| `base.prt` | 土台となるベースプレート<br>Base plate |
| `shaft.prt` | 差し込まれる円筒シャフト<br>Cylindrical shaft |
| `bracket.asm` | 上記2部品を結合したアセンブリ<br>Assembly combining base & shaft |
| `bracket_assembly.pdf` | 注記付き組立図<br>Annotated assembly drawing |

🔗 [💻 View Repo](https://github.com/Samizo-AITL/EduMecha/tree/main/02_assembly_design)

---

## 📝 **演習課題 | Exercises**

1. `base.prt` と `shaft.prt` をアセンブリ化し、 `bracket.asm` を作成する。  
   Assemble `base.prt` and `shaft.prt` into `bracket.asm`.  
2. シャフトの円筒面とベースの穴内面を **同軸拘束（Coincident）** で位置合わせする。  
   Align the shaft axis with the hole using **coincident constraint**.  
3. シャフトの底面とベース上面を **接触拘束（Mate）** で固定する。  
   Mate the bottom of the shaft with the top of the base.  
4. 拘束の自由度が過剰になっていないか確認する。  
   Verify that no redundant constraints exist.  
5. 組立図を `bracket_assembly.pdf` として出力し、寸法・注記を追加する。  
   Output an annotated drawing as `bracket_assembly.pdf`.  

---

## 💻 **推奨環境 | Recommended Environment**

- Creo Parametric **8.0 以降 / Version 8.0 or later**  
- モデルファイル構成 / File organization:  
  - `parts/` → 個別パーツ / individual parts  
  - `assembly/` → 完成アセンブリ / completed assembly  
  - `drawings/` → PDF図面 / drawings (PDF)  

---

## 🔗 **次章との関連 | Relation to Next Chapter**

この演習は **次章「03_drawing_skills」** と連動し、  
**組立図の出力・注記追加** に発展します。  

This exercise connects to **Chapter 03: Drawing Skills**,  
where you will expand into **assembly drawings with annotations**.  

---

## 👤 **著作・ライセンス | Author & License**

- ✍️ 著作 / Author: **三溝真一（Samizo-AITL）**  
- 📜 ライセンス / License: **MIT** （教育目的での再利用を歓迎）  
  MIT License (Free reuse for educational purposes)  
