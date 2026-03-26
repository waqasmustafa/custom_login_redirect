from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home


class CustomLoginRedirect(Home):

    @http.route('/web/login', type='http', auth='none', sitemap=False)
    def web_login(self, redirect=None, **kw):
        response = super().web_login(redirect=redirect, **kw)

        # Check if login was successful
        if request.session.uid:
            # In auth='none' routes, request.env.user is an empty recordset.
            # We must browse the user explicitly using sudo() to get a valid singleton.
            user = request.env['res.users'].sudo().browse(request.session.uid)

            # Internal users (admin/staff) ko redirect na karo
            is_internal_user = user.has_group('base.group_user')

            # Sirf portal/external users ko /slides par bhejo
            if not is_internal_user:
                return request.redirect('/slides')

        return response