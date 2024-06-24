import allure

from demoqa_tests.data import users
from demoqa_tests.pages.registration_page import RegistrationPage

@allure.title("demoqa - test practice form")
@allure.tag("Registration", 'QA.GURU')
@allure.severity(allure.severity_level.NORMAL)
@allure.label("owner", "Alma")
@allure.parent_suite("demoqa")
@allure.suite("Регистрация пользователя")
@allure.sub_suite("Пользователь успешно регистрируется")
def test_registration():
    registration_page = RegistrationPage()
    with allure.step('Открываем форму регистрации'):
        registration_page.open()
    # WHEN
    with allure.step('Регистрируем пользователя'):
        registration_page.register(users.student)

    # THEN
    with allure.step('Проверка данных пользователя'):
        registration_page.assert_user_info(
            'Alma Bekbergenova', 'test@test.ru', 'Male', '1234567890',
            '02 January,1991', 'Maths, Chemistry', 'Sports, Reading, Music', 'orig.jpg',
            'Test Address', 'NCR Delhi'
        )
        # registration_page.close_modal_window()