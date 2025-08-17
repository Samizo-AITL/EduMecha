---
layout: default
title:  03_drawing_skills - 機械図面の基本 | Drawing Skills
---

---

# 📝 **03_drawing_skills - 機械図面の基本 | Drawing Skills**

---

## 📖 **概要 | Overview**

このセクションでは、3Dモデルから2D図面を作成する方法を学びます。  
**三面図の構成、寸法の配置ルール、公差・注記の記入** など、製図における基本スキルを習得します。  

In this section, you will learn how to create **2D drawings from 3D models**.  
The focus is on **orthographic views, dimensioning rules, tolerances, and annotations**, which are fundamental to technical drafting.  

---

## 🎯 **学習目標 | Learning Goals**

- 📐 **三角法（正面図・上面図・側面図）の配置理解**  
  Understanding the placement of **orthographic views** (front, top, side)  
- 📏 **寸法記入・中心線・ねじ穴の記載方法**  
  Applying **dimensioning, centerlines, and hole notations**  
- 🖨️ **Creoを用いた図面テンプレート作成とPDF出力**  
  Creating drawing templates and exporting to PDF in Creo  

---

## 📂 **演習対象モデル | Target Models**

| 📄 **ファイル名 / File** | 📘 **説明（日本語） / Description (English)** |
|---------------------------|----------------------------------------------|
| `shaft.prt`   | 単一部品の三面図作成<br>Create orthographic views of a single part |
| `bracket.asm` | アセンブリ図としての寸法配置<br>Dimensioning of an assembly drawing |

🔗 [💻 View Repo](https://github.com/Samizo-AITL/EduMecha/tree/main/03_drawing_skills)

---

## 📁 **教材ファイル構成 | File Organization**

- `parts/` → 図面対象の3Dパーツ / 3D parts for drawings  
- `drawings/` → 出力されたPDF図面 / Exported PDF drawings  
- `templates/` → 図面テンプレート（枠・表題欄） / Drawing templates (frame, title block)  
- `exercises.md` → 練習課題 / Exercises  

---

## 📝 **推奨演習課題 | Suggested Exercises**

1. `shaft.prt` の三面図を作成し、全寸法を記入する。  
   Create orthographic views of `shaft.prt` and add all dimensions.  
2. `bracket.asm` のアセンブリ図を作成し、主要な位置・直径・深さを注記する。  
   Produce an assembly drawing of `bracket.asm` with dimensions and annotations.  
3. 表題欄付きテンプレート（`drawing_frame.drw`）を適用し、PDFに出力する。  
   Apply the drawing template (`drawing_frame.drw`) and export as PDF.  

---

## ⚠️ **注意点 | Notes**

- ❗ 寸法の **過剰・不足** に注意（必要十分性の確保）  
  Avoid excessive or missing dimensions (ensure completeness without redundancy).  
- 🔩 ネジ穴・軸穴には **中心線・ピッチ円・ねじ記号** を必ず記載  
  For holes and shafts, always include **centerlines, pitch circles, and thread symbols**.  

---

## 👤 **著作・ライセンス | Author & License**

- ✍️ 著作 / Author: **三溝真一（Samizo-AITL）**  
- 📜 ライセンス / License: **MIT** （教育目的での使用・改変を歓迎）  
  MIT License (Free use and modification for educational purposes)  
