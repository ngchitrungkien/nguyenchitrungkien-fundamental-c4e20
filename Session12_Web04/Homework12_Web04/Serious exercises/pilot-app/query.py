from models.service import Service
import mlab

mlab.connect()

id_to_find = "5b781f060b2d7e2ce07aca2f"

# hera = Service.objects(id=id_to_find) ## => [Service obj]
# hera = Service.objects.get(id=id_to_find) ## => Service obj
service = Service.objects.with_id(id_to_find)
if service is not None:
    # service.delete()
    # print("Deleted")
    print("Before: ")
    print(service.to_mongo())
    service.update(set__yob=2005,set__name="Linh Kute")
    service.reload()
    print("After: ")
    print(service.to_mongo())
else:
    print("Not found")