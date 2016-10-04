from django.shortcuts import render, get_object_or_404

from models import Badge

def overview(request, extra_context={}):
    badges = Badge.objects.active().order_by("level")
    
    context = locals()
    context.update(extra_context)
    return render(request, "badges/overview.html", context)

def detail(request, slug, extra_context={}):
    badge = get_object_or_404(Badge, id=slug)
    users = badge.user.all()
    
    context = locals()
    context.update(extra_context)
    return render(request, "badges/detail.html", context)