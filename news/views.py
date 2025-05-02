from django.shortcuts import render, redirect
from .models import Post, PostAttachment
from .form import Postform
# Create your views here.
def Post_list(request):
    posts = Post.objects.all().order_by('time_stamp')
    for post in posts:
        att=PostAttachment.objects.filter(post_id = post.pk)
        post.att = att
    return render(request, 'news/post_list.html', {'posts': posts} ) 

def postDetails(request, pid):
    post = Post.objects.get(pk=pid)
    images = PostAttachment.objects.filter(post_id = pid)
    return render(request, 'news/details_page.html', {'post': post, 'images': images})

def addPost(request):
    if request.method != 'POST':
        form = Postform()
    else:
        form = Postform(request.POST, request.FILES)
        att = request.FILES.getlist('images')
        if form.is_valid():
            post = form.save(commit=False)
            # add author to post
            post.save()
            for img in att:
                PostAttachment.objects.create(post_id = post.pk, image=img)
        return redirect(to='details', pid=post.pk)
    return render(request, 'news/newpost.html', {'form':form})

def editPost(request, pid):
    post = Post.objects.get(pk=pid)
    post_att = PostAttachment.objects.filter(post_id=pid)
    if request.method != 'POST':
        form = Postform(instance=post)
    else:
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            att = request.FILES.getlist('images')
            for img in att:
                PostAttachment.objects.create(post_id = post.pk, image=img)
            chosen = request.POST.getlist('attachments')
            for img_id in chosen:
                PostAttachment.objects.get(pk=int(img_id)).delete()
            post.edited = True
            post.save()

        return redirect(to='details', pid=post.pk)
    return render(request, 'news/editpost.html', {'form':form, 'post_att':post_att})

def deletePost(request, pid):
    post = Post.objects.get(pk=pid).delete()
    return redirect(to='post-list')