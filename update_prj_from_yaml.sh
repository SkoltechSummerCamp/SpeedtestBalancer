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

head -2 server/swagger_server/__main__.py | grep vinogradov.alek@gmail.com
#If the patch has not been applied then the $? which is the exit status 
#for last command would have a success status code = 0
if [ $? -eq 0 ];
then
    echo "already pathed"
else
    #apply the patch
    echo "patching __main__.py"
    patch server/swagger_server/__main__.py < server/__main__.patch
fi