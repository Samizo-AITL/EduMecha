---
title: "Creo Template Specification - sensor_mount_template.prt"
author: "EduMecha Project / 三溝真一"
license: "MIT"
tags: ["Creo", "Template", "Part", "EduMecha", "Sensor Mount"]
---

---

# 🔧 Creo テンプレート仕様書 | **`sensor_mount_template.prt`**

---

## ■ 概要 | **Overview**

このテンプレートは、**MEMS / PZT センサなどを固定・実装するためのマウントベース** 設計に使用されます。  
取り付け穴、パラメトリック寸法、リファレンス平面が事前定義されており、**センサ統合 PoC** や **筐体内実装モデル** の土台として活用できます。  

This template provides a **mounting base for MEMS / PZT sensors**.  
It includes predefined mounting holes, parametric dimensions, and reference planes, enabling use in **sensor integration PoCs** and **enclosure implementations**.  

---

## ■ モデル仕様 | **Model Specifications**

| **項目 / Item**          | **内容 / Details** |
|---------------------------|---------------------|
| **モデル名 / Filename**  | `sensor_mount_template.prt` |
| **種別 / Type**           | Part（単体パーツ / Single Part） |
| **単位系 / Unit System**  | mmks（mm, kg, sec, N） |
| **外形形状 / Shape**      | 円形 φ60 mm または 矩形 80×40 mm（選択可 / Selectable） |
| **厚み / Thickness**      | 8 mm（Param: `thickness`） |
| **取付穴 / Mounting Holes** | φ3.0 mm × 3（等配または対称配置 / Circular or symmetric placement） |
| **リファレンス平面 / Reference Planes** | 上面 / 下面 / 中心軸（拘束用 / For constraints） |
| **凹み / Recess (Optional)** | φ20 mm × 0.1 mm（Param: `recess_depth`） |
| **注釈 / Note**           | “センサ固定用の中間部品 / Intermediate part for sensor mounting” |

---

## ■ 作成手順（Creo） | **Creation Steps in Creo**

1. **新規パート作成 / New Part**  
   - 名前：`sensor_mount_template`  
   - 単位系：`mmks`  
   - データム：Top / Front / Right  

2. **外形スケッチ / Sketch Outer Shape**  
   - Top 平面に φ60 mm の円、または 80×40 mm の長方形  
   - Parameters: `diameter = 60` または `length = 80`, `width = 40`  

3. **押し出し / Extrude (Thickness)**  
   - 片側方向に **8 mm**  
   - Param: `thickness`  

4. **取付穴の作成 / Create Mounting Holes**  
   - 上面に φ3.0 mm 円を 3 つ配置  
   - 円形形状：120° 等配  
   - 矩形形状：左右対称配置  
   - 押し出しカット → 貫通  

5. **凹みの作成（オプション） / Optional Recess**  
   - φ20 mm × 0.1 mm の凹みを中央に追加  
   - Param: `recess_depth = 0.1`  

6. **パラメータ命名 / Parameter Naming**  
   - `thickness`, `hole_diameter`, `recess_depth`, `diameter`  
   - or `length`, `width`  

7. **注釈の追加 / Add Note**  
   - 上面に Note を追加  
   - 内容：**“センサ固定用の中間部品 / Intermediate part for sensor mounting”**  

---

## ■ 使用例 | **Example Usage**

- **`05_mechatronic_integration/`**：MEMS センサや PZT ユニットのベースモデル  
- **`02_assembly_design/`**：Mate / Align 演習用モデル  
- **`03_drawing_skills/`**：簡易製図演習  

---

## ■ 派生展開候補 | **Future Extensions**

- `sensor_mount_with_pins.prt`：ピン付きバージョン / With locating pins  
- `sensor_mount_param_demo.asm`：アセンブリ構成例 / Assembly demo  
- `sensor_mount_drawing.drw`：図面生成演習用 / For drawing practice  

---

## © 著作・利用条件 | **License**

© 2025 EduMecha Project / 三溝真一  
本テンプレートは **教育・研究目的において自由に使用・改変・再配布可能** です。  
This template is **free to use, modify, and redistribute** for **educational and research purposes**.  
