---
layout: default
title:  04_legacy2parametric - 手描き図面からの3D復元演習 | Legacy 2D → Parametric 3D
---

---

# 🏗️ **04_legacy2parametric - 手描き図面からの3D復元演習 | Legacy 2D → Parametric 3D**

---

## 📖 **概要 | Overview**

このセクションでは、**手描きや旧来の2D図面から3Dパラメトリックモデルを復元** する課題に取り組みます。  
図面から設計意図を読み解き、形状・寸法・拘束条件を合理的に推定し、再現する力を養います。  

In this section, you will work on **reconstructing 3D parametric models from legacy or hand-drawn 2D drawings**.  
The goal is to interpret design intent, infer missing dimensions, and apply constraints logically in Creo.  

---

## 🎯 **学習目標 | Learning Goals**

- 🖼️ **三面図の読解と空間的形状の想像**  
  Understanding orthographic views and visualizing 3D geometry  
- 📏 **欠落寸法や不明瞭な指示の補完スキル**  
  Estimating and supplementing missing or unclear dimensions  
- ⚙️ **Creoによる拘束設計での正確なモデル再現**  
  Accurate model reconstruction using parametric constraints in Creo  

---

## 📂 **教材構成 | File Organization**

| 📁 **フォルダ名 / Folder** | 📘 **内容（日本語） / Description (English)** |
|-----------------------------|------------------------------------------------|
| `legacy_drawings/` | 元図面（PDFやスキャン）<br>Original drawings (PDF/scans) |
| `recreated_models/` | 復元3Dモデル（`.prt`）<br>Recreated 3D models (`.prt`) |
| `verification/` | 形状・寸法比較用の考察ログ<br>Logs for shape & dimension verification |
| `exercises.md` | 演習課題<br>Exercises for drawing-to-model reconstruction |

🔗 [💻 View Repo](https://github.com/Samizo-AITL/EduMecha/tree/main/04_legacy2parametric)

---

## 📝 **演習課題例 | Example Exercises**

1. `old_mount_plate.pdf` をもとに、プレート構造を再構築する。  
   Recreate the plate structure from `old_mount_plate.pdf`.  
2. 欠落している穴位置寸法を推定し、合理的に配置する。  
   Estimate missing hole dimensions and create a logical layout.  
3. `shaft_holder_handdrawn.jpg` の手描き図を復元し、制御対象に使用可能な拘束構造を設計する。  
   Reconstruct `shaft_holder_handdrawn.jpg` into a parametric model suitable for mechanical constraints.  
4. `comparison_notes.md` に設計意図と再現過程を記述する。  
   Document the design intent and reconstruction process in `comparison_notes.md`.  

---

## ⚠️ **注意事項 | Notes**

- ❗ 一部寸法が欠落した図面を教材とすることで、**推定・判断・根拠の説明力** を養う。  
  Some drawings intentionally omit dimensions to train **estimation, reasoning, and justification skills**.  
- 🔄 正解が1つとは限らず、**設計合理性と一貫性** を重視する。  
  Multiple correct solutions may exist; emphasis is on **design logic and consistency**.  

---

## 👤 **著作・ライセンス | Author & License**

- ✍️ 著作 / Author: **三溝真一（Samizo-AITL）**  
- 📜 ライセンス / License: **MIT** （教育目的での使用・改変を歓迎）  
  MIT License (Free use and modification for educational purposes)  

