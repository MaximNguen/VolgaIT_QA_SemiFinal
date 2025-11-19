from solutions import *

class TestData:
    DataForRequiredField = [
        ("Max", "Nguyen", "88005553535", "MaxLikePizza", "main@example.com", "12345678"),
        ("Pasha", "Ivanov", "901230912391", "PashaCoolGuy", "balalalal@gmail.com", "929929292"),
        ("Ivan", "Pushkin", "12123432423", "PushkinBestPoet", "tutuutu@maily.com", "saldsakdasd")
    ]

    EXPECTED_URL = 'https://way2automation.com/way2auto_jquery/registration.php#load_box'

    DataForAllField = [
        ("Max", "Nguyen", 1, "88005553535", "MaxLikePizza", "main@example.com", "staticFiles/photo1.jpg", f"{first_task()}, {second_task()}, {third_task()}", "12345678"),
        ("Pasha", "Ivanov", 2, "14324123434", "PashaCoolGuy", "main@example.com", "staticFiles/photo1.jpg", f"{first_task()}, {second_task()}, {third_task()}", "121231212"),
        ("Ivan", "Pushkin", 3, "23452345525", "PushkinBestPoet", "main@example.com", "staticFiles/photo1.jpg", f"{first_task()}, {second_task()}, {third_task()}", "12323121")
    ]