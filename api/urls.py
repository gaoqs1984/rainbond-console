from django.conf.urls import patterns, url, include
from rest_framework.authtoken import views
from api.views.services import SelectedServiceView, PublishServiceView
from api.views.tenants.services import TenantServiceStaticsView, TenantHibernateView, TenantView, AllTenantView, GitCheckCodeView
from api.views.tenants import move

urlpatterns = patterns(
    '',
    url(r'^services/(?P<serviceId>[a-z0-9\-]+)$', SelectedServiceView.as_view()),
    url(r'^tenants/services/statics$', TenantServiceStaticsView.as_view()),
    url(r'^tenants/services/hibernate$', TenantHibernateView.as_view()),
    url(r'^tenants/services/publish$', PublishServiceView.as_view()),
    url(r'^tenants/member$', TenantView.as_view()),
    url(r'^tenants/all-members$', AllTenantView.as_view()),
    url(r'^tenants/services/codecheck', GitCheckCodeView.as_view()),
    url(r'^tenants/(?P<tenantId>[a-z0-9\-]+)/move/stop_prepare$', move.TenantStopView.as_view()),
    url(r'^tenants/(?P<tenantId>[a-z0-9\-]+)/move/start$', move.TenantStartView.as_view()),
    url(r'^tenants/(?P<tenantId>[a-z0-9\-]+)/move/follow_up$', move.TenantFollowUpView.as_view()),
    url(r'^tenants/(?P<tenantId>[a-z0-9\-]+)/move/update$', move.TenantMoveUpdateView.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth', views.obtain_auth_token),
    url(r'^docs/', include('rest_framework_swagger.urls')),
)
