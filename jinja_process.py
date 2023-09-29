import sys
from jinja2 import Template
import yaml

def _load_color_config(file_config):
    # 读取模板文件内容
    with open(file_config, 'r') as f:
        template_string = f.read()

    template = Template(template_string)
    data_ = yaml.load(template_string.split("\nproject:")[0], Loader=yaml.FullLoader)

    filled_template = template.render(colors=data_["colors"])
    return filled_template

print(_load_color_config(sys.argv[1]))
