from jinja2 import Environment, FileSystemLoader
import os

# Configurar Jinja2
env = Environment(loader=FileSystemLoader('templates'))

# Renderizar index.html
template = env.get_template('index.html')
output = template.render()

# Salvar o arquivo renderizado
output_dir = 'dist'
os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(output)

print(f"✓ index.html renderizado em {output_dir}/")
