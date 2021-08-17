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