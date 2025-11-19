class ExpectedTexts:
    """ Класс для хранения ожидаемых результатов"""

    REQUIRED_FIELD = 'This field is required.'
    COMMENT_ABOUT_BOX = 'Ожидалось, что ячейка потеряет статус "Выбрана", после подтверждения формы, но ячейка осталась выбранной'

    @staticmethod
    def expected_text(element, text):
        return element.text == text

    @staticmethod
    def boxState(element):
        return element.get_attribute("checked") is None