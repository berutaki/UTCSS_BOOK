import nbformat
from nbformat.notebooknode import NotebookNode
import sys  # sysモジュールをインポート

def trim_outputs(nb_path, max_lines=50):
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    for cell in nb.cells:
        if cell.cell_type == 'code':
            if 'outputs' in cell:
                for output in cell.outputs:
                    if output.output_type == 'stream':
                        lines = output.text.splitlines()
                        if len(lines) > max_lines:
                            trimmed_text = '\n'.join(lines[:max_lines]) + '\n...\n(出力をトリミングしました)'
                            output.text = trimmed_text

    with open(nb_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

if __name__ == "__main__":
    # コマンドライン引数からノートブックのパスを取得
    if len(sys.argv) < 2:
        print("Usage: python trim_outputs.py <path_to_notebook>")
        sys.exit(1)
    notebook_path = sys.argv[1]
    trim_outputs(notebook_path)
