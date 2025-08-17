---
layout: default
title:  05_mechatronic_integration - 制御筐体統合設計演習 | Mechatronic Integration
---

---

# 🔧 **05_mechatronic_integration - 制御筐体統合設計演習 | Mechatronic Integration**

---

## 📖 **概要 | Overview**

このセクションでは、**制御対象（モーター、センサー、基板など）を収める筐体設計** を演習形式で学びます。  
Creo Parametric による3D設計と、**AITL-H / EduController** で扱う制御構造との連携を意識した実践的課題を扱います。  

In this section, you will practice **designing mechanical enclosures for control systems (motors, sensors, PCBs, etc.)**.  
The exercises emphasize **integration with AITL-H / EduController** architectures for mechatronic applications.  

---

## 🎯 **学習目標 | Learning Goals**

- ⚙️ **制御対象を収める筐体設計の基本**  
  Basics of enclosure design for control devices  
- 🪛 **モジュール間インターフェースの定義**  
  Defining interfaces between mechatronic modules  
- 📐 **Creoを用いた拘束・干渉チェック**  
  Using Creo for constraint and interference checks  
- 🔄 **制御アーキテクチャとの連携**  
  Connecting CAD design with control system design  

---

## 📂 **教材構成 | File Organization**

| 📁 **フォルダ名 / Folder** | 📘 **内容（日本語） / Description (English)** |
|-----------------------------|------------------------------------------------|
| `03_gimbal_frame/` | ジンバル筐体設計演習<br>Gimbal frame design exercise |
| `exercises.md` | 課題リストと手順書<br>Exercise list and instructions |
| `drawings/` | 出力図面（PDF）<br>Generated drawings (PDF) |
| `models/` | Creo モデルファイル（`.prt`, `.asm`）<br>Creo model files (`.prt`, `.asm`) |

🔗 [💻 View Repo](https://github.com/Samizo-AITL/EduMecha/tree/main/05_mechatronic_integration)

---

## 📝 **演習課題例 | Example Exercises**

1. **ジンバル筐体設計**  
   - `03_gimbal_frame/` の仕様を参考に、2軸ジンバルフレームを作成する。  
   - Design a 2-axis gimbal frame based on `03_gimbal_frame/` specs.  

2. **干渉チェックと修正**  
   - モーター・基板を組み込み、干渉解析を実施する。  
   - Assemble motors and PCBs, and perform interference analysis.  

3. **制御モジュールの統合**  
   - EduController / AITL-H に対応するI/O配置を考慮した筐体設計を行う。  
   - Design the enclosure considering I/O placement for EduController / AITL-H.  

---

## ⚠️ **注意事項 | Notes**

- 📌 実寸大設計ではなく、教育用に縮小・簡略化したモデルを扱う。  
  Models are scaled/simplified for educational purposes.  
- 🔗 実際の制御対象との連携は **EduController** 演習に展開可能。  
  Real integration can be extended via **EduController** exercises.  

---

## 👤 **著作・ライセンス | Author & License**

- ✍️ 著作 / Author: **三溝真一（Samizo-AITL）**  
- 📜 ライセンス / License: **MIT** （教育目的での使用・改変を歓迎）  
  MIT License (Free use and modification for educational purposes)  
