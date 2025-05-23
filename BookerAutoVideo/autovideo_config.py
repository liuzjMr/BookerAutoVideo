from os import path

DIR = path.abspath(path.dirname(__file__))

config = {
    'name': '',
    'format': 'mp4',
    'font': 'kaiti.ttf',
    'bgm': '',
    'bgImg': '',
    'size': [1920, 1080],
    'fps': 30,
    'sr': 22050,
    'padding': 0,
    'contents': [],
    'header': '', 
    'footer': '',
    'external': '',
    # 爬虫模块配置
    'crawler': {},
    # PaddleSpeech 配置
    'tts': {},
    'resizeMode': 'wrap',
    'subtitleMaxLen': 30,
    'assetDir': None,
    'ttsVoice': 'zh-CN-XiaoyiNeural',
    'ttsVolume': '+0%',
    'ttsRate': '-10%',
    'ttiModel': 'dall-e-3',
    'ttiQuality': 'standard',
    'ttiSize': '1024x1024',
    'ttiRetry': 10,
    'ttsRetry': 10,
    'defaultImg': path.join(DIR, 'asset', 'sound_only.png'),
    'onePic': None,
}