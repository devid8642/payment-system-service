from django.shortcuts import redirect
from ninja import NinjaAPI

app = NinjaAPI(title='Payment System API', version='1.0.0')

# api.add_router("/pagamento/", pagamento_router)


@app.get('/', include_in_schema=False)
def redirect_to_docs(request):
    return redirect('/docs', permanent=True)
