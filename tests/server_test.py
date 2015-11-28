from unittest import TestCase
import server
from unittest.mock import patch, call, MagicMock
import json
import lib.gpio.RPi.GPIO as GPIO

class TestCoffeeWebservice(TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_root(self):
        request = self.app.get("/")

        self.assertEquals(418, request.status_code)

    @patch('lib.gpio.RPi.GPIO.setup', autospec=True)
    @patch('lib.gpio.RPi.GPIO.input', autospec=True)
    def test_get_on_when_off(self, mocked_gpio_input, mocked_gpio_setup):
        mocked_gpio_input.return_value = False

        request = self.app.get("/on")

        mocked_gpio_setup.assert_has_calls([call(12, GPIO.IN)])

        self.assertEquals(200, request.status_code)
        self.assertEquals(False, json.loads(request.get_data(as_text=True))["state"])

    @patch('lib.gpio.RPi.GPIO.setup', autospec=True)
    @patch('lib.gpio.RPi.GPIO.input', autospec=True)
    def test_get_on_when_on(self, mocked_gpio_input, mocked_gpio_setup):
        mocked_gpio_input.return_value = True

        request = self.app.get("/on")

        mocked_gpio_setup.assert_has_calls([call(12, GPIO.IN)])

        self.assertEquals(200, request.status_code)
        self.assertEquals(True, json.loads(request.get_data(as_text=True))["state"])

    # @patch('lib.gpio.RPi.GPIO')
    # def test_on_when_off(self, mocked_gpio):
    #     request = self.app.post("/on")
    #
    #     self.assertEquals(200, request.status_code)