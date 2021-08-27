# SpeedtestBalancer

![Code Generator](https://github.com/AleksandrVin/SpeedtestBalancer/actions/workflows/swagger_gen_and_publish.yaml/badge.svg)
![Tox testing](https://github.com/AleksandrVin/SpeedtestBalancer/actions/workflows/tox_testing.yaml/badge.svg)

Used to provide users with IP addresses of Iperf servers.
See [Iperf Server](https://github.com/SkoltechSummerCamp/SpeedtestService) and [Mobile App](https://github.com/SkoltechSummerCamp/SpeedtestApplication)

> __Do not change swagger.yaml without swagger hub__
[Swagger HUB with API](https://app.swaggerhub.com/apis/vsasha1305/Skoltech_OpenRAN_5G_Group_Balancer_API/0.0.1-oas3)


### Server operation 

Just start server

```bash
cd server
python3 setup.py install --user
pip3 install -r requirements.txt
python3 setup.py install --user
export BALANCER_PORT=8080 # port for server to run
python3 -m swagger_server
```

or with docker

```bash
cd server
docker run -p $PORT_OUT:$BALANCER_PORT docker_image_name
```

Make use of __SERVERLOGPATH__ environment variable. Server list will be stored there. Deleted and used

```bash
export SERVERLOGPATH=../logs/log.txt
echo $SERVERLOGPATH
```

## WorkFlow

1. Update Swagger-api
[Swagger HUB with API](https://app.swaggerhub.com/apis/vsasha1305/Skoltech_OpenRAN_5G_Group_Balancer_API/0.1.0-oas3)
2. Sync Swagger Hub with GitHub. Action will regenerate code and commit it.
3. Pull changes
4. Implement new endpoints inside *_controllers.py, using Connexion library. Generated templates stored in *_controllers_new.py.
5. Push changes to github. 

> NOTE. Project based on Python-flask. Do not use it on production.
> Install Swagger and fix update_prj_from_yaml.sh to regenerate swagger locally. Do not change API locally!

### GitHub Action

On every Push to github action regenerate project. Code inside *_controller.py stays without changes.

### About

Code based on Swagger CodeGenerator

Created during Skoltech Summer Camp. Inspired byEugene Mavrin.
Developed by Aleksandr Vinogradov and Vladimir Prokhorov.