from ..Script import Script

class DaVinciConvert(Script):
    def __init__(self):
        super().__init__()
    
    def getSettingDataString(self):
        return """{
            "name": "XYZ DaVinci 1.1 converter",
            "key": "DaVinciConvert",
            "metadata": {},
            "version": 2,
            "settings":
            { 
                "ignore_temp_settings":
                {
                    "label": "Ignore temperature settings",
                    "description": "Ignore any nozzle or bed temperatures set in Cura and use the printer\'s default temperatures.",
                    "type": "bool",
                    "default_value": true
                },
                "replace_GO":
                {
                    "label": "Replace G0 with G1",
                    "description": "When enabled, the G0 moves will be replaced with G1.",
                    "type": "bool",
                    "default_value": true
                }
            }
        }"""

    def execute(self, data):
        ignore_temps = self.getSettingValueByKey("ignore_temp_settings")
        replace_GO = self.getSettingValueByKey("replace_GO")

        for line in data[0].split('\n'):
            if ";Filament used: " in line:
                filament = line.replace(";Filament used: ","").replace("m","")
                if filament!='':
                    filament = float(filament)*1000
            if ";TIME:" in line:
                print_time = line.replace(";TIME:","")
            if ";Layer height: " in line:
                layer_height = line.replace(";Layer height: ","")

        for line in data[1].split('\n'):
            if ";LAYER_COUNT:" in line:
                layer_count = line.replace(";LAYER_COUNT:","")

        if replace_GO or ignore_temps:
            for layer_number, layer in enumerate(data):
                if replace_GO:
                    data[layer_number] = layer.replace("G0 ","G1 ") #Replace G0
                if ignore_temps:
                    converted_lines = []
                    for line in data[layer_number].split('\n'):
                        if "M104" not in line and "M109" not in line and "M140" not in line and "M190" not in line:
                            converted_lines += [line]
                    data[layer_number] = '\n'.join(converted_lines)

        data[0] = self.getXYZHeader().format(print_time, filament, layer_height, layer_count)
        data[len(data)-1] += self.getXYZFooter()
        return data

    def getXYZHeader(self):
        return """; filename = composition.3w
; print_time = {0}
; machine = daVinciF11
; total_layers = {3}
; version = 17032409
; total_filament = {1}
; nozzle_diameter = 0.40
; layer_height = {2}
; support_material = 0
; support_material_extruder = 1
; extruder_filament = {1}:0.00
; extruder = 1
; threads = 1
"""
    def getXYZFooter(self):
        return """;XYZ footer
M84     ; disable motors
"""
