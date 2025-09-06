# -*- coding: utf-8 -*-
"""
Created on Sat Sep  6 20:09:49 2025

@author: yuki
"""

import os
import glob
from deep_translator import GoogleTranslator
import re

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

                    paragraphs = text.split('\n\n')

                    translated_paragraphs = []
                    for paragraph in paragraphs:
                        # #から始まる段落（ヘッダー）
                        header_match = re.match(r'#\s*(.*)', paragraph)
                        if header_match:
                            header = header_match.group(1)
                            remaining_text = paragraph[len(header) + 1:]
                            translated_text = translator.translate(remaining_text)
                            translated_paragraph = f"{header} {translated_text}"
                        # ![](から始まる段落（画像）
                        elif paragraph.startswith("![]("):
                            translated_paragraph = paragraph
                        # 数式
                        elif re.search(r'\$\$[.\n]*?\$\$', paragraph):
                            translated_paragraph = paragraph
                        else:
                            # 段落内の改行をスペースに置換
                            cleaned_paragraph = paragraph.replace('\n', ' ')
                            translated_text = translator.translate(cleaned_paragraph)
                            translated_paragraph = translated_text
                        translated_paragraphs.append(translated_paragraph)

                    translated_text = '\n\n'.join(translated_paragraphs)

                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(translated_text)

                    print(f"Translated: {source_file} -> {target_file}")

                except Exception as e:
                    print(f"Error translating {source_file}: {e}")

# 使用例
source_directory = "markdown_en_test"
target_directory = "markdown_jp_google"

translate_markdown_files(source_directory, target_directory)


