# Creo 無料プラン活用による `.prt` / `.asm` ファイル作成・入手手順

この文書は、EduMecha教材において必要となる Creo Parametric 向けの部品ファイル（`.prt`）およびアセンブリファイル（`.asm`）を、PTC社が提供する無料プランを活用して作成・取得・活用する手順を整理したものです。

---

## ✅ 利用目的

- `01_parametric_basics/` 以下の各演習に対応する3D CADモデルの作成
- `.prt`, `.asm`, `.step` 等のエクスポートによる教材配布
- Creo Simulation Live 等での検証付き演習構築

---

## 🎓 対象読者

- 教育関係者（高専・大学・専門学校など）
- 教育支援者（教材制作者、設計支援者）
- 学習者（学生、技術者志望者）

---

## 🧩 無料プランの選択肢

| プラン名 | 利用対象 | 機能制限 | 有効期間 | URL |
|----------|-----------|-----------|------------|-----|
| Creo Parametric Free Trial | 一般技術者、教育関係者 | ほぼ制限なし | 14日間 | [PTC Try & Buy](https://www.ptc.com/en/try-and-buy/free-trials) |
| Creo University Student Version | 学生・教員（教育用） | 商用利用不可 | 1年間 | [PTC Education Portal](https://www.ptc.com/en/education/free-software/creo-university-download) |

> ✅ **推奨**：教材開発・モデル取得目的には、14日間の「Free Trial」を集中活用。

---

## 🛠️ 作成／入手ステップ

### 1. 無料トライアルの申請
1. 上記URLより「Creo Free Trial」を選択
2. 氏名、メールアドレス、所属などを入力
3. メールでインストーラとライセンスキーが送付される

### 2. Creoのインストールと起動
- Creo Parametric をPCにインストール
- 起動時にライセンス入力（14日間有効）

### 3. `.prt` / `.asm` ファイルの作成
例：
- `block_with_holes.prt`：スケッチ → 押し出し → 穴あけ → 保存
- `bracket_assembly.asm`：複数部品配置と拘束 → 保存

### 4. ファイルのエクスポート（教材用）
- `.step` や `.iges`、`.pdf` 形式でエクスポートし、配布・再利用が可能
- エクスポート方法：`File > Save As > Save a Copy` → 形式選択

### 5. 作成ファイルの整理・教材反映
- 各教材フォルダに格納（例：`01_block_with_holes/block_with_holes.prt`）
- スクリーンショットや操作手順書も `.md` として添付推奨

---

## 📁 出力ファイル例（フォルダ構造）

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

## 📌 注意点とヒント

- トライアル終了後はCreoが使用できなくなるため、**必ずエクスポート保存を行うこと**。
- 作業は **期間内（14日）に集中して進める**。
- 学校環境などで継続利用が必要な場合は、**University版の申請も検討**。

---

## 💡 参考リンク

- [Creo Free Trial（PTC公式）](https://www.ptc.com/en/try-and-buy/free-trials)
- [PTC Education（学生・教員向け）](https://www.ptc.com/en/education/free-software)
- [Creo Parametric ドキュメント（操作マニュアル）](https://support.ptc.com/help/creo/creo_pma/usascii/index.html)

---

## 📎 教材連動用タグ（例）

- `#creo-model`
- `#edu-parametric`
- `#step-export`
- `#eduMecha-compatible`

---
