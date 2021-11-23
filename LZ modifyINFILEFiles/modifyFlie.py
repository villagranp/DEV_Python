import os


INPUTFOLDER = r'\\172.16.23.204\nowapp\jbossnowtest\addonfel\Pruebas\NOW'

files = os.listdir(INPUTFOLDER)
for item in files:
    filecontent = ''
    with open(INPUTFOLDER+'\\'+item,'r') as openfile:
        for line in openfile:
            lineSplited = line.split('|')
            if lineSplited[0] == 'DR' and lineSplited[1] == '6':
                lineSplited[-1] = '\"San Pedro\"\n'
                line = '|'.join(map(str, lineSplited))
                
            if lineSplited[0] == 'DR' and lineSplited[1] == '7':
                lineSplited[-1] = '\"San Pedro\"\n'
                line = '|'.join(map(str, lineSplited))
            
            if lineSplited[0] == 'IT' and lineSplited[-4] == '1':
                lineSplited[-4] = '2'
                line = '|'.join(map(str, lineSplited))
            filecontent += line
    openfile.close()
    
    witerfile = open(INPUTFOLDER+'\\'+item,'w') 
    witerfile.write(filecontent)
    witerfile.close()
    
