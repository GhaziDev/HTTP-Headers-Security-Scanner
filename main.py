import httpx
import logging


logging.basicConfig(filename='errors.log',level=logging.error)
logger = logging.getLogger(__name__)

logger = logging.set
def write_inspect_file(info:str,file:str='inspect.txt'):
      with open(file,'w') as file_ :
            file_.write(info)
            
      

SECURITY_HEADERS:list[(str,str,int)] =[
    ("strict-transport-security",'high',10),
    ("content-security-policy",'high',10),
    ("x-frame-options","medium",5),
    ("x-content-type-options","medium",5),
    ("referrer-policy","low",2),
    ("permissions-policy","low",2),
    ("content-type","low",2),
    ("x-robots-tag","low",2),
]

HEADERS_VALUES = list(map(lambda x:x[2],SECURITY_HEADERS))






INSPECTOR = ["Severity \t\t Details \t\t \n ------------------------------- \n"]
def construct_url(url:str,method='GET'):
      if not url.startswith('http') or  not url.startswith('https'):
            
            raise Exception ('A scheme need to be specified as either http or https')
      
      if url.startswith('http') and not url.startswith('https') :
            INSPECTOR.append('Severity \t\t Details \t\t \n------------------------------- \n High \t\t Non-secure protocol (http)\n\n')
            
            #write_inspect_file(' '.join(INSPECTOR))
            return
                 
      if not len(url):
            logger.error('[construct_url() function call] error start here at line 46')
            logger.error('Invalid Url Format')
            logger.error('[construct_url() function call] error end here.')
            raise Exception("Insert an actual URL")
      print(url)           
      return url

def check_present_headers(headers):
      
        headers = list(map(lambda x: x.lower(),headers.keys()))
        
        for index,header in enumerate(SECURITY_HEADERS):
            if header[0] not in headers:
                  INSPECTOR.append(f"{header[1]} \t\t Missing header: {header[0]}\n  ")
                  SECURITY_HEADERS.pop(index)

                  
                  


def calculate_grade():
    

      total = sum(HEADERS_VALUES)
      
      for el in SECURITY_HEADERS:
            total-=el[2]
      

      grade_check = (sum(HEADERS_VALUES) - total) * 100 / sum(HEADERS_VALUES)
      
      if grade_check<=100 and grade_check>=85:
            print(f'Security Grade : A, Score : {grade_check}%')
            
      if grade_check<=84 and grade_check>=65:
            print(f'Security Grade : B, Score : {grade_check}%')
            
      if grade_check<=64 and grade_check>=50:
            print(f'Security Grade : C, Score : {grade_check}%')
            
      if grade_check<=49 and grade_check>=0:
            print(f'Security Grade : F, Score : {grade_check}%. FAILED HEADERS .SECURITY CHECKS.')
      
                            
def make_api_call():
      url = input('Insert URL with the scheme (http:// or https://) : ')
      try:
            res = httpx.get(construct_url(url))
           
            check_present_headers(dict(res.headers))
            calculate_grade()  
           
            info = ' '.join(INSPECTOR)
            print(info)
            write_inspect_file(info)
            print('Check full log in inspect.txt file')
      except Exception as e:
            logger.error("[make_api_call() function call] error start here at line 101.")
            logger.error(e)
            logger.error('[make_api_call() function call] error end here.')
            raise e



if "__main__"==__name__:
      make_api_call()





                 
                 
                 
                

    
    