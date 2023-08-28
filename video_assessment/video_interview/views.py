from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .models import QuestionPack, Question
from apicalling import test_api
import requests


def home(request):
    return render(request, 'video_interview/home.html')

def form(request):
    if request.method == 'POST':
        org_id="flipped"
        access_status = True
        s_no=1
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        max_attempts = int(request.POST.get('max_attempts'))
        min_response_duration = int(request.POST.get('min_response_duration'))
        max_response_duration = int(request.POST.get('max_response_duration'))
        submit_screen_title = request.POST.get('submit_screen_title')
        submit_screen_message = request.POST.get('submit_screen_message')
        show_question_numbers = request.POST.get('show_question_numbers') == 'on'
        feedback_url = request.POST.get('feedback_url')
        feedback_message = request.POST.get('feedback_message')
        feedback_button_text = request.POST.get('feedback_button_text')
        expiration_timestamp = int(request.POST.get('expiration_timestamp', 0))
        end_timestamp = int(request.POST.get('end_timestamp', 0))
        ended_message = request.POST.get('ended_message', '')
        require_linkedin = request.POST.get('require_linkedin') == 'on'
        linkedin_username = request.POST.get('linkedin_username', '')
        largest = QuestionPack.objects.all().order_by('access_id').last()
        if not largest:
            access_id= 1
        else:
            access_id = largest.access_id + 1

        ques_text = request.POST.get('ques_text')
        ques_type = request.POST.get('ques_type')
            

        # Create a new QuestionPack instance and save it to the database
        question_pack = QuestionPack(
            org_id=org_id,
            access_status = access_status,
            s_no=s_no,
            access_id=access_id,
            title=title,
            summary=summary,
            max_attempts=max_attempts,
            min_response_duration=min_response_duration,
            max_response_duration=max_response_duration,
            submit_screen_title=submit_screen_title,
            submit_screen_message=submit_screen_message,
            show_question_numbers=show_question_numbers,
            feedback_url=feedback_url,
            feedback_message=feedback_message,
            feedback_button_text=feedback_button_text,
            expiration_timestamp=expiration_timestamp,
            end_timestamp=end_timestamp,
            ended_message=ended_message,
            require_linkedin=require_linkedin,
            linkedin_username=linkedin_username
        )

        question_pack.save()
        Question.objects.create(org_id=org_id,access_id=question_pack,ques_id=1,ques_text=ques_text, ques_type=ques_type)
        #Login
        login_endpoint="/api/v1/user/login"
        payload = {
        "email": "info@flipped.ai",
        "password": "flipped123"
        }
        content_type = "application/json"
        headers = {"Content-Type": content_type}
        test_api(login_endpoint, payload, headers)

        create_qp_endpoint="/api/v1/qp/"
        payload={
            "qp_name": org_id+access_id,
            "title": title,
            "description": summary,
            "max_tries": max_attempts,
            "min_duration_secs": min_response_duration,
            "max_duration_secs": max_response_duration,
            "questions": [
                {
                    "title": ques_text,
                    "response_type": ques_type
                },
            ],
            "show_numbers": show_question_numbers,
            "post_header-title": submit_screen_title,
            "post_message": submit_screen_message,
            "feedback_url": feedback_url,
            "feedback_message": feedback_message,
            "feedback_button_text": feedback_button_text,
            "expiration": expiration_timestamp,
            "ended": end_timestamp,
            "end_message": ended_message,
            "require_linkedin": require_linkedin
        }

        headers = {
            "Authorization": f"Bearer {token_regular}",
            "Content-Type": "application/json"
            }
        
        test_api(create_qp_endpoint, payload, headers)



        return redirect('home')  # Redirect after successful submission

    return render(request, 'video_interview/form.html')

def assessments_for_org(request, org_id):
    assessments = QuestionPack.objects.filter(org_id=org_id)
    context = {'assessments': assessments}
    return render(request, 'video_interview/assessments_for_org.html', context)

def delete_assessment(request, org_id,access_id):
    assessment =get_object_or_404(QuestionPack, org_id=org_id, access_id=access_id)
    assessment.access_status = False
    assessment.save()
    delete_qp_endpoint=api/v1/qp/{{assessment.access_id}}
    headers = {
    "Authorization": "Bearer {{token_regular}}",
    "Content-Type": "application/json"
    }

    return redirect('assessments_for_org', org_id=assessment.org_id)


def update_assessment(request, org_id, access_id):
    assessment = get_object_or_404(QuestionPack, org_id=org_id, access_id=access_id)
    if request.method == 'POST':
        # Handle form submission and update the assessment
        # Example: assessment.title = request.POST.get('title')
        # Save the updated assessment
        update_qp_endpoint="api/v1/qp/{{ assessment.access_id }}"
        assessment.title = request.POST.get('title')
        assessment.summary = request.POST.get('summary')
        assessment.max_attempts = int(request.POST.get('max_attempts'))
        assessment.min_response_duration = int(request.POST.get('min_response_duration'))
        assessment.max_response_duration = int(request.POST.get('max_response_duration'))
        assessment.submit_screen_title = request.POST.get('submit_screen_title')
        assessment.submit_screen_message = request.POST.get('submit_screen_message')
        assessment.show_question_numbers = request.POST.get('show_question_numbers') == 'on'
        assessment.feedback_url = request.POST.get('feedback_url')
        assessment.feedback_message = request.POST.get('feedback_message')
        assessment.feedback_button_text = request.POST.get('feedback_button_text')
        assessment.expiration_timestamp = int(request.POST.get('expiration_timestamp', 0))
        assessment.end_timestamp = int(request.POST.get('end_timestamp', 0))
        assessment.ended_message = request.POST.get('ended_message', '')
        assessment.require_linkedin = request.POST.get('require_linkedin') == 'on'
        assessment.linkedin_username = request.POST.get('linkedin_username', '')
        assessment.save()
        payload={
            "qp_name": org_id+access_id,
            "title": assessment.title,
            "description": assessment.summary,
            "max_tries": assessment.max_attempts,
            "min_duration_secs": assessment.min_response_duration,
            "max_duration_secs": assessment.max_response_duration,
            "questions": [
                {
                    "title": ques_text,
                    "response_type": ques_type
                },
            ],
            "show_numbers": assessment.show_question_numbers,
            "post_header-title": assessment.submit_screen_title,
            "post_message": assessment.submit_screen_message,
            "feedback_url": assessment.feedback_url,
            "feedback_message": assessment.feedback_message,
            "feedback_button_text": assessment.feedback_button_text,
            "expiration": assessment.expiration_timestamp,
            "ended": assessment.end_timestamp,
            "end_message": assessment.ended_message,
            "require_linkedin": assessment.require_linkedin
        }

        headers = {
            "Authorization": "Bearer {{token_regular}}",
            "Content-Type": "application/json"
            }
        try:
            response = requests.put(api_url, json=payload, headers=headers)
            
            if response.status_code == 200:
                print("Request was successful!")
                print("Response JSON:")
                print(response.json())  # Assuming the response is in JSON format
            else:
                print(f"Request failed with status code: {response.status_code}")
                print("Response content:")
                print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")


        return render(request, 'video_interview/update_success.html', {'org_id':org_id})
    
    context = {'question_pack': assessment}
    return render(request, 'video_interview/update_assessment.html', context)