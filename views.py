from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
def index(request): return render(request,"index.html",{"notes":Note.objects.order_by("-created_at")})
def add_note(request):
 if request.method=="POST":
  title=request.POST.get("title","").strip(); content=request.POST.get("content","").strip()
  if title and content: Note.objects.create(title=title,content=content)
 return redirect("index")
def delete_note(request,pk): get_object_or_404(Note,pk=pk).delete(); return redirect("index")
