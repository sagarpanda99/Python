from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client.test_database
courses = db.course

arr_courses =[
    {
        'author' : 'Akash' ,
        'course' : 'MongoDb',
        'price' : '100',
        'rating' : 5
    },
    {
        'author' : 'Sritam' ,
        'course' : 'Python',
        'price' : '200',
        'rating' : 5
    },
    {
        'author' : 'Arihant' ,
        'course' : 'Java',
        'price' : '150',
        'rating' : 4
    }
]

'''
result = courses.insert_one(course)

if result.acknowledged:
    print('course added and course id is', str(result.inserted_id))
'''

results = courses.insert_many(arr_courses)

for object_id in results.inserted_ids:
    print('course added and course id is', str(object_id))