---
title: "Creo Template Specification - sensor_mount_template.prt"
author: "EduMecha Project / 三溝真一"
license: "MIT"
tags: ["Creo", "Template", "Parametric", "EduMecha"]
---

---

# 📐 Creo テンプレート仕様書 | **`sensor_mount_template.prt`**

---

## ■ 概要 | **Overview**

このテンプレートは、**センサ固定用の円形マウントプレート** をモデル化したものです。  
中心穴および複数の取り付け穴があらかじめ定義されており、**制御対象や筐体へのセンサ実装** を想定した派生設計のベースとして使用可能です。  

This template represents a **circular sensor mounting plate** in Creo.  
It includes a central hole and multiple mounting holes, designed as a **base model for sensor integration** into enclosures or control targets.  

---

## ■ モデル仕様 | **Model Specifications**

| **項目 / Item** | **内容 / Details** |
|-----------------|---------------------|
| **モデル名 / Filename** | `sensor_mount_template.prt` |
| **種別 / Type** | Part（単体パーツ / Single Part） |
| **単位系 / Unit System** | mmks（mm, kg, sec, N） |
| **外形寸法 / Outer Diameter** | φ80 mm（`plate_diameter`） |
| **厚み / Thickness** | 8 mm（`plate_thickness`） |
| **中心穴 / Center Hole** | φ25 mm（`center_hole_diameter`） |
| **取付穴 / Mounting Holes** | φ6 mm × 4（円周60 mm ピッチ円 / On Ø60 mm PCD, `mount_hole_diameter`） |
| **データム / Datums** | Top / Front / Right（中心で交差 / Intersect at center） |
| **注釈 / Note** | “センサ固定用の円形プレートテンプレート” / "Circular plate template for sensor mounting" |

---

## ■ 作成手順（Creo） | **Creation Steps in Creo**

1. **新規パート作成 / New Part**  
   - ファイル名 / Filename：`sensor_mount_template`  
   - 単位系 / Units：`mmks`  
   - データム / Datums：**Top / Front / Right at origin**

2. **外形円スケッチ / Outer Circle Sketch**  
   - Top 平面に φ80 mm の円  
   - パラメータ名：`plate_diameter = 80`

3. **押し出し / Extrusion**  
   - 厚み：8 mm  
   - パラメータ名：`plate_thickness`

4. **中心穴作成 / Center Hole**  
   - 上面にスケッチ、原点に φ25 mm 円  
   - 押し出しカット → Through All  
   - パラメータ名：`center_hole_diameter = 25`

5. **取付穴作成 / Mounting Holes**  
   - 半径30 mm の位置に φ6 mm 穴を1つ作成  
   - 円周上に4等配パターン  
   - パラメータ名：`mount_hole_diameter = 6`

6. **注釈追加 / Add Note**  
   - 上面に **Note** を追加  
   - 内容：**“センサ固定用の円形プレートテンプレート”**

---

## ■ 使用例 | **Example Usage**

- **`05_mechatronic_integration/`**：センサ搭載構造演習  
- **`08_production_process/`**：BOM付き量産検討モデル  
- 制御対象（モータ／センサ筐体）の固定プレート設計への応用  

---

## ■ 今後の展開候補 | **Future Extensions**

- `sensor_mount_with_slots.prt`（長穴スロット付き / With elongated slots）  
- `sensor_mount_drawing.drw`（製図用テンプレート / Drawing template）  
- 小型・大型センサ向け派生版（φ40, φ120 Variants）  

---

## © ライセンス | **License**

© 2025 EduMecha Project / 三溝真一  
**教育・研究目的に限り、自由に使用・改変・再配布可能**  
Free to use, modify, and redistribute for **educational and research purposes**.  
