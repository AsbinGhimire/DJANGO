from django.shortcuts import render

def bmi_calculator(request):
    if request.method == 'POST':
        try:
            weight = float(request.POST.get('weight', 0))  # in kg
            height = float(request.POST.get('height', 0)) / 100  # Convert cm to meter
            
            if weight > 0 and height > 0:
                bmi = weight / (height ** 2)
                
                # Determine BMI category
                if bmi < 18.5:
                    category = "Underweight"
                    color = "blue"
                elif 18.5 <= bmi < 25:
                    category = "Normal weight"
                    color = "green"
                elif 25 <= bmi < 30:
                    category = "Overweight"
                    color = "orange"
                else:
                    category = "Obese"
                    color = "red"
                
                return render(request, 'bmi_result.html', {
                    'bmi': round(bmi, 2),
                    'category': category,
                    'color': color,
                    'weight': weight,
                    'height': height * 100  # Convert back to cm for display
                })
            else:
                error = "Please enter valid positive numbers for weight and height."
                return render(request, 'bmi_form.html', {'error': error})
                
        except (ValueError, ZeroDivisionError):
            error = "Invalid input. Please enter numeric values."
            return render(request, 'bmi_form.html', {'error': error})
    
    return render(request, 'bmi_form.html')