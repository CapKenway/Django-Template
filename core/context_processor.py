import git
from django.conf import settings as config

def custom_context(request):
    app_version = f"0.3.{git.Repo(config.BASE_DIR,search_parent_directories=True).head.object.hexsha[0:6]}-beta"
    return {"APP_VERSION":app_version,}