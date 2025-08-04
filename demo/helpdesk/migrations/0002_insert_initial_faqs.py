from django.db import migrations

def insert_faqs(apps, schema_editor):
    FAQ = apps.get_model('helpdesk', 'FAQ')
    FAQ.objects.create(question="What are the admission requirements?", answer="You need your high school transcripts, ID, and application form.")
    FAQ.objects.create(question="What is the fee structure?", answer="Fees vary by program; please check the fees section on the website.")
    FAQ.objects.create(question="When is the gym open for males?", answer="Gym timings for males: Monday-Friday 6am-9pm.")
    FAQ.objects.create(question="When is the gym open for females?", answer="Gym timings for females: Monday-Friday 7am-8pm.")
    FAQ.objects.create(question="What are the library timings?", answer="Library is open Monday-Saturday 8am-10pm.")
    FAQ.objects.create(question="What extracurricular activities are available?", answer="We have sports, music clubs, drama, and more.")

class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),  # ✅ Replace with your previous migration if different
    ]

    operations = [
        migrations.RunPython(insert_faqs),
    ]
