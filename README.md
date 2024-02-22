# Create Proto file according to models

python manage.py generateproto --model django.contrib.auth.models.User --fields <id,username> --file <filename.proto>


# Create _pb2.py, _pb2.pyi and _pb2_grpc.py file

python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. filename.proto


# Run server

python manage.py grpcrunserver --dev


### **Currently, gRPC supports only to Django version 4.0**

python3.11 manage.py generateproto --model unit_purchase.models.UnitPurchase  --file unit_purchase.proto