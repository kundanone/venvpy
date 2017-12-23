from Test.envset.test_chrome import EnvSetup


class x(EnvSetup):
    def test_a(self):
        self.driver.get("https://www.facebook.com/")
