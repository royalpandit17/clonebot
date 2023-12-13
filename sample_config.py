#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("6443682508:AAFdQe76jnOWKiZVBX1eDubveCJNDnxzVbg", "")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("25738617", ""))

    # Get from my.telegram.org
    API_HASH = os.environ.get("2a7d66a33fbc472ae31cf9c6c4d6634d", "")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("BQB6bF7BDCQY2IqxeCjOaVHNqwjjdg7jQZiTuw_yyRVO2CgtqH3MimbLU86MZaQhCiWbC2mteP287ECgh5S-FXhN3_Qj_DrYgv3QZ5WqGgXRt75tqLjPYWV-smP73xy4M1R-GDqp1Tr-0dvNd0xxfUzCz4uwx_7iy_ruBrX9XBVhhgH8x7JAedBppmTe_p4rbyepwIdudd46FepZAlLaorPkCUvEb5Nzz36G8gcT4AKFsgSMhGGEc_q4wReusDov8usZSrnjko_M0XWpnJxTkzOAjRMnW_CVBexyTFyNgirQyT1fn9Tk6OwN08xyx8kQx2DtmatQqObCtuFokQ9MXDZxTzQhnQA", "")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
