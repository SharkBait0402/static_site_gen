from blocks import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path}')

    with open(from_path, encoding='utf-8') as f:
        from_data = f.read()
    # print(from_data)

    with open(template_path, encoding='utf-8') as f:
        template_data = f.read()

    html_node = markdown_to_html_node(from_data)   
    # print(html_node)
    content = html_node.to_html()

    title = extract_title(from_data)

    full_html = template_data.replace("{{ Title }}", title)
    full_html = full_html.replace("{{ Content }}", content)

    dirpath = os.path.dirname(dest_path)
    os.makedirs(dirpath, exist_ok=True)
    
    # print(full_html)

    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(full_html)
