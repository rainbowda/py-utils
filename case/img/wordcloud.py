
def wordCloudImage(wordlist,width,height,bgcolor,savepath):
    # 可以打开你喜欢的词云展现背景图
    # cloud_mask = np.array(Image.open('nezha.png'))
    # 定义词云的一些属性
    wc = WordCloud(
        width=width,  # 图幅宽度 900
        height=height,  # 图幅高度 3000
        background_color=bgcolor,  # 背景图分割颜色为白色 "black"
        # mask=cloud_mask,  # 背景图样
        max_words=300,  # 显示最大词数
        font_path='./fonts/simhei.ttf',  # 显示中文
        collocations=False,
        # min_font_size=5,  # 最小尺寸
        # max_font_size=100,  # 最大尺寸
    )

    # wordfile是分词后的词汇列表
    x = wc.generate(wordlist)
    # 生成词云图片
    image = x.to_image()
    # 展示词云图片
    image.show()
    # savepath是图片保存地址，保存词云图片
    wc.to_file(savepath)