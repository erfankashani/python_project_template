from python_project_template.calculator.calculator import Calculator
import configs.app_config as params
from utils.log import configure_logger
from logging import getLogger

# read app configs in the application
app_env = params.APP_ENV

# logger setup
logger = getLogger()
configure_logger(logger=logger)


logger.info(f"The application running in {app_env} mode...")

calc = Calculator()
result = calc.add(a=1, b=1, c=10 )
print(result)