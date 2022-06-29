import pandas as pd
import psycopg2
import xlsxwriter
import datetime
from datetime import date
from datetime import datetime
from urllib import response
from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Inicializando el", dt_string)	

conn = None
username= 'jvillagran'
password= 'Liztex+22'
GtEkko = {}
xlsxHeader = ('Centro',
                'Grupo de compras',
                'N° Solicitud',
                'Indicador borrado',
                'Fecha Creación Solicitud',
                'Fecha Liberación Solicitud',
                'Fecha Modificación Solicitud',
                'Fecha de Entrega (Posición)',
                'Liberado por',
                'Clase de pedido',
                'Indicador de borrado',
                'Usuario de Pedido',
                'Apellido de Usuario',
                'N° Pedido Compras completado',
                'Fecha de pedido',
                'Grupo de artículos',
                'Denominación GrpComp',
                'Material',
                'Texto breve',
                'Cantidad de pedido',
                'Valor del Pedido',
                'Moneda del Pedido',
                'Denom.gr-artículos',
                'Status tratamiento doc.',
                'Status tratamiento doc.',
                'Estrategia liberac.',
                'Ind.liberación',
                'Descripción',
                'Fecha Rechazo',
                'Hora Rechazo',
                'Usuario Rechazo',
                'Apellido Rechazo',
                'Fecha Ultima Modificación Pedido',
                'Estado de Liberación',
                'Denominación del estado de liberación',
                'Fecha de Activación de Estrategia',
                'Liberación',
                'Valor del anticipo 1 (moneda local)',
                'Valor anticipo moneda registro 1',
                'Moneda registro 1',
                'Fecha de anticipo 1',
                'Entrega final',
                'Fecha recepción de mercancías',
                'Posición',
                'N° documento de EM',
                'Cantidad entrada',
                'Clase de Movimiento',
                'Ultima Fecha de modificación de Recepció',
                'Fecha aceptación del servicio',
                'N° de aceptación del servicio',
                'Última modificación de recepción de acep',
                'Fecha de Recepción de Factura',
                'N° de documento RE-L',
                'Fecha Pago Programada',
                'Fecha de liberación de ultimo nivel de p',
                'Fecha de Necesidad',
                'N1 Usuario',
                'N2 Usuario',
                'N3 Usuario',
                'N4 Usuario',
                'N1FechaLib',
                'N2FechaLib',
                'N3FechaLib',
                'N4FechaLib',
                'Fecha de liberación de ultimo nivel de p',
                'Fecha de liberación de ultimo nivel de p',
                'Fecha de liberación de ultimo nivel de p',
                'Fecha de liberación de ultimo nivel de p',
                'Fecha entrega estad.',
                'Fecha de entrega')

#wsdl = "http://gtdvfdb001.liztex.local:8220/sap/bc/srt/wsdl/flv_10002A10MAR1/bndg_url/sap/bc/srt/rfc/sap/zws_zmsc001/100/zws_zmsc001/zws_zmsc001?sap-client=100"
wsdl = 'http://gtprvap009.liztex.local:8250/sap/bc/srt/wsdl/flv_10002A111AD1/bndg_url/sap/bc/srt/rfc/sap/zws_zmsc001_v1/500/zws_zscm001_v1/zws_zscm001_v1?sap-client=500'
session = Session()
session.auth = HTTPBasicAuth(username, password)
session.verify=False
client=Client(wsdl,transport=Transport(session=session))

reposne=client.service.ZMM_GET_DATA_EKKO(GV_FECHA ='2021-01-01',GT_EKKO = GtEkko )
print (len(reposne.DATA['item']))
row = 0
col = 0

documentoAnterior = None
itemDocAnterior = None
today = date.today()
today = today.strftime("%d-%m-%Y")

workbook = xlsxwriter.Workbook(r'C:\Users\pablo.villagran\Documents\DEV_Python\LZCONSUMEAPI\DataAbastecimientos'+today+'.xlsx')
worksheet = workbook.add_worksheet()

#set worksheet header 
for item in xlsxHeader:
    worksheet.write(row, col, item)
    col += 1

