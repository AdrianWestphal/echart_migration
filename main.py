import re

mapping_dic = {
    r"(?<!\w)data\.": "context.panel.data.",  # Match 'data.' when not preceded by a word character
    "theme.": "context.grafana.theme.",
    "echartsInstance.": "context.panel.chart.",
    "echarts.": "context.echarts.",
    "replaceVariables": "context.grafana.replaceVariables",
    "eventBus": "context.grafana.eventBus",
    "locationService.": "context.grafana.locationService.",
    "notifySuccess": "context.grafana.notifySuccess",
    "notifyError": "context.grafana.notifyError",
    ".buffer": "", 
}

def replace_all(file_path, dic):
    with open(file_path, 'r') as file:
        text = file.read()
        
    for i, j in dic.items():
        # Use re.sub for regex replacements
        text = re.sub(i, j, text)
        
    with open("updated_echart.js", 'w') as updated_file:
        updated_file.write(text)

replace_all("echart.js", mapping_dic)
