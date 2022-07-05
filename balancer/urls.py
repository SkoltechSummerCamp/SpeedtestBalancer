from django.urls import path, include

urlpatterns = [
    path('Skoltech_OpenRAN_5G/iperf_load_balancer/0.1.0/', include('balancer.urls_v_0_1_0')),
]
