import logging
from datetime import datetime

reset       = "\033[0m"
red         = "\033[0;31m"
green       = "\033[0;32m"
blue        = "\033[0;34m"
purple      = "\033[0;35m"
cyan        = "\033[0;36m"
yellow      = "\033[1;33m"
magenta     = "\033[1;35m"
white       = "\033[1;37m"
light_green = "\033[1;32m"
light_blue  = "\033[1;34m"

fmt = '%(asctime)s ->| %(message)s'

_urgency_map = {
    'DEBUG'   : 1, 
    'INFO'    : 2, 
    'WARNING' : 3, 
    'ERROR'   : 4, 
    'CRITICAL': 5, 
    }

class FancyFormatter(logging.Formatter): 
  
  def __init__(self, fmt): 
    super().__init__()
    self.fmt = fmt.split('|')
    self.formats = {
        logging.DEBUG   : reset + self.fmt[0] + green  + self.fmt[1] + reset,
        logging.INFO    : reset + self.fmt[0] + blue   + self.fmt[1] + reset,
        logging.WARNING : reset + self.fmt[0] + cyan   + self.fmt[1] + reset,
        logging.ERROR   : reset + self.fmt[0] + yellow + self.fmt[1] + reset,
        logging.CRITICAL: reset + self.fmt[0] + red    + self.fmt[1] + reset,
      }

  def format(self, fmt): 
    log_fmt = self.formats.get(fmt.levelno)
    formatter = logging.Formatter(log_fmt)
    return formatter.format(fmt)

class TheLoggah: 
  loggah = None
  msg = None

  def __init__(self): 
    self.loggah = self.create_loggah()

  def create_loggah(self):
      loggah = logging.Logger('loggah')
      loggah.setLevel(logging.DEBUG)

      # This handles logging to the console!! 
      stream_handler = logging.StreamHandler()
      stream_handler.setLevel(logging.DEBUG)
      stream_formatter = FancyFormatter(fmt)

      # This handles logging to the file!!
      today        = datetime.today()
      file_handler = logging.FileHandler('xformance_{}.log'.format(today.strftime('%Y_%m_%d')))
      file_handler.setLevel(logging.DEBUG)
      file_handler.setFormatter(FancyFormatter(fmt))

      loggah.addHandler(file_handler)
      loggah.addHandler(stream_handler)

      return loggah

  def log(self, msg, urgency): 
    if urgency == _urgency_map['DEBUG']: self.loggah.debug(msg)
    if urgency == _urgency_map['INFO']: self.loggah.info(msg)
    if urgency == _urgency_map['WARNING']: self.loggah.warning(msg)
    if urgency == _urgency_map['ERROR']: self.loggah.error(msg)
    if urgency == _urgency_map['CRITICAL']: self.loggah.critical(msg)
    

    

