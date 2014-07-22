# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields,osv
from openerp import tools
# from .. import crm



class product_elote_report(osv.osv):
    """ Phone calls by user and section """

    _name = "product.elote.report"
    _description = "Product report - Lots of e-lote attributes"
    _auto = False

    
    _columns = {
        'publishing_bs': fields.many2one('product.publishing_bs', 'Publishing BS' , readonly=True),
        'ean13': fields.char('ISBN', readonly=True),
        'ubs_code_no': fields.char('UBS Code', readonly=True),
        'ubs_code_suffix': fields.char('UBS Code Suffix', readonly=True),
        'ean13': fields.char('ISBN', readonly=True),
        'language': fields.many2one('product.language', 'Language' , readonly=True),
        'version': fields.many2one('product.version', 'Version' , readonly=True),
	'categ_id': fields.many2one('product.category','Category',readonly=True),
        'categoria': fields.many2one('product.categoria', 'Categoria' , readonly=True),
        'subcategoria': fields.many2one('product.subcategoria', 'Sub-Categoria' , readonly=True),
        'bible_binding': fields.many2one('product.binding', 'Binding' , readonly=True),
        'bible_colour': fields.many2one('product.colour', 'Bible Colour' , readonly=True),
        'bible_size': fields.many2one('product.size', 'Bible Size' , readonly=True),
        'carton_quantity': fields.float('Carton Quantity' , readonly=True),
        'carton_weight': fields.float('Carton Weight' , readonly=True),
        'carton_width': fields.float('Carton Width' , readonly=True),
        'carton_length': fields.float('Carton Length' , readonly=True),
        'carton_heigth': fields.float('Carton Height' , readonly=True),
        'carton_volume': fields.float('Carton Volume' , readonly=True),
        'exw_price': fields.float('EXW Price' , readonly=True),
        'service_fee': fields.float('Service Fee' , readonly=True),
        'developing_cost': fields.float('Developing Cost' , readonly=True),
        'royalties': fields.float('Royalties' , readonly=True),
        # 'publishing_bs': fields.char('Publishing BS', readonly=True),
        'default_code': fields.char('Ref', readonly=True),
        'name': fields.char('Name', readonly=True),
        'product_new': fields.boolean('New', readonly=True),
        'partner_id': fields.many2one('res.partner', 'Partner' , readonly=True),
        'quantity': fields.integer('Quantity',readonly=True ),
    }

    def init(self, cr):

        """ Purchase Orders by partner, date and product
        """
        tools.drop_view_if_exists(cr, 'product_elote_report')
        cr.execute("""
            create or replace view product_elote_report as (
		select a.id,a.publishing_bs,a.ean13,a.ubs_code_prefix,a.ubs_code_no,a.ubs_code_suffix,a.language,
		a.version,pt.categ_id,a.categoria,a.subcategoria,a.bible_binding,a.bible_colour,a.bible_size,
		ps.carton_quantity as carton_quantity,ps.carton_weight as carton_weight,ps.carton_width as carton_width,
		ps.carton_length as carton_length,ps.carton_heigth as carton_heigth,ps.carton_volume as carton_volume,
		ps.supplier_price as exw_price,ps.service_fee as service_fee,ps.developing_cost as developing_cost,
		ps.royalties as royalties,a.default_code as default_code,pt.name as name,a.producto_nuevo as product_new, ps.name as partner_id,
		1 as quantity 
			from product_product a  
			left join product_size i on a.bible_size = i.id inner join product_template pt on pt.id = a.product_tmpl_id 
			left join product_supplierinfo ps on pt.id = ps.product_tmpl_id 
            )""")

product_elote_report()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
