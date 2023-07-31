# pylint: disable=E1101
"""
Librairies
"""
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from partners.models import Partner
from partners.forms import PartnerForm

################# Views with Partner Model - Organized in the order of CRUD ####################
def c_partner(request):
    """
    Create Partner
    """
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PartnerForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required - I don't know if it is necessary

            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/partners/")

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PartnerForm()

    return render(request, "Partners/CreatePartner.html", {"form":form})

def r_partners(request):
    """
    Read Partners
    """
    partners = Partner.objects.all()
    context = {'Partners':partners}

    return render(request, "Partners/PartnersMain.html", context)

def u_partner(request, id_partner):
    """
    Update Partner
    """
    partner_to_update = Partner.objects.get(id=id_partner)
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = PartnerForm(request.POST, request.FILES, instance=partner_to_update)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required - I don't know if it is necessary

            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect("/partners/")

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PartnerForm(instance=partner_to_update)

    return render(request, "Partners/UpdatePartner.html", {"form":form})

def d_partner(request, id_partner):
    """
    Delete Partner
    """
    partner_to_delete = Partner.objects.get(id=id_partner)
    url_remove = 'Partner_d'
    url_cancel = 'Partners_r'
    context = {'Id': partner_to_delete.id, 'UrlRemove':url_remove, 'UrlCancel':url_cancel}
    if request.method == "POST":
        partner_to_delete.delete()
        return redirect('/partners/')

    return render(request, "base/confirmDelete.html", context)
