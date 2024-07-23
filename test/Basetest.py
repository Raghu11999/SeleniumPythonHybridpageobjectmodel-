from datetime import datetime

import pytest


@pytest.mark.usefixtures("setup_and_teardown")

class Basetest:
    def generate_email_with_time_stamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "Raghu" + time_stamp + "@gmail.com"
