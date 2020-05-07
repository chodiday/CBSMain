from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, json
)
from werkzeug.exceptions import abort
from flask import Markup
#from flaskr.auth import login_required
#from flaskr.db import get_db

bp = Blueprint('cbs', __name__)

#convert sentence into array 
def convertToArray(sentence): 
	#return sentence.split()
	return list(sentence)

#convert array to string
def convertToString(keywords):
	str = ""
	for keyword in keywords:
		str += keyword + ' '
	return str	


@bp.route('/')
def index():
    
    sentence = "Hello Road?, Is this, the emergency hotline?.. I would like to report that there " + "is a heavy traffic due to a collision... between MitsubishiV.02 & mazda3 car " + "along District 11th Kamuning road. " 
    jap_sentence = "こんにちは道路、これは緊急ホットラインですか？第11地区カムニン道路沿いの 三菱とマツダ3両が 衝突して渋 滞しているとのことです。"
    keywords = ["三菱","トラフィック","マツダ","衝突","道路"]
    #keywords = ["Mitsubishi","traffic", "Mazda", "Collision", "road"]

    sentence_array = convertToArray(jap_sentence)
    print(sentence_array)

    #=== FRO ENGLISH WORDS ====
    #check if keywords are present in the realtime sentence.
    # for n, word in enumerate(sentence_array):
    #    for keyword in keywords:
    #       if keyword.upper() == word.upper() or word.upper().find(keyword.upper()) > -1:
    #          sentence_array[n] = "<span style=\'background-color:yellow;\'>"+word+"</span>"
    
    #=== FOR JAPANESE ===
    for n, word in enumerate(sentence_array):
       for keyword in keywords:
          if word in keyword:
          	 print(word +"->"+ keyword)
          	 sentence_array[n] = "<span class=\"keyword\">"+word+"</span>"
          
    data = {'name':'ben', 'info':'sample data', 'content': Markup("".join(sentence_array))}
    data2 = {'sentence':jap_sentence, 'keywords': convertToString(keywords).strip()}

    return render_template('cbs/index.html', data=data, data2=data2)

