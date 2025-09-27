from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import subprocess
import re

def home(request):
    return render(request, 'home.html')

def investment(request):
    return render(request, 'investment.html')

def broker(request):
    return render(request, 'broker.html')

def roadmap_page(request):
    return render(request, 'roadmap.html')

@csrf_exempt
def generate_roadmap(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON received'})

        investment_type = data.get('investmentType')
        current_level = data.get('currentLevel')
        target_level = data.get('targetLevel')

        if not (investment_type and current_level and target_level):
            return JsonResponse({'error': 'All fields are required.'})

        prompt = (
            f"Create a detailed and structured learning roadmap for someone currently at '{current_level}' "
            f"knowledge level who wants to reach '{target_level}' in '{investment_type}' investing.\n\n"
            "Follow this exact format:\n"
            "Title: <A concise title for the roadmap>\n"
            "Objective: <A clear statement of what the learner will achieve>\n"
            "Step 1: <Short title> (Time: x weeks)\n"
            "1. \n"
            "2. \n"
            "Step 2: <Short title> (Time: x weeks)\n"
            "1. \n"
            "2. \n"
            "... (add as many steps as needed)\n"
            "Conclusion: <Final advice or wrap-up>\n\n"
            "Make sure each step has at least 2 bullet points."
        )

        try:
            result = subprocess.run(
                ["ollama", "run", "llama2", prompt],
                capture_output=True,
                text=True,
                check=True
            )
            response = result.stdout.strip()

            # Split output into blocks based on expected structure
            lines = response.splitlines()
            blocks = []
            buffer = []

            for line in lines:
                if re.match(r"^(Title|Objective|Step \d+|Conclusion):", line):
                    if buffer:
                        blocks.append('\n'.join(buffer).strip())
                        buffer = []
                buffer.append(line)

            if buffer:
                blocks.append('\n'.join(buffer).strip())

            return JsonResponse({'roadmap': blocks})

        except subprocess.CalledProcessError as e:
            return JsonResponse({'error': f"AI Error: {e.stderr}"})

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
