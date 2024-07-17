import base64
import os
import pytest
import pytest_html
from pytest_metadata.plugin import metadata_key


def pytest_html_report_title(report):
    report.title = "BuyAndShip test report"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" and report.failed:
        # Assuming your screenshot is saved correctly at the specified path
        screenshot_path = os.getenv("../", "failed.png")
        with open(screenshot_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        extra.append(pytest_html.extras.png(encoded_string))
        report.extra = extra
