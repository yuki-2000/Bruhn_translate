import pypandoc
import os
import base64
import mimetypes
import re


def embed_images_as_base64(html_file, resource_path):
    with open(html_file, encoding='utf-8') as f:
        html = f.read()

    def repl(m):
        src = m.group(1)
        img_path = os.path.join(str(resource_path), src)
        if not os.path.exists(img_path):
            print(f"  Warning: image not found: {src}  (in {html_file})")
            return m.group(0)
        mime = mimetypes.guess_type(img_path)[0] or 'image/png'
        b64 = base64.b64encode(open(img_path, 'rb').read()).decode('ascii')
        return f'src="data:{mime};base64,{b64}"'

    html = re.sub(r'src="([^"]+\.(?:png|jpg|jpeg|gif))"', repl, html)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)


def convert_md_to_html(input_file, output_file, resource_path):
    title = os.path.splitext(os.path.basename(input_file))[0]

    # Pandocのオプション設定
    # --standalone: ヘッダーやCSSを含む完全なHTMLを作成
    # -self-contained: 画像などをHTML内に埋め込む (オプション)
    # --katex: 数式の描写。mathjaxはうまくいかず
    # --metadata title="タイトル": ページのタイトルを設定
    # --toc: 目次の作成
    args = [
        '--standalone',
        #'--self-contained', #数式SVG埋め込みと相性が
        #'--katex', #数式はhtml側で
        '--mathjax',
        '--template=./templates/bootstrap_menu2.html',
        '--toc',        
        f'--resource-path={resource_path}',
        f'--metadata=title:{title}',
    ]


    try:
        #if not os.path.exists(output_file):
            pypandoc.convert_file(
                input_file,
                'html',
                format='md',
                extra_args=args,
                outputfile=output_file
            )
            # 変換成功後に画像をbase64埋め込み
            embed_images_as_base64(output_file, resource_path)
            print(f"Success: {output_file} generated.")
    except RuntimeError as e:
        print(f"Error: {e}")


#マルチプロセスによる並列化（推奨）
import glob
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
import functools

# 元の変換関数（引数を受け取れるように）
def process_single_file(md_file):
    # パスの定義
    input_file = str(md_file)
    output_file = md_file.with_suffix(".html")
    resource_path = md_file.parent

    # ここで元の関数を呼び出す
    # 子プロセス内であらゆる例外を捕捉し、結果を文字列で返す。
    # こうしないと1件の失敗で executor.map が例外を送出し、全変換が中断される。
    try:
        convert_md_to_html(input_file, output_file, resource_path)
        return f"Converted: {md_file}"
    except Exception as e:
        return f"Error processing {md_file}: {e}"

def main():
    base_path = Path(".")
    # 1. 先にファイルリストを作成する
    md_files = list(base_path.rglob("*.md"))
    
    print(f"開始: {len(md_files)} ファイルの変換...")

    # 2. ProcessPoolExecutorを使って並列実行
    # max_workersを省略するとCPUのコア数に合わせて自動設定されます ProcessPoolExecutor(max_workers=4)
    with ProcessPoolExecutor() as executor:
        # map関数で各ファイルに対してprocess_single_fileを適用
        results = list(executor.map(process_single_file, md_files))

    # 各ファイルの結果を表示し、失敗を可視化する
    for res in results:
        print(res)
    errors = [r for r in results if r.startswith("Error")]
    print(f"すべての変換が完了しました。（成功 {len(results) - len(errors)} / 失敗 {len(errors)}）")





if __name__ == "__main__":
    
    #convert_md_to_html('TableOfContents.md', 'TableOfContents.html', ".")

    """
    from pathlib import Path
    import glob
    base_path = Path(".")        
    # 指定ディレクトリ以下の全.mdファイルを再帰的に取得（rglobを使用）
    for md_file in base_path.rglob("*.md"):
        
        input_file = str(md_file)
        output_file = md_file.with_suffix(".html")
        resource_path = md_file.parent
        
        convert_md_to_html(input_file, output_file, resource_path)
    """
    
    main()
    