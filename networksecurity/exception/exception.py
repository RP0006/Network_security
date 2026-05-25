import sys
from networksecurity.logging import logger
class NetworkSecurityException(Exception):
    def __init__(self, error_message,error_details):
        self.error_message=error_message
        _,_,exe_tb=error_details.exc_info()
        
        self.lineno=exe_tb.tb_lineno
        self.filename=exe_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occured in python script namr[{0}] line number [{1}] error message [{2}]".format(
            self.filename,self.lineno,str(self.error_message)
        )
if __name__=="__main__":
    try:
        a=1/0
        logger.logging.info("Enter the try block")
        a=1/0
        print("Tis will not be printed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
        
        