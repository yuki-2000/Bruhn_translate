import pypandoc

def convert_md_to_html(input_file, output_file, resource_path):
   


    # Pandocのオプション設定
    # --standalone: ヘッダーやCSSを含む完全なHTMLを作成
    # -self-contained: 画像などをHTML内に埋め込む (オプション)
    # --katex: 数式の描写。mathjaxはうまくいかず
    # --metadata title="タイトル": ページのタイトルを設定
    # --toc: 目次の作成
    args = [
        '--standalone',
        '--self-contained',
        '--katex',
        '--template=./templates/bootstrap_menu.html',
        '--toc',
        f'--resource-path={resource_path}'    
    ]




    try:
        import os
        if not os.path.exists(output_file):
        
            # 変換実行
            output = pypandoc.convert_file(
                input_file, 
                'html', 
                format='md', 
                extra_args=args, 
                outputfile=output_file
            )
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
    convert_md_to_html(input_file, output_file, resource_path)
    return f"Converted: {md_file}"

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

    print("すべての変換が完了しました。")





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
    