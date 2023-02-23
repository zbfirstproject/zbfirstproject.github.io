class TypeMsg(object):
    def __init__(self, xmlData):
        # 私有对象，禁止外部访问
        self.__dict = dict()
        self.__dict['ToUserName'] = xmlData.find('ToUserName').text
        self.__dict['FromUserName'] = xmlData.find('FromUserName').text
        self.__dict['CreateTime'] = xmlData.find('CreateTime').text
        self.__dict['MsgType'] = xmlData.find('MsgType').text
        self.__dict['MsgId'] = xmlData.find('MsgId').text
        if self.__dict['MsgType'] == 'text':
            self.__dict['Content'] = xmlData.find('Content').text
        elif self.__dict['MsgType'] == 'image':
            self.__dict['PicUrl'] = xmlData.find('PicUrl').text
            self.__dict['MediaId'] = xmlData.find('MediaId').text
        print(self.__dict)
    def send(self):
        result = getattr(self, self.__dict['MsgType'])
        return result

    @property
    def text(self):
        XmlForm = """
                    <xml>
                        <ToUserName><![CDATA[{FromUserName}]]></ToUserName>
                        <FromUserName><![CDATA[{ToUserName}]]></FromUserName>
                        <CreateTime>{CreateTime}</CreateTime>
                        <MsgType><![CDATA[{MsgType}]]></MsgType>
                        <Content><![CDATA[{Content}]]></Content>
                        <MsgId>{MsgId}</MsgId>
                    </xml>
                    """
        return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/xml"},
        "body": XmlForm.format(**self.__dict)
        }

    @property
    def image(self):
        XmlForm = """
                    <xml>
                        <ToUserName><![CDATA[{FromUserName}]]></ToUserName>
                        <FromUserName><![CDATA[{ToUserName}]]></FromUserName>
                        <CreateTime>{CreateTime}</CreateTime>
                        <MsgType><![CDATA[{MsgType}]]></MsgType>
                        <Image>
                            <MediaId><![CDATA[{MediaId}]]></MediaId>
                        </Image>
                    </xml>
                    """
        return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": {"Content-Type": "application/xml"},
        "body": XmlForm.format(**self.__dict)
        }