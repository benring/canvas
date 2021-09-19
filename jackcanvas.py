# Import the Canvas class
from canvasapi import Canvas
from canvasapi import exceptions as canexc
import pandas as pd
from datetime import datetime, timezone


EDT = datetime.now(timezone.utc).astimezone().tzinfo

def printcalls(fname, obj):
	with open(fname, 'w') as out: 
		out.write('\n'.join(dir(obj))) 

class Work:
	def __init__


TOKEN='3123~4qDFCHeEwDE6iLg99X9apITO8PKbMAPcxO2t3tRBHTOrLuvgCzqBLSUEY9czXivB'

# Canvas API URL
API_URL = "https://hcpss.instructure.com/"
# Canvas API key
API_KEY = TOKEN

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)

jack = canvas.get_current_user()


headers = ['Class', 'Assignment', 'Due', 'Submitted', 'Available', 'Points', 'Submitted', 'Missing', ]
df = pd.DataFrame(columns = headers)


courses = []
for c in canvas.get_courses():
	try:
		name = c.name
		id = c.id
		courses.append(id)
	except AttributeError:
		continue

COURSES_FALL21 = [159937, 164053, 164779, 162295, 163681, 34488, 75645, 164328, 164986]
COURSE_NAMES = ['Art', 'Government', 'Chemistry', 'English', 'Math', 'StuResources', 'RHSCommunity', 'Spanish', 'Tutorial']
for c in COURSES_FALL21:
	print(canvas.get_course(c))

sheet = []
for i, cid in enumerate(COURSES_FALL21):
	course = canvas.get_course(cid)
	assignments = course.get_assignments()
	for assignment in assignments:
		submission = assignment.get_submission(jack.id)
		row = {'Class': COURSE_NAMES[i], 'Assignment' :  assignment.name,'Due' :  assignment.due_at,'Available' : (not assignment.locked_for_user),'Points' : assignment.points_possible,'Submitted' : (not (submission.submitted_at is None)),'Missing' : submission.missing}
		sheet.append(row)

df = pd.DataFrame(sheet, columns = headers)

course_calls = {}
for f in dir(c):
	if not f.startswith('get'):
		continue
	func = 'c.' + f + '(user_id=id)'
	try:
		print(func)
		x = eval(func)
		course_calls[f] = True
	except canexc.Unauthorized:
		course_calls[f] = False


d.astimezone(EDT).strftime('%b %-d, %H:%M %z')

