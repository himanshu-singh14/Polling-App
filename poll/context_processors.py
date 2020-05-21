from poll.models import Question

def PollCount(request):
    count = Question.objects.count()
    return {"poll_count": count}