row +=1
#set worksheet Data
for item in reposne.DATA['item']:
    col = 0  
    
    if (item['N1_FECHALIB'] == '0000-00-00'):
        item['N1_FECHALIB'] = ''
        
    if (item['N2_FECHALIB'] == '0000-00-00'):
        item['N2_FECHALIB'] = ''
        
    if (item['N3_FECHALIB'] == '0000-00-00'):
        item['N3_FECHALIB'] = ''
        
    if (item['N4_FECHALIB'] == '0000-00-00'):
        item['N4_FECHALIB'] = ''
        
    if (item['FECHA_RECHAZO'] == '0000-00-00'):
        item['FECHA_RECHAZO'] = ''
        
    if (item['HORA_RECHAZO'] == '0'):
        item['HORA_RECHAZO'] = ''
        
    if (item['FECHA_ACTIVACION_ESTRATEGIA'] == '0000-00-00'):
        item['FECHA_ACTIVACION_ESTRATEGIA'] = ''
        
    if (item['FECHA_LIBERACION'] == '0000-00-00'):
        item['FECHA_LIBERACION'] = ''
        
    if (item['FECHA_ULTIMO_ANTICIPO'] == '0000-00-00'):
        item['FECHA_ULTIMO_ANTICIPO'] = ''
        
    if (item['FECHA_RECEPCION_MERCANCIA'] == '0000-00-00'):
        item['FECHA_RECEPCION_MERCANCIA'] = ''
        
    if (item['ULTIMA_FECHA_MOD_RECEPCION'] == '0000-00-00'):
        item['ULTIMA_FECHA_MOD_RECEPCION'] = ''
        
    if (item['FECHA_ACEPTACION_SERVICIO'] == '0000-00-00'):
        item['FECHA_ACEPTACION_SERVICIO'] = ''
     
    if (item['ULTIMA_FECHA_REP_ACEPT'] == '0000-00-00'):
            item['ULTIMA_FECHA_REP_ACEPT'] = ''
    
    if (item['FECHA_RECEPCION_FACTURA'] == '0000-00-00'):
        item['FECHA_RECEPCION_FACTURA'] = '' 

    if (item['FECHA_ENTREGA_ESTADISTICA'] == '0000-00-00'):
        item['FECHA_ENTREGA_ESTADISTICA'] = '' 
        
    if (item['FECHA_ENTREGA_POSICION'] == '0000-00-00'):
        item['FECHA_ENTREGA_POSICION'] = '' 

    if (item['FECHA_NECESIDAD'] == '0000-00-00'):
        item['FECHA_NECESIDAD'] = '' 

        
    if (documentoAnterior == item['NO_PEDIDO_COMPRAS_COMPLETADO'] and itemDocAnterior == item['POSICION']):
        item['VALOR_PEDIDO'] = 0
        item['MONEDA_PEDIDO'] = 0.0
        
    worksheet.write(row, col, item['CENTRO'])
    worksheet.write(row, col + 1 , item['GRUPO_COMPRAS'])
    worksheet.write(row, col + 2 , item['NO_SOLICITUD'])
    worksheet.write(row, col + 3 , item['INDICADOR_BORRADO_S'])
    worksheet.write(row, col + 4 , item['FECHA_SOLICITUD'])
    worksheet.write(row, col + 5 , item['FECHA_LIBERACION_SOLICITUD'])
    worksheet.write(row, col + 6 , item['FECHA_MODIFICACION'])
    worksheet.write(row, col + 7 , item['FECHA_ENTREGA'])
    worksheet.write(row, col + 8 , item['LIBERADOR'])
    worksheet.write(row, col + 9 , item['CLASE_PEDIDO'])
    worksheet.write(row, col + 10 , item['INDICADOR_BORRADO_DC'])
    worksheet.write(row, col + 11 , item['USUARIO_PEDIDO'])
    worksheet.write(row, col + 12 , item['APELLIDO_USUARIO'])
    worksheet.write(row, col + 13 , item['NO_PEDIDO_COMPRAS_COMPLETADO'])
    worksheet.write(row, col + 14 , item['FECHA_PEDIDO'])
    worksheet.write(row, col + 15 , item['GRUPO_ARTICULOS'])
    worksheet.write(row, col + 16 , item['DENOMINACION_GRPCOMP'])
    worksheet.write(row, col + 17 , item['MATERIAL'])
    worksheet.write(row, col + 18 , item['TEXTO_BREVE'])
    worksheet.write(row, col + 19 , item['CANTIDAD_PEDIDO'])
    worksheet.write(row, col + 20 , item['VALOR_PEDIDO'])
    worksheet.write(row, col + 21 , item['MONEDA_PEDIDO'])
    worksheet.write(row, col + 22 , item['DENOMINACION_ARTICULOS'])
    worksheet.write(row, col + 23 , item['STATUS_TRATAMIENTO_DOC'])
    worksheet.write(row, col + 24 , item['STATUS_TRATAMIENTO_DOC_TEXT'])
    worksheet.write(row, col + 25 , item['ESTRATEGIA_LIBERACION'])
    worksheet.write(row, col + 26 , item['INDICADOR_LIBERACION'])
    worksheet.write(row, col + 27 , item['DESCRIPCION'])
    worksheet.write(row, col + 28 , item['FECHA_RECHAZO'])
    worksheet.write(row, col + 29 , item['HORA_RECHAZO'])
    worksheet.write(row, col + 30 , item['USUARIO_RECHAZO'])
    worksheet.write(row, col + 31 , item['APELLIDO_RECHAZO'])
    worksheet.write(row, col + 32 , item['ULTIMO_MOVIMIENTO'])
    worksheet.write(row, col + 33 , item['ESTADO_LIBERACION'])
    worksheet.write(row, col + 34 , item['DENOMINACION_ESTADO_LIBERACION'])
    worksheet.write(row, col + 35 , item['FECHA_ACTIVACION_ESTRATEGIA'])
    worksheet.write(row, col + 36 , item['FECHA_LIBERACION'])
    worksheet.write(row, col + 37 , item['TOTAL_ANTICIPO_ML'])
    worksheet.write(row, col + 38 , item['TOTAL_ANTICIPO'])
    worksheet.write(row, col + 39 , item['MONEDA'])
    worksheet.write(row, col + 40 , item['FECHA_ULTIMO_ANTICIPO'])
    worksheet.write(row, col + 41 , item['FECHA_FINAL'])
    worksheet.write(row, col + 42 , item['FECHA_RECEPCION_MERCANCIA'])
    worksheet.write(row, col + 43 , item['POSICION'])
    worksheet.write(row, col + 44 , item['NO_DOCUMENTO_EM'])
    worksheet.write(row, col + 45 , item['CANTIDAD_ENTRADA'])
    worksheet.write(row, col + 46 , item['CLASE_MOVIMIENTO'])
    worksheet.write(row, col + 47 , item['ULTIMA_FECHA_MOD_RECEPCION'])
    worksheet.write(row, col + 48 , item['FECHA_ACEPTACION_SERVICIO'])
    worksheet.write(row, col + 49 , item['NO_ACEPTACION_SERVICIO'])
    worksheet.write(row, col + 50 , item['ULTIMA_FECHA_REP_ACEPT'])
    worksheet.write(row, col + 51 , item['FECHA_RECEPCION_FACTURA'])
    worksheet.write(row, col + 52 , item['NO_ACEPTACION_REL'])
    if(item['FECHA_BASE'] != '0000-00-00' and str.isnumeric(item['FECHA_BASE'])):
        if item['DIAS_PAGO'] > 0:
            worksheet.write(row, col + 53 , datetime.datetime.strptime(item['FECHA_BASE'], "%Y-%m-%d") + datetime.timedelta(days=item['DIAS_PAGO']) )
        else:
            worksheet.write(row, col + 53 , datetime.datetime.strptime(item['FECHA_BASE'], "%Y-%m-%d") )
    else:
        worksheet.write(row, col + 53 , '')
    worksheet.write(row, col + 54 , '')
    worksheet.write(row, col + 55 , item['FECHA_NECESIDAD'])
    worksheet.write(row, col + 56 , item['N1_USUARIO'])
    worksheet.write(row, col + 57 , item['N2_USUARIO'])
    worksheet.write(row, col + 58 , item['N3_USUARIO'])
    worksheet.write(row, col + 59 , item['N4_USUARIO'])
    worksheet.write(row, col + 60 , item['N1_FECHALIB'])
    worksheet.write(row, col + 61 , item['N2_FECHALIB'])
    worksheet.write(row, col + 62 , item['N3_FECHALIB'])
    worksheet.write(row, col + 63 , item['N4_FECHALIB'])
    worksheet.write(row, col + 64 , item['FECHA_LIBERACION_N1'])
    worksheet.write(row, col + 65 , item['FECHA_LIBERACION_N2'])
    worksheet.write(row, col + 66 , item['FECHA_LIBERACION_N3'])
    worksheet.write(row, col + 67 , item['FECHA_LIBERACION_N4'])
    worksheet.write(row, col + 68 , item['FECHA_ENTREGA_ESTADISTICA'])
    worksheet.write(row, col + 69 , item['FECHA_ENTREGA_POSICION'])
    row += 1
    documentoAnterior =item['NO_PEDIDO_COMPRAS_COMPLETADO']
    itemDocAnterior = item['POSICION']
    
workbook.close()

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Finalizando el: ", dt_string)	

"""
try:    
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(
            host="172.16.23.153",
            database="dbliztex",
            user="liztex",
            password="golosin")
    conn.set_client_encoding('SQLASCII')
    cur = conn.cursor()
    cur.execute('SELECT * FROM lzty_variable limit 10;')
    conn.commit()
    
    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
        print('Database connection closed.')"""