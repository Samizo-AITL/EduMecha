# EduMecha

**機械設計教育のためのパラメトリック設計教材（Creo対応）**  
**Parametric Mechanical Design Educational Materials (for Creo users)**

---

- 🇺🇸 [English version available here](./README_en.md)

---

## 📘 概要 | Overview

**EduMecha** は、パラメトリック3D CAD（主に PTC Creo Parametric）を活用し、機械設計の基礎から応用までを体系的に学ぶための教育用教材です。  
2D図面からの3Dモデリング、設計意図の可視化、筐体設計、三角法、アセンブリ設計、CAEとの連携など、**実践的な技術スキルを段階的に習得**できます。

**EduMecha** is an educational repository designed for structured learning of mechanical design using parametric 3D CAD (primarily PTC Creo Parametric).  
It provides hands-on learning in 2D-to-3D modeling, design intent visualization, enclosure modeling, third-angle projection, assembly design, and CAE integration.

---

## 🔧 特徴 | Features

- ✏️ **三面図からの3Dモデリング演習**  
  *2D → 3D modeling exercises*

- 📐 **拘束条件と設計意図の理解**  
  *Understanding parametric constraints and design intent*

- 🧩 **組立設計と部品図演習**  
  *Assembly modeling and part drawing training*

- 🛠 **AITL-H知能制御と連携した筐体設計**  
  *Enclosure design integrated with AITL-H intelligent control system*

- 📊 **Creo Simulate等とのCAE連携**  
  *Integration with CAE tools such as Creo Simulate (stress analysis, center of gravity, etc.)*

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
├── 08_production_process/       # 量産移行までの一貫プロセス教材
├── templates/                   # Creo用パラメトリックテンプレート（仕様書付き）
└── assets/                      # モデルデータ・図面PDF・教材画像など
```

📁 Creo用テンプレート一覧 → [`templates/`](./templates/)

---

## 🔗 関連プロジェクト | Related Projects

- [**Edusemi**](https://github.com/Samizo-AITL/Edusemi-v4x)  
  半導体設計・回路・sky130教材  
  *Semiconductor design and IC implementation using sky130*

- [**EduController**](https://github.com/Samizo-AITL/EduController)  
  制御理論・AI制御の実装教材（PID, 状態空間, 強化学習, LLM対応）  
  *Control theory and AI control (PID, state-space, reinforcement learning, LLM integration)*

- [**AITL-H**](https://github.com/Samizo-AITL/AITL-H)  
  FSM×PID×LLMによる階層型知能制御アーキテクチャ  
  *Hierarchical intelligent control using FSM, PID, and LLM*

- [**SamizoGPT**](https://github.com/Samizo-AITL/SamizoGPT)  
  ChatGPTプロンプト支援・教材テンプレート・構成管理支援フレームワーク  
  *Prompt engineering and education framework based on ChatGPT*

- [**PTC Creo Parametric（公式サイト）**](https://www.ptc.com/en/products/creo)  
  モデリング・アセンブリ・シミュレーションに対応した3D CADシステム  
  *Official site for PTC Creo Parametric*

---

## 📜 ライセンス | License

MIT License に基づき公開しています。非営利・教育目的での再利用を歓迎します。  
This repository is released under the MIT License. Educational and non-commercial reuse is welcome.

---

## 👤 執筆者情報 | Author

**三溝 真一（Shinichi Samizo）**  
- 信州大学大学院 電気電子工学 修了  
- 元 セイコーエプソン株式会社 技術者（1997年〜）

📌 **経験領域**  
- 半導体デバイス（ロジック／メモリ／高耐圧混載）  
- 薄膜ピエゾアクチュエータ技術  
- PrecisionCoreプリントヘッド製品化と構成管理

📬 **連絡先**  
- ✉️ [shin3t72@gmail.com](mailto:shin3t72@gmail.com)  
- 🐦 [@shin3t72 on X](https://x.com/shin3t72)  
- 💻 [samizo-aitl.github.io](https://samizo-aitl.github.io/)

---

## 💬 フィードバック・質問 | Feedback & Discussion

教材に関するご質問・改善提案・使用事例の共有などは、GitHub Discussions にて歓迎します。  
ぜひお気軽にご参加ください。

👉 [EduMecha Discussions ページへ移動](https://github.com/Samizo-AITL/EduMecha/discussions)

We welcome your questions, suggestions, and use case sharing in [EduMecha Discussions](https://github.com/Samizo-AITL/EduMecha/discussions).  
Feel free to join the conversation
