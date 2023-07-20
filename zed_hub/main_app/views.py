from django.shortcuts import render, redirect

from zed_hub.main_app.forms import TemplateModelCreateForm, TemplateModelEditForm, \
    TemplateModelDeleteForm, TemplateModelShowForm
from zed_hub.main_app.models import TemplateModel


def index_view(request):
    template = 'main_app/main_app_index.html'
    context = {}
    return render(request, template, context)


def list_view(request):
    template = 'main_app/main_app_list.html'
    all_objects = TemplateModel.objects.all()
    context = {
        'all_objects': all_objects,
    }
    return render(request, template, context)


def create_view(request):
    template = 'main_app/main_app_add.html'
    form = TemplateModelCreateForm()

    if request.method == 'GET':
        form = TemplateModelCreateForm()
    elif request.method == 'POST':
        form = TemplateModelCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main app index')

    context = {
        'form': form,
    }
    return render(request, template, context)


def show_view(request, pk, slug):
    template = 'main_app/main_app_show.html'
    current_object = TemplateModel.objects.get(pk=pk)
    context = {
        'current_object': current_object,
    }
    return render(request, template, context)


def edit_view(request, pk, slug):
    template = 'main_app/main_app_edit.html'
    current_object = TemplateModel.objects.get(pk=pk)
    form = TemplateModelEditForm()

    if request.method == 'GET':
        form = TemplateModelEditForm(instance=current_object)
    elif request.method == 'POST':
        form = TemplateModelEditForm(request.POST, instance=current_object)
        if form.is_valid():
            form.save()
            return redirect('main app index')

    context = {
        'form': form,
        'current_object': current_object,
    }
    return render(request, template, context)


def delete_view(request, pk, slug):
    template = 'main_app/main_app_delete.html'
    current_object = TemplateModel.objects.get(pk=pk)
    form = TemplateModelDeleteForm()

    if request.method == 'GET':
        form = TemplateModelDeleteForm(instance=current_object)
    elif request.method == 'POST':
        form = TemplateModelDeleteForm(request.POST, instance=current_object)
        if form.is_valid():
            form.save()
            return redirect('main app index')

    context = {
        'form': form,
        'current_object': current_object,
    }
    return render(request, template, context)
