---
layout: default
title:  EduMecha 概要 | EduMecha Overview
---

---

# EduMecha 概要 | EduMecha Overview

**EduMecha** は、PTC Creo Parametric を活用した、機械設計教育のためのオリジナル教材群です。  
基本操作からアセンブリ設計、図面生成、制御対象の筐体設計、さらには産業応用例までを段階的に学ぶことができます。

**EduMecha** is a specialized educational project for mechanical design using PTC Creo Parametric.  
It provides a structured learning path from basic modeling and assembly to technical drawings, enclosure design for control systems, and real-world industrial applications.

---

## 📁 ディレクトリ構成 | Directory Structure

| 📂 ディレクトリ | 📘 内容（日本語） | 📘 Description (English) |
|----------------|-------------------|---------------------------|
| **00_overview** | 教材の概要と構成マップ | Overview & Map |
| **01_parametric_basics** | Creo入門とパーツ設計の基礎（with Creo） | Intro to Creo & Parametric Basics (with Creo) |
| **02_assembly_design** | 部品の拘束・組立設計（with Creo） | Assembly Design Templates (with Creo) |
| **03_drawing_skills** | 三角法・図面生成と読解（with Creo） | Drawing & Projection Skills (with Creo) |
| **04_legacy2parametric** | 手描き図面からの3D再構築（with Creo） | Legacy 2D → Parametric 3D (with Creo) |
| **05_mechatronic_integration** | 制御対象との統合設計（筐体設計, with Creo） | Mechatronic Integration (with Creo) |
| **06_drafting_fundamentals** | 製図の基本（寸法・公差・JIS, 機械設計全般） | Drafting Fundamentals (General Mechanical Design) |
| **07_measurement_tools** | 寸法測定・校正・トレーサビリティ（機械設計全般） | Measurement Tools & Traceability (General Mechanical Design) |
| **08_production_process** | 製造プロセス教育の構成案（機械設計全般） | Production Process (General Mechanical Design) |
| **09_geometric_tolerancing** | 幾何公差（GD&T）の記法・演習・検査（機械設計全般） | Geometric Dimensioning & Tolerancing (GD&T, General Mechanical Design) |
| **templates** | テンプレート仕様設計（with Creo） | Template Specifications (with Creo) |
| **assets** | 教材用画像・参考図面（演習データは含まず） | Assets & Reference Figures |

---

## 🧭 学習フロー | Learning Flow

```plaintext
01: Creo入門（基本操作・スケッチ・押し出し）
 ↓
02: アセンブリ設計（拘束・干渉・接続）
 ↓
03: 図面生成（三角法・寸法記入・製図規格）
 ↓
04: 図面からの3D再構築（逆設計・意図推定）
 ↓
05: 制御対象の筐体設計（FSM/PID構造と接続）
```

---

## 🎯 主な特徴 | Key Features

- ✅ Creoによる **設計 → 組立 → 製図 → PoC接続** までを一貫して学習  
- ✅ 制御対象との **統合筐体設計**（FSM/PID連携）を演習化  
- ✅ **図面再構築（逆設計）** による図面理解力・空間認識力の育成  
- ✅ EduController・AITL-H・Edusemi との連携による **複合技術統合型教材**

---

## 🔗 関連プロジェクト | Related Projects

| プロジェクト | 内容 | リンク |
|--------------|------|--------|
| **Edusemi-v4x** | 半導体プロダクト開発のための基礎教育教材 | [![🌐 View Site](https://img.shields.io/badge/View%20Site-Edusemi-brightgreen?logo=github)](https://samizo-aitl.github.io/Edusemi-v4x/)<br>[![💻 View Repo](https://img.shields.io/badge/View%20Repo-Edusemi-blue?logo=github)](https://github.com/Samizo-AITL/Edusemi-v4x) |
| **EduController** | 制御理論／AI制御教材 | [![🌐 View Site](https://img.shields.io/badge/View%20Site-EduController-brightgreen?logo=github)](https://samizo-aitl.github.io/EduController/)<br>[![💻 View Repo](https://img.shields.io/badge/View%20Repo-EduController-blue?logo=github)](https://github.com/Samizo-AITL/EduController) |
| **AITL-H** | 知能制御統合アーキテクチャ | [![🌐 View Site](https://img.shields.io/badge/View%20Site-AITL--H-brightgreen?logo=github)](https://samizo-aitl.github.io/AITL-H/)<br>[![💻 View Repo](https://img.shields.io/badge/View%20Repo-AITL--H-blue?logo=github)](https://github.com/Samizo-AITL/AITL-H) |
| **SamizoGPT** | 教材構成・プロンプト支援 | [![🌐 View Site](https://img.shields.io/badge/View%20Site-SamizoGPT-brightgreen?logo=github)](https://samizo-aitl.github.io/SamizoGPT/)<br>[![💻 View Repo](https://img.shields.io/badge/View%20Repo-SamizoGPT-blue?logo=github)](https://github.com/Samizo-AITL/SamizoGPT) |
| **Inkjet** | インクジェット技術アーキテクチャ教材 | [![🌐 View Site](https://img.shields.io/badge/View%20Site-Inkjet-brightgreen?logo=github)](https://samizo-aitl.github.io/Inkjet/)<br>[![💻 View Repo](https://img.shields.io/badge/View%20Repo-Inkjet-blue?logo=github)](https://github.com/Samizo-AITL/Inkjet) |
| **PTC Creo Parametric（公式）** | 商用3D CAD | [![🌐 View Site](https://img.shields.io/badge/View%20Site-PTC%20Creo-brightgreen?logo=ptc)](https://www.ptc.com/en/products/creo) |

---

## 📝 ライセンスと利用について | License & Usage

本教材は [MITライセンス](https://opensource.org/licenses/MIT) に基づき、教育・研究・教材開発目的での自由な使用・改変・再配布が可能です。  
図面やモデルの編集、授業や演習での利用、PoCとの連携も歓迎します。

This content is released under the [MIT License](https://opensource.org/licenses/MIT).  
Free to use, modify, and redistribute for educational, research, and development purposes.
