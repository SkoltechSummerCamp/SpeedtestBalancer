#!/bin/bash
cp server/swagger_server/controllers/*_controller.py . # save our implementation for later use
# generate swagger code
java -jar ../swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
    -i server/swagger_server/swagger/swagger.yaml \
    -l python-flask \
    -o server

echo saving generated controllers to controllers_new
for filename in server/swagger_server/controllers/*_controller.py; # renaming file
do
mv "$filename" "$(echo "$filename" | sed s/_controller.py/_controller_template.py/)";
done

echo restoring controllers
cp *_controller.py server/swagger_server/controllers/
rm *_controller.py
sed -i 's/python_dateutil == 2.6.0/python_dateutil == 2.7.0/' server/requirements.txt # replace dateutil version. Error with UTP on 2.6.0
sed -i 's/flask_testing==0.8.0/flask_testing==0.8.1/' server/test-requirements.txt # replace flask_testing version ( error in tox )