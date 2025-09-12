# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要
Discord botプロジェクト - Twitter/X.comのURLをFxTwitterに変換してDiscordの埋め込みを修正

## 開発コマンド

### セットアップと実行
```bash
# 依存関係のインストール
poetry install

# 環境変数の設定
cp .env.example .env
# .envファイルにDiscord bot TOKENを設定

# Botの実行
poetry run python app/main.py
```

### コードフォーマット
```bash
# Black でフォーマット
poetry run black app/

# isort でimportの整理
poetry run isort app/
```

## アーキテクチャ

### 主要コンポーネント
- **app/main.py**: Discord botのメインエントリーポイント
  - `on_message`イベントでメッセージを監視
  - Twitter/X.comのURLを検出して変換処理を呼び出し
  
- **app/edit_url.py**: URL変換ロジック
  - `edit_twitter_url()`: メッセージ内のTwitter URLを検出・変換
  - `replace_twitter_urls()`: twitter.com/x.com → fxtwitter.comへの変換
  - `suppress_embeds()`: 元メッセージの埋め込みを抑制
  - スポイラー（||で囲まれたテキスト）に対応

### 依存関係管理
- Poetry使用（pyproject.toml）
- Python 3.11以上が必要