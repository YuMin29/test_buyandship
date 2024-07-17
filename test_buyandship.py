from buyandship import BuyAndShip
import pytest

TW_URL = "https://www.buyandship.com.tw/"


@pytest.mark.parametrize(
    "test_region, target_region",
    [
        ("香港 - 正體中文", "香港 - 繁體中文"),
        ("香港 - English", "Hong Kong - English"),
        ("澳門 - 正體中文", "澳門 - 繁體中文"),
        ("台灣 - 正體中文", "台灣 - 正體中文"),
        ("日本 - 日本語", "日本 - 日本語"),
        ("新加坡 - English", "Singapore - English"),
        ("馬來西亞 - English", "Malaysia - English"),
        ("印度 - English", "India - English"),
        ("阿聯酋 - English", "UAE - English"),
        ("澳洲 - English", "Australia - English"),
        ("菲律賓 - English", "Philippines - English"),
        ("英國 - English", "United Kingdom - English"),
        ("越南 - Tiếng Việt", "Vietnam - tiếng Việt"),
    ],
)
def test_switch_region_from_tw(test_region, target_region):
    buyAndShip = BuyAndShip(tw_url)
    try:
        buyAndShip.click_region_element()
        new_region = buyAndShip.switch_region(test_region)
        assert new_region.text in target_region
        buyAndShip.quit_chrome()
    except Exception as e:
        buyAndShip.quit_chrome()
        pytest.fail(f"Test failed due to exception: {repr(e)}")
