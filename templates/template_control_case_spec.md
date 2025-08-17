---
title: "Creo Template Specification - control_case_template.asm"
author: "EduMecha Project / 三溝真一"
license: "MIT"
tags: ["Creo", "Template", "Assembly", "EduMecha"]
---

---

# 🏗️ Creo テンプレート仕様書 | **`control_case_template.asm`**

---

## ■ 概要 | **Overview**

このテンプレートは、**制御回路やセンサモジュールを収納する筐体（ケース）構造** を設計・アセンブリ演習するための基本モデルです。  
ベース・カバーの **2部品構成** により、**アセンブリ拘束（Mate, Align, Insert）** や **寸法連携** を学べるように設計されています。  
AITL-H 筐体や量産設計 PoC にも展開可能です。  

This template models a **control case (enclosure) for electronic and sensor modules**.  
It consists of **two main parts (base and cover)** and is designed to train assembly constraints (**Mate, Align, Insert**) and **parameter sharing** in Creo.  
It can be extended to **AITL-H integration** and **mass-production PoC** scenarios.  

---

## ■ モデル仕様 | **Model Specifications**

| **項目 / Item**       | **内容 / Details** |
|------------------------|---------------------|
| **モデル名 / Filename** | `control_case_template.asm` |
| **種別 / Type**        | Assembly（アセンブリ / Assembly） |
| **単位系 / Unit System** | mmks（mm, kg, sec, N） |
| **構成部品 / Components** | `case_base.prt`, `case_cover.prt` |
| **外形寸法 / Dimensions** | 100 × 60 × 30 mm (initial) |
| **ケース厚み / Wall Thickness** | 2 mm (Cover) / 3 mm (Base) |
| **ネジ穴 / Screw Holes** | φ3.2 mm × 4 (corners) |
| **拘束方式 / Constraints** | Mate / Align / Insert |
| **パラメータ共有 / Shared Parameters** | `case_height`, `cover_thickness`, `hole_spacing` |
| **注釈 / Note** | “筐体構造の統合設計用テンプレート”<br>“Template for control case structure integration” |

---

## ■ 作成手順（Creo） | **Creation Steps in Creo**

### 🔹 **`case_base.prt`（ベース部品 / Base Part）**
1. 新規作成 → Top 平面に **100 × 60 mm** のスケッチ  
2. 押し出し高さ：**27 mm**（`case_height`）  
3. 外壁厚み：**3 mm**（Shell 処理可）  
4. 四隅に **φ3.2 mm 穴 ×4**  
5. パラメータ名：`base_length`, `base_width`, `case_height`  

---

### 🔹 **`case_cover.prt`（カバー部品 / Cover Part）**
1. 新規作成 → 同サイズ（100 × 60 mm）のスケッチ  
2. 押し出し厚み：**2 mm**（`cover_thickness`）  
3. 嵌合用の段差・凸部を設計（ベースと一致）  
4. 拘束基準面に **Note** を追加  

---

### 🔹 **`control_case_template.asm`（アセンブリ / Assembly）**
1. `case_base.prt` を **Default** で挿入  
2. `case_cover.prt` を **Mate**（上下）、**Align**（側面）で拘束  
3. 必要に応じて **Insert**（ネジ穴 ↔ 仮想ネジ）を使用  
4. 寸法共有または **Copy Geometry** により連携  

---

## ■ 使用例 | **Example Usage**

- **`05_mechatronic_integration/`**：センサ＋制御系統合 PoC  
- **`02_assembly_design/`**：Mate / Align / Insert 基本演習  
- **`08_production_process/`**：図面・加工・組立・評価演習  

---

## ■ 派生展開候補 | **Future Extensions**

- `control_case_exercise1.asm`（寸法変更演習モデル / Dimensional variation exercise）  
- `control_case_with_board.asm`（内部に基板を追加 / With PCB inside）  
- `control_case_drawing.drw`（図面演習用アセンブリ / For drawing practice）  

---

## © 著作・利用条件 | **License**

© 2025 EduMecha Project / 三溝真一  
**教育・研究目的に限り、自由に使用・改変・再配布可能**  
Free to use, modify, and redistribute for **educational and research purposes**.  
