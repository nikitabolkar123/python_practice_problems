# ORM stands for Object-Relational Mapping
# ORM queries in Django are used to perform operations on the database without having to write raw SQL queries. Instead,
# you can use Python code to perform database operations, making it easier to read and maintain your code.

# from myapp.models import Person
# Model.objects.all():----returns all objects in the table.
people = Person.objects.all()

#filter()
# Model.objects.filter()---- returns a QuerySet of objects that match the specified filter.

people = Person.objects.filter(age__gte=18) # age__gte ---greater than 18

#create()
#Model.objects.create():---- creates a new object and saves it to the database.

person = Person.objects.create(name='abc', age=21, email='abc@example.com')

#save()
# model_instance.save(): saves the changes made to a model instance to the database.

person = Person(name='xyz', age=21, email='xyz@gmail.com')
person.save()

#get()
# Model.objects.get():----- returns a single object that matches the specified filter.
person = Person.objects.get(name='nikita')

# If more than one object matches the query parameters, a Person.MultipleObjectsReturned exception is raised.

#first()
#Model.objects.first(): returns the first object in the QuerySet.
person = Person.objects.first()

# Model.objects.last(): returns the last object in the QuerySet.
person = Person.objects.last()

# It's important to note that the first() and last() methods return None if the QuerySet is empty.

#delete
# model_instance.delete(): deletes a model instance from the database.

person = Person.objects.get(id=2)  # retrieve the Person object with id=2
person.delete()  # delete the Person object from the database

#update()-----
# Model.objects.update(): updates one or more fields in all objects that match the specified query parameters.

# update the author for all books published before 2000
Book.objects.filter(published_date__lt='2000-01-01').update(author='New Author')



#order_by()
# Model.objects.order_by(): returns a QuerySet of objects ordered by the specified field(s). it is in ascending ordered
# you can use the order_by() method on a model's manager (accessed through the model's class)
# to order the QuerySet of objects by one or more fields
persons = Person.objects.order_by('name')
# order_by() method orders the QuerySet of Person objects by the name field in ascending order (i.e., from A to Z).
persons = Person.objects.order_by('age', 'name') #we can use multiple attributes

# in descending order by prefixing the field name with a - (minus) sign:
persons = Person.objects.order_by('-name')
# In this example, the order_by() method orders the QuerySet of Person objects by the name field in descending order
# (i.e., from Z to A).

#values()
# Model.objects.values(): returns a QuerySet of dictionaries containing the specified fields.