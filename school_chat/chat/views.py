from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Message
from django.utils import timezone

def home(request):
    rooms = Room.objects.all()
    return render(request, 'chat/home.html', {'rooms': rooms})

def room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    messages = Message.objects.filter(room=room)
    
    if request.method == 'POST':
        content = request.POST.get('content', '').strip()
        if content and request.user.is_authenticated:
            Message.objects.create(
                room=room,
                user=request.user,
                content=content,
                timestamp=timezone.now()
            )
            return redirect('room', room_id=room.id)
    
    return render(request, 'chat/room.html', {
        'room': room,
        'messages': messages
    })