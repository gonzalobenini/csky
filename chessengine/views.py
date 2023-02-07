from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .Game import generate_random_pieces
from .Engine import ini_engine,calculate_nextmove

import copy
# Create your views here.

def base(request):
    return HttpResponse('hola')

def get_pieces(request):
    return JsonResponse({"white":generate_random_pieces('white'), "black":generate_random_pieces('black')})


@csrf_exempt
def get_move(request):
    req = json.loads(request.body)
    print('--------------------------')
    print(req)
    print('--------------------------')
    board = req['board']
    elo = req['elo']
    engine = ini_engine()
    return JsonResponse(calculate_nextmove(engine, board, elo))