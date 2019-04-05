import requests
import pandas as pd

baseurl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/'
headers = {'token' : '<token>'}



optparam_list_ds = ['datatypeid', 'locationid', 'stationid', 'startdate', 'enddate', 'sortfield', 'sortorder', 'limit', 'offset']
optparam_list_dc = ['datasetid', 'locationid', 'stationid', 'startdate', 'enddate', 'sortfield', 'sortorder', 'limit', 'offset']
optparam_list_dt = ['datasetid', 'locationid', 'stationid', 'datacategoryid', 'startdate', 'enddate', 'sortfield', 'sortorder', 'limit', 'offset']
optparam_list_lc = ['datasetid', 'startdate', 'enddate', 'sortfield', 'sortorder', 'limit', 'offset']
optparam_list_l = ['datasetid', 'locationcategoryid', 'datacategoryid', 'startdate', 'enddate', 'sortfield', 'sortorder', 'limit', 'offset']
optparam_list_s = ['datasetid', 'locationid', 'datacategoryid', 'datatypeid', 'extent', 'startdate', 'enddate', 'sortfield', 'sortorder', 'limit', 'offset']
optparam_list_d = ['datasetid', 'datatypeid', 'locationid', 'stationid', 'startdate', 'enddate', 'units', 'sortfield', 'sortorder', 'limit', 'offset', 'includemetadata']
otherparam_list = ['limit', 'offset']

def optparam(x):
    param = input('enter optional ' + x + ' separated by comma or press return key: ')
    if len(param) < 1:
        return None
    else: 
        param = param.split(',')
        joiner = '&' + x + '='
        param = x +'=' + joiner.join(param)
        parameterscode.append(param)
    
def getdata(url):
    print(url)
    response = requests.get(url, headers = headers)
    df = pd.DataFrame.from_dict(response.json()['results'])
    df.to_csv('output.txt')

def getinfo(url):
    response = requests.get(url, headers = headers)
    df = pd.DataFrame.from_dict(response.json(), orient='index')
    df.to_csv('output.txt')


endpoint = input('select endpoint: datasets, datacategories, datatypes, locationcategories, locations, stations, data: ')

if endpoint == 'datasets':
    fetchallds = input('fetch all datasets? ')
    if fetchallds == 'yes':
        parameterscode = []
        for parameter in otherparam_list:
            optparam(parameter)
        pcode = '&'.join(parameterscode)
        url = baseurl + endpoint + '?' + pcode
        getdata(url)
    elif fetchallds == 'no':
        dsinfo = input('fetch info on specific dataset? ')
        if dsinfo == 'yes':
            dsinfoid = input('enter datasetid: ')
            url = baseurl + endpoint + '/' + dsinfoid
            getinfo(url)
        elif dsinfo == 'no':
            parameterscode = []
            for parameter in optparam_list_ds:
                optparam(parameter)
            pcode = '&'.join(parameterscode)
            url = baseurl + endpoint + '?' + pcode
            getdata(url)
            
elif endpoint == 'datacategories':     
    fetchalldc = input('fetch all datacategories? ')
    if fetchalldc == 'yes':
        parameterscode = []
        for parameter in otherparam_list:
            optparam(parameter)
        pcode = '&'.join(parameterscode)
        url = baseurl + endpoint + '?' + pcode
        getdata(url)
    elif fetchalldc == 'no':
        dcinfo = input('fetch info on specific datacategory? ')
        if dcinfo == 'yes':
            dcinfoid = input('enter datacategoryid: ')
            url = baseurl + endpoint + '/' + dcinfoid
            getinfo(url)
        elif dcinfo == 'no':
            parameterscode = []
            for parameter in optparam_list_dc:
                optparam(parameter)
            pcode = '&'.join(parameterscode)
            url = baseurl + endpoint + '?' + pcode
            getdata(url)


elif endpoint == 'datatypes':  
    fetchalldt = input('fetch all datatypes? ')
    if fetchalldt == 'yes':
        parameterscode = []
        for parameter in otherparam_list:
            optparam(parameter)
        pcode = '&'.join(parameterscode)
        url = baseurl + endpoint + '?' + pcode
        getdata(url)
    elif fetchalldt == 'no':
        dtinfo = input('fetch info on specific datatype? ')
        if dtinfo == 'yes':
            dtinfoid = input('enter datatypeid: ')
            url = baseurl + endpoint + '/' + dtinfoid
            getinfo(url)
        elif dtinfo == 'no':
            parameterscode = []
            for parameter in optparam_list_dt:
                optparam(parameter)
            pcode = '&'.join(parameterscode)
            url = baseurl + endpoint + '?' + pcode
            getdata(url)


elif endpoint == 'locationcategories':
    fetchalllc = input('fetch all locationcategories? ')
    if fetchalllc == 'yes':
        parameterscode = []
        for parameter in otherparam_list:
            optparam(parameter)
        pcode = '&'.join(parameterscode)
        url = baseurl + endpoint + '?' + pcode
        getdata(url)
    elif fetchalllc == 'no':
        lcinfo = input('fetch info on specific locationcategory? ')
        if lcinfo == 'yes':
            lcinfoid = input('enter locationcategoryid: ')
            url = baseurl + endpoint + '/' + lcinfoid
            getinfo(url)
        elif lcinfo == 'no':
            parameterscode = []
            for parameter in optparam_list_lc:
                optparam(parameter)
            pcode = '&'.join(parameterscode)
            url = baseurl + endpoint + '?' + pcode
            getdata(url)


elif endpoint == 'locations':
    fetchalll = input('fetch all locations? ')
    if fetchalll == 'yes':
        parameterscode = []
        for parameter in otherparam_list:
            optparam(parameter)
        pcode = '&'.join(parameterscode)
        url = baseurl + endpoint + '?' + pcode
        getdata(url)
    elif fetchalll == 'no':
        linfo = input('fetch info on specific location? ')
        if linfo == 'yes':
            dsinfoid = input('enter locationid: ')
            url = baseurl + endpoint + '/' + dsinfoid
            getinfo(url)
        elif linfo == 'no':
            parameterscode = []
            for parameter in optparam_list_l:
                optparam(parameter)
            pcode = '&'.join(parameterscode)
            url = baseurl + endpoint + '?' + pcode
            getdata(url)


elif endpoint == 'stations':
    fetchalls = input('fetch all stations? ')
    if fetchalls == 'yes':
        parameterscode = []
        for parameter in otherparam_list:
            optparam(parameter)
        pcode = '&'.join(parameterscode)
        url = baseurl + endpoint + '?' + pcode
        getdata(url)
    elif fetchalls == 'no':
        sinfo = input('fetch info on specific station? ')
        if sinfo == 'yes':
            sinfoid = input('enter stationid: ')
            url = baseurl + endpoint + '/' + sinfoid
            getinfo(url)
        elif sinfo == 'no':
            parameterscode = []
            for parameter in optparam_list_s:
                optparam(parameter)
            pcode = '&'.join(parameterscode)
            url = baseurl + endpoint + '?' + pcode
            getdata(url)



elif endpoint == 'data':
    parameterscode = []
    for parameter in optparam_list_d:
        optparam(parameter)
    pcode = '&'.join(parameterscode)
    url = baseurl + endpoint + '?' + pcode
    getdata(url)
