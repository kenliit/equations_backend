from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from captcha.equations import question_picker, verify_answer


def check_connection(request):
    return HttpResponse('ok')


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_question(request):
    return JsonResponse(question_picker(), safe=False)


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def check_answer(request):
    question_id = request.data['question_id']
    answer = request.data['answer']
    response = verify_answer(question_id, answer)
    if "yes" in response.keys():
        return Response(response, status=status.HTTP_202_ACCEPTED)
    else:
        return Response(response, status=status.HTTP_406_NOT_ACCEPTABLE)


