from django.shortcuts import render
import json
from django.http.response import HttpResponse

#dict type의 데이터
lan = {
    'id' : 111,
    'name':'파이썬',
    'history':[
        {'date':'2010-07-20', 'exam':'basic'},
        {'date':'2010-10-20', 'exam':'django'},
        ]
    }
# Create your views here.
def IndexFunc(request):
    '''
    print(type(lan)) # <class 'dict'>
    
    # json Encoding : dict(list, tuple...) => str(문자열)로 바꿈
    jsonString = json.dumps(lan)
    print(type(jsonString)) # <class 'str'>
    
    # 들여쓰기가 있는 형태로 변환
    jsonString = json.dumps(lan, indent = 4)
    print(jsonString) 
    print('~~' * 10)
    
    # json Decoding : str(문자열-key: value 형태여야 함.) => dict로 변환
    dictData = json.loads(jsonString)
    print(dictData)
    print(type(dictData))
    print(dictData['name']) # python의 dict 클래스 관련 명령어를 사용할 수 있다.
    
    for h in dictData['history']:
        print(h['date'], h['exam'])
        
        '''
    
    return render(request, 'abc.html')

def Func1(request):
    msg = request.GET['msg']
    print(msg)
    msg = msg + '아작스'
    context = {'key':msg}
    return HttpResponse(json.dumps(context), content_type="application/json")
    
def Func2(request):
    datas= [
        {'irum':'홍길동', 'nai':22},
        {'irum':'고길동', 'nai':32},
        {'irum':'신길동', 'nai':27},
        ]   
    
    return HttpResponse(json.dumps(datas), content_type="application/json") 