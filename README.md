# EduMecha

**機械設計教育のためのパラメトリック設計教材（Creo対応）**  
**Parametric Mechanical Design Educational Materials (for Creo users)**

---
- 🇺🇸 [English version available here](./README_en.md)
---

## 📘 概要 | Overview

**EduMecha** は、パラメトリック3D CAD（主に PTC Creo Parametric）を活用して、機械設計の基礎から応用までを体系的に学ぶための教育用教材です。  
2D図面からの3Dモデリング、設計意図の可視化、筐体設計、三角法、アセンブリ設計、CAE連携など、実践的な技術スキルを段階的に習得できます。

**EduMecha** is an educational repository for structured learning of mechanical design using parametric 3D CAD (primarily PTC Creo Parametric).  
It covers essential topics including 2D-to-3D modeling, visualization of design intent, enclosure design, third-angle projection, assembly design, and CAE integration.

---

## 🔧 特徴 | Features

- ✏️ **三面図からの3Dモデリング演習** / 2D → 3D modeling exercises  
- 📐 **拘束条件と設計意図の理解** / Parametric constraints and design intent  
- 🧩 **組立設計と部品図演習** / Assembly and part drawing training  
- 🛠 **AITL-H知能制御と連携した筐体設計** / Enclosure design integrated with AITL-H intelligent control  
- 📊 **Creo Simulate等とのCAE連携**（応力解析、重心評価など） / CAE integration (stress analysis, center of mass evaluation)

---

## 🧱 教材構成 | Directory Structure

```text
EduMecha/
├── 00_overview/                 # 教材概要とマップ
├── 01_parametric_basics/        # Creo操作入門とパラメトリック設計演習
├── 02_assembly_design/          # 組立・アセンブリ設計
├── 03_drawing_skills/           # 三角法と図面生成の理解
├── 04_legacy2parametric/        # 手描き図面 → 3Dモデリング教材
├── 05_mechatronic_integration/  # 制御対象との連携PoC（AITL-H筐体設計など）
├── 06_drafting_fundamentals/    # 製図の基本（投影・断面・寸法・公差・JIS）
├── 07_measurement_tools/        # 計測器と寸法評価（測定・校正・トレーサビリティ）
└── assets/                      # モデルデータ・図面PDF・教材画像など
```

## 🔗 関連プロジェクト | Related Projects

- [**Edusemi**](https://github.com/Samizo-AITL/Edusemi-v4x)  
  半導体設計・回路・sky130教材 / Semiconductor design and IC implementation using sky130

- [**EduController**](https://github.com/Samizo-AITL/EduController)  
  制御理論・AI制御の実装教材 / Control theory and AI control (PID, state-space, NN, LLM)

- [**AITL-H**](https://github.com/Samizo-AITL/AITL-H)  
  FSM×PID×LLMによる知能制御アーキテクチャ / Hierarchical intelligent control using FSM, PID, and LLM

- [**SamizoGPT**](https://github.com/Samizo-AITL/SamizoGPT)  
  ChatGPTプロンプト支援・教材構築テンプレート集 / ChatGPT-based prompting and education support framework

---

## 📜 ライセンス | License

MIT License に基づき公開しています。非営利・教育目的での再利用を歓迎します。  
This repository is released under the MIT License. Educational and non-commercial reuse is welcome.

---

## 🧑‍🔬 執筆者情報 | Author

- **氏名 / Name**：三溝 真一（Shinichi Samizo）  
- **学歴 / Education**：信州大学大学院 電気電子工学修士課程 修了  

- **職歴 / Experience**：  
  セイコーエプソン株式会社にて以下の開発・製品化に従事：  
  - 半導体デバイス技術（0.35µm〜0.18µmノード）  
  - ロジック／メモリ／高耐圧インテグレーション技術  
  - インクジェット薄膜ピエゾアクチュエータ設計  
  - PrecisionCoreプリントヘッドの製品化展開

- **連絡先 / Contact**：  
  - GitHub：[Samizo-AITL](https://github.com/Samizo-AITL)  
  - Email：[shin3t72@gmail.com](mailto:shin3t72@gmail.com)

---
