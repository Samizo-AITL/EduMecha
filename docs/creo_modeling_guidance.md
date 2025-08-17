---
layout: default
title: Creo Free Plan Guide - 無料プランによる `.prt` / `.asm` 作成手順
---

# Creo 無料プラン活用による `.prt` / `.asm` ファイル作成・入手手順  
**Guide for Creating & Exporting Creo `.prt` / `.asm` Files Using Free Plans**

---

## ✅ 利用目的 | Purpose

- `01_parametric_basics/` 以下の演習で必要となる3D CADモデルの作成  
- `.prt`, `.asm`, `.step` などのエクスポートによる教材配布  
- Creo Simulation Live 等を利用した設計検証付き演習の構築  

This guide explains how to create and export **Creo Parametric files** (`.prt`, `.asm`) using **PTC’s free plan options**, for use in EduMecha training materials.

---

## 🎓 対象読者 | Audience

- 教育関係者（高専・大学・専門学校など）  
- 教育支援者（教材制作者、設計支援者）  
- 学習者（学生、技術者志望者）  

For **educators, supporters, and learners** who need CAD models for training and coursework.

---

## 🧩 無料プランの選択肢 | Free Plan Options

| プラン名 | 利用対象 | 機能制限 | 有効期間 | URL |
|----------|-----------|-----------|------------|-----|
| **Creo Parametric Free Trial** | 一般技術者・教育関係者 | ほぼ制限なし | 14日間 | [PTC Try & Buy](https://www.ptc.com/en/try-and-buy/free-trials) |
| **Creo University Student Version** | 学生・教員（教育用） | 商用利用不可 | 1年間 | [PTC Education Portal](https://www.ptc.com/en/education/free-software/creo-university-download) |

> ✅ **推奨**：教材開発やモデル取得目的には、**14日間 Free Trial** を集中活用。  
> For education purposes, the **14-day Free Trial** is recommended for efficient model creation.

---

## 🛠️ 作成／入手ステップ | Steps to Create & Export Files

### 1. 無料トライアルの申請 | Apply for Free Trial
1. 上記URLから **Creo Free Trial** を選択  
2. 氏名・メール・所属を入力  
3. メールで **インストーラ＋ライセンスキー** を受領  

### 2. Creoのインストールと起動 | Install & Launch
- インストール後、起動時にライセンスキーを入力  
- 有効期間：14日間  

### 3. `.prt` / `.asm` ファイルの作成 | Create Parts/Assemblies
例：  
- `block_with_holes.prt` → スケッチ → 押し出し → 穴あけ  
- `bracket_assembly.asm` → 複数部品の配置＋拘束  

### 4. ファイルのエクスポート | Export Files
- 教材配布用に `.step`, `.iges`, `.pdf` 形式で保存  
- 方法：`File > Save As > Save a Copy` → 形式選択  

### 5. 教材反映・整理 | Organize for Training
- 各教材フォルダに格納（例：`01_block_with_holes/block_with_holes.prt`）  
- スクリーンショットや操作説明を `.md` として添付推奨  

---

## 📁 出力ファイル例 | Example Directory

```
01_parametric_basics/
├── 01_block_with_holes/
│   ├── block_with_holes.prt
│   ├── block_with_holes.step
│   └── 操作手順.md
├── 02_l_bracket_design/
│   ├── l_bracket.prt
│   └── bracket_assembly.asm
```

---

## 📌 注意点とヒント | Notes & Tips

- トライアル終了後はCreoが使用不可 → **必ずエクスポート保存**  
- 作業は **14日以内に集中** して進める  
- 継続利用が必要な場合 → **University版の申請**を検討  

---

## 💡 参考リンク | References

- [Creo Free Trial（PTC公式）](https://www.ptc.com/en/try-and-buy/free-trials)  
- [PTC Education（学生・教員向け）](https://www.ptc.com/en/education/free-software)  
- [Creo Parametric ドキュメント（操作マニュアル）](https://support.ptc.com/help/creo/creo_pma/usascii/index.html)  

---

## 📎 教材連動用タグ | Tags

- `#creo-model`  
- `#edu-parametric`  
- `#step-export`  
- `#eduMecha-compatible`  

---

著作：三溝真一（Samizo-AITL）  
ライセンス：MIT（教育目的での利用・改変を歓迎）
