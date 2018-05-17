import numpy as np 
f = open('CK34011.txt', 'r') 
k = ''
inf = f.read().split('\n')[1]
product = inf.split()[1:2]
productid = str(k.join(product))
print(inf)
print(productid)
lot = inf.split()[3:4]
lotidori = str(k.join(lot))
lotid = lotidori[1:6]
print(lotid)
f.close()
p = open('CK34011.txt', 'r')
time = p.read().split('\n')[2]
dateori = time.split()[0:1]
dates = str(k.join(dateori))
date = '20'+str(dates[6:8]) +'-'+ str(dates[0:2]) +'-'+str(dates[3:5])
print(date)
p.close()
fp = open('CK34011.txt', 'r') 
cnt = 0
for line in fp:
    cnt += 1
count = 0
cnt += -1
fp.close()
fpf = open('CK34011.txt', 'r')
bob_in_trash=fpf.readlines()
for line in bob_in_trash:
    if "******** EOW ********" in line:
        count += 1
rowperpiece = (cnt - 3)/count
rpp = round(rowperpiece)
rpp += -3
print(cnt)
print(count)
print(rowperpiece)
print(rpp)
#path = 'C:/Users/SSL/AppData/Local/Programs/Python/Python36/'
file = open(str(lotid)+'SPEC'+'.xml', 'w')
specbegin = str('<?xml version="1.0" ?>'  + '\n' + '<TANGO_LIMITFILE_FORMAT>'  + '\n' + '<HEADER>'  + '\n' + '<PRODUCT_ID>' + str(productid) + '</PRODUCT_ID>'  + '\n' + '<LIMITFILE_NAME>' + str(productid)+'-SPEC'+ '</LIMITFILE_NAME>' + '\n' + '<AUTHOR></AUTHOR>' + '\n' + '</HEADER>' + '\n' + '<LIMITS>' + '\n')
specend = str('</LIMITS>'+'\n'+'</TANGO_LIMITFILE_FORMAT>')
file.write(specbegin)
for ks in range(1,rpp):
    bs = round(rpp)
    ds = bs+7+ks
    fpfpf = open('CK34011.txt', 'r')
    for line in fpfpf:
        hs = ''
        rows = fpfpf.read().split('\n')[ds]
        column1ori = rows.split()[0:1]
        column1 = str(hs.join(column1ori))
        column8ori = rows.split()[8:9]
        column8 = str(hs.join(column8ori))
        column8num = np.float(column8)
        column9ori = rows.split()[9:10]
        column9 = str(hs.join(column9ori))
        column9num = np.float(column9)
        ave = (column8num + column9num)/2
        ave = str(round(ave, 3))
        ss = ''
        values = '<TEST>'+str(ss.join(column1))+'||'+str(ave)+'|'+str(ss.join(column8))+'|'+str(ss.join(column9))+'</TEST>'+'\n'
        file.write(values)
    fpfpf.close()
file.write(specend)
for n in range(0,count):
    textend = str('</DIEDATA>' + '\n' + '</TANGO_PCM_FORMAT>')
    file = open(str(lotid)+'-'+str(n+1)+'.xml', 'w')
    text = str('<?xml version="1.0"?>' + '\n' + '<TANGO_PCM_FORMAT>' + '\n' + '<HEADER>'  + '\n' + '<VERSION>1.4</VERSION>'  + '\n' + '<LOT_ID>'+str(lotid)+'</LOT_ID>'  + '\n' + '<OP_NAME>PCM1</OP_NAME>'  + '\n' + '<WAF_NO>'+str(n+1)+'</WAF_NO>'  + '\n' + '<WAFER_ID>'+str(lotid)+'-'+str(n+1)+'</WAFER_ID>'  + '\n' + '<PRODUCT_ID>'+str(productid)+'</PRODUCT_ID>'  + '\n' + '<PART_ID>'+str(productid)+'</PART_ID>'  + '\n' + '<PROD_TYPE>LOGIC</PROD_TYPE>'  + '\n' + '<P_CODE></P_CODE>'  + '\n' + '<EQP_ID></EQP_ID>'  + '\n' + '<EQP_NAME></EQP_NAME>'  + '\n' + '<SUBSYS_ID></SUBSYS_ID>'  + '\n' + '<OPERATOR_ID></OPERATOR_ID>'  + '\n' + '<TEST_PG></TEST_PG>'  + '\n' + '<ST_TIME>'+str(date)+'</ST_TIME>'  + '\n' + '<END_TIME>'+str(date)+'</END_TIME>'  + '\n' + '<PROB_CARD_ID></PROB_CARD_ID>' + '\n' + '<LOAD_BOARD_ID></LOAD_BOARD_ID>' + '\n' + '<TEMPERATURE></TEMPERATURE>' + '\n' + '<PCM_DEF_NAME>'+str(productid)+'.PCM1</PCM_DEF_NAME>' + '\n' + '<VENDOR_ID>SOLOMON</VENDOR_ID>' + '\n' + '<VENDORLOT_ID>'+str(productid)+'</VENDORLOT_ID>' + '\n' + '<NOTCH>D</NOTCH>' + '\n' + '<XYDIR>1</XYDIR>' + '\n' + '<LIMITFILE_NAME>'+str(productid)+'-SPEC'+'</LIMITFILE_NAME>' + '\n' + '<FAB_VENDOR_ID>CSMC</FAB_VENDOR_ID>' + '\n' + '<FORCE_UPDATE>N</FORCE_UPDATE>' + '\n' + '</HEADER>' + '\n' + '<DIEDATA>' + '\n')
    file.write(text)
    for l in range(2,7):
        q = 0
        r = 0
        if l == 2:
           q = 5
           r = 5
        elif l == 3:
            q = 3
            r = 5
        elif l == 4:
            q = 5
            r = 7
        elif l == 5:
            q = 7
            r = 5
        elif l == 6:
            q = 5
            r = 3
        sitebegin = str('<SITE NO="'+str(l-1)+'" X="'+str(q)+'" Y="'+str(r)+'">' + '\n')
        siteend = str('</SITE>' + '\n')
        file.write(sitebegin)
        for k in range(1,rpp):
            a = n
            b = round(a*rpp)
            c = 3*n
            d = b+4+k+c
            fpfp = open('CK34011.txt', 'r')
            for line in fpfp:
                h = ''
                row = fpfp.read().split('\n')[d]
                column1ori = row.split()[0:1]
                column1 = str(h.join(column1ori))
                column3ori = row.split()[l:(l+1)]
                column3 = str(h.join(column3ori))
                s = ''
                value = str(s.join(column1))+'|'+str(s.join(column3))+'\n'
            file.write(value)
        file.write(siteend)
    file.write(textend)