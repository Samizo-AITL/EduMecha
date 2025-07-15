# EduMecha 概要 | EduMecha Overview

EduMechaは、Creoを用いた機械設計の教育教材群です。  
基本操作から、組立設計、図面出力、制御対象設計、さらには産業応用までを段階的に学べます。

EduMecha is an educational project for mechanical design using Creo.  
It covers basic modeling, assembly, drawing, control-targeted structures, and industrial applications.

---

## 📁 ディレクトリ構成 | Directory Structure

| ディレクトリ | 内容（日本語） | Description (English) |
|--------------|------------------|-------------------------|
| `00_overview/` | 教材の概要と構成マップ | Overview and structure map |
| `01_parametric_basics/` | Creo入門と部品設計の基礎 | Basic part design with Creo |
| `02_assembly_design/` | 複数部品の組立・拘束設計 | Assembly and constraint design |
| `03_drawing_skills/` | 三角法による図面生成・読解 | 2D drawing creation and reading |
| `04_legacy2parametric/` | 手描き図面 → 3Dモデル再構築 | Rebuilding 3D models from 2D drawings |
| `05_mechatronic_integration/` | 制御対象との統合設計教材 | Mechatronic integration for control |
| `06_inkjet_actuator/` | ピエゾアクチュエータ構造設計 | Inkjet actuator structural design |
| `assets/` | モデル・図面・教材画像など | Models, drawings, and educational images |

---

## 🧭 学習フロー | Learning Flow

```plaintext
01: パーツ設計（Creo入門）
 ↓
02: アセンブリ設計（拘束と動作理解）
 ↓
03: 図面生成と三角法の理解
 ↓
04: 図面から3Dモデル再構築（設計意図の逆探索）
 ↓
05: 制御対象の構造設計（FSM/PIDと接続）
 ↓
06: 応用設計（産業構造例としてのインクジェット）
```

From basic modeling to assembly, drawing, reverse modeling, and PoC-level structural design.

---

## 🎯 教材の特徴 | Key Features

- ✅ Creoによる**パーツ設計 → 組立 → 製図 → PoC**の一貫教材  
- ✅ FSM・PID制御対象モデル（AITL-HX）と連携可能  
- ✅ 手描き図面からの再構築など「図面しか知らない層」もカバー  
- ✅ 半導体・制御・知能教材と統合されたクロス教材設計  

---

## 🔗 関連プロジェクト | Related Projects

- [EduController](https://github.com/Samizo-AITL/EduController)  
  制御理論・AI制御教材（PID/NN/RL/LLM）

- [AITL-H](https://github.com/Samizo-AITL/AITL-H)  
  FSM × PID × LLM 統合制御アーキテクチャ

- [Edusemi](https://github.com/Samizo-AITL/Edusemi-v4x)  
  半導体設計と製造・検査・PoC教材群

- [SamizoGPT](https://github.com/Samizo-AITL/SamizoGPT)  
  ChatGPT活用・教材設計支援テンプレート

---

## 📝 ライセンスと利用について | License and Usage

本教材は、教育・研究・教材開発用途に自由に使用・改変できます（MITライセンス）。  
図面やモデルの改変、授業利用、PoC連携なども歓迎します。

This content is licensed under the MIT License and is free to use for education, research, and development purposes.

---
