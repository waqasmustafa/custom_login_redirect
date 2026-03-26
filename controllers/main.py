from odoo.http import request
from odoo.addons.web.controllers.home import Home


class CustomLoginRedirect(Home):

    def _login_redirect(self, uid, redirect=None):
        """
        Override post-login redirect URL.
        This method is only called after a SUCCESSFUL login — no template
        rendering happens here — so droggol's pricelist/env.user issue is
        completely avoided.
        """
        # Fetch the authenticated user safely
        user = request.env['res.users'].sudo().browse(uid)

        # Portal / external users → send to eLearning courses page
        if not user.has_group('base.group_user'):
            return '/slides'

        # Internal users (admin/staff) → default Odoo behaviour
        return super()._login_redirect(uid, redirect=redirect)