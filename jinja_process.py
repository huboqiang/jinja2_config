import sys
from jinja2 import Template
import yaml


def _load_color_config(file_config, sep):
    # 读取模板文件内容
    with open(file_config, 'r') as f:
        template_string = f.read()

    template = Template(template_string)
    data_ = yaml.load(template_string.split("\nproject:")[0], Loader=yaml.FullLoader)
    filled_template = template.render(colors=data_[sep])
    return filled_template

def _convert_jh(template):
    data = yaml.load(template, Loader=yaml.FullLoader)
    key = "project"
    for project in data[key]:
        for dataset in data[key][project]:
            dict_new = {
                "default": {"project_name": project, "dataset": dataset},
                "colors": data[key][project][dataset]
            }
            print(yaml.dump(dict_new, default_flow_style=False, sort_keys=False))



sep = "colors"
if len(sys.argv) > 2:
    sep = sys.argv[2]

_convert_jh(_load_color_config(sys.argv[1], sep))
