from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def home(request):
	'''
	create a home page  "brawser topics, main Room, recent activity
	'''
	q = request.GET.get('q') if request.GET.get('q') != None else ''
	rooms = Room.objects.filter(
		Q(topic__name__icontains=q)|
		Q(name__icontains=q)|
		Q(description__icontains=q)|
		Q(host__username__icontains=q)
	)
	room_count = rooms.count()
	topics = Topic.objects.all()
	messages = Message.objects.all()
	return render(request, 'chatterbox/home.html', {
	'rooms':rooms,
	'topics':topics,
	'room_count': room_count,
	'messages': messages
	})


def room(request, pk):
	'''
	Page Room contient the exchange between users of specific topics
	'''
	room = get_object_or_404(Room, id=pk)
	# for many to one (_set)
	model_messages = room.message_set.all()
	# for many to many without (_set)
	participants = room.participants.all()

	if request.method == "POST":
		message_comment = Message.objects.create(
		user=request.user,
		room=room,
		content=request.POST.get('content')
		)
		room.participants.add(request.user)
		return redirect('room', pk=room.id)


	return render(request, 'chatterbox/room.html', {
	'room':room,
	'model_messages':model_messages,
	'participants':participants,
	})


def profileUser_view(request, pk):
	'''
	profile of each login in user
	'''
	user = User.objects.get(id=pk)
	rooms = user.room_set.all()
	topics = Topic.objects.all()
	return render(request, 'chatterbox/profile.html', {
		'rooms':rooms,
		'topics':topics,
	})


@login_required(login_url='/user/login/')
def roomRemove_comment(request, pk):
	'''
	remove a comment of  the user 
	'''
	message_room_delete = get_object_or_404(Message, id=pk)
	if request.method == "POST":
		message_room_delete.delete()
		return redirect("home")
	return render(request, 'chatterbox/room_delete.html', {
			'message_room_delete': message_room_delete
		})


@login_required(login_url='/user/login/')
def create_room(request):
	"""
	create a new room with new topic
	"""
	page='create'
	topics = Topic.objects.all()
	if request.method == "POST":
		#form = RoomForm(request.POST)
		#if form.is_valid():
			#room = form.save(commit=False)
			#room.host = request.user
			#form.save()
		topic_name = request.POST.get("topic")
		topic, create = Topic.objects.get_or_create(name=topic_name)
		Room.objects.create(
			host=request.user,
			topic=topic,
			name=request.POST.get("name"),
			description = request.POST.get("description")
		)
		return redirect('home')
	form = RoomForm()
	return render(request, 'chatterbox/room_create_update.html', {
			'form':form,
			'topics':topics,
			'page':page
			})


@login_required(login_url='/user/login/')
def update_room(request, pk):
	'''
	update a topics of the room
	'''
	room = get_object_or_404(Room, id=pk)
	if request.user != room.host:
		return HttpResponse(' NOT ALLOWED !!')
	if request.method == 'POST':
		topic_name = request.POST.get("topic")
		topic, create = Topic.objects.get_or_create(name=topic_name)
		room.topic = topic
		room.name = request.POST.get('name')
		room.description = request.POST.get("description") 
		#form = RoomForm(request.POST, instance=target)
		#if form.is_valid():
		room.save()
		return redirect('home')
	form = RoomForm(instance=room)
	return render(request, 'chatterbox/room_create_update.html', {'form': form})


@login_required(login_url='/user/login/')
def delete_room(request, pk):
	'''
	delete a room that was created by the user
	'''
	room = get_object_or_404(Room, id=pk)
	if request.user != room.host:
		return HttpResponse("NOT ALLOWED !!")
	if request.method == "POST":
		room.delete()
		return redirect('home')
	return render(request, 'chatterbox/room_delete.html', {'room': room})
