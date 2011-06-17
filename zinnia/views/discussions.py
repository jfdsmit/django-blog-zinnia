"""Views for Zinnia discussions"""

from django.shortcuts import render
from django.contrib.comments.models import Comment

def comment_posted(request):
    comment = Comment.objects.get(request["c"])
    return {"ok": True,
            "id": request.GET.get("c"),
            "comment": render(request, "blog/comment_template.html", {"id": comment.id, "comment": comment.comment})
            }
