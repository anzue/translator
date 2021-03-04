import language_tool_python as langtool

class Checker:
    def __init__(self):
        self._tool_en = langtool.LanguageTool('en-US')
        self._tool_de = langtool.LanguageTool('de')

    def correct(self, sent, lang='en'):
        res = ''
        if lang == 'en':
            res = self._tool_en.correct(sent)
        else:
            res = self._tool_en.correct(sent)

        if res:
            return res
        else:
            return sent

    def check(self, sent, lang='en'):
        matches = []
        if lang == 'en':
            matches = self._tool_en.check(sent)
        else:
            matches = self._tool_de.check(sent)
        return matches


if __name__ == '__main__':
    checker = Checker()
    res = checker.correct('I m feeel sickk', 'en')
    print(res)
