from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.urls import include, path
from .views import *
# from rest_framework.schemas import get_schema_view
from django.contrib.auth.decorators import login_required
from rest_framework import routers


# router = routers.DefaultRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="API Silant",
        default_version='ver 1.0.0',
        description="API documentation",
        terms_of_service="https://www.termsofservicegenerator.net/live.php?token=2osovODN2S0I3urRQYV6YKp8etpttYXF",
        contact=openapi.Contact(
            name="Dmitriy",
            url="https://github.com/gitustimov",
            email="udv0902@yandex.ru",
        ),
        license=openapi.License(
            name="MIT License",
            url="https://opensource.org/licenses/MIT",
        ),
    ),
    #     public=True,
    # permission_classes=(permissions.AllowAny,),
    # permission_classes=(permissions.IsAdminUser,),
    # permission_classes=(permissions.IsAuthenticated ,),
    #     permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
)

urlpatterns = [
    path('lift_track/', ForkliftsList.as_view(), name='forklift_list'),
    path('lift_track/<int:pk>/', ForkliftDetail.as_view(), name='forklift_detail'),
    path('lift_track/create/', ForkliftCreate.as_view(), name='forklift_create'),
    path('lift_track/<int:pk>/update/',
         ForkliftUpdate.as_view(), name='forklift_update'),
    path('lift_track/<int:pk>/delete/',
         ForkliftDelete.as_view(), name='forklift_delete'),
    path('lift_track/model_equipment/<int:pk>/',
         ModelEquipmentDetail.as_view(), name='model_equipment_detail'),
    path('lift_track/model_equipment/create/',
         ModelEquipmentCreate.as_view(), name='model_equipment_create'),
    path('lift_track/model_equipment/<int:pk>/update/',
         ModelEquipmentUpdate.as_view(), name='model_equipment_update'),
    path('lift_track/model_equipment/<int:pk>/delete/',
         ModelEquipmentDelete.as_view(), name='model_equipment_delete'),
    path('lift_track/model_equipment/<int:pk>/',
         ModelEquipmentDetail.as_view(), name='model_equipment_detail'),
    path('lift_track/engine_model/<int:pk>/',
         EngineModelDetail.as_view(), name='engine_model_detail'),
    path('lift_track/engine_model/create/',
         EngineModelCreate.as_view(), name='engine_model_create'),
    path('lift_track/engine_model/<int:pk>/update/',
         EngineModelUpdate.as_view(), name='engine_model_update'),
    path('lift_track/engine_model/<int:pk>/delete/',
         EngineModelDelete.as_view(), name='engine_model_delete'),
    path('lift_track/transmission_model/<int:pk>/',
         TransmissionModelDetail.as_view(), name='transmission_model_detail'),
    path('lift_track/transmission_model/create/',
         TransmissionModelCreate.as_view(), name='transmission_model_create'),
    path('lift_track/transmission_model/<int:pk>/update/',
         TransmissionModelUpdate.as_view(), name='transmission_model_update'),
    path('lift_track/transmission_model/<int:pk>/delete/',
         TransmissionModelDelete.as_view(), name='transmission_model_delete'),
    path('lift_track/drive_axle_model/<int:pk>/',
         DriveAxleModelDetail.as_view(), name='drive_axle_model_detail'),
    path('lift_track/drive_axle_model/create/',
         DriveAxleModelCreate.as_view(), name='drive_axle_model_create'),
    path('lift_track/drive_axle_model/<int:pk>/update/',
         DriveAxleModelUpdate.as_view(), name='drive_axle_model_update'),
    path('lift_track/drive_axle_model/<int:pk>/delete/',
         DriveAxleModelDelete.as_view(), name='drive_axle_model_delete'),
    path('lift_track/controlled_bridge_model/<int:pk>/',
         ControlledBridgeModelDetail.as_view(), name='controlled_bridge_model_detail'),
    path('lift_track/controlled_bridge_model/create/',
         ControlledBridgeModelCreate.as_view(), name='controlled_bridge_model_create'),
    path('lift_track/controlled_bridge_model/<int:pk>/update/',
         ControlledBridgeModelUpdate.as_view(), name='controlled_bridge_model_update'),
    path('lift_track/controlled_bridge_model/<int:pk>/delete/',
         ControlledBridgeModelDelete.as_view(), name='controlled_bridge_model_delete'),
    path('to/', ToList.as_view(), name='to_list'),
    path('to/<int:pk>/', ToDetail.as_view(), name='to_detail'),
    path('to/create/', ToCreate.as_view(), name='to_create'),
    path('to/<int:pk>/update/', ToUpdate.as_view(), name='to_update'),
    path('to/<int:pk>/delete/', ToDelete.as_view(), name='to_delete'),
    path('to/type_to/<int:pk>/', TypeToDetail.as_view(), name='type_to_detail'),
    path('to/type_to/create/', TypeToCreate.as_view(), name='type_to_create'),
    path('to/type_to/<int:pk>/update/',
         TypeToUpdate.as_view(), name='type_to_update'),
    path('to/type_to/<int:pk>/delete/',
         TypeToDelete.as_view(), name='type_to_delete'),
    path('claim/', ClaimList.as_view(), name='claim_list'),
    path('claim/<int:pk>/', ClaimDetail.as_view(), name='claim_detail'),
    path('claim/create/', ClaimCreate.as_view(), name='claim_create'),
    path('claim/<int:pk>/update/', ClaimUpdate.as_view(), name='claim_update'),
    path('claim/<int:pk>/delete/', ClaimDelete.as_view(), name='claim_delete'),
    path('claim/nature_failure/<int:pk>/',
         NatureRefusalDetail.as_view(), name='nature_failure_detail'),
    path('claim/nature_failure/create/',
         NatureRefusalCreate.as_view(), name='nature_failure_create'),
    path('claim/nature_failure/<int:pk>/update/',
         NatureRefusalUpdate.as_view(), name='nature_failure_update'),
    path('claim/nature_failure/<int:pk>/delete/',
         NatureRefusalDelete.as_view(), name='nature_failure_delete'),
    path('claim/recovery_method_detail/<int:pk>/',
         RecoveryMethodDetail.as_view(), name='recovery_method_detail'),
    path('claim/recovery_method/create/',
         RecoveryMethodCreate.as_view(), name='recovery_method_create'),
    path('claim/recovery_method/<int:pk>/update/',
         RecoveryMethodUpdate.as_view(), name='recovery_method_update'),
    path('claim/recovery_method/<int:pk>/delete/',
         RecoveryMethodDelete.as_view(), name='recovery_method_delete'),
    path('lift_track/client_detail/<int:pk>/',
         ClientDetail.as_view(), name='client_detail'),
    path('lift_track/service_company_detail/<int:pk>/',
         ServiceCompanyDetail.as_view(), name='service_company_detail'),


    path('api/forklift/', ForkliftAPIView.as_view()),
    path('api/to/', ToAPIView.as_view()),
    path('api/claim/', ClaimAPIView.as_view()),


    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    path('api/forklift/', ForkliftAPIView.as_view()),
    path('api/to/', ToAPIView.as_view()),
    path('api/claim/', ClaimAPIView.as_view()),
    #     path('openapi', get_schema_view(title="API Silant",
    #          description="API Silant", version="v 1.0.0"), name='openapi-schema'),
]
