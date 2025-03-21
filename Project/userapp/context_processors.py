from userapp.models import *  

def user_info(request):
    """
    Context processor to pass user information globally to templates
    if a user is logged in.
    """
    user_id = request.session.get('user_id_after_login')
    user = None
    if user_id:
        user = User.objects.filter(id=user_id).first()
    return {
        'is_user_login': user
    }