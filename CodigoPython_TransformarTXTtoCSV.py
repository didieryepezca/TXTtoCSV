import csv
from itertools import islice
import pandas as pd

with open('D:\\SALP0705.TXT', 'r') as in_file:
       
    reader = csv.reader((line.replace('\0','') for line in in_file), delimiter=" ")   
    data = []
    while True:        
        
        lines = list(in_file)       
        for line in lines[1:10]:   ## remover el rango para tener toda la data        
         
            
            data.append([line[:18], line[19:26], line[27:28], line[28:53], line[54:55], line[55:65], line[65:115], line[115:120]
                        , line[120:122], line[122:124], line[124:125], line[125:129], line[129:148], line[148:163], line[163:173]
                        , line[173:177], line[177:196], line[196:197], line[197:200], line[200:203], line[203:206], line[206:209]
                        , line[209:212], line[212:215], line[215:218], line[218:221], line[221:224], line[224:227], line[227:230]
                        , line[230:233], line[233:244], line[244:248], line[248:252], line[252:256], line[256:260], line[260:264]
                        , line[264:268], line[268:283], line[283:293], line[293:294], line[293:294], line[294:299], line[299:306]
                        , line[306:313], line[313:328], line[328:329], line[329:330], line[330:340], line[340:350], line[350:351]
                        , line[351:353], line[353:354], line[354:357], line[357:360], line[360:361], line[361:364], line[364:378]
                        , line[378:] ])
           
            ##print(','.join((line[:18], line[19:26], line[27:28], line[28:53], line[54:55], line[55:65], line[65:115])))            
            ##print(data)
        if not lines:
            break
            
            
    dfsalp = pd.DataFrame(data, columns=["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14"
                                    , "C15", "C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23", "C24", "C25", "C26", "C27"
                                    , "C28", "C29", "C30", "C31", "C32", "C33", "C34", "C35", "C36", "C37", "C38", "C39", "C40"
                                    , "C41", "C42", "C43", "C44", "C45", "C46", "C47", "C48", "C49", "C50", "C51", "C52", "C53"
                                    , "C54", "C55", "C56", "C57", "C58"])       
    print(dfsalp)
    
    
    dfsalp.to_csv('D:\\SALP2.csv', index=False)