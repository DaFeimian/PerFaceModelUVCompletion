
class AutoToolsLib:
    """自动化工具补全库，禁止修改"""
    def __init__(self):
        pass

    def FormCommit(self, FormData):
        # type: (dict) -> list
        """
        表单提交
        :param FormData: 提交数据
        :return: 返回自动化运行任务列表
        """
        pass

    class FormControl:
        """表单控件
        其中Key表示表单数据Dict的Key，将会通过FormCommit中的参数FormData回调
        """

        def LineEdit(Key, Name, SubType=None, DefaultValue=''):
            # type: (str, str, str, str) -> dict
            """
            单行文本输入框
            :param Key: 控件Key，用于提交数据
            :param Name: 控件名称，用于显示
            :param SubType: 控件子类型，可选[None(无规则限制), str(合法字符串), int(整数), float(浮点数), s_str(小写合法字符串), item_str(物品/方块Id,合法MC内容)]
            :param DefaultValue: 控件默认值
            :return: 控件数据
            """
            pass

        def PushButton(Key, Name, SubType=None, DefaultValue='选择'):
            # type: (str, str, str, str) -> dict
            """
            功能按钮
            :param Key: 控件Key，用于提交数据
            :param Name: 控件名称，用于显示
            :param SubType: 控件子类型，可选[FolderPath(选择文件夹), FilePath(选择文件), PngPath(选择图片), JsonValue(选择json文件直接返回值), JsonPaths(批量选择Json文件路径), PngPaths(批量选择Json文件路径)] \n 填写xxxPaths，将会自动选择批量*.xxx文件路径，如zipPaths，则选择*.zip文件
            :param DefaultValue: 按钮显示的文字
            :return: 控件数据
            """
            pass

        def ComboBox(Key, Name, SubType=None, DefaultValue=[]):
            # type: (str, str, str, list) -> dict
            """
            下拉选项框
            :param Key: 控件Key，用于提交数据
            :param Name: 控件名称，用于显示
            :param SubType: 控件子类型，只有None
            :param DefaultValue: 选项列表
            :return: 控件数据
            """
            pass

        def TextEdit(Key, Name, SubType=None, DefaultValue=''):
            # type: (str, str, str, str) -> dict
            """
            多行文本输入框
            :param Key: 控件Key，用于提交数据
            :param Name: 控件名称，用于显示
            :param SubType: 控件子类型，固定为None
            :param DefaultValue: 控件默认值
            :return: 控件数据
            """
            pass

    class Create:
        """创建文件或文件夹"""

        def CreateFolder(Path):
            # type: (str) -> dict
            """
            创建文件夹
            :param Path: 文件夹路径，最后一个字符不需要'/'，例如'C:/Administrator/Desktop'
            :return: 任务数据
            """
            pass

        def CreateJson(Path, Content):
            # type: (str, dict) -> dict
            """
            创建json文件
            :param Path: json文件路径，需要携带文件后缀名
            :param Content: json文件内容
            :return: 任务数据
            """
            pass

        def CreatePython(Path, ContentList):
            # type: (str, list) -> dict
            """
            创建python文件
            :param Path: python文件路径，需要携带文件后缀名
            :param ContentList: python文件内容列表(拆分为每行)
            :return: 任务数据
            """
            pass

    class Zip:
        """压缩工具"""

        def UnZip(Path, UnZipPath, URL):
            # type: (str, str, str) -> dict
            """
            解压文件
            :param Path: 压缩包下载至文件路径，需要携带文件后缀名
            :param UnZipPath: 将压缩包解压至指定路径，最后一个字符不需要'/'，例如'C:/Administrator/Desktop'
            :param URL: 压缩包下载地址，只能是软件服务端地址，不支持第三方链接！
            :return: 任务数据
            """
            pass

    class MinecraftOrigin:
        """原生我的世界"""
        def TestListJsonAndAddContent(Path, Content):
            # type: (str, str) -> dict
            """
            给我的世界资源包UI界面清单添加新的UI界面路径
            :param Path: json文件路径，需要携带文件后缀名
            :param Content: UI界面路径，例如'ui/dfm_require.json'
            :return: 任务数据
            """
            pass

        def TerrainTexture(TerrainTexturePath, Key, ValueDict):
            # type: (str, str, dict) -> dict
            """
            我的世界贴图定义json添加
            :param TerrainTexturePath: terrain_texture.json路径，需要携带文件后缀名
            :param Key: 符合我的世界terrain_texture要求的Key，例如'dfm:dafeimian'
            :param ValueDict: 符合我的世界terrain_texture要求的ValueDict，例如{'textures': 'textures/entity/dafeimian'}
            :return: 任务数据
            """
            pass

        def ItemTexture(ItemTexturePath, Key, ValueDict):
            # type: (str, str, dict) -> dict
            """
            我的世界贴图定义json添加
            :param ItemTexturePath: item_texture.json路径，需要携带文件后缀名
            :param Key: 符合我的世界item_texture要求的Key，例如'dfm:dafeimian'
            :param ValueDict: 符合我的世界item_texture要求的ValueDict，例如{'textures': 'textures/entity/dafeimian'}
            :return: 任务数据
            """
            pass

        def Blocks(BlocksPath, Key, ValueDict):
            # type: (str, str, dict) -> dict
            """
            我的世界方块定义json添加
            :param BlocksPath: 资源包blocks.json路径，需要携带文件后缀名
            :param Key: 符合我的世界blocks要求的Key，例如'dfm:dafeimian'
            :param ValueDict: 符合我的世界blocks要求的ValueDict，例如{'client_entity': {'block_icon': 'dfm:dafeimian_icon', 'destroyed_textures': 'dfm:dafeimian', 'hand_model_use_client_entity': True, 'identifier': 'dfm:dafeimian'}}
            :return: 任务数据
            """
            pass

    class Other:
        """其他特殊工具"""

        def AddLines(Path, ContentList):
            # type: (str, list) -> dict
            """
            给文件添加新的行，通常用于我的世界zh_cn.lang翻译文件
            :param Path: 文件路径，需要携带文件后缀名
            :param ContentList: 新的行列表，每个元素为一行内容
            :return: 任务数据
            """
            pass

        def CopyFile(OriginPath, TargetPath, ReName):
            # type: (str, str, str) -> dict
            """
            复制文件
            :param OriginPath: 源文件路径，需要携带文件后缀名
            :param TargetPath: 目标文件夹路径，最后一个字符需要为'/'，例如'C:/Administrator/Desktop/'
            :param ReName: 粘贴后目标文件重命名
            :return: 任务数据
            """
            pass

        def ResizeImageWidth(ImagePath, TargetPath, Width):
            # type: (str, str, int) -> dict
            """
            复制并调整图片宽度
            :param ImagePath: 源图片路径，需要携带文件后缀名
            :param TargetPath: 目标图片路径，需要携带文件后缀名
            :param Width: 目标图片宽度px
            :return: 任务数据
            """
            pass