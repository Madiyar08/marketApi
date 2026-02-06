from django.http import HttpResponseForbidden

# Разрешённые IP
ALLOWED_IPS = ["217.30.160.187"]  # IP колл-центра

class AllowOnlyCallCenterIPMiddleware:
    """
    Middleware, который разрешает доступ только с указанных IP.
    Всем остальным возвращает 403 Forbidden.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Получаем IP пользователя
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        ip = x_forwarded_for.split(",")[0].strip() if x_forwarded_for else request.META.get("REMOTE_ADDR")

        # Проверяем, есть ли IP в списке разрешённых
        if ip not in ALLOWED_IPS:
            return HttpResponseForbidden("Доступ запрещён")

        return self.get_response(request)
