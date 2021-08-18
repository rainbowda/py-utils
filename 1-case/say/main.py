import pyttsx3

# 初始化来获取语音引擎
engine = pyttsx3.init()

# 去掉文本中的换行符
text ='偷偷告诉你哦'
# 朗读文本
engine.say(text)
engine.runAndWait()

# 保存音频到本地，格式为mp3
##engine.save_to_file(text, 'test.mp3')
##engine.runAndWait()

# 调整人声类型
##voices = engine.getProperty('voices')
##engine.setProperty('voice', voices[0].id)

# 调整语速,范围一般在0~500之间
##rate = engine.getProperty('rate')
##engine.setProperty('rate', 200)

# 调整声量，范围在0~1之间
##volume = engine.getProperty('volume')
##engine.setProperty('volume',0.8)