# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 20:09:49 2025

@author: yuki
"""

import os
import glob
from deep_translator import GoogleTranslator

def translate_markdown_files(source_dir, target_dir):
    """
    指定されたフォルダにあるMarkdownファイルをGoogle翻訳で翻訳し、
    指定されたターゲットフォルダに同じフォルダ構成で保存します。
    """

    translator = GoogleTranslator(source='en', target='ja')  # 翻訳インスタンスを作成

    for root, dirs, files in os.walk(source_dir):
        # ソースディレクトリのすべてのファイルとフォルダを探索
        target_path = os.path.join(target_dir, os.path.relpath(root, source_dir))

        # ターゲットフォルダの対応するフォルダを作成
        os.makedirs(target_path, exist_ok=True)

        for file in files:
            if file.endswith(".md"):  # Markdownファイルのみ処理
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_path, file)

                try:
                    with open(source_file, "r", encoding="utf-8") as f:
                        text = f.read()

                    translated_text = translator.translate(text)

                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(translated_text)

                    print(f"Translated: {source_file} -> {target_file}")

                except Exception as e:
                    print(f"Error translating {source_file}: {e}")

# 使用例
source_directory = "markdown_en"
target_directory = "markdown_jp_google"

translate_markdown_files(source_directory, target_directory)