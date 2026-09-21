# Hermes Skill Library

[English](README.md) | [한국어](README.ko.md) | **日本語** | [中文](README.zh-CN.md)

Hermes Agent 系アシスタント向けの再利用可能なスキルライブラリです。単一用途のパッケージではなく、全体または目的別コレクションを導入できます。

## コレクション

| コレクション | 用途 |
|---|---|
| [`gstack-safe`](collections/gstack-safe/) | 根拠重視の仕様策定・レビュー・調査 |
| [`agent-engineering`](collections/agent-engineering/) | コーディングエージェント CLI への範囲限定した委任 |
| [`research-workflows`](collections/research-workflows/) | 情報収集・監視・ML 実験・評価根拠の管理 |
| [`comfyui-image-workflows`](collections/comfyui-image-workflows/) | ComfyUI の生成・バッチ・検証・障害対応 |
| [`wsl-operator`](collections/wsl-operator/) | Windows/WSL パスと GUI ランチャー |
| [`oauth-browser-handoff`](collections/oauth-browser-handoff/) | ヘッドレス・WSL・遠隔環境からの OAuth ブラウザ完了 |
| [`profile-context-diet`](collections/profile-context-diet/) | 古い、または過剰なプロファイルコンテキストの整理 |
| [`hermes-profile-operations`](collections/hermes-profile-operations/) | 複数プロファイルの設定・容量・コンテキスト管理 |
| [`local-development-safety`](collections/local-development-safety/) | 範囲の狭いローカル変更と最新の完了根拠 |
| [`github-publishing`](collections/github-publishing/) | WSL 対応の公開と遠隔状態検証 |
| [`telegram-operator`](collections/telegram-operator/) | 簡潔で事実に基づく Telegram 進捗・結果報告 |
| [`computer-use-safety`](collections/computer-use-safety/) | バックグラウンド優先のデスクトップ操作と安全な段階移行 |
| [`web-interface-verification`](collections/web-interface-verification/) | レスポンシブ・タッチ・ホバー・タブレット幅の検証 |
| [`repository-maintenance`](collections/repository-maintenance/) | フォーク・ミラー・ベンダースナップショット・下流コードの監査 |
| [`artifact-recovery`](collections/artifact-recovery/) | 曖昧な過去のローカルファイルを根拠に基づいて復元し安全に受け渡す |

各リンクには収録スキルと利用案内があります。機械可読の一覧は [`catalog.json`](catalog.json) です。

## 全スキルの導入

```bash
git clone https://github.com/Bum-Boo/hermes-skill-library.git
cd hermes-skill-library
./scripts/install.sh
hermes skills list
```

```bash
# Install for one profile
./scripts/install.sh ~/.hermes/profiles/<profile>/skills
hermes --profile <profile> skills list
```

既定の導入先は `~/.hermes/skills` です。CLI が `skills list` の `--profile` に対応しない場合、そのプロファイルでチャットを開始し、導入済みスキルの一覧表示または読み込みを依頼してください。

> インストーラーは対象へファイルをコピーし、同じパスのファイルを置き換える場合があります。実行前にソースと対象をご確認ください。

## 1 コレクションのみ導入

```bash
./scripts/install-collection.sh <collection-name>
./scripts/install-collection.sh comfyui-image-workflows ~/.hermes/profiles/<profile>/skills
```

上表の名前を使用してください。[`scripts/install-collection.sh`](scripts/install-collection.sh) に実装されていない名前はエラーになります。

## リポジトリ構成

```text
skills/<category>/<skill-name>/SKILL.md  導入可能なスキル
collections/<collection>/README.md      目的別の案内
scripts/install.sh                      全スキルを導入
scripts/install-collection.sh           1 コレクションを導入
catalog.json                            コレクション一覧
SECURITY.md                             セキュリティ方針
LICENSE                                 MIT ライセンス
```

## 安全な貢献

有効な Hermes frontmatter を持つスキルを `skills/<category>/<skill-name>/SKILL.md` に置き、コレクション文書と `catalog.json` を更新してください。共有前に一時ディレクトリへの導入を試し、認証情報、個人パス、アカウント識別子、ブラウザプロファイル、顧客データが含まれないことをご確認ください。実際の秘密値はコミットしないでください。詳しくは [`SECURITY.md`](SECURITY.md) をご覧ください。

## 表記のお願い

本ライブラリや派生物を公開する際は、可能であれば **@Bum-Boo** と[元のリポジトリ](https://github.com/Bum-Boo/hermes-skill-library)をご紹介いただけると幸いです。これは謝意表記のお願いであり、ライセンス条件の追加・変更ではありません。

## ライセンス

MIT です。[`LICENSE`](LICENSE) をご覧ください。
