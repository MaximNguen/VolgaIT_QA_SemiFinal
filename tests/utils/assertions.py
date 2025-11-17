import allure

class Assertions:
    @staticmethod
    @allure.step("Проверка текста: ожидаемый '{expected}', фактический '{actual}'")
    def assert_text_equal(expected, actual):
        message = f"Ожидалось вывод текста {expected}, но получили {actual}"
        assert expected == actual, message

