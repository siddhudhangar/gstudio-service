from django.shortcuts import render
import requests
from gstudio_service.settings import HOSTNAME
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
# Create your views here.
@csrf_exempt
def create_or_update_page(request):
	if request.GET:
		group_id = request.GET.get("group_id")
		lan = request.GET.get("lan")
		name = request.GET.get("name")
		content_org = request.GET.get("content_org")
		alt_name = request.GET.get("alt_name")
		api_call = request.GET.get("api_call")
		created_by = request.GET.get("created_by")
		node_id = request.GET.get("node_id")
	elif request.POST:
		group_id = request.POST.get("group_id")
		lan = request.POST.get("lan")
		name = request.POST.get("name")
		content_org = request.POST.get("content_org")
		alt_name = request.POST.get("alt_name")
		api_call = request.POST.get("api_call")
		created_by = request.POST.get("created_by")
		node_id = request.POST.get("node_id")

	URL = HOSTNAME + group_id + "/course/save_course_page/"
	response = requests.post(URL,data={"lan":lan,"name":name,"content_org":content_org,"alt_name":alt_name,"api_call":api_call,"created_by":created_by,"node_id":node_id})
	return HttpResponse(response,content_type="application/json")

@csrf_exempt
def get_pages(request):
	if request.GET:
		group_id = request.GET.get("group_id")
		api_call = request.GET.get("api_call")

	elif request.POST:
		group_id = request.POST.get("group_id")
		api_call = request.GET.get("api_call")

	URL = HOSTNAME + group_id + "/course/activities/"
	response = requests.post(URL,data={"api_call":api_call})
	return HttpResponse(response,content_type="application/json")

@csrf_exempt
def delete_page(request):
	if request.GET:
		delete_files_list = request.GET.getlist('delete_files_list[]', '')
		activity_id = request.GET.get('activity_id', '')
		group_id = request.GET.get("group_id", '')
		username = request.GET.get("username", '')

	elif request.POST:
		delete_files_list = request.POST.getlist('delete_files_list[]', '')
		activity_id = request.POST.get('activity_id', '')
		group_id = request.POST.get("group_id",'')
		username = request.POST.get("username")

	URL = HOSTNAME + group_id + "/course/delete_activity_page/"
	response = requests.post(URL,data={"username":username,"group_id":group_id,"delete_files_list":delete_files_list,"activity_id":activity_id})
	return HttpResponse(response,content_type="application/json")

@csrf_exempt
def get_groups(request):
	if request.GET:
		api_call = request.GET.get("api_call")

	elif request.POST:
		api_call = request.GET.get("api_call")

	URL = HOSTNAME + "explore/workspaces"
	response = requests.post(URL,data={"api_call":api_call})
	return HttpResponse(response,content_type="application/json")

@csrf_exempt
def get_courses(request):
	if request.GET:
		api_call = request.GET.get("api_call")

	elif request.POST:
		api_call = request.GET.get("api_call")

	URL = HOSTNAME + "explore/courses"
	response = requests.post(URL,data={"api_call":api_call})
	return HttpResponse(response,content_type="application/json")

@csrf_exempt
def get_draftcourses(request):
	if request.GET:
		api_call = request.GET.get("api_call")

	elif request.POST:
		api_call = request.POST.get("api_call")

	URL = HOSTNAME + "explore/basecourses"
	response = requests.post(URL,data={"api_call":api_call})
	return HttpResponse(response,content_type="application/json")

@csrf_exempt
def upload_file(request):
	if request.GET:
		group_id = request.GET.get("group_id",'')
		# api_call = request.GET.get("api_call")
		asset_cont_desc = request.GET.get("asset_cont_desc")
		asset_cont_name = request.GET.get("asset_cont_name")
		filehive = request.FILES.getlist("filehive",[])
		FILE_PATH = request.GET.get("FILE_PATH")
		asset_obj = request.GET.get("asset_obj")
		created_by = request.GET.get("created_by")
	elif request.POST:
		# api_call = request.POST.get("api_call")
		group_id = request.POST.get("group_id",'')
		asset_cont_desc = request.POST.get("asset_cont_desc")
		asset_cont_name = request.POST.get("asset_cont_name")
		filehive = request.FILES.getlist("filehive",[])
		asset_obj = request.POST.get("asset_obj")
		created_by = request.POST.get("created_by")
	# print(filehive)
	# print(group_id)
	files = [('filehive', ('course.png', open('course.png', 'rb'), 'image/png'))]
	URL = HOSTNAME + group_id + "/ajax/add_assetcontent"
	# print(URL)
	response = requests.post(URL,data={"asset_cont_name":asset_cont_name,"asset_cont_desc":asset_cont_desc,"asset_obj":asset_obj,"created_by":created_by},files=files)
	return HttpResponse(response,content_type="application/json")
