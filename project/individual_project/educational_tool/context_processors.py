from educational_tool.models import video, exercise,topic, tutorial

def extras(request):
    context_dict = {}
    # context_dict['boldmessage'] = 'Why Learn Code?'
    # context_dict['videos'] = video.objects.all()
    # context_dict['excercises'] = exercise.objects.all()
    # context_dict['topics'] = topic.objects.all()

    videos = video.objects.all()
    exercises = exercise.objects.all()
    topics = topic.objects.all()
    tutorials = tutorial.objects.all()

    return{'videos': videos,'excercises': exercises,'topics': topics, 'tutorials':tutorials}