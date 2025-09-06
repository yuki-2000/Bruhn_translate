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

    translator = GoogleTranslator(source='en', target='ja')

    for root, dirs, files in os.walk(source_dir):
        target_path = os.path.join(target_dir, os.path.relpath(root, source_dir))
        os.makedirs(target_path, exist_ok=True)

        for file in files:
            if file.endswith(".md"):
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_path, file)

                try:
                    with open(source_file, "r", encoding="utf-8") as f:
                        text = f.read()

                    # 段落を抽出
                    paragraphs = text.split('\n\n')  # 2つ以上の改行で分割

                    # 段落内の改行を削除
                    cleaned_paragraphs = [p.replace('\n', ' ') for p in paragraphs]  # 段落内の改行をスペースに置換


                    # 段落ごとに翻訳
                    translated_paragraphs = [translator.translate(p) for p in cleaned_paragraphs]

                    # 翻訳結果を結合
                    translated_text = '\n\n'.join(translated_paragraphs)  # 2つ以上の改行で結合

                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(translated_text)

                    print(f"Translated: {source_file} -> {target_file}")

                except Exception as e:
                    print(f"Error translating {source_file}: {e}")

# 使用例
source_directory = "markdown_en_test"
target_directory = "markdown_jp_google"

translate_markdown_files(source_directory, target_directory)


