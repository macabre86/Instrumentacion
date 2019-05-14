# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:52:56 2019

@author: macabre
"""
#PARA PARALELIZAR
import concurrent.futures
import urllib.request
#Se usa esto para hacer IO-bounds (espera interaccion) 

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://some-made-up-domain.com/']
#Tengo 4 direcciones y una que no existe

# Retrieve a single page and report the URL and contents

def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()
#Baja las paginas y las lee.
        

# We can use a with statement to ensure threads are cleaned up promptly
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Start the load operations and mark each future with its URL
    
    #Distribuye la cola y executor la distribuye
    
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    #El primer elemento agarra una funcion, con los parametros. Alimento las cosas para hacer
    #60 es el timeout
    
#    # Esto es una forma corta de
#    x=[]
#    for url in URLS:
#        o=executor.submit(load_url,url,60)
#        x[o]=url
#        
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))
            
 #La idea es darle la cola.           