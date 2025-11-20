import traceback
from libs.AutoToolsLib import AutoToolsLib


class AutoTools(AutoToolsLib):
    def __init__(self):
        pass

    def FormData(self):
        # 此处编写用户填写表单
        FormData = [
            self.FormControl.PushButton('GeoModelJson', '模型文件', 'JsonValue', '选择geo模型文件'),
            self.FormControl.PushButton('OutputFolder', '输出文件夹', 'FolderPath', '选择输出文件夹')
        ]
        return FormData

    def FormCommit(self, FormData):
        RunLogic = []
        UVList = ['north', 'south', 'west', 'east', 'up', 'down']  # 完整的UV列表
        UVNormalValue = {'uv': [0, 0], 'uv_size': [0, 0]}
        JsonValue = FormData['GeoModelJson']
        ModelName = JsonValue['minecraft:geometry'][0]['description']['identifier']
        if ModelName.startswith('geometry.'):
            ModelName = ModelName[9:]
        ConvertDict = JsonValue.copy()
        OutputFolder = FormData['OutputFolder']
        RemoveDict = {}  # 缺失六面uv信息
        ErrorDict = {}  # 错误的uv信息
        RightDict = {}
        # 遍历骨骼数据
        for m, CubeDict in enumerate(ConvertDict['minecraft:geometry'][0]['bones']):
            if 'cubes' in CubeDict.keys():
                for i, Cube in enumerate(CubeDict['cubes']):
                    UVKeys = Cube['uv']
                    if type(Cube['uv']) != dict:
                        ErrorDict[f'{CubeDict['name']}_{m}_{i}'] = {
                            'parent': CubeDict.get('parent', None),
                            'bones_num': m,
                            'cubes_num': i,
                            'uv': Cube['uv'],
                            'error_type': f'存在非逐面形内容，请看key为uv的字节片段{traceback.format_exc()}'
                        }
                        continue
                    if len(UVKeys) != 6:
                        # 记录缺失的UV信息
                        RemoveDict[f'{CubeDict['name']}_{m}_{i}'] = {
                            'parent': CubeDict.get('parent', None),
                            'bones_num': m,
                            'cubes_num': i,
                            'uv': Cube['uv']
                        }
                        # 补全缺失的UV信息为默认值
                        # 计算当前已有UV数量
                        existing_uv_count = len(Cube['uv'])
                        for j in range(existing_uv_count, 6):
                            try:
                                Cube['uv'][UVList[j]] = UVNormalValue
                            except:
                                ErrorDict[f'{CubeDict['name']}_{m}_{i}'] = {
                                    'parent': CubeDict.get('parent', None),
                                    'bones_num': m,
                                    'cubes_num': i,
                                    'uv': Cube['uv'],
                                    'error_data': j,
                                    'error_type': f'存在错误信息{traceback.format_exc()}'
                                }
                    # else:
                    # RightDict[f'{CubeDict['name']}_{i}'] = True
        # 输出缺失UV信息的文件

        NeedRemoveDict = RemoveDict.copy()
        # 根据缺失数据进行补全
        for AllCubeName, CubeData in NeedRemoveDict.items():
            # 找到缺失的骨骼
            BonesNum = int(AllCubeName.split('_')[-2])
            # 找到缺失的立方体
            CubeName = '_'.join(AllCubeName.split('_')[:-2])
            CubesNum = int(AllCubeName.split('_')[-1])
            # 补全缺失的UV信息
            for UVKey in UVList:
                if type(CubeData['uv']) != dict:
                    break
                if UVKey not in CubeData['uv'].keys():
                    try:
                        if 'missing_uv' not in RemoveDict[AllCubeName].keys():
                            RemoveDict[AllCubeName]['missing_uv'] = []
                        RemoveDict[AllCubeName]['missing_uv'].append(UVKey)
                        ConvertDict['minecraft:geometry'][0]['bones'][BonesNum]['cubes'][CubesNum]['uv'][
                            UVKey] = UVNormalValue
                    except:
                        RemoveDict[
                            f'{CubeName}_{BonesNum}_{CubesNum}_{UVKey}'] = f'补全UV时发生错误{traceback.format_exc()}'
        # RemoveDict.update(RightDict)
        # RunLogic.append(self.Create.CreateJson(OutputFolder + f'/{ModelName}_log.json', RemoveDict))
        # 输出补全后的转换文件
        RunLogic.append(self.Create.CreateJson(OutputFolder + f'/{ModelName}_convert.geo.json', ConvertDict))
        if ErrorDict:
            RunLogic.append(self.Create.CreateJson(OutputFolder + f'/{ModelName}_error.json', ErrorDict))
        return RunLogic
