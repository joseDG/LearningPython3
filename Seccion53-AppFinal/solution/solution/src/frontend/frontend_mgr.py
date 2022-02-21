from ..backend.user import Customer
from .siteaccess_mgr import SiteAccessManager
from .customer_frontend_mgr import CustomerFrontendManager


class FrontendManager:
    def __init__(self):
        self.access_mgr = SiteAccessManager()

    def run(self):
        while True:
            try:    # Don't let ur site crash!
                user = self.access_mgr.get_accessed_user()

                if isinstance(user, Customer):
                    CustomerFrontendManager(user).run()
                else:
                    raise NotImplementedError

            except BaseException as exp:
                print(exp)
                raise exp